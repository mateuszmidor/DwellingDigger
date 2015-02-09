# -*- coding: utf-8 -*-
'''
Created on 16-01-2015

@author: mateusz
'''
from lightwebframework.light_web_framework import LightWebFramework
from offers.web_document_fetcher import WebDocumentFetcher
from offers.gumtree.offer_search_query import OfferSearchQuery as GumtreeOfferSearchQuery
from offers.gumtree.offer_searcher import OfferSearcher as GumtreeOfferSearcher
from offers.gumtree.gumtree import Gumtree

from src.offers.olx.offer_searcher import OfferSearcher as OlxOfferSearcher
from src.offers.olx.offer_search_query import OfferSearchQuery as OlxOfferSearchQuery
from src.offers.olx.olx import Olx
from src.addressextractor.evaluator.evaluator import Evaluator
from src.addressextractor.address_extractor import AddressExtractor
import cProfile
import pstats

'''
Predefined map points and coordinates
'''
POINTS = ur"""[[50.095613, 19.927883699999999, '<b>jasna </b></br>KOMPLETNIE UMEBLOWANE, PO KAPITALNYM REMONCIE 2013! - 24/07/2014 <b>Z\u0142 \xa01 700,00</b></br><i>Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Mam do wynaj\u0119cia pi\u0119kne mieszkanie po\u0142o\u017cone w osiedlu Z\u0142oty Wiek, mieszkanie o powierzchni 70m2, bardzo praktyczny uk\u0142ad, 3 du\u017ce pokoje [wszystkie osobne wej\u015bcia], du\u017ca jasna kuchnia, \u0142azienka i WC osobno, du\u017cy ustawny przedpok\xf3j, salon o powierzchn</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/kompletnie-umeblowane-po-kapitalnym-remoncie-2013-594941739?featuredAd=true" target="_blank">Link</a></br>', icon_older], [50.079234399999997, 19.889957800000001, '<b>armii krajowej</b></br>super lokalizacja !!!! , blisko do centrum , AGH, - 29/07/2014 <b>Z\u0142 \xa01 500,00</b></br><i>Armii Krajowej, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia od 1.09, \u0142adne, s\u0142oneczne,przytulne i ciche , wyposa\u017cone mieszkanie o pow.37 m [ dwa nie przechodnie pokoje ] , Super lokalizacja na ul. Armii Krajowej 7 , dobre po\u0142\u0105czenia komunikacji , do Rynku G\u0142\xf3wnego 10 min , zielona okolica , obok</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/super-lokalizacja-blisko-do-centrum-agh-607828587" target="_blank">Link</a></br>', icon_today], [50.058838599999987, 19.980830999999998, '<b>widok </b></br>mieszkanie jednopokojowe z kuchnia - 29/07/2014 <b>Z\u0142 \xa01 000,00</b></br><i>Ma\u0142opolskie\r\nKrak\xf3w</i></br>Mieszkanie: pokoj z kuchnia, swiezo po remoncie na trzecim pietrze z balkonem i ogrzewaniem miejskim.\r\nObejmuje 36m2, jest sloneczne, cieple w zimie i ma widok na zielen.\r\nJest oddalone okolo 3 - 5 minut od przystanku tramwajowego, i ma mozliwosc za</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-jednopokojowe-z-kuchnia-607821025" target="_blank">Link</a></br>', icon_today], [50.0634759, 19.941756600000001, '<b>szpitalna</b></br>ul. Szpitalna, Stare Miasto, 2 pok. + kuchnia, garderoba - 29/07/2014 <b>Z\u0142 \xa01 500,00</b></br><i>Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia mieszkanie przy ul. Szpitalnej [tj. przy samym Rynku G\u0142\xf3wnym]. Lokal umeblowany, od\u015bwie\u017cony po poprzednich najemcach, zlokalizowany w zadbanej kamienicy. Mieszkanie o pow. ok 50 m2 sk\u0142ada si\u0119 z 2 przestronnych pokoi, du\u017cej kuchni, \u0142azien</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ul-szpitalna-stare-miasto-2-pok-kuchnia-garderoba-607821906" target="_blank">Link</a></br>', icon_today], [50.024467100000003, 19.9162976, '<b>pszczelna</b></br>\u0141adne mieszkanie dwupokojowe przy ul. Pszczelnej [Ruczaj] - 27/07/2014 <b>Z\u0142 \xa01 500,00</b></br><i>Pszczelna, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Oferuj\u0119 do wynaj\u0119cia \u0142adne\xa0mieszkanie na Ruczaju\xa0przy ul. Pszczelnej. Mieszkanie zlokalizowane na 2 pi\u0119trze w bloku oddanym w 2009 roku. Pokoje nieprzechodnie [w ka\u017cdym z pokoi dwuosobowa wersalka], kuchnia, \u0142azienka. Mieszkanie w pe\u0142ni wyposa\u017cone i</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ladne-mieszkanie-dwupokojowe-przy-ul-pszczelnej-ruczaj-607012750?featuredAd=true" target="_blank">Link</a></br>', icon_older], [50.0598569, 19.945533900000001, '<b>miko\u0142aja zyblikiewicza</b></br>Atrakcyjne 2 pok 50 m w scis\u0142ym centrum Krakowa - 22/07/2014 <b>Z\u0142 \xa01 650,00</b></br><i>Miko\u0142aja Zyblikiewicza, 31-029 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia mieszkanie na ul Zyblikiewicza w dzielnicy Stare Miasto o powierzchni 50m 2. Mieszkanie sk\u0142ada si\u0119 z: Przedpok\xf3j[2,5 m2], w kt\xf3rym znajduje si\u0119 pojemna szafa wn\u0119kowa \u0141azienka [2 m2] z kabina z hydromasa\u017cem, WC i pralk\u0105 Kuchnia[10</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/atrakcyjne-2-pok-50-m-w-scislym-centrum-krakowa-606411301?featuredAd=true" target="_blank">Link</a></br>', icon_older], [50.0787646, 19.981914199999999, '<b>fio\u0142kowa</b></br>urocza kawalerka - 29/07/2014 <b>Z\u0142 \xa01 000,00</b></br><i>Fio\u0142kowa, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>kawalerka po generalnym remoncie, parter, blok 4-pi\u0119trowy, cicha i zielona okolica</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/urocza-kawalerka-607822524" target="_blank">Link</a></br>', icon_today], [50.073835799999998, 19.899138700000002, '<b>cicha</b></br>Nowoczesne umeblowane 2-pokojowe 40m2 BOREK FA\u0141\u0118CKI - 29/07/2014 <b>Z\u0142 \xa01 400,00</b></br><i>Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia nowoczesne, w pe\u0142ni umeblowane i wyposa\u017cone mieszkanie 2-pokojowe o powierzchni 40m2 z balkonem na I pi\u0119trze w niskim, nowym, ciep\u0142ym bloku oddanym do u\u017cytku w 2008 r. przy ulicy Borkowskiej - cicha, dobrze usytuowana okolica. Mieszkanie</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowoczesne-umeblowane-2-pokojowe-40m2-borek-falecki-607814979" target="_blank">Link</a></br>', icon_today], [50.083426000000003, 19.872812499999998, '<b>bronowice</b></br>Bardzo \u0142adne mieszkanie na G\u0142owackiego/ Bronowice - 29/07/2014 <b>Z\u0142 \xa01 800,00</b></br><i>G\u0142owackiego 10B, 30-085 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Bardzo \u0142adne i zadbane mieszkanie w budynku przy ul. G\u0142owackiego w dzielnicy Bronowice. Wysoki parter.\r\n2 pokoje z niezale\u017cn\u0105 kuchni\u0105, balkon, 60m2.\r\nDoskona\u0142a lokalizacja \u2013 3 min od przystanku tramwajowego \u201eG\u0142owackiego\u201d \u2013 10-15 min do centrum, 2</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/bardzo-ladne-mieszkanie-na-glowackiego-bronowice-607822343" target="_blank">Link</a></br>', icon_today], [49.975221400000002, 19.828168099999999, '<b>pokoju</b></br>Nowe, wyposa\u017cone mieszkanie do wynaj\u0119cia, 2 pokoje - 29/07/2014 <b>Z\u0142 \xa01 600,00</b></br><i>Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Wynajm\u0119 mieszkanie komfortowo urz\u0105dzone na osiedlu D\u0105bie.Mieszkanie jest nowe [z 2013r], w pe\u0142ni urz\u0105dzone, Sk\u0142ada si\u0119 z 2 samodzielnych pokoi [10 i 16m2], oddzielnej kuchni 9,5 m2 , eleganckiej \u0142azienki ,przedpokoju.\r\nNa wyposa\u017ceniu kuchni: piekarn</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowe-wyposazone-mieszkanie-do-wynajecia-2-pokoje-607819766" target="_blank">Link</a></br>', icon_today], [50.081329799999999, 19.962268999999999, '<b>brogi</b></br>OD ZARAZ MIESZKANIE DO WYNAJ\u0118CIA - KRAK\xd3W \u2013 OLSZA - 29/07/2014 <b>Z\u0142 \xa02 000,00</b></br><i>Brogi, Polska\r\n\r\nPoka\u017c map\u0119</i></br>OD ZARAZ MIESZKANIE DO WYNAJ\u0118CIA - KRAK\xd3W \u2013 OLSZA okolice ronda m\u0142y\u0144skiego! Wynajm\u0119 mieszkanie osobom spokojnym i nie przesadzaj\u0105cym z imprezami W Okolicach Olszy i Ronda M\u0142y\u0144skiego - DU\u017bE, PRZESTRONNE, 3POKOJOWE Mo\u017cliwo\u015b\u0107 ogl\u0105dania mieszka\u0144 i\xa0rezerw</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/od-zaraz-mieszkanie-do-wynajecia-krakow-olsza-607819980" target="_blank">Link</a></br>', icon_today], [50.0144989, 20.045500499999999, '<b>leopolda flanka</b></br>Niedroga kawalerka do wynaj\u0119cia w Krakowie - Podg\xf3rzu - 27/07/2014 <b>Z\u0142 \xa0600,00</b></br><i>Leopolda Flanka, 30-898 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Niedroga niezale\u017cna kawalerka o pow. 30m2 s\u0142oneczna na I pi\u0119trze urz\u0105dzona umeblowana sk\u0142adaj\u0105ca si\u0119 z pokoju kuchni obok \u0142azienka, oddzielne wej\u015bcie klatka schodowa podw\xf3rze. Dobra lokalizacja i komunikacja, 20 minut dojazd do centrum Krakowa. Do wy</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/niedroga-kawalerka-do-wynajecia-w-krakowie-podgorzu-607754458?featuredAd=true" target="_blank">Link</a></br>', icon_older], [50.016192799999999, 20.005657200000002, '<b>teligi 14</b></br>\u0141adne mieszkanie dwupokojowe wynajm\u0119 - 29/07/2014 <b>Z\u0142 \xa01 000,00</b></br><i>Teligi 14, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Mam mieszkanie dwupokojowe, umeblowane, kt\xf3re chce wynaj\u0105\u0107. Lokalizacja: Prokocim ul. Teligi. Blok 4- pi\u0119trowy bez windy, II pi\u0119tro. Pi\u0119kny, s\u0142oneczny balkon, przestronne pokoje, w\u0105ska kuchnia, oddzielnie wc i \u0142azienka. Dodatkowe koszty utrzymania to</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ladne-mieszkanie-dwupokojowe-wynajme-607821639" target="_blank">Link</a></br>', icon_today], [50.025865000000003, 19.9201896, '<b>ruczaj </b></br>Wynajm\u0119 studentkom dwupokojowe mieszkanie 37m\xb2 - 29/07/2014 <b>Z\u0142 \xa01 200,00</b></br><i>Krak\xf3w\r\n\r\nPoka\u017c map\u0119</i></br>Ruczaj - ul. Mi\u0142kowskiego - dwupokojowe mieszkanie 37 m\xb2 na III pi\u0119trze wynajm\u0119 studentkom tel. 666-095-640</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/wynajme-studentkom-dwupokojowe-mieszkanie-37m-607827079" target="_blank">Link</a></br>', icon_today], [50.069856999999999, 19.915524699999999, '<b>chocimska</b></br>dwupokojowe ul.Lea - Chocimska - 28/07/2014 <b>Z\u0142 \xa01 500,00</b></br><i>Chocimska, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Dwupokojowe mieszkanie blisko centrum, pokoje z oddzielnymi wej\u015bciami ; 20 i 15 m. Oddzielna kuchnia,balkon , umeblowane: pralka, lod\xf3wka.W \u0142azience kabina prysznicowa.Ogrzewanie centralne. Op\u0142aty w\u0142a\u015bciciel 1500 pln + 540 pln czynsz administracyjny</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/dwupokojowe-ul-lea-chocimska-599048679" target="_blank">Link</a></br>', icon_older], [50.032240799999997, 19.915012099999998, '<b>pychowicka 16</b></br>Krak\xf3w, Ruczaj, Zakrz\xf3wek, Kampus UJ, Pychowicka, 2pokoje+ gara\u017c - 10/07/2014 <b>Z\u0142 \xa01 550,00</b></br><i>Pychowicka 16, 30-364 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Wynajm\u0119 46 metrowe mieszkanie wraz z gara\u017cem w nowym bloku: Krak\xf3w, Podg\xf3rze, ul. Pychowicka 16 w okolicy malowniczego zalewu Zakrz\xf3wek. W pobli\u017cu Kaufland, Tesco, Kampus UJ. Dogodny dojazd do centrum [12 min] liniami autobusowymi: 194 liniami tramwa</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/krakow-ruczaj-zakrzowek-kampus-uj-pychowicka-2pokoje-garaz-602187607?featuredAd=true" target="_blank">Link</a></br>', icon_older], [50.061339799999999, 19.894598999999999, '<b>j\xf3zefa korzeniowskiego</b></br>930z\u0142 Wola Justowska jednopokojowe,niskie media cisza spokoj - 29/07/2014 <b>Z\u0142 \xa0930,00</b></br><i>J\xf3zefa Korzeniowskiego, 30-214 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>1/Ulica Korzeniowskiego-nowe, umeblowane, parter z ogr\xf3dkiem, spokojna i ekskluzywna okolica na Woli Justowskiej, 34mkw\r\n2/kilka minut autobusem od RYNKU G\u0141\xd3WNEGO,przystanek autobusowy 5 min, parking,\r\n3/Kuchnia, pok\xf3j, \u0142azienka ,\r\n4/950 z\u0142 plus med</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/930zl-wola-justowska-jednopokojowe-niskie-media-cisza-spokoj-607826685" target="_blank">Link</a></br>Dwupokojowe,parter 38 mkw Centrum Miastaul.Zamkowa - 29/07/2014 <b>Z\u0142 \xa0980,00</b></br><i>J\xf3zefa Korzeniowskiego, 30-214 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>ZAMKOWA\r\n1/Centrym Krakowa,5min pieszo do Rynku,kilkana\u015bcie autobus\xf3w,tramwaje\r\n2/Dwupokojowe 38mkw, parter, odremontowane stare budownictwo , ulica Zamkowa - jeden pok\xf3j 19 mkw, drugi 8 mkw, /uk\u0142ad przechodni/, \u0142azienka ,kuchnia wyposa\u017cone .\r\n3/Cena</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/dwupokojowe-parter-38-mkw-centrum-miastaul-zamkowa-607826735" target="_blank">Link</a></br>', icon_today], [50.092979999999997, 19.992258, '<b>o\u015bwiecenia 42</b></br>Dwupokojowe po remoncie - 29/07/2014 <b>Z\u0142 \xa01 400,00</b></br><i>osiedle O\u015bwiecenia 42, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Powierzchnia: 48 m2. Dwa du\u017ce pokoje, 2 balkony , \u0142azienka, kuchnia, \u0142adnie\xa0 umeblowane, pralka, kuchenka, mikrofala, czajnik, lod\xf3wka, \xa0 internet . Mieszkanie \u015bwie\u017co po remoncie. W okolicy Multikino, Aquapark, Biedronka Bardzo dobra komunikacja z Ce</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/dwupokojowe-po-remoncie-607821654" target="_blank">Link</a></br>', icon_today], [50.085657900000001, 19.9318989, '<b>kluczborska 50</b></br>Krowodrza G\xf3rka, Os. Ukryte Pragnienia,strze\u017cone osiedle+parking - 29/07/2014 <b>Z\u0142 \xa01 600,00</b></br><i>Kluczborska 50, 31-271 Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia pi\u0119kne s\u0142oneczne 52-metrowe mieszkanie sk\u0142adaj\u0105ce si\u0119 z 2 pokoi [22 m2 i 11m2], kuchni [7 m2], \u0142azienki [5 m2] i korytarza [7 m2]. Mieszkanie w apartamentowym osiedlu Ukryte Pragnienia przy p\u0119tli tramwajowo-autobusowej Krowodrza G\xf3rka.</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/krowodrza-gorka-os-ukryte-pragnienia-strzezone-osiedle-parking-607820293" target="_blank">Link</a></br>', icon_today], [50.050724600000002, 19.944987999999999, '<b>nowa </b></br>\u0141adne mieszkanie w Nowej Hucie- do wynaj\u0119cia - 29/07/2014 <b>Z\u0142 \xa01 190,00</b></br><i>Nowa Huta, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Mieszkanie w Nowej Hucie, na osiedlu Hutniczym,\xa0po remoncie, 60 m2, dwa pokoje z balkonami, plus\xa0 kuchnia i \u0142azienka. Nowe okna, drzwi antyw\u0142amaniowe, panele. Wyposa\u017cenie: kuchenka gazowa, pralka, lod\xf3wka, podstawowe umeblowanie. Mieszkanie znajduje</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ladne-mieszkanie-w-nowej-hucie-do-wynajecia-607821187" target="_blank">Link</a></br>', icon_today], [50.041789700000002, 19.952543800000001, '<b>parkowa</b></br>sympatyczna kawalerka 1000 z\u0142 z mediami blisko centrum - 28/07/2014 <b>Z\u0142 \xa01 000,00</b></br><i>Olsza, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Sympatyczna kawalerka z wn\u0119k\u0105 kuchenn\u0105 i niezale\u017cna \u0142azienk\u0105 mieszcz\u0105ca si\u0119 na poddaszu ma\u0142ego domku z ogrodem [mo\u017cliwo\u015b\u0107 parkowania].Okolice\xa0 ulicy Brogi,\u015bwietna komunikacyjnie.Dla os\xf3b ceni\u0105cych cisz\u0119 i spok\xf3j [kawalerka ma okna na ogr\xf3d].Ca\u0142okowi</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/sympatyczna-kawalerka-1000-zl-z-mediami-blisko-centrum-607820332" target="_blank">Link</a></br>', icon_older], [50.064650099999987, 19.9449799, '<b>Krakow</b></br>Jednopokojowe w spokojnej okolicy - 29/07/2014 <b>Z\u0142 \xa01 400,00</b></br><i>Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia mieszkanie jednopokojowe z aneksem kuchennym i \u0142azienk\u0105 o powierzchni 38 m2. Dodatkowe zalety to przedpok\xf3j z obszern\u0105 szaf\u0105 wn\u0119kow\u0105 [blisko trzymetrow\u0105] oraz wyj\u0105tkowo du\u017cy balkon. Mieszkanie mie\u015bci si\u0119 na czwartym [ostatnim] pi\u0119trze w</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/jednopokojowe-w-spokojnej-okolicy-607821772" target="_blank">Link</a></br>', icon_today], [50.070464800000003, 19.9770164, '<b>ostatnia</b></br>ul. Ostatnia, 2 pok.+ jasna kuchnia, umeblowane, rej. Uczelni - 29/07/2014 <b>Z\u0142 \xa01 600,00</b></br><i>Krak\xf3w\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia umeblowane mieszkanie przy ul. Ostatniej [rejon ul. Mogilskiej]. Lokal o pow. 50 m2 sk\u0142ada si\u0119 z 2 niezale\u017cnych pokoi, oddzielnej jasnej kuchni, du\u017cej \u0142azienki z wc oraz przestronnego przedpokoju. Do mieszkania przynale\u017cy balkon. Umeblow</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ul-ostatnia-2-pok-jasna-kuchnia-umeblowane-rej-uczelni-607821868" target="_blank">Link</a></br>', icon_today], [50.099589299999998, 19.911183999999999, '<b>w\u0142adys\u0142awa \u0142okietka</b></br>\u0141ADNE MIESZKANIE DWUPOKOJOWE PO REMONCIE ul. \u0141OKIETKA!!! - 29/07/2014 <b>Z\u0142 \xa01 400,00</b></br><i>W\u0142adys\u0142awa \u0141okietka, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Witam, mam do wynaj\u0119cia mieszkanie w samym centrum Krakowa ul. \u0141okietka, 20 minut na piechot\u0119 do Rynku, \u015bwietna lokalizacja - dojazd [ewentualnie doj\u015bcie] do wszystkich uczelni. Mieszkanie jest dwupokojowe, ma 50 metr\xf3w, 2 nieprzechodnie pokoje, jasn</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ladne-mieszkanie-dwupokojowe-po-remoncie-ul-lokietka-607819553" target="_blank">Link</a></br>', icon_today], [50.0769308, 19.982878100000001, '<b>ugorek 4</b></br>3 pokoje Krak\xf3w \u015ar\xf3dmie\u015bcie ul. Ugorek - 29/07/2014 <b>Z\u0142 \xa01 300,00</b></br><i>Ugorek 4, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynaj\u0119cia trzypokojowe mieszkanie o pow. 60 m2 usytuawane na \xa0 pi\u0105tym pi\u0119trze w dziesi\u0119ciopi\u0119trowym \xa0 bloku przy ulicy Ugorek. Rozk\u0142ad mieszkania: 3 pokoje /w tym jeden przechodni/, kuchna, \u0142azienka, WC, balkon. Mieszkanie umeblowane i wyposa\u017con</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/3-pokoje-krakow-srodmiescie-ul-ugorek-607820471" target="_blank">Link</a></br>', icon_today], [50.072925699999999, 19.922847900000001, '<b>kujawska</b></br>Bezczynszowe, bezprowizyjne, dwupokojowe-rejon ul. Kr\xf3lewskiej - 29/07/2014 <b>Z\u0142 \xa01 200,00</b></br><i>Kujawska, Krak\xf3w, Polska\r\n\r\nPoka\u017c map\u0119</i></br>Do wynajecia, bezposrednio, dwa pokoje z aneksem kuchennym [40 m2]. Mieszkanie na pierwszym pietrze w spokojnej kamienicy. Ogrzewanie energooszczedne - gazowe [kociol dwufunkcyjny]. Cena 1200 pln + media wg zuzycia [internet wliczony w cene mieszkani</br><a href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/bezczynszowe-bezprowizyjne-dwupokojowe-rejon-ul-krolewskiej-607828721" target="_blank">Link</a></br>', icon_today]]"""
MAP_CENTER_LONG = 50.0646501 
MAP_CENTER_LATT = 19.9449799
MAP_ZOOM = 11
TEMPLATE_HTML_FILENAME = u"data/DesktopView.htm"
RESULT_HTML_FILENAME = u"DwellingMap.html"

class DesktopMain:

    @staticmethod
    def demo_run():
#         DesktopMain.print_5_gumtree_offer_details()
#         DesktopMain.print_learning_samples()
        # DesktopMain.print_5_o€lx_offer_details()
#         DesktopMain.evaluate_address_extractor()
#         DesktopMain.print_5_gumtree_offers_addr()
        run_func = DesktopMain.print_5_gumtree_offers_addr
        cProfile.runctx("run_func()", 
                        {"global_variables" : "none"},
                        {"run_func" : run_func}, 
                        filename="DesktopMain_profile.txt")
        p = pstats.Stats("DesktopMain_profile.txt")
        p.strip_dirs().sort_stats('cumulative').print_stats(20) # sortujemy, i pierwsze 20 do PROFILER_TXT
        
       
       
    @staticmethod
    def print_5_gumtree_offers_addr():
        """Prints out details and addresses of 5 offers found on Gumtree"""
        
        dict_files = ["DwellingDigger/data/krakow_streets.txt", 
                    "DwellingDigger/data/krakow_districts.txt", 
                    "DwellingDigger/data/cities.txt"
                      ]
        extractor = AddressExtractor.rank_based(dict_files)
        offers = Gumtree.get_offers(city="Krakow", min_price="1900",  max_offer_count=5)

        for i, offer in enumerate(offers, 1):
            address = extractor.extract([offer["address_section"], offer["title"],offer["summary"]])
            print("%i." % i)
            print(offer["title"])
            print("Address: %s" % address)
            print(offer["date"])
            print(offer["price"])
            print(offer["address_section"])
            print(offer["summary"])
            print("")
             
    @staticmethod
    def evaluate_address_extractor():
        dict_files = ["DwellingDigger/data/krakow_streets.txt", 
                    "DwellingDigger/data/krakow_districts.txt", 
                    "DwellingDigger/data/cities.txt"
                      ]
        extractor = AddressExtractor.rank_based(dict_files)
        Evaluator.evaluate(extractor)
        
    @staticmethod
    def print_learning_samples():
        """ 
        Prints learning samples for AddressExtractor. It looks like this:
        # 1.
        source= [address section]
        source= [title]
        source= [summary]
        expected= [to be manually filled]
        ... repeat
        """   

        offers = Olx.get_offers(city="Krakow", 
                                    max_offer_count=100)
        for i, offer in enumerate(offers, 1):
            print("# %i." % i)
            print("source=%s" % offer["address_section"])
            print("source=%s" % offer["title"].replace("\n", "").replace("\r", ""))
            print("source=%s" % offer["summary"].replace("\n", "").replace("\r", ""))
            print("expected= ")
                     
    @staticmethod
    def print_5_olx_offer_details():
        """Prints out details of 5 offers found on OLX"""
        
        offers = Olx.get_offers(city="Krakow", 
                                    num_rooms="1", 
                                    max_price="1200",
                                    max_offer_count=5)
        for i, offer in enumerate(offers, 1):
            print("%i." % i)
            print("Title:" , offer["title"])
            print("Date:", offer["date"])
            print("Price:", offer["price"])
            print("Address:", offer["address_section"])
            print("Summary:", offer["summary"])
            print("Url:", offer["url"])
            print()
              
    @staticmethod
    def print_5_olx_offer_urls():
        """Prints out 5 urls to offers found on OLX"""
        
        query = OlxOfferSearchQuery.compose(city="Krakow",  whereabouts="ruczaj")
        print(query)
        urls = OlxOfferSearcher.search(query, 5, WebDocumentFetcher)
        for i, url in enumerate(urls, 1):
            print("{0}. {1}".format(i, url))
             
    @staticmethod
    def print_5_gumtree_offer_details():
        """Prints out details of 5 offers found on Gumtree"""
        
        offers = Gumtree.get_offers(city="Kraków", 
                                    whereabouts="Prądnik",
                                    num_rooms="1", 
                                    max_price="1200",
                                    max_offer_count=5)
        for i, offer in enumerate(offers, 1):
            print("%i." % i)
            print(offer["title"])
            print(offer["date"])
            print(offer["price"])
            print(offer["address_section"])
            print(offer["summary"])
            print()

    @staticmethod
    def print_5_gumtree_offer_urls():
        """Prints out 5 urls to offers found on Gumtree"""
        
        query = GumtreeOfferSearchQuery.compose(city="Krakow")
        for url in GumtreeOfferSearcher.search(query, 5, WebDocumentFetcher):
            print(url)
            
    @staticmethod
    def generate_html_with_points():
        """Creates "DwellingMap.html" showing some predefined points on Cracow map"""
     
        FIELDS = {u"$POINTS$": POINTS,
                  u"$MAP_CENTER_LONG$": MAP_CENTER_LONG,
                  u"$MAP_CENTER_LATT$": MAP_CENTER_LATT,
                  u"$MAP_ZOOM$" : MAP_ZOOM}
                   
        LightWebFramework.render_page_as_file(TEMPLATE_HTML_FILENAME, RESULT_HTML_FILENAME, FIELDS)
        print("Demo web page saved as %s" % RESULT_HTML_FILENAME)