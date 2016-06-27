# -*- coding: utf-8 -*-

'''
Created on 20-01-2015

@author: mateusz
'''
import unittest
from src.mvc.model.gumtree.offer_extractor import OfferExtractor
from datetime import datetime

class OfferExtractorTest(unittest.TestCase):

    def test_extract_price(self):
        ACTUAL_PRICE = u"1 200 zł"
        price = OfferExtractor.extract(OFFER_HTML)["price"]
        self.assertEquals(ACTUAL_PRICE, price)

    def test_extract_date(self):
        ACTUAL_DATE = datetime(2016, 6, 27) 
        date = OfferExtractor.extract(OFFER_HTML)["date"]
        self.assertEquals(ACTUAL_DATE, date)
        
    def test_extract_title(self):
        ACTUAL_TITLE = u"2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ – Kraków – 169136399 | Gumtree"
        title = OfferExtractor.extract(OFFER_HTML)["title"]
        self.assertEquals(ACTUAL_TITLE, title)
        
    def test_extract_address(self):
        ACTUAL_ADDRESS = u"Kraków, Małopolskie"
        address = OfferExtractor.extract(OFFER_HTML)["address_section"]
        self.assertEquals(ACTUAL_ADDRESS, address)
        
    def test_extract_description(self):
        ACTUAL_DESCRIPTION = u"""Nr oferty 2650. Kraków. Płaszów, ul. Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielnych pokoi, kuchni, łazienki i garderoby."""
        description = OfferExtractor.extract(OFFER_HTML)["description"]
        self.assertEquals(ACTUAL_DESCRIPTION, description)
        
    def test_extract_summary(self):
        ACTUAL_SUMMARY = u"""Nr oferty 2650. Kraków. Płaszów, ul. Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielny...169136399"""
        summary = OfferExtractor.extract(OFFER_HTML)["summary"]
        self.assertEquals(ACTUAL_SUMMARY, summary)

    def test_extract_image_url(self):
        ACTUAL_URL = u"http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_20.JPG?set_id=8800005007"
        url = OfferExtractor.extract(OFFER_HTML)["image_url"]
        self.assertEquals(ACTUAL_URL, url)

    def test_extract_numrooms(self):
        ACTUAL_NUMROOMS = 2
        num_rooms = OfferExtractor.extract(OFFER_HTML)["num_rooms"]
        self.assertEquals(ACTUAL_NUMROOMS, num_rooms, 
                          "There should be %s rooms in the offer but extracted count is %s" % (ACTUAL_NUMROOMS, num_rooms))
  
    def test_extract_numrooms_1(self):
        ACTUAL_NUMROOMS = 1
        num_rooms = OfferExtractor.extract(OFFER2_HTML)["num_rooms"]
        self.assertEquals(ACTUAL_NUMROOMS, num_rooms, 
                          "There should be %s rooms in the offer but extracted count is %s" % (ACTUAL_NUMROOMS, num_rooms))
                
        
    def test_extract_area(self):
        ACTUAL_AREA = 47
        area = OfferExtractor.extract(OFFER_HTML)["area"]
        self.assertEquals(ACTUAL_AREA, area, 
                          "Room area should be %s but extracted area is %s" % (ACTUAL_AREA, area))
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
   
OFFER_HTML = u"""



<!DOCTYPE html>
<!--[if IEMobile 7]>
<html data-locale="pl_PL" lang="pl_PL" class="iem7 oldie VIP"><![endif]-->
<!--[if (IE 7)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie7 lt-ie8 lt-ie9 lt-ie10 oldie VIP"><![endif]-->
<!--[if (IE 8)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie8 lt-ie9 lt-ie10 oldie VIP"><![endif]-->
<!--[if (IE 9)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie9 lt-ie10 VIP"><![endif]-->
<!--[if (gt IE 9)|(gt IEMobile 7)]><!-->
<html data-locale="pl_PL" lang="pl_PL" xmlns="http://www.w3.org/1999/html" class="VIP"><!--<![endif]-->
<head>
    <title>2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ – Kraków – 169136399 | Gumtree</title>
    <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
    <meta name="description" content="Nr oferty 2650. Kraków. Płaszów, ul. Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielny...169136399"/>
    <meta name="robots" content="index,follow"/>
    <meta name="format-detection" content="telephone=no"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    
    
    

    
    

    
        <meta property="og:title" content="2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ – Kraków – 169136399 | Gumtree"/>
        <meta property="og:type" content="product"/>
        <meta property="og:image" content='http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_20.JPG?set_id=8800005007'/>
        <meta property="og:url" content="http://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/2-pok-47-m2-na-plaszowskiej-dla-3-osob-blisko-rm-grzegorzeckiego-lini-tramwajowej/1001691363990910474413109"/>
        <meta property="og:site_name" content="Gumtree"/>
        <meta property="og:country-name" content="Poland"/>
        <meta property="og:description" content="Nr oferty 2650. Kraków. Płaszów, ul. Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielny...169136399"/>
        <meta property="og:locale" content="pl_PL"/>
    
    
    
    
    
        <link rel="stylesheet" type="text/css" href='http://inc.t9.classistatic.com/1.1.288/css/all/Gumtree/PL/pl_PL/Main.min.css'/>

    
        <link rel="stylesheet" type="text/css" href='http://inc.t9.classistatic.com/1.1.288/css/all/Gumtree/PL/pl_PL/SeoViewPage.min.css'/>

    
    <link rel="publisher" href="" />
    <link rel="shortcut icon" type="image/png" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="shortcut icon" type="image/x-icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="shortcut icon" type="image/vnd.microsoft.icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="apple-touch-icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-iphone.png"/>
    <link rel="apple-touch-icon" sizes="72x72" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-ipad.png"/>
    <link rel="apple-touch-icon" sizes="114x114" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-iphone-retina.png"/>
    <link rel="apple-touch-icon" sizes="144x144" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-ipad-retina.png"/>



    
        <link rel="canonical" href="http://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/2-pok-47-m2-na-plaszowskiej-dla-3-osob-blisko-rm-grzegorzeckiego-lini-tramwajowej/1001691363990910474413109"/>
    
    
    
      
      
    
    <script>!function(e,t,n){function a(a){var m=o.document.createElement("link"),A=o.document.getElementsByTagName("script")[0],d=a&&r;m.rel="stylesheet",m.href=d?e:a?t:n,A.parentNode.insertBefore(m,A),d||(document.documentElement.className+=" no-svg")}if(3===arguments.length){var o=window,r=!(!o.document.createElementNS||!o.document.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect||!document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image","1.1")||window.opera&&-1===navigator.userAgent.indexOf("Chrome")),m=new o.Image;m.onerror=function(){a(!1)},m.onload=function(){a(1===m.width&&1===m.height)},m.src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="}}
    ("http://inc.t9.classistatic.com/1.1.288/css/icons.data.svg_pl_PL.css","http://inc.t9.classistatic.com/1.1.288/css/icons.data.png_pl_PL.css","http://inc.t9.classistatic.com/1.1.288/css/icons.fallback_pl_PL.css");</script>

    <noscript>
       <link href="http://inc.t9.classistatic.com/1.1.288/css/icons.fallback_pl_PL.css" rel="stylesheet">
       <style type="text/css">
            .jsOnly {display:none !important;}
            .nonJsOnlyInlineBlock{display:inline-block !important;}
            .nonJsOnlyBlock {display:block !important;}
            .nonJsOnlyInline {display:inline !important;}
       </style>
    </noscript>

    
    
      

            <script>
            var dataLayer = dataLayer || [];
            dataLayer.push({});(function(l) {
                var dl=l[0];
                dl["p"]={};
                     dl["p"]["t"] = "VIP";
                     dl["p"]["pl"] = "BOLT-RUI";
                     dl["p"]["v"] = "1.1.288";
                     dl["p"]["lng"] ="pl_PL";
                     
                dl["u"]={};
                dl["u"]["tg"]={};
                     
                     
                     
                     
                      
                     
                     
                     
                    
                dl["c"]={};
                dl["c"]["c"]={};
                      dl["c"]["c"]["id"] = "9008";
                     dl["c"]["l0"]={};dl["c"]["l0"]["id"]="0";
                     dl["c"]["l1"]={};dl["c"]["l1"]["id"]="2";
                     dl["c"]["l2"]={};dl["c"]["l2"]["id"]="9008";
                     
                     
                dl["l"]={};
                dl["l"]["c"]={};
                      dl["l"]["c"]["id"] = "3200208";
                     dl["l"]["l0"]={};dl["l"]["l0"]["id"]="202";
                     dl["l"]["l1"]={};dl["l"]["l1"]["id"]="3200003";
                     dl["l"]["l2"]={};dl["l"]["l2"]["id"]="3200208";
                     
                     

             
      dl["a"]={};
        dl["a"]["id"] ="169136399";  
        dl["a"]["cdt"] ="1467057981"; 
        dl["a"]["lpdt"] =""; 


            })(dataLayer);

                    //gtm script
                     (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push(
                             {'gtm.start': new Date().getTime(),event:'gtm.js'}
                     );var f=d.getElementsByTagName(s)[0],
                             j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                             '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                     })(window,document,'script','dataLayer','GTM-KSFR4N');
       </script>
      
    
    <script>
        var Bolt = Bolt || {};
        Bolt.BASEJSURL = "http://inc.t9.classistatic.com/1.1.288/js/";
        Bolt.BASECSSURL = "http://inc.t9.classistatic.com/1.1.288/css/";
        Bolt.BASEIMAGEURL = "http://inc.t9.classistatic.com/1.1.288/images/";
        Bolt.BRANDNAME = "Gumtree";
        Bolt.COUNTRY = "PL";
        Bolt.DECIMAL = ",";
        Bolt.PLACEHOLDER = ".";
        Bolt.LOCALE = "pl_PL";
        Bolt.LOCALIZEAPIROOTURL = "/rui-api/localize/rui/pl_PL";
    </script>
    
        <input id='ga-account' type='hidden' value='' />
        <input id='ga-domain' type='hidden' value='' />
        <script type="text/javascript">
            var _gaq = _gaq || [];
        
            
                _gaq.push(['siteTracker._setAccount', 'UA-9157637-1']);
                _gaq.push(['siteTracker._setAllowAnchor', true]);
                _gaq.push(['siteTracker._setDomainName', '.gumtree.pl']);
                
                    _gaq.push(['siteTracker._addIgnoredRef', 'gumtree.pl']);
                
                _gaq.push(['siteTracker._setSessionCookieTimeout', 1800000]);
                _gaq.push(['siteTracker._setCampaignCookieTimeout', 15768000000]);
                _gaq.push(['siteTracker._setVisitorCookieTimeout', 63072000000]);
                _gaq.push(['siteTracker._trackPageview']);

                (function() {
                    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
                    //ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                })();


            
        
        </script>
    

    

    

</head>
<body>
    
<div id="cookieWarning">
    <div class="messageContainer">
        Aby zapewnić najwyższą jakość usług i wygodne korzystanie z serwisu, używamy informacji zapisanych w przeglądarce za pomocą plików cookies (pol.: ciasteczek). Korzystając z serwisu wyrażasz zgodę na stosowanie plików <a href="http://pomoc.gumtree.pl/PL/articles/pl/KB_Article/Cookies" target="_blank">cookies</a>. W każdej chwili możesz je zablokować korzystając z ustawień swojej przeglądarki internetowej.
        <a class="accept icon-gl-message-close" style="width:15px;height:15px;margin-top:12px"></a>
    </div>
</div>

    
        <noscript>
            <iframe src="//www.googletagmanager.com/ns.html?id=GTM-KSFR4N"
              height="0" width="0" style="display:none;visibility:hidden">
            </iframe>
        </noscript>
    
     

    <noscript>
        <div class="js-message-error">
            <div>
                <span class="icon-warning-sign"></span>
                <div class="no-js pl_PL message"></div>
            </div>
        </div>
    </noscript>


    <div class="viewport" id="div-gpt-oop">

    <div class="header">
    <!-- mobile:false -->
    <header>
        <div class="wrap">
            <div class="elements">
                <div class="left">

                    
                    

<div class="logo">
    <a href="http://www.gumtree.pl/">
        
            
                <img class="logo" src="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/logo.png" alt='Darmowe Ogłoszenia' />
            
        
    </a>
</div>


                </div>
                <div class="right ">


                    


                    
                    
    <div class="post">
        <a class="sudo-link sudo-link post-btn postcommercial" data-gtm="pc|PostAdBegin" href="/post.html">
            <span>
                
                    Dodaj ogłoszenie
                
            </span>
        </a>
    </div>

                    

                    
                    


                    
                    
<div class="nav">
    <nav>




        
        




<div class="profile" aria-haspopup="true">
    <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nqf.ugzy">
        <span class="icon  "
              style="
               ">
            <span class="icon-header-profile-out"></span>
            <span class="icon-header-profile-over"></span>
        </span>
        <span class="label">Moje Gumtree</span>
    </span>
</div>
<div class="clear"></div>

        




        <ul>
            
            
                
                    <li>
                        <span class="sudo-link sudo-link-toConvert" data-o-uri="/ybtva.ugzy">Zaloguj się</span>
                    </li>
                
            

            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zljngpuyvfg.ugzy">Zachowane ogłoszenia</span>
            </li>

            
            
            
            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nyregf.ugzy">Moje powiadomienia</span>
            </li>

            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nqf.ugzy">Moje ogłoszenia</span>
            </li>

            
            
                <li>
                    <span class="sudo-link menu-text sudo-link-toConvert"  data-gtm="pc|FeatureAdBegin"  data-o-uri="/zl/cebzbgr.ugzy">Wypromuj ogłoszenia</span>
                </li>
            

            

            
            

            
            

            
                <li>
                    <span class="sudo-link sudo-link-toConvert" data-o-uri="/ertvfgre.ugzy">Zarejestruj się</span>
                </li>
            

        </ul>
    </nav>
</div>
                    
                    
                    
    
        
            <div class="signin">
                <span class="sudo-link sudo-link-toConvert" data-o-uri="/ybtva.ugzy">Zaloguj się</span>
            </div>
        
    



                </div>
            </div>
        </div>
    </header>
</div>



<div class="postSection headerPost">
    <div class="header diff">
        <div class="right">
            <div class="post post-btn-wrap">
                <a class="sudo-link sudo-link post-btn postcommercial"  data-gtm="pc|PostAdBegin" href="/post.html">
                    <span class="long">Dodaj ogłoszenie</span>
                </a>
            </div>
        </div>
    </div>
    <div class="clear"></div>
</div>




    
    <div class="searchbar">
        <section role="search">
            <div class="wrap">


                <form action='/search.html?page=1' class="has-location-true"
                        data-instant-search="false"
                        data-clear-searches-message='Wyczyść'
                        data-saved-search="true"
                        data-auto-complete="true"
                        data-auto-complete-api="http://cache.gumtree.pl/rui-api/autocomplete/model/pl_PL/{catId}/{locId}/{value}">
                    <fieldset>


                        
                        <div class="keyword">
    <input tabindex="1" type="text" name="q" value="" placeholder='Czego szukasz?' autocomplete="off" />
</div>
                        


                        
                        <div class="category">
    <span class="icon main-icon">
        <span class='icon-header-categories'></span>
    </span>
    <input tabindex="2" type="text" data-all='Wszystkie kategorie' placeholder='Kategoria' value="" autocomplete="off" disabled="disabled" readonly="readonly" />
    <input type="hidden" name="catId" value="" />
    <!--[if (IE 8)&!(IEMobile)]>
        <span class="icon-caret-down"></span>
    <![endif]-->
    
        <script type="text/plain">{"children":[{"children":[{"children":[],"localizedName":"pokoje do wynajęcia","id":9000},{"children":[],"localizedName":"mieszkania i domy do wynajęcia","id":9008},{"children":[],"localizedName":"mieszkania i domy - sprzedam","id":9073},{"children":[],"localizedName":"działki","id":9194},{"children":[],"localizedName":"krótki termin i domki letniskowe","id":9074},{"children":[],"localizedName":"lokal i biuro","id":9072},{"children":[],"localizedName":"parking i garaż","id":9071},{"children":[],"localizedName":"kupię mieszkanie, dom, lokal, działkę","id":9772},{"children":[],"localizedName":"szukam mieszkania do wynajęcia","id":9773},{"children":[],"localizedName":"szukam pokoju do wynajęcia","id":9774}],"localizedName":"Nieruchomości","id":2},{"children":[{"children":[],"localizedName":"samochody osobowe","id":9026},{"children":[],"localizedName":"części i akcesoria samochodowe","id":9636},{"children":[],"localizedName":"samochody dostawcze","id":9027},{"children":[],"localizedName":"motocykle i skutery","id":9028},{"children":[],"localizedName":"części i akcesoria do motocykli","id":9634},{"children":[],"localizedName":"ciągniki i maszyny rolnicze","id":9154},{"children":[],"localizedName":"ciężki sprzęt","id":9622},{"children":[],"localizedName":"przyczepy i naczepy","id":9155},{"children":[],"localizedName":"quady, atv i inne","id":9621},{"children":[],"localizedName":"części i akcesoria do innych pojazdów","id":9635},{"children":[],"localizedName":"kupię samochód","id":9763},{"children":[],"localizedName":"kupię motocykl, skuter, pojazd","id":9764},{"children":[],"localizedName":"kupię części, akcesoria samochodowe","id":9765},{"children":[],"localizedName":"kupię części, akcesoria do innych pojazdów","id":9766}],"localizedName":"Motoryzacja","id":5},{"children":[{"children":[],"localizedName":"motorówki","id":9219},{"children":[],"localizedName":"skutery wodne","id":9222},{"children":[],"localizedName":"żaglówki","id":9221},{"children":[],"localizedName":"kajaki i pontony","id":9220},{"children":[],"localizedName":"silniki do łodzi","id":9223},{"children":[],"localizedName":"akcesoria do łodzi","id":9224},{"children":[],"localizedName":"inne pojazdy wodne","id":9225},{"children":[],"localizedName":"łodzie wiosłowe","id":9226},{"children":[],"localizedName":"kupię łódź, części, akcesoria","id":9787}],"localizedName":"Łodzie i Pojazdy wodne","id":9218},{"children":[{"children":[],"localizedName":"audio i hi-fi","id":9260},{"children":[],"localizedName":"cesje","id":9353},{"children":[],"localizedName":"fotografia i video","id":9281},{"children":[],"localizedName":"gry video i konsole","id":9265},{"children":[],"localizedName":"komputery i software","id":9238},{"children":[],"localizedName":"radiokomunikacja","id":9352},{"children":[],"localizedName":"tablety i bookreadery","id":9259},{"children":[],"localizedName":"telefony i akcesoria","id":9247},{"children":[],"localizedName":"telewizory i odtwarzacze","id":9276},{"children":[],"localizedName":"elektronika inne","id":9286},{"children":[],"localizedName":"kupię sprzęt elektroniczny","id":9767}],"localizedName":"Elektronika","id":9237},{"children":[{"children":[],"localizedName":"akwarystyka","id":9612},{"children":[],"localizedName":"koty i kocięta","id":9125},{"children":[],"localizedName":"psy i szczenięta","id":9131},{"children":[],"localizedName":"ptaki","id":9617},{"children":[],"localizedName":"inne zwierzaki","id":9126},{"children":[],"localizedName":"zwierzęta gospodarskie","id":9618},{"children":[],"localizedName":"zgubiono lub znaleziono","id":9128},{"children":[],"localizedName":"akcesoria dla zwierząt","id":9129},{"children":[],"localizedName":"usługi dla zwierząt","id":9130},{"children":[],"localizedName":"kupię zwierzaka","id":9775},{"children":[],"localizedName":"szukam akcesoriów, usług dla zwierząt","id":9776}],"localizedName":"Zwierzaki","id":9124},{"children":[{"children":[],"localizedName":"drobne pytania i hobby","id":9030},{"children":[],"localizedName":"sport, taniec i partnerzy do gry","id":9032},{"children":[],"localizedName":"zespoły i muzycy","id":9033},{"children":[],"localizedName":"wolontariat","id":9227},{"children":[],"localizedName":"wydarzenia lokalne","id":9228},{"children":[],"localizedName":"wymiana umiejętności","id":9035},{"children":[],"localizedName":"zgubiono lub znaleziono","id":9036},{"children":[],"localizedName":"przejazdy","id":9037},{"children":[],"localizedName":"podróże","id":9038},{"children":[],"localizedName":"dziękuję","id":9039},{"children":[],"localizedName":"wyznania","id":9084},{"children":[],"localizedName":"szukam starych przyjaciół","id":9132}],"localizedName":"Społeczność","id":6},{"children":[{"children":[],"localizedName":"AGD","id":9366},{"children":[],"localizedName":"meble","id":9376},{"children":[],"localizedName":"narzędzia i materiały budowlane","id":9384},{"children":[],"localizedName":"ogród","id":9398},{"children":[],"localizedName":"produkty żywnościowe i napoje","id":9407},{"children":[],"localizedName":"wyposażenie wnętrz","id":9408},{"children":[],"localizedName":"inne do domu i ogrodu","id":9023},{"children":[],"localizedName":"kupię do ogrodu","id":9784},{"children":[],"localizedName":"kupię do domu","id":9783}],"localizedName":"Dom i Ogród","id":4},{"children":[{"children":[],"localizedName":"karty kolekcjonerskie","id":9673},{"children":[],"localizedName":"książki i poligrafia","id":9674},{"children":[],"localizedName":"lampy, świeczniki i  lustra","id":9675},{"children":[],"localizedName":"meble zabytkowe","id":9676},{"children":[],"localizedName":"medale i odznaczenia","id":9677},{"children":[],"localizedName":"monety i banknoty","id":9678},{"children":[],"localizedName":"obrazy i rzeźby","id":9679},{"children":[],"localizedName":"rękodzieło","id":9680},{"children":[],"localizedName":"zastawy kuchenne","id":9681},{"children":[],"localizedName":"zabytkowe tekstylia i dekoracje","id":9682},{"children":[],"localizedName":"zegary","id":9683},{"children":[],"localizedName":"znaczki pocztowe","id":9684},{"children":[],"localizedName":"inne kolekcje","id":9685},{"children":[],"localizedName":"kupię antyki, kolekcje","id":9762}],"localizedName":"Antyki i kolekcje","id":9672},{"children":[{"children":[],"localizedName":"artykuły szkolne","id":9468},{"children":[],"localizedName":"bezpieczeństwo i zdrowie dziecka","id":9460},{"children":[],"localizedName":"buty dla dzieci","id":9461},{"children":[],"localizedName":"chrzciny i komunie","id":9469},{"children":[],"localizedName":"ciąża i karmienie","id":9464},{"children":[],"localizedName":"foteliki - nosidełka","id":9462},{"children":[],"localizedName":"kąpiel i zdrowie","id":9470},{"children":[],"localizedName":"kojce i chodziki","id":9471},{"children":[],"localizedName":"meble i wystrój pokoju","id":9463},{"children":[],"localizedName":"rowerki i inne pojazdy","id":9472},{"children":[],"localizedName":"odzież dziecięca","id":9465},{"children":[],"localizedName":"wózki dla dzieci","id":9466},{"children":[],"localizedName":"zabawki","id":9467},{"children":[],"localizedName":"inne dla dziecka","id":9489},{"children":[],"localizedName":"kupię ubranka, buty dla dziecka","id":9780},{"children":[],"localizedName":"kupię zabawki","id":9781},{"children":[],"localizedName":"kupię inne dla dziecka","id":9782}],"localizedName":"Dla Dziecka","id":9459},{"children":[{"children":[],"localizedName":"akcesoria i galanteria","id":9542},{"children":[],"localizedName":"biżuteria i zegarki","id":9563},{"children":[],"localizedName":"obuwie damskie","id":9596},{"children":[],"localizedName":"obuwie męskie","id":9604},{"children":[],"localizedName":"odzież damska","id":9565},{"children":[],"localizedName":"odzież męska","id":9584},{"children":[],"localizedName":"odzież i obuwie robocze","id":9660},{"children":[],"localizedName":"pasmanteria","id":9549},{"children":[],"localizedName":"torebki i torby","id":9551},{"children":[],"localizedName":"inne ubrania","id":9553},{"children":[],"localizedName":"walizki i plecaki","id":9552},{"children":[],"localizedName":"kupię ubrania, buty","id":9769},{"children":[],"localizedName":"kupię inne z działu mody","id":9768}],"localizedName":"Moda","id":9541},{"children":[{"children":[],"localizedName":"zdrowie","id":9691},{"children":[],"localizedName":"kosmetyki","id":9697},{"children":[],"localizedName":"perfumy i dezodoranty","id":9698},{"children":[],"localizedName":"kupię produkty zdrowotne, kosmetyki","id":9786}],"localizedName":"Zdrowie i Uroda","id":9690},{"children":[{"children":[],"localizedName":"fitness i siłownia","id":9745},{"children":[],"localizedName":"sport","id":9746},{"children":[],"localizedName":"karty i gadżety sportowe","id":9753},{"children":[],"localizedName":"sprzęt turystyczny","id":9756},{"children":[],"localizedName":"kupię sprzęt fitness, do siłowni","id":9771},{"children":[],"localizedName":"kupię sprzęt sportowy","id":9770}],"localizedName":"Sport i Fitness","id":9706},{"children":[{"children":[],"localizedName":"bilety","id":9491},{"children":[],"localizedName":"instrumenty i akcesoria muzyczne","id":9496},{"children":[],"localizedName":"komiksy i czasopisma","id":9497},{"children":[],"localizedName":"książki","id":9498},{"children":[],"localizedName":"CD, kasety i płyty","id":9514},{"children":[],"localizedName":"filmy i DVD","id":9513},{"children":[],"localizedName":"gry planszowe i puzzle","id":9515},{"children":[],"localizedName":"kupię instrument muzyczny","id":9777},{"children":[],"localizedName":"kupię bilet","id":9778},{"children":[],"localizedName":"kupię inne z działu muzyka i rozrywka","id":9779}],"localizedName":"Muzyka i Rozrywka","id":9490},{"children":[{"children":[],"localizedName":"bar, restauracja i gastronomia","id":9056},{"children":[],"localizedName":"biuro i administracja","id":9052},{"children":[],"localizedName":"praca na budowie i pracownicy fizyczni","id":9142},{"children":[],"localizedName":"fachowcy","id":9203},{"children":[],"localizedName":"finanse i księgowość","id":9050},{"children":[],"localizedName":"grafika i web design","id":9140},{"children":[],"localizedName":"hostessy, modele i aktorzy","id":9141},{"children":[],"localizedName":"hr, kadry i rekrutacja","id":9053},{"children":[],"localizedName":"inżynierowie, technicy i architekci","id":9094},{"children":[],"localizedName":"kierowcy i kurierzy","id":9097},{"children":[],"localizedName":"kontrola i inwentaryzacja","id":9208},{"children":[],"localizedName":"krawiectwo i moda","id":9204},{"children":[],"localizedName":"magazynier","id":9619},{"children":[],"localizedName":"marketing, media i pr","id":9048},{"children":[],"localizedName":"mlm","id":9532},{"children":[],"localizedName":"nauczyciele i edukacja","id":9060},{"children":[],"localizedName":"obsługa klienta i call center","id":9098},{"children":[],"localizedName":"ochrona","id":9200},{"children":[],"localizedName":"opiekunki i nianie","id":9059},{"children":[],"localizedName":"pielęgnacja i uroda","id":9054},{"children":[],"localizedName":"praca dla studentów","id":9206},{"children":[],"localizedName":"praca na produkcji","id":9620},{"children":[],"localizedName":"praca w hotelu","id":9058},{"children":[],"localizedName":"prawo i prokuratura","id":9049},{"children":[],"localizedName":"programiści, informatyka i internet","id":9005},{"children":[],"localizedName":"służba zdrowia i farmacja","id":9055},{"children":[],"localizedName":"spedycja","id":9205},{"children":[],"localizedName":"sport i fitness","id":9202},{"children":[],"localizedName":"sprzątanie i pomoc domowa","id":9138},{"children":[],"localizedName":"sprzedaż, handel  i praca w sklepie","id":9061},{"children":[],"localizedName":"turystyka","id":9207},{"children":[],"localizedName":"ulotki","id":9201},{"children":[],"localizedName":"weterynaria i rolnictwo","id":9095},{"children":[],"localizedName":"video i fotografia","id":9212},{"children":[],"localizedName":"praca inne","id":9099}],"localizedName":"Oferty Pracy","id":8},{"children":[{"children":[],"localizedName":"gastronomia","id":9291},{"children":[],"localizedName":"biuro i administracja","id":9292},{"children":[],"localizedName":"pracownicy fizyczni","id":9293},{"children":[],"localizedName":"specjaliści i technicy","id":9294},{"children":[],"localizedName":"kierowcy i kurierzy","id":9300},{"children":[],"localizedName":"marketing, reklama i PR","id":9304},{"children":[],"localizedName":"opiekunki i edukacja","id":9305},{"children":[],"localizedName":"ochrona","id":9306},{"children":[],"localizedName":"pielęgnacja i uroda","id":9308},{"children":[],"localizedName":"sprzedaż i praca w sklepie","id":9311},{"children":[],"localizedName":"szukam pracy studenckiej","id":9309},{"children":[],"localizedName":"turystyka","id":9312},{"children":[],"localizedName":"praca inne","id":9313}],"localizedName":"Szukający Zatrudnienia","id":9290},{"children":[{"children":[],"localizedName":"biura podróży","id":9150},{"children":[],"localizedName":"współpraca biznesowa","id":9325},{"children":[],"localizedName":"catering","id":9554},{"children":[],"localizedName":"usługi finansowe","id":9066},{"children":[],"localizedName":"fotografia i video","id":9146},{"children":[],"localizedName":"graficy i usługi IT","id":9234},{"children":[],"localizedName":"hurt i handel","id":9065},{"children":[],"localizedName":"komputery serwis i handel","id":9102},{"children":[],"localizedName":"usługi kurierskie","id":9337},{"children":[],"localizedName":"nauka i edukacja","id":9063},{"children":[],"localizedName":"mechanika, autoskup, pomoc drogowa","id":9145},{"children":[],"localizedName":"media i reklama","id":9217},{"children":[],"localizedName":"muzycy i artyści","id":9148},{"children":[],"localizedName":"ogrodnictwo","id":9214},{"children":[],"localizedName":"opieka i agencje niań","id":9152},{"children":[],"localizedName":"pielęgnacja i uroda","id":9064},{"children":[],"localizedName":"usługi prawne","id":9233},{"children":[],"localizedName":"przeprowadzki i transport towarów","id":9144},{"children":[],"localizedName":"przyjęcia, śluby, komunie","id":9104},{"children":[],"localizedName":"remont i budowa","id":9101},{"children":[],"localizedName":"serwis i montaż","id":9236},{"children":[],"localizedName":"sport i fitness","id":9151},{"children":[],"localizedName":"sprzątanie","id":9149},{"children":[],"localizedName":"taxi i przewozy osobowe","id":9147},{"children":[],"localizedName":"telefony","id":9341},{"children":[],"localizedName":"tłumaczenia i redakcja tekstu","id":9216},{"children":[],"localizedName":"utylizacja","id":9213},{"children":[],"localizedName":"wypożyczalnie","id":9215},{"children":[],"localizedName":"zdrowie","id":9235},{"children":[],"localizedName":"inne usługi","id":9105},{"children":[],"localizedName":"szukam usług finansowych","id":9759},{"children":[],"localizedName":"szukam usług budowlanych","id":9760},{"children":[],"localizedName":"szukam innych usług","id":9761},{"children":[],"localizedName":"szukam kursu, lekcji, korepetycji","id":9758}],"localizedName":"Usługi","id":9}],"localizedName":"Wszystkie kategorie","id":0}</script>
    
</div>
                        


                        
                        
    <div class="location">
        <span class="icon main-icon">
            <span class='icon-header-location-pin'></span>
        </span>
        <input tabindex="3" type="text" data-all='Polska' placeholder='Polska' value='Polska' autocomplete="off" disabled="disabled" readonly="readonly" />
        <input type="hidden" name="locId" value="" />
        <!--[if (IE 8)&!(IEMobile)]>
        <span class="icon-caret-down"></span>
        <![endif]-->
        
            <script type="text/plain">{"children":[{"children":[{"children":[],"localizedName":"Bardo","id":3200595},{"children":[],"localizedName":"Bielawa","id":3200085},{"children":[],"localizedName":"Bierutów","id":3200435},{"children":[],"localizedName":"Bogatynia","id":3200086},{"children":[],"localizedName":"Boguszów-Gorce","id":3200437},{"children":[],"localizedName":"Bolesławiec","id":3200087},{"children":[],"localizedName":"Bolków","id":3200436},{"children":[],"localizedName":"Brzeg Dolny","id":3200438},{"children":[],"localizedName":"Bystrzyca Kłodzka","id":3200439},{"children":[],"localizedName":"Chocianów","id":3200440},{"children":[],"localizedName":"Chojnów","id":3200441},{"children":[],"localizedName":"Długołęka","id":3200609},{"children":[],"localizedName":"Duszniki Zdrój","id":3200594},{"children":[],"localizedName":"Dzierżoniów","id":3200088},{"children":[],"localizedName":"Głogów","id":3200089},{"children":[],"localizedName":"Góra","id":3200090},{"children":[],"localizedName":"Gryfów Śląski","id":3200442},{"children":[],"localizedName":"Jawor","id":3200091},{"children":[],"localizedName":"Jelcz-Laskowice","id":3200443},{"children":[],"localizedName":"Jelenia Góra","id":3200092},{"children":[],"localizedName":"Kamienna Góra","id":3200093},{"children":[],"localizedName":"Karpacz","id":3200094},{"children":[],"localizedName":"Kąty Wrocławskie","id":3200621},{"children":[],"localizedName":"Kłodzko","id":3200095},{"children":[],"localizedName":"Kowary","id":3200444},{"children":[],"localizedName":"Kudowa-Zdrój","id":3200445},{"children":[],"localizedName":"Legnica","id":3200096},{"children":[],"localizedName":"Lubań","id":3200097},{"children":[],"localizedName":"Lubin","id":3200098},{"children":[],"localizedName":"Lubomierz","id":3200597},{"children":[],"localizedName":"Lwówek Śląski","id":3200099},{"children":[],"localizedName":"Marciszów","id":3200598},{"children":[],"localizedName":"Międzylesie","id":3200599},{"children":[],"localizedName":"Milicz","id":3200100},{"children":[],"localizedName":"Nowa Ruda","id":3200101},{"children":[],"localizedName":"Oborniki Śląskie","id":3200446},{"children":[],"localizedName":"Oleśnica","id":3200103},{"children":[],"localizedName":"Oława","id":3200102},{"children":[],"localizedName":"Piechowice","id":3200434},{"children":[],"localizedName":"Pieszyce","id":3200447},{"children":[],"localizedName":"Piława Górna","id":3200448},{"children":[],"localizedName":"Polanica-Zdrój","id":3200104},{"children":[],"localizedName":"Polkowice","id":3200105},{"children":[],"localizedName":"Sobótka","id":3200600},{"children":[],"localizedName":"Strzegom","id":3200449},{"children":[],"localizedName":"Strzelin","id":3200107},{"children":[],"localizedName":"Syców","id":3200450},{"children":[],"localizedName":"Szczawno-Zdrój","id":3200601},{"children":[],"localizedName":"Szklarska Poręba","id":3200106},{"children":[],"localizedName":"Środa Śląska","id":3200108},{"children":[],"localizedName":"Świdnica","id":3200109},{"children":[],"localizedName":"Świebodzice","id":3200110},{"children":[],"localizedName":"Trzebnica","id":3200111},{"children":[],"localizedName":"Wałbrzych","id":3200112},{"children":[],"localizedName":"Wołów","id":3200113},{"children":[],"localizedName":"Wrocław","id":3200114},{"children":[],"localizedName":"Ząbkowice Śląskie","id":3200115},{"children":[],"localizedName":"Zgorzelec","id":3200116},{"children":[],"localizedName":"Ziębice","id":3200451},{"children":[],"localizedName":"Złotoryja","id":3200117},{"children":[],"localizedName":"Żarów","id":3200452},{"children":[],"localizedName":"Żmigród","id":3200453}],"localizedName":"Dolnośląskie","id":3200007},{"children":[{"children":[],"localizedName":"Aleksandrów Kujawski","id":3200118},{"children":[],"localizedName":"Barcin","id":3200454},{"children":[],"localizedName":"Brodnica","id":3200119},{"children":[],"localizedName":"Bydgoszcz","id":3200120},{"children":[],"localizedName":"Chełmno","id":3200121},{"children":[],"localizedName":"Chełmża","id":3200455},{"children":[],"localizedName":"Ciechocinek","id":3200456},{"children":[],"localizedName":"Gniewkowo","id":3200457},{"children":[],"localizedName":"Golub-Dobrzyń","id":3200122},{"children":[],"localizedName":"Grudziądz","id":3200123},{"children":[],"localizedName":"Inowrocław","id":3200124},{"children":[],"localizedName":"Janikowo","id":3200458},{"children":[],"localizedName":"Koronowo","id":3200459},{"children":[],"localizedName":"Kruszwica","id":3200460},{"children":[],"localizedName":"Lipno","id":3200125},{"children":[],"localizedName":"Mogilno","id":3200126},{"children":[],"localizedName":"Nakło nad Notecią","id":3200127},{"children":[],"localizedName":"Radziejów","id":3200128},{"children":[],"localizedName":"Rypin","id":3200129},{"children":[],"localizedName":"Sępólno Krajeńskie","id":3200130},{"children":[],"localizedName":"Solec Kujawski","id":3200461},{"children":[],"localizedName":"Strzelno","id":3200462},{"children":[],"localizedName":"Szubin","id":3200463},{"children":[],"localizedName":"Świecie","id":3200131},{"children":[],"localizedName":"Toruń","id":3200132},{"children":[],"localizedName":"Tuchola","id":3200133},{"children":[],"localizedName":"Wąbrzeźno","id":3200134},{"children":[],"localizedName":"Więcbork","id":3200464},{"children":[],"localizedName":"Włocławek","id":3200135},{"children":[],"localizedName":"Żnin","id":3200136}],"localizedName":"Kujawsko - pomorskie","id":3200075},{"children":[{"children":[],"localizedName":"Bełżyce","id":3200465},{"children":[],"localizedName":"Biała Podlaska","id":3200137},{"children":[],"localizedName":"Biłgoraj","id":3200138},{"children":[],"localizedName":"Chełm","id":3200139},{"children":[],"localizedName":"Dęblin","id":3200466},{"children":[],"localizedName":"Hrubieszów","id":3200140},{"children":[],"localizedName":"Janów Lubelski","id":3200141},{"children":[],"localizedName":"Krasnystaw","id":3200142},{"children":[],"localizedName":"Kraśnik","id":3200143},{"children":[],"localizedName":"Lubartów","id":3200144},{"children":[],"localizedName":"Lublin","id":3200145},{"children":[],"localizedName":"Łęczna","id":3200146},{"children":[],"localizedName":"Łuków","id":3200147},{"children":[],"localizedName":"Międzyrzec Podlaski","id":3200467},{"children":[],"localizedName":"Opole Lubelskie","id":3200148},{"children":[],"localizedName":"Parczew","id":3200149},{"children":[],"localizedName":"Poniatowa","id":3200468},{"children":[],"localizedName":"Puławy","id":3200150},{"children":[],"localizedName":"Radzyń Podlaski","id":3200151},{"children":[],"localizedName":"Ryki","id":3200152},{"children":[],"localizedName":"Świdnik","id":3200153},{"children":[],"localizedName":"Terespol","id":3200469},{"children":[],"localizedName":"Tomaszów Lubelski","id":3200154},{"children":[],"localizedName":"Włodawa","id":3200155},{"children":[],"localizedName":"Zamość","id":3200156}],"localizedName":"Lubelskie","id":3200076},{"children":[{"children":[],"localizedName":"Drezdenko","id":3200158},{"children":[],"localizedName":"Gorzów Wielkopolski","id":3200157},{"children":[],"localizedName":"Gubin","id":3200159},{"children":[],"localizedName":"Kostrzyn nad Odrą","id":3200470},{"children":[],"localizedName":"Kożuchów","id":3200471},{"children":[],"localizedName":"Krosno Odrzańskie","id":3200160},{"children":[],"localizedName":"Lubsko","id":3200161},{"children":[],"localizedName":"Międzyrzecz","id":3200162},{"children":[],"localizedName":"Nowa Sól","id":3200163},{"children":[],"localizedName":"Rzepin","id":3200472},{"children":[],"localizedName":"Skwierzyna","id":3200473},{"children":[],"localizedName":"Słubice","id":3200164},{"children":[],"localizedName":"Strzelce Krajeńskie","id":3200165},{"children":[],"localizedName":"Sulechów","id":3200166},{"children":[],"localizedName":"Sulęcin","id":3200167},{"children":[],"localizedName":"Szprotawa","id":3200168},{"children":[],"localizedName":"Świebodzin","id":3200169},{"children":[],"localizedName":"Witnica","id":3200474},{"children":[],"localizedName":"Wschowa","id":3200170},{"children":[],"localizedName":"Zielona Góra","id":3200171},{"children":[],"localizedName":"Żagań","id":3200172},{"children":[],"localizedName":"Żary","id":3200173}],"localizedName":"Lubuskie","id":3200077},{"children":[{"children":[],"localizedName":"Aleksandrów Łódzki","id":3200174},{"children":[],"localizedName":"Andrespol","id":3200588},{"children":[],"localizedName":"Bełchatów","id":3200175},{"children":[],"localizedName":"Brzeziny","id":3200176},{"children":[],"localizedName":"Głowno","id":3200177},{"children":[],"localizedName":"Koluszki","id":3200475},{"children":[],"localizedName":"Konstantynów Łódzki","id":3200178},{"children":[],"localizedName":"Kutno","id":3200179},{"children":[],"localizedName":"Łask","id":3200180},{"children":[],"localizedName":"Łęczyca","id":3200181},{"children":[],"localizedName":"Łowicz","id":3200182},{"children":[],"localizedName":"Łódź","id":3200183},{"children":[],"localizedName":"Opoczno","id":3200184},{"children":[],"localizedName":"Ozorków","id":3200185},{"children":[],"localizedName":"Pabianice","id":3200186},{"children":[],"localizedName":"Pajęczno","id":3200187},{"children":[],"localizedName":"Piotrków Trybunalski","id":3200188},{"children":[],"localizedName":"Poddębice","id":3200189},{"children":[],"localizedName":"Radomsko","id":3200190},{"children":[],"localizedName":"Rawa Mazowiecka","id":3200191},{"children":[],"localizedName":"Sieradz","id":3200192},{"children":[],"localizedName":"Skierniewice","id":3200193},{"children":[],"localizedName":"Tomaszów Mazowiecki","id":3200194},{"children":[],"localizedName":"Tuszyn","id":3200476},{"children":[],"localizedName":"Wieluń","id":3200195},{"children":[],"localizedName":"Wieruszów","id":3200196},{"children":[],"localizedName":"Zduńska Wola","id":3200197},{"children":[],"localizedName":"Zelów","id":3200477},{"children":[],"localizedName":"Zgierz","id":3200198},{"children":[],"localizedName":"Żychlin","id":3200478}],"localizedName":"Łódzkie","id":3200004},{"children":[{"children":[],"localizedName":"Alwernia","id":3200610},{"children":[],"localizedName":"Andrychów","id":3200199},{"children":[],"localizedName":"Bochnia","id":3200200},{"children":[],"localizedName":"Brzesko","id":3200201},{"children":[],"localizedName":"Brzeszcze","id":3200479},{"children":[],"localizedName":"Bukowina Tatrzańska","id":3200202},{"children":[],"localizedName":"Bukowno","id":3200480},{"children":[],"localizedName":"Chełmek","id":3200481},{"children":[],"localizedName":"Chrzanów","id":3200203},{"children":[],"localizedName":"Czorsztyn","id":3200611},{"children":[],"localizedName":"Dąbrowa Tarnowska","id":3200204},{"children":[],"localizedName":"Gorlice","id":3200205},{"children":[],"localizedName":"Kęty","id":3200206},{"children":[],"localizedName":"Kocmyrzów","id":3200618},{"children":[],"localizedName":"Kościelisko","id":3200207},{"children":[],"localizedName":"Kraków","id":3200208},{"children":[],"localizedName":"Krościenko nad Dunajcem","id":3200491},{"children":[],"localizedName":"Krynica-Zdrój","id":3200209},{"children":[],"localizedName":"Krzeszowice","id":3200482},{"children":[],"localizedName":"Libiąż","id":3200483},{"children":[],"localizedName":"Limanowa","id":3200210},{"children":[],"localizedName":"Miechów","id":3200211},{"children":[],"localizedName":"Mszana Dolna","id":3200484},{"children":[],"localizedName":"Myślenice","id":3200212},{"children":[],"localizedName":"Niedzica","id":3200612},{"children":[],"localizedName":"Niepołomice","id":3200485},{"children":[],"localizedName":"Nowy Sącz","id":3200213},{"children":[],"localizedName":"Nowy Targ","id":3200214},{"children":[],"localizedName":"Olkusz","id":3200215},{"children":[],"localizedName":"Oświęcim","id":3200216},{"children":[],"localizedName":"Piwniczna-Zdrój","id":3200486},{"children":[],"localizedName":"Proszowice","id":3200217},{"children":[],"localizedName":"Rabka-Zdrój","id":3200487},{"children":[],"localizedName":"Skawina","id":3200218},{"children":[],"localizedName":"Słomniki","id":3200619},{"children":[],"localizedName":"Stary Sącz","id":3200488},{"children":[],"localizedName":"Sucha Beskidzka","id":3200219},{"children":[],"localizedName":"Szczawnica","id":3200220},{"children":[],"localizedName":"Tarnów","id":3200221},{"children":[],"localizedName":"Trzebinia","id":3200222},{"children":[],"localizedName":"Tuchów","id":3200489},{"children":[],"localizedName":"Wadowice","id":3200223},{"children":[],"localizedName":"Wieliczka","id":3200224},{"children":[],"localizedName":"Wolbrom","id":3200490},{"children":[],"localizedName":"Zakopane","id":3200225}],"localizedName":"Małopolskie","id":3200003},{"children":[{"children":[],"localizedName":"Pd - wsch powiaty","id":3200043},{"children":[],"localizedName":"Pd - zach powiaty","id":3200044},{"children":[],"localizedName":"Pn - wsch powiaty","id":3200036},{"children":[],"localizedName":"Pn - zach powiaty","id":3200041},{"children":[],"localizedName":"Południowe powiaty","id":3200042},{"children":[],"localizedName":"Północne powiaty","id":3200027},{"children":[],"localizedName":"Warszawa","id":3200008},{"children":[],"localizedName":"Wschodnie powiaty","id":3200045},{"children":[],"localizedName":"Zachodnie powiaty","id":3200046}],"localizedName":"Mazowieckie","id":3200001},{"children":[{"children":[],"localizedName":"Brzeg","id":3200226},{"children":[],"localizedName":"Głubczyce","id":3200227},{"children":[],"localizedName":"Grodków","id":3200526},{"children":[],"localizedName":"Kędzierzyn-Koźle","id":3200228},{"children":[],"localizedName":"Kluczbork","id":3200229},{"children":[],"localizedName":"Krapkowice","id":3200230},{"children":[],"localizedName":"Namysłów","id":3200231},{"children":[],"localizedName":"Niemodlin","id":3200527},{"children":[],"localizedName":"Nysa","id":3200232},{"children":[],"localizedName":"Olesno","id":3200233},{"children":[],"localizedName":"Opole","id":3200234},{"children":[],"localizedName":"Ozimek","id":3200528},{"children":[],"localizedName":"Paczków","id":3200529},{"children":[],"localizedName":"Praszka","id":3200530},{"children":[],"localizedName":"Prószków","id":3200593},{"children":[],"localizedName":"Prudnik","id":3200235},{"children":[],"localizedName":"Strzelce Opolskie","id":3200236},{"children":[],"localizedName":"Zawadzkie","id":3200531},{"children":[],"localizedName":"Zdzieszowice","id":3200532}],"localizedName":"Opolskie","id":3200078},{"children":[{"children":[],"localizedName":"Brzozów","id":3200237},{"children":[],"localizedName":"Cisna","id":3200607},{"children":[],"localizedName":"Dębica","id":3200238},{"children":[],"localizedName":"Jarosław","id":3200239},{"children":[],"localizedName":"Jasło","id":3200240},{"children":[],"localizedName":"Kolbuszowa","id":3200241},{"children":[],"localizedName":"Krosno","id":3200242},{"children":[],"localizedName":"Lesko","id":3200243},{"children":[],"localizedName":"Leżajsk","id":3200244},{"children":[],"localizedName":"Lubaczów","id":3200245},{"children":[],"localizedName":"Łańcut","id":3200246},{"children":[],"localizedName":"Mielec","id":3200247},{"children":[],"localizedName":"Nisko","id":3200248},{"children":[],"localizedName":"Nowa Dęba","id":3200533},{"children":[],"localizedName":"Przemyśl","id":3200249},{"children":[],"localizedName":"Przeworsk","id":3200250},{"children":[],"localizedName":"Ropczyce","id":3200251},{"children":[],"localizedName":"Rzeszów","id":3200252},{"children":[],"localizedName":"Sanok","id":3200253},{"children":[],"localizedName":"Sędziszów Małopolski","id":3200534},{"children":[],"localizedName":"Stalowa Wola","id":3200254},{"children":[],"localizedName":"Strzebowiska","id":3200608},{"children":[],"localizedName":"Strzyżów","id":3200255},{"children":[],"localizedName":"Tarnobrzeg","id":3200256},{"children":[],"localizedName":"Ustrzyki Dolne","id":3200257}],"localizedName":"Podkarpackie","id":3200079},{"children":[{"children":[],"localizedName":"Augustów","id":3200258},{"children":[],"localizedName":"Białystok","id":3200259},{"children":[],"localizedName":"Bielsk Podlaski","id":3200260},{"children":[],"localizedName":"Czarna Białostocka","id":3200535},{"children":[],"localizedName":"Dąbrowa Białostocka","id":3200536},{"children":[],"localizedName":"Grajewo","id":3200261},{"children":[],"localizedName":"Hajnówka","id":3200262},{"children":[],"localizedName":"Kolno","id":3200263},{"children":[],"localizedName":"Łapy","id":3200264},{"children":[],"localizedName":"Łomża","id":3200265},{"children":[],"localizedName":"Mońki","id":3200266},{"children":[],"localizedName":"Sejny","id":3200267},{"children":[],"localizedName":"Siemiatycze","id":3200268},{"children":[],"localizedName":"Sokółka","id":3200269},{"children":[],"localizedName":"Suwałki","id":3200270},{"children":[],"localizedName":"Wasilków","id":3200537},{"children":[],"localizedName":"Wysokie Mazowieckie","id":3200271},{"children":[],"localizedName":"Zambrów","id":3200272}],"localizedName":"Podlaskie","id":3200080},{"children":[{"children":[],"localizedName":"Bytów","id":3200407},{"children":[],"localizedName":"Chojnice","id":3200408},{"children":[],"localizedName":"Czersk","id":3200539},{"children":[],"localizedName":"Człuchów","id":3200409},{"children":[],"localizedName":"Gdańsk","id":3200072},{"children":[],"localizedName":"Gdynia","id":3200073},{"children":[],"localizedName":"Gniew","id":3200543},{"children":[],"localizedName":"Hel","id":3200410},{"children":[],"localizedName":"Jastarnia","id":3200411},{"children":[],"localizedName":"Jastrzębia Góra","id":3200412},{"children":[],"localizedName":"Kartuzy","id":3200413},{"children":[],"localizedName":"Karwia","id":3200414},{"children":[],"localizedName":"Kościerzyna","id":3200415},{"children":[],"localizedName":"Krynica Morska","id":3200416},{"children":[],"localizedName":"Kwidzyn","id":3200417},{"children":[],"localizedName":"Lębork","id":3200419},{"children":[],"localizedName":"Łeba","id":3200418},{"children":[],"localizedName":"Malbork","id":3200420},{"children":[],"localizedName":"Miastko","id":3200538},{"children":[],"localizedName":"Nowy Dwór Gdański","id":3200421},{"children":[],"localizedName":"Pelplin","id":3200541},{"children":[],"localizedName":"Pępowo","id":3200589},{"children":[],"localizedName":"Prabuty","id":3200540},{"children":[],"localizedName":"Pruszcz Gdański","id":3200422},{"children":[],"localizedName":"Puck","id":3200423},{"children":[],"localizedName":"Reda","id":3200424},{"children":[],"localizedName":"Rumia","id":3200425},{"children":[],"localizedName":"Skarszewy","id":3200542},{"children":[],"localizedName":"Słupsk","id":3200426},{"children":[],"localizedName":"Sopot","id":3200074},{"children":[],"localizedName":"Starogard Gdański","id":3200427},{"children":[],"localizedName":"Stegna","id":3200428},{"children":[],"localizedName":"Sztum","id":3200429},{"children":[],"localizedName":"Sztutowo","id":3200544},{"children":[],"localizedName":"Tczew","id":3200430},{"children":[],"localizedName":"Ustka","id":3200431},{"children":[],"localizedName":"Wejherowo","id":3200432},{"children":[],"localizedName":"Władysławowo","id":3200433},{"children":[],"localizedName":"Żukowo","id":3200590}],"localizedName":"Pomorskie","id":3200005},{"children":[{"children":[],"localizedName":"Będzin","id":3200273},{"children":[],"localizedName":"Bielsko-Biała","id":3200274},{"children":[],"localizedName":"Bieruń","id":3200275},{"children":[],"localizedName":"Blachownia","id":3200545},{"children":[],"localizedName":"Brenna","id":3200605},{"children":[],"localizedName":"Bytom","id":3200277},{"children":[],"localizedName":"Chorzów","id":3200278},{"children":[],"localizedName":"Cieszyn","id":3200279},{"children":[],"localizedName":"Czechowice-Dziedzice","id":3200546},{"children":[],"localizedName":"Czeladź","id":3200547},{"children":[],"localizedName":"Czerwionka-Leszczyny","id":3200548},{"children":[],"localizedName":"Częstochowa","id":3200280},{"children":[],"localizedName":"Dąbrowa Górnicza","id":3200281},{"children":[],"localizedName":"Gliwice","id":3200282},{"children":[],"localizedName":"Imielin","id":3200549},{"children":[],"localizedName":"Jastrzębie-Zdrój","id":3200283},{"children":[],"localizedName":"Jaworzno","id":3200284},{"children":[],"localizedName":"Kalety","id":3200550},{"children":[],"localizedName":"Katowice","id":3200285},{"children":[],"localizedName":"Kłobuck","id":3200286},{"children":[],"localizedName":"Knurów","id":3200551},{"children":[],"localizedName":"Korbielów","id":3200604},{"children":[],"localizedName":"Lędziny","id":3200552},{"children":[],"localizedName":"Lubliniec","id":3200287},{"children":[],"localizedName":"Łaziska Górne","id":3200553},{"children":[],"localizedName":"Mikołów","id":3200288},{"children":[],"localizedName":"Milówka","id":3200606},{"children":[],"localizedName":"Mysłowice","id":3200289},{"children":[],"localizedName":"Myszków","id":3200290},{"children":[],"localizedName":"Orzesze","id":3200554},{"children":[],"localizedName":"Piekary Śląskie","id":3200291},{"children":[],"localizedName":"Poręba","id":3200555},{"children":[],"localizedName":"Pszczyna","id":3200292},{"children":[],"localizedName":"Pszów","id":3200556},{"children":[],"localizedName":"Pyskowice","id":3200557},{"children":[],"localizedName":"Racibórz","id":3200293},{"children":[],"localizedName":"Radlin","id":3200558},{"children":[],"localizedName":"Radzionków","id":3200559},{"children":[],"localizedName":"Ruda Śląska","id":3200294},{"children":[],"localizedName":"Rybnik","id":3200295},{"children":[],"localizedName":"Rydułtowy","id":3200560},{"children":[],"localizedName":"Siemianowice Śląskie","id":3200296},{"children":[],"localizedName":"Siewierz","id":3200602},{"children":[],"localizedName":"Skoczów","id":3200561},{"children":[],"localizedName":"Sosnowiec","id":3200297},{"children":[],"localizedName":"Szczyrk","id":3200299},{"children":[],"localizedName":"Świerklaniec","id":3200603},{"children":[],"localizedName":"Świętochłowice","id":3200298},{"children":[],"localizedName":"Tarnowskie Góry","id":3200300},{"children":[],"localizedName":"Tychy","id":3200301},{"children":[],"localizedName":"Ustroń","id":3200562},{"children":[],"localizedName":"Wisła","id":3200302},{"children":[],"localizedName":"Wodzisław Śląski","id":3200303},{"children":[],"localizedName":"Wojkowice","id":3200563},{"children":[],"localizedName":"Zabrze","id":3200304},{"children":[],"localizedName":"Zawiercie","id":3200305},{"children":[],"localizedName":"Żory","id":3200306},{"children":[],"localizedName":"Żywiec","id":3200307}],"localizedName":"Śląskie","id":3200002},{"children":[{"children":[],"localizedName":"Busko-Zdrój","id":3200308},{"children":[],"localizedName":"Jędrzejów","id":3200309},{"children":[],"localizedName":"Kazimierza Wielka","id":3200310},{"children":[],"localizedName":"Kielce","id":3200311},{"children":[],"localizedName":"Końskie","id":3200312},{"children":[],"localizedName":"Opatów","id":3200313},{"children":[],"localizedName":"Ostrowiec Świętokrzyski","id":3200314},{"children":[],"localizedName":"Pińczów","id":3200315},{"children":[],"localizedName":"Połaniec","id":3200564},{"children":[],"localizedName":"Sandomierz","id":3200316},{"children":[],"localizedName":"Skarżysko-Kamienna","id":3200317},{"children":[],"localizedName":"Starachowice","id":3200318},{"children":[],"localizedName":"Staszów","id":3200319},{"children":[],"localizedName":"Suchedniów","id":3200565},{"children":[],"localizedName":"Włoszczowa","id":3200320}],"localizedName":"Świętokrzyskie","id":3200082},{"children":[{"children":[],"localizedName":"Barczewo","id":3200613},{"children":[],"localizedName":"Bartoszyce","id":3200321},{"children":[],"localizedName":"Biskupiec","id":3200322},{"children":[],"localizedName":"Braniewo","id":3200323},{"children":[],"localizedName":"Dobre Miasto","id":3200324},{"children":[],"localizedName":"Działdowo","id":3200325},{"children":[],"localizedName":"Elbląg","id":3200326},{"children":[],"localizedName":"Ełk","id":3200327},{"children":[],"localizedName":"Giżycko","id":3200328},{"children":[],"localizedName":"Gołdap","id":3200329},{"children":[],"localizedName":"Górowo Iławieckie","id":3200615},{"children":[],"localizedName":"Iława","id":3200330},{"children":[],"localizedName":"Kętrzyn","id":3200331},{"children":[],"localizedName":"Lidzbark Warmiński","id":3200332},{"children":[],"localizedName":"Lubawa","id":3200566},{"children":[],"localizedName":"Mikołajki","id":3200333},{"children":[],"localizedName":"Morąg","id":3200567},{"children":[],"localizedName":"Mrągowo","id":3200334},{"children":[],"localizedName":"Nidzica","id":3200335},{"children":[],"localizedName":"Nowe Miasto Lubawskie","id":3200336},{"children":[],"localizedName":"Olecko","id":3200337},{"children":[],"localizedName":"Olsztyn","id":3200338},{"children":[],"localizedName":"Olsztynek","id":3200568},{"children":[],"localizedName":"Orneta","id":3200569},{"children":[],"localizedName":"Ostróda","id":3200339},{"children":[],"localizedName":"Pasłęk","id":3200570},{"children":[],"localizedName":"Pieniężno","id":3200616},{"children":[],"localizedName":"Pisz","id":3200340},{"children":[],"localizedName":"Ruciane-Nida","id":3200617},{"children":[],"localizedName":"Szczytno","id":3200341},{"children":[],"localizedName":"Węgorzewo","id":3200342}],"localizedName":"Warmińsko-mazurskie","id":3200083},{"children":[{"children":[],"localizedName":"Buk","id":3200587},{"children":[],"localizedName":"Chodzież","id":3200343},{"children":[],"localizedName":"Czarnków","id":3200344},{"children":[],"localizedName":"Gniezno","id":3200345},{"children":[],"localizedName":"Gostyń","id":3200346},{"children":[],"localizedName":"Grodzisk Wielkopolski","id":3200347},{"children":[],"localizedName":"Jarocin","id":3200348},{"children":[],"localizedName":"Jastrowie","id":3200571},{"children":[],"localizedName":"Kalisz","id":3200349},{"children":[],"localizedName":"Kępno","id":3200350},{"children":[],"localizedName":"Koło","id":3200351},{"children":[],"localizedName":"Konin","id":3200352},{"children":[],"localizedName":"Kostrzyn","id":3200572},{"children":[],"localizedName":"Kościan","id":3200353},{"children":[],"localizedName":"Kórnik","id":3200573},{"children":[],"localizedName":"Krotoszyn","id":3200354},{"children":[],"localizedName":"Leszno","id":3200355},{"children":[],"localizedName":"Luboń","id":3200356},{"children":[],"localizedName":"Międzychód","id":3200357},{"children":[],"localizedName":"Mosina","id":3200358},{"children":[],"localizedName":"Murowana Goślina","id":3200359},{"children":[],"localizedName":"Nowy Tomyśl","id":3200360},{"children":[],"localizedName":"Oborniki","id":3200361},{"children":[],"localizedName":"Opalenica","id":3200574},{"children":[],"localizedName":"Ostrów Wielkopolski","id":3200362},{"children":[],"localizedName":"Ostrzeszów","id":3200363},{"children":[],"localizedName":"Piła","id":3200364},{"children":[],"localizedName":"Pleszew","id":3200365},{"children":[],"localizedName":"Pniewy","id":3200575},{"children":[],"localizedName":"Pobiedziska","id":3200576},{"children":[],"localizedName":"Poznań","id":3200366},{"children":[],"localizedName":"Puszczykowo","id":3200577},{"children":[],"localizedName":"Rawicz","id":3200367},{"children":[],"localizedName":"Rogoźno","id":3200578},{"children":[],"localizedName":"Słupca","id":3200368},{"children":[],"localizedName":"Swarzędz","id":3200369},{"children":[],"localizedName":"Szamotuły","id":3200370},{"children":[],"localizedName":"Śrem","id":3200371},{"children":[],"localizedName":"Środa Wielkopolska","id":3200372},{"children":[],"localizedName":"Trzcianka","id":3200373},{"children":[],"localizedName":"Trzemeszno","id":3200579},{"children":[],"localizedName":"Turek","id":3200374},{"children":[],"localizedName":"Wągrowiec","id":3200375},{"children":[],"localizedName":"Witkowo","id":3200580},{"children":[],"localizedName":"Wolsztyn","id":3200376},{"children":[],"localizedName":"Wronki","id":3200581},{"children":[],"localizedName":"Września","id":3200377},{"children":[],"localizedName":"Złotów","id":3200378}],"localizedName":"Wielkopolskie","id":3200006},{"children":[{"children":[],"localizedName":"Barlinek","id":3200379},{"children":[],"localizedName":"Białogard","id":3200380},{"children":[],"localizedName":"Cedynia","id":3200381},{"children":[],"localizedName":"Chojna","id":3200620},{"children":[],"localizedName":"Choszczno","id":3200382},{"children":[],"localizedName":"Czaplinek","id":3200586},{"children":[],"localizedName":"Darłowo","id":3200383},{"children":[],"localizedName":"Dębno","id":3200384},{"children":[],"localizedName":"Drawno","id":3200385},{"children":[],"localizedName":"Drawsko Pomorskie","id":3200386},{"children":[],"localizedName":"Goleniów","id":3200387},{"children":[],"localizedName":"Gryfice","id":3200388},{"children":[],"localizedName":"Gryfino","id":3200389},{"children":[],"localizedName":"Kamień Pomorski","id":3200390},{"children":[],"localizedName":"Kołobrzeg","id":3200391},{"children":[],"localizedName":"Koszalin","id":3200392},{"children":[],"localizedName":"Łobez","id":3200393},{"children":[],"localizedName":"Mielno","id":3200395},{"children":[],"localizedName":"Międzyzdroje","id":3200394},{"children":[],"localizedName":"Myślibórz","id":3200396},{"children":[],"localizedName":"Nowogard","id":3200397},{"children":[],"localizedName":"Police","id":3200398},{"children":[],"localizedName":"Połczyn-Zdrój","id":3200582},{"children":[],"localizedName":"Pyrzyce","id":3200399},{"children":[],"localizedName":"Sławno","id":3200400},{"children":[],"localizedName":"Stargard Szczeciński","id":3200401},{"children":[],"localizedName":"Szczecin","id":3200402},{"children":[],"localizedName":"Szczecinek","id":3200403},{"children":[],"localizedName":"Świdwin","id":3200404},{"children":[],"localizedName":"Świnoujście","id":3200405},{"children":[],"localizedName":"Trzebiatów","id":3200583},{"children":[],"localizedName":"Wałcz","id":3200406},{"children":[],"localizedName":"Wolin","id":3200584},{"children":[],"localizedName":"Złocieniec","id":3200585}],"localizedName":"Zachodniopomorskie","id":3200084}],"localizedName":"Polska","id":202}</script>
        
    </div>

                        


                        
                        <div class="button">
    <button tabindex="4">
        <span class="icon">
            <span class='icon-header-search-out'></span>
            <span class='icon-header-search-over'></span>
        </span>
        <span class="label">Szukaj</span>
    </button>
</div>
                        


                    </fieldset>


                    
                    
                    



                    
                    
                    


                </form>


            </div>
        </section>
    </div>


    




    


    <div class="containment">

        

        <div class="page extra" >


            


    

    

    
    
   
   





            
            
    <div class="breadcrumbs ">
            
                


    <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
        <a class="category" href="http://www.gumtree.pl/s-malopolskie/v1l3200003p1">
            <span class="microdata" itemprop="title">Małopolska</span>
        </a>
        <meta itemprop="url" content="http://www.gumtree.pl/s-malopolskie/v1l3200003p1" />
    </span>
    <span class="icon-chevron-right"></span>
    <span></span>





            
            
                


    <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
        <a class="category" href="http://www.gumtree.pl/s-nieruchomosci/krakow/v1c2l3200208p1">
            <span class="microdata" itemprop="title">Nieruchomości</span>
        </a>
        <meta itemprop="url" content="http://www.gumtree.pl/s-nieruchomosci/krakow/v1c2l3200208p1" />
    </span>
    <span class="icon-chevron-right"></span>
    <span></span>





            
        
            <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                <a class="category" href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1">
                    <span class="microdata" itemprop="title">
                        
                            mieszkania i domy do wynajęcia
                        
                        
                            | 
                            Kraków
                        
                    </span>
                </a>
                <meta itemprop="url" content="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1"/>
            </span>
            <span class="icon-chevron-right"></span>
            <span></span>
            <span class="title">ogłoszenie 169136399</span>
        
    </div>

<div class="clear"></div>





            

            <div class="content">
                <section role="content">
                    <div class="wrap">
                        
                        

    
       
       
        <div class="vip-controls">
            





        </div>

        <div id="seovip-left-column" class="vip-left-column vip-header-and-details hasImages">
            <div class="vip-content-header">
                <div class="vip-title clearfix">
                    <h1 class="item-title" >
                        <span class="myAdTitle">2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ</span>
                        
                    </h1>
                    <div class="price">


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>


</div>
                    
                </div>

                <div class="vip-gallery seoVip">
                    
    <div class="wrap has-thumbs" data-base-js-url="http://inc.t9.classistatic.com/1.1.288/js/">

        
            <div class="main-bg">
                <div class="main">
                    <span class="icon-vip-arrow-left"></span>
                    <span class='vertical-alignment-helper'></span><img  data-index="0" src = "http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_20.JPG?set_id=8800005007" alt="2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ" />
                    
                    <span class="icon-vip-arrow-right"></span>
                    <span class="icon-zoom-image"></span>
                </div>
                
                    
    <div class="counter-pic"><span class="index"></span> z <span class="length"></span></div>

                
            </div>
        
        
        
        
        <script id="vip-gallery-data" type="text/x-bolt-json">
            {"small":"[http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/SqwAAOSwGIRXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/dyUAAOSwc1FXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/dysAAOSwc1FXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/Y0EAAOSwZ1BXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/P1EAAOSwepJXcYcz/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/d94AAOSwc1FXcYc3/$_19.JPG?set_id=8800005007]","medium":"[http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/SqwAAOSwGIRXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/dyUAAOSwc1FXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/dysAAOSwc1FXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/Y0EAAOSwZ1BXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/P1EAAOSwepJXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/d94AAOSwc1FXcYc3/$_20.JPG?set_id=8800005007]","large":"[http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/7JAAAOSw3YNXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/SqwAAOSwGIRXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/dyUAAOSwc1FXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/dysAAOSwc1FXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/Y0EAAOSwZ1BXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/P1EAAOSwepJXcYcz/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/ODAwWDYwMA==/z/d94AAOSwc1FXcYc3/$_20.JPG?set_id=8800005007]","alt-tags":"[2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 1, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 2, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 3, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 4, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 5, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 6, 2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow zdjęcie: 7]"}
        </script>
    </div>

        
        



                   
 <div class='post-it-yourself'>
    <span class='sudo-link' data-gtm="pc|PostAdBegin|eventLabel|src=SimilarAd" data-o-uri='/cbfg.ugzy?fvzvyneNqVq=1001691363990910474413109'>Dodaj takie ogłoszenie!</span>
 </div>

                </div>
                
                
<!-- TODO: separate templates with different Locale  -->
<ul class="selMenu">

<li>
    <div class="attribute">
        <span class="name">Data dodania</span>
        <span class="value">
            
                27/06/2016
            
        </span>
        
    </div>
</li>

<li>
    <div class="attribute">
        <span class="name">Lokalizacja</span>
            <span class="value">
                
<div class="location" >
    
    
        <a href="http://www.gumtree.pl/s-krakow/v1l3200208p1" >Kraków</a>, 
    
    
        <a href="http://www.gumtree.pl/s-malopolskie/v1l3200003p1" >Małopolskie</a>
    
    
</div>

            </span>
    </div>
</li>

<!-- Vehicle -->





























































<!-- End Vehicle -->



<!-- Property -->



    
    <li>
        <div class="attribute">
            <span class="name">Do wynajęcia przez</span>
            <span class="value">Agencja</span>
        </div>
    </li>









    
    <li>
        <div class="attribute">
            <span class="name">Dostępny</span>
            <span class="value">27/06/2016</span>
        </div>
    </li>











    
    <li>
        <div class="attribute">
            <span class="name">Rodzaj nieruchomości</span>
            <span class="value">Mieszkanie</span>
        </div>
    </li>






















    
    <li>
        <div class="attribute">
            <span class="name">Liczba pokoi</span>
            <span class="value">2 pokoje</span>
        </div>
    </li>








    
    <li>
        <div class="attribute">
            <span class="name">Liczba łazienek</span>
            <span class="value">1 łazienka</span>
        </div>
    </li>





    
    <li>
        <div class="attribute">
            <span class="name">Wielkość (m2)</span>
            <span class="value">47</span>
        </div>
    </li>

















<!-- Baby, kids, pregnant -->


<!-- End Baby, kids, pregnant -->

<!-- Computers and Electronics -->











<!-- End Computers and Electronics -->

<!-- Courses, Workshops -->











<!-- End Courses, Workshops -->

<!-- Home/Fashion -->

















<!-- End Home Fashion -->

<!-- Services -->











<!-- End Services -->

<!-- Free time/leisure -->











<!-- End Free time -->

<!-- Pet -->









<!-- End Pet -->

<!-- Job -->






<!-- new for SG -->




































































































































































































































































































































































































































<li>

  

</li>
</ul>

                <div class="clear"></div>
            </div>
            <div class="vip-details seoVip">
                 
    <div class="description" >
        <span class="pre"
            
                
                style="font-family: inherit; white-space: pre-wrap;"
            
        ><p>Nr oferty 2650. Kraków. Płaszów, ul. Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielnych pokoi, kuchni, łazienki i garderoby.</p></span>
    </div>

    

             </div>



        </div>

        <div class="vip-right-column">
            <div class="vip-seller-forms-container">
                <div class="contact-wrapper ">
                    <div id="sm-share-cnt" class="clearfix">
                         <div id="sm-cnt">
                            
                               
    <div id="sm">
        <ul class="sm-ul buttons clearfix">
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-facebook sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-gmailplus sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span data-text='Sprawdź co dzieje się na Gumtree! {0}' class="icon-seo-twitter sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-pinterest sm-icons"></span></a></li>
            
            <li class="button last mailto"><a href="#"><span data-subject = 'To może Cię zainteresować! {0}' data-body = 'Witaj! Myślę, że to ogłoszenie na Gumtree może Cię zainteresować. {0} %0D%0ADołącz do społeczności Gumtree:%0D%0AFacebook: https://www.facebook.com/GumtreePolska %0D%0A Google+: https://plus.google.com/103950977256553454134/posts %0D%0A Twitter: https://twitter.com/gumtreepolska' class="icon-seo-mail sm-icons"></span></a></li>
        </ul>
    </div>

                            
                         </div>

                        <div id="share">
                         
    <div class="sharevisitInfo no-visit-0">
        
        
        
    </div>

                        </div>
                    </div>

                    <div class="abt1 vip-seller-container clearfix">

                        <div class="vip-seller clearfix">
                            




    <span class="icon-user"></span>


<span class="username">

    <a 

        
        href="/u-oferty-sprzedazy/beata-stawiarz/v1u104744131p1"
        

        >

        
            Beata
        

        <span class="more-ads">(Zobacz więcej ogłoszeń)</span>
    </a>
</span>


    
        
    
        <span class="usersince">Użytkownik od 05-2010</span>
    

    




                        </div>

                        <div class="vip-usr-interactions clearfix">
                            
                            <div class="usr-interactions">
                                <div class="vip vip-contact">
                                    
                                    
<div class='reply_controls clearfix '>
    
    <a href="tel:797578988" class="button telephone">
    <span class="icon-phone-blue icon-phone-green"></span>
    <span class="icon-phone-white"></span>
    <span id='phone-number' class="label"  data-shortname-text='Połączenia' data-show-number-text='*** Pokaż numer telefonu'>797578988</span>
</a>
    
    <a href="javascript:void(0)" class="title other-country">
        <span class="icon-envelope-alt-green"></span>
        <span class="icon-envelope-alt-white"></span>
        <span class="label reply-label" data-shortname-text='E-mail'>E-mail</span>
    </a>
</div>

<form class="replyAd" data-attachment-size="2097152" data-gtm="npc|R2SEmailBegin"  data-success-msg='Twoja wiadomość została wysłana' method="post" action="/rui-api/page/reply/model/pl_PL" novalidate>
    <input name="machineId" type="hidden"/>
    <input name="rand" id="rand" type="hidden"/>
    <input name="fileName" id="fileName" type="hidden"/>

    
    <div class="gl-messages-replyAds-srp">
        <a href="javascript:void(0)" class="close_btn">
            <span class="icon-gl-message-close"></span>
        </a>
    </div>

    
    <label>
        <span class="label">Wiadomość</span>
    </label>
    

    
  
<div class="messageArea">
    
    <ul class="canned-responses">
        
         <li>
             <label class="checkbox-label">
                 <input type="checkbox" class="checkbox" />
                 <span data-i18n="vip.reply.canned.imInterested">Zainteresowała mnie ta oferta. Proszę o kontakt.</span>
             </label>
         </li>
         
         <li>
             <label class="checkbox-label">
                 <input type="checkbox" class="checkbox" />
                 <span data-i18n="vip.reply.canned.whenWhereICanSeeIt">Gdzie i kiedy mogę to zobaczyć?</span>
             </label>
         </li>
         
    </ul>
    
</div>



    
    <label>
        
        <textarea name="replyMessage"></textarea>
        
    </label>
    

    
    <label>
        <span class="label">Imię</span>
        
        <input name="buyerName" type="text" value=""/>
        
    </label>
    

    
    <label>
        <span class="label">E-mail</span>
        
        <input name="email" type="email" value=""/>
        
    </label>
    

    
    <label>
        <span class="phone label">Telefon (Opcjonalnie)</span>
        
        <input name="phoneNumber" type="text" value=""/>
        
    </label>
    

    

    
    <label class="checkbox-label">
        <input type="checkbox" name="isSendMeCopyEmail"  />
        <span class="label">Wyślij mi kopię e-maila</span>
    </label>
    



    <input type="hidden" name="adId" value="1001691363990910474413109"/>



    <button class="submit-reply" type="submit">Wyślij</button>

    
<div class="privacypolicy">
    Klikając "Wyślij", wyrażasz zgodę na nasze <span class=sudo-link data-o-uri="uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Mnfnql-xbemlfgnavn" data-target="_self"> Zasady korzystania</span> i <span class=sudo-link data-o-uri="/cevinpl-cbyvpl" data-target="_self">Politykę prywatności</span> oraz zgadzasz się na otrzymywanie naszych newsletterów i ofert promocyjnych.
</div>

</form>
<form name="fileAttachmentForm" id="fileAttachmentForm" target="uploadedFile" method="post" action="/fileattachmentuploader" enctype="multipart/form-data">
    <input type="hidden" name="adId" value="1001691363990910474413109"/>
</form>



                                </div>
                            </div>
                            
                        </div>

                    </div>
                </div>
                
                
                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL"  data-adid="169136399">
                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                    <span class="label" data-toggle-text='Dodane do Zachowanych'>Dodaj do Zachowanych</span>
                </div>
                
                
                <div class="vip-seller-form-details">
                    
                        
                            <div class="vip vip-flagad">
                                
    <label class="reported-ad is-title-disabled hide">
        
        <span class="icon-warning-sign"></span>
        
        <span>Ogłoszenie zgłoszone</span>
    </label>
    <div class="unreported-ad flagad-container">
        
    <span class="sudo-link security-tips"  data-target="_blank">
    <span class="icon-lock"></span>
        <span class="security-tips-text">Porady Bezpieczeństwa</span> <span>- Twoje bezpieczeństwo jest dla nas ważne, zachęcamy do zachowania czujności.</span>
        <span data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NFnsrglCY' data-target="_blank"  >Dowiedz się więcej</span>
        
    </span>
    

        <a class="title" href="javascript:void(0)">
            
            <span class="icon-warning-sign"></span>
            
            <span class="label">Zgłoś ogłoszenie</span>
            <span class="caret-icon-area icon-caret-right"></span>
        </a>
        <form class="flagAd tallForm"  data-flagad-success='Dziękujemy za zgłoszenie. Sprawdzimy tę ofertę najszybciej jak to możliwe. '
            method="post" action="/rui-api/page/flag/confirm/pl_PL" novalidate>
            <label>
                <span class="label ">Powód</span>
            </label>
            <div>
                <input type="hidden" name="adId" value="1001691363990910474413109" />
                <input type="hidden" name="captchaToken" value="Q0FQVENIQTowMTQwOjE0NjcwNTg3OTMyNjE6MmMzMTcwY2VmMDJlNjhmNmYyY2IxMjFiYzA4ZDY1MWIzZDFhZjg1Ng==" />                
                <ul>
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="InappropriateContent"   checked="checked" /><label>Nieodpowiednia treść</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>InappropriateContent=Nieodpowiednia treść</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="DuplicateSpam"   /><label>Duplikat/Spam</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>DuplicateSpam=Duplikat/Spam</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="PossibleFraud"   /><label>Możliwe oszustwo</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>PossibleFraud=Możliwe oszustwo</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="NotRelevant"   /><label>Nieaktualne</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>NotRelevant=Nieaktualne</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="WrongCategory"   /><label>Zła kategoria</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>WrongCategory=Zła kategoria</label></li> -->
                
                </ul>
            </div>
            <label>
                <span class="label">E-mail</span>
                                
                    <input type="email" name="email" value=""  />
                
                <!--  handle error -->
            </label>
               <label>
                <span class="label">Komentarz&nbsp;<span class="optional">(Opcjonalnie)</span></span>
                <textarea name="comments"></textarea>
                <!--  handle error -->
            </label>
            <label>
                <span class="label">Wpisz numer</span>
                <div>            
                    <img class="imageAlign" name="captchaTokenImg" width="75" height="50" border="0" src="/captcha/image?token=Q0FQVENIQTowMTQwOjE0NjcwNTg3OTMyNjE6MmMzMTcwY2VmMDJlNjhmNmYyY2IxMjFiYzA4ZDY1MWIzZDFhZjg1Ng==" alt='Włącz zdjęcia' />
                    <!--
                    <embed src="/captcha/audio?token=Q0FQVENIQTowMTQwOjE0NjcwNTg3OTMyNjE6MmMzMTcwY2VmMDJlNjhmNmYyY2IxMjFiYzA4ZDY1MWIzZDFhZjg1Ng==" width="100%" height="60">
                        <noembed>
                              <img src="yourimage.gif" >
                           </noembed>
                    </embed>
                    -->
                    <input class="textAlign" type="text" name="captchaValue" value=""/>
                </div>
                <br class="clear" />                
            </label>        
            <label class='privacypolicy'>Wysyłając Zgłoszenie, wyrażasz zgodę na nasze <a href="http://pomoc.gumtree.pl/PL/articles/pl/KB_Article/Zasady-korzystania"> Zasady korzystania</a> z Gumtree.</label>
            <div class="button-area">
                <button class="action-button" type="submit">Zgłoś</button>
                <button class="action-button cancel" type="button" name="cancel">Anuluj</button>
            </div>
        </form>
    </div>






                            </div>
                        

                        

                                 
                    
                </div>
            </div>

            <input type='hidden' id='adId' value='1001691363990910474413109' />  
        </div>




         <div class="vip-seller-form-details seoVip_banner">
                <div>
                     
                     
                     
                    
                        

 


             <div class="moreSearches">
                <div class="titleContainer">
                    <span>Popularne</span>
                </div>
                <ul class="resultsContainer relSearchMenu">
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/krakow/v1c9008l3200208q0p1">krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/kawalerka+krakow/v1c9008l3200208q0p1">kawalerka krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/mieszkanie+krakow/v1c9008l3200208q0p1">mieszkanie krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/mieszkanie+do+wynajecia/v1c9008l3200208q0p1">mieszkanie do wynajecia</a>
                    </li>
                    
                </ul>
               </div> 

                           
                     
                     
                    
                    <div class="suggestedSearch">
                     
                     

 


             <div class="moreSearches">
                <div class="titleContainer">
                    <span>Proponowane</span>
                </div>
                <ul class="resultsContainer relSearchMenu">
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/warszawa/kawalerki+do+wynajecia+warszawa/v1c9008l3200008q0p1">kawalerki do wynajęcia warszawa</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/rzeszow/mieszkania+do+wynajecia+rzeszow/v1c9008l3200252q0p1">mieszkania do wynajęcia rzeszów</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/mieszkania+krakow+wynajem/v1c9008l3200208q0p1">mieszkania kraków wynajem</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie+do+wynajecia+krakow/v1c9008l3200208q0p1">mieszkanie do wynajęcia kraków</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/kawalerka+do+wynajecia/v1c9008q0p1">kawalerka do wynajęcia</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie+krakow+wynajem/v1c9008l3200208q0p1">mieszkanie kraków wynajem</a>
                    </li>
                    
                </ul>
               </div> 

                      
                    </div>
                     
                     
              </div>
              
              <div>
                     
                           
    <div style="margin-top:10px;">
        <div class="rightbanner">
            <div id="div-vip-ad-banner" class="vipbanner"></div>
        </div>
    </div>
    
                     
              </div>
         </div>
         
       
          
             <div class="seo_similar results list-view">
                 <div class="section-divider">Podobne ogłoszenia, które mogą Cię zainteresować.</div>
                 <div class="view">
                     <ul>
                        
                               
        <li class="result pictures" data-adid="1001671110790910510768709" data-criteoadid="167111079">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/ZEgAAOSwqBJXVmwq/$_19.JPG?set_id=8800005007" alt="2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ z Krakow, zobacz zdjęcie" class="thumbM"/>
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-pok-47-m2-na-p%C5%82aszowskiej-dla-3-os%C3%B3b-blisko-rm-grzeg%C3%B3rzeckiego-lini-tramwajowej/1001671110790910510768709">2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ</a>
                            
                        </div>

                        
                            <div class="description hidden" >Nr oferty 2650. Kraków. Płaszów, ul.
Płaszowska blisko Krakowskiej Akademii. Mieszkanie o powierzchni ok.
48 m2 składa się z dwóch oddzielnych pokoi, kuchni, łazienki i
garderoby. Mieszkanie znajduje się na 1 piętrze. Mieszkanie bardzo
ładne w nowym bloku z 2000 roku. Mieszkanie umeblowane w dużym
pokoju łóżko, komoda, stół i krzesła w małym duża szafa na
ubrania. Brak łóżka ale jest możliwo ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167111079">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001672694720910910876109" data-criteoadid="167269472">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDQ4WDYwMA==/z/AikAAOSwnNBXassf/$_19.JPG?set_id=8800005007" alt="LOFT HOUSE Płaszowska Saska Podgórze z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 9</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/loft-house-p%C5%82aszowska-saska-podg%C3%B3rze/1001672694720910910876109">LOFT HOUSE Płaszowska Saska Podgórze</a>
                            
                        </div>

                        
                            <div class="description hidden" >LOFT HOUSE Nieruchomości prezentuje do wynajęcia mieszkanie w bardzo dobrym standardzie o powierzchni 53 m2 z dwoma niezależnymi pokojami i osobną widną kuchnią.LOKALIZACJA:Mieszkanie zlokalizowane jest w spokojnej, dobrze skomunikowanej okolicy przy ulicy Płaszowskiej, w dzielnicy Podgórze. Doskonałe połączenie z krakowskimi uczelniami i centrum miasta.BUDYNEK:Mieszkanie położone jest na parterze ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 600 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167269472">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001682180750910469692109" data-criteoadid="168218075">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDgwWDY0MA==/z/ZhkAAOSwvg9XZQ8d/$_19.JPG?set_id=8800005007" alt="2 pok.dla 3 osób,Płaszów,blisko Akademia Krakowska z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 6</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-pok-dla-3-os%C3%B3b-p%C5%82asz%C3%B3w-blisko-akademia-krakowska/1001682180750910469692109">2 pok.dla 3 osób,Płaszów,blisko Akademia Krakowska</a>
                            
                        </div>

                        
                            <div class="description hidden" >Kraków. Płaszów, ul. Płaszowska blisko: Krakowska Akademia.Mieszkanie o powierzchni ok. 48 m2 składa się z dwóch oddzielnych pokoi, kuchni, łazienki i garderoby. Mieszkanie znajduje się na 1 piętrze. Mieszkanie bardzo ładne w nowym bloku z 2000 roku. Mieszkanie umeblowane w dużym pokoju łóżko, komoda, stół i krzesła w małym duża szafa na ubrania. Brak łóżka ale jest możliwość dokupienia przez właś ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168218075">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001691325410910493764009" data-criteoadid="169132541">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDI5WDY0Ng==/z/89UAAOSw-4BXcXJY/$_19.JPG?set_id=8800005007" alt="3-pok 65 m2, 2009 rok, Podgórze, ul. Płaszowska z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/3+pok-65-m2-2009-rok-podg%C3%B3rze-ul-p%C5%82aszowska/1001691325410910493764009">3-pok 65 m2, 2009 rok, Podgórze, ul. Płaszowska</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia 3 pokojowe (65 m2) mieszkanie przy ul. Płaszowskiej (Podgórze) razem z miejscem w garażu podziemnym !  Mieszkanie usytuowane jest na parterze w 5 piętrowym bloku z 2009 r.. Składa się z 2 osobnych pokoi, salonu połączonego z aneksem kuchennym, łazienki, przedpokoju, balkonu oraz tarasu.Mieszkanie jest w pełni umeblowane i wyposażone.W kuchni meble w zabudowie, zmywarka, piekarnik elek ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 000 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="169132541">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001676681670910494978909" data-criteoadid="167668167">
            
                
                    <div class="result-link highlight ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NTMwWDgwMA==/z/DnYAAOSwuhhXXe72/$_19.JPG?set_id=8800005007" alt="Ładne i atrakcyjne 2-poz. mieszkanie Kraków Płaszów, ul. Krzywda - wynajmę z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/%C5%82adne-i-atrakcyjne-2+poz-mieszkanie-krak%C3%B3w-p%C5%82asz%C3%B3w-ul-krzywda-+-wynajm%C4%99/1001676681670910494978909">Ładne i atrakcyjne 2-poz. mieszkanie Kraków Płaszów, ul. Krzywda - wynajmę</a>
                            
                        </div>

                        
                            <div class="description hidden" >Ciekawa oferta:Wynajmę od lipca 2016, ładne i atrakcyjne 2-poziomowe mieszkanie w wyjątkowo cichej, ze starą zielenią okolicy 
Krakowa-Plaszowa. Stosunkowo nowe, młode budownictwo, mieszkanie o 
powierzchni użytkowej 64m2,
 kompozycja o ciekawej architekturze aranżacji wnętrz ze  
skosami, ściennymi tatuażami, przestronnymi i ustawnymi pokojami w 
dolnej części i przytulnym poddaszem.Ładna ar ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 550 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167668167">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001664695680910493064409" data-criteoadid="166469568">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NzY4WDY5Mg==/z/Mk8AAOSw0gdXTYVU/$_19.JPG?set_id=8800005007" alt="Wynajem 2 pokojowe 38 mkw, osobna kuchnia ul. Płaszowska z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/wynajem-2-pokojowe-38-mkw-osobna-kuchnia-ul-p%C5%82aszowska/1001664695680910493064409">Wynajem 2 pokojowe 38 mkw, osobna kuchnia ul. Płaszowska</a>
                            
                        </div>

                        
                            <div class="description hidden" >Posiadamy do wynajęcia komfortowe mieszkanie przy ul. Płaszowskiej 59. Lokalizacja ta zapewnia bardzo dobrą komunikację z centrum Krakowa i innymi dzielnicami, do Rynku Głównego 4km. Nowe budownictwo, 2 bloki, teren ogrodzony, bramy na pilota, teren monitorowany. Mieszkanie o pow. 38 mkw. Składa się z 2 oddzielnych pokoi, osobnej kuchni, przestronnej łazienki, przedpokoju, zadaszonego balkonu. Okn ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166469568">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001663506350910787232609" data-criteoadid="166350635">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/Mzg3WDYxMg==/z/3rIAAOSw6btXTC0K/$_19.JPG?set_id=8800005007" alt="2-pok.słoneczne mieszk.ul.Saska z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 6</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2+pok-s%C5%82oneczne-mieszk-ul-saska/1001663506350910787232609">2-pok.słoneczne mieszk.ul.Saska</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia od 1 lipca 2016 mieszkanie zlokalizowane przy ul.Saskiej w Krakowie, 50m2, 2 pokoje, 3 piętro,  Mieszkanie składa się z:- przedpokój (duża szafa wnękowa z lustrem, pawlacze, półki na buty i klucze)- kuchnia w zabudowie (gazowa, piekarnik w zabudowie, duża lodówka, stół &#43; krzesła, czajnik)- mały pokój (cała ściana w zabudowie w tym duża szafa o szer 120 cm, dużo półek zamkniętych i otw ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 400 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166350635">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001672719240910472156209" data-criteoadid="167271924">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDUwWDYwMA==/z/QQoAAOSwqBJXWA9D/$_19.JPG?set_id=8800005007" alt=" OKAZJA! 2 osobne pokoje, Płaszów, ulica Płaszowska!  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 4</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/okazja-2-osobne-pokoje-p%C5%82asz%C3%B3w-ulica-p%C5%82aszowska/1001672719240910472156209"> OKAZJA! 2 osobne pokoje, Płaszów, ulica Płaszowska! </a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia przestronne 2 pokojowe mieszkanie w bloku mieszkalnym w Krakowie, w dzielnicy Płaszów, ul. PłaszowskaMieszkanie:- parter,- 52m2,- 2 niezależne pokoje, osobna jasna kuchnia, łazienka, przedpokój, balkon- ogrzewanie: gazowe.Cena wynajmu: 1200zł &#43; 200zł czynsz administracyjny &#43; media.Kontakt w sprawie oferty:Aneta Nosal



T: 785 811 636Home Broker 
    </div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167271924">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001684216730910468454409" data-criteoadid="168421673">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDgwWDY0MA==/z/pxsAAOSwzJ5XZ~e4/$_19.JPG?set_id=8800005007" alt="2-pokojowe ul. Płaszowska  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2+pokojowe-ul-p%C5%82aszowska/1001684216730910468454409">2-pokojowe ul. Płaszowska </a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia 2-pokojowe mieszkanie w wysokim standardzie w budynku przy ul. Płaszowskiej. Mieszkanie jak i budynek po kapitalnym remoncie. Składa się z dwóch umeblowanych pokoi, wyposażonej kuchni (lodówka, zmywarka) oraz łazienki z wanną. W przedpokoju duża zabudowana szafa. Do mieszkania przynależy duży taras. Mieszkanie na parterze, teren wokół budynku jest ogrodzony i monitorowany. Telewizor w ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 400 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168421673">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001688323890910672916909" data-criteoadid="168832389">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDUwWDgwMA==/z/x~AAAOSwbYZXbQrf/$_19.JPG?set_id=8800005007" alt=" 3 pokojowe | klimatyzacja | Podgórze | Płaszów | taras | Umeblowane  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 9</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/3-pokojowe-klimatyzacja-podg%C3%B3rze-p%C5%82asz%C3%B3w-taras-umeblowane/1001688323890910672916909"> 3 pokojowe | klimatyzacja | Podgórze | Płaszów | taras | Umeblowane </a>
                            
                        </div>

                        
                            <div class="description hidden" >LuxHome Group – mieszkania do wynajęciaLuxHome Group poleca przestronne 3 pokojowe mieszkanie z klimatyzacją i dużym tarasem przy ulicy Koszykarskiej.* Saska * Stoczniowców * Nowohucka * Płaszowska * Myśliwska * Kuklińskiego * Wielicka *Mieszkanie dostępne od 1 Maja!Oferowane 3 pokojowe mieszkanie o powierzchni 56,6 m2 znajduje się na 3 piętrze w małym, kameralnym bloku bez windy z 2010 r. W skład ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 300 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168832389">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001652300380910612579109" data-criteoadid="165230038">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/b3IAAOSwH71XO2ZK/$_19.JPG?set_id=8800005007" alt="Mieszkanie o wysokim standardzie do wynajęcia z garażem z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-o-wysokim-standardzie-do-wynaj%C4%99cia-z-gara%C5%BCem/1001652300380910612579109">Mieszkanie o wysokim standardzie do wynajęcia z garażem</a>
                            
                        </div>

                        
                            <div class="description hidden" >Ekskluzywny apartament do wynajęcia dla osób pracujących lub studentów. Mieszkanie w nowym IV piętrowym bloku przy ulicy Strycharskiej. Składa się z dwóch niezależnych pokoi oraz salonu połączonego z kuchnią, łazienki oraz balkonu. Mieszkanie w pełni wyposażone, kuchnia w zabudowie, płyta indukcyjna, piekarnik, okap, lodówka. Łazienka- prysznic, pralka,toaletka, lustro, łazienka. W pokojach znajdu ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="165230038">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001666870320910470516809" data-criteoadid="166687032">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NTk5WDgwMA==/z/AqIAAOSwJhNXUCDd/$_19.JPG?set_id=8800005007" alt="Podgórze! 3-pokojowe mieszkanie tuż przy linii 20 i 50! +garaż, balkon z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 11</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/podg%C3%B3rze-3+pokojowe-mieszkanie-tu%C5%BC-przy-linii-20-i-50-%2Bgara%C5%BC-balkon/1001666870320910470516809">Podgórze! 3-pokojowe mieszkanie tuż przy linii 20 i 50! &#43;garaż, balkon</a>
                            
                        </div>

                        
                            <div class="description hidden" >Victoria Estate prezentuje 3-pokojowy nowoczesny apartament z garażem podziemnym na ul. Strycharskiej/Podgórze wolne od 1 lipca!Nieruchomość:Apartament zlokalizowany na II-piętrze IV-piętrowego apartamentowca z 2015 r. na ul. Strycharskiej - Podgórze. Składa się z salonu z aneksem kuchennym, 2 niezależnych pokoi, łazienki, przedpokoju oraz balkonu. W pełni wyposażony i umeblowany: kuchnia- meble w ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166687032">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001685320160910481775309" data-criteoadid="168532016">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NTMzWDgwMA==/z/FDoAAOSwc1FXaT-P/$_19.JPG?set_id=8800005007" alt="mieszkanie wynajem 2 pokojowe z parking płaszowska podgórze z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 5</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-wynajem-2-pokojowe-z-parking-p%C5%82aszowska-podg%C3%B3rze/1001685320160910481775309">mieszkanie wynajem 2 pokojowe z parking płaszowska podgórze</a>
                            
                        </div>

                        
                            <div class="description hidden" >witam, mam do wynajęcia mieszkanie 2 pokojowe(sypialnia &#43;salon) od 1 sierpnia 2016 bardzo blisko centrum Krakowa - 10 min tramwajem do Rynku Głównego. Nowy 3 piętrowy blok, całościowe wyposażenie kuchni( zmywarka, mikrofala w zabudowie , piekarnik, płyta indukcyjna, lodówka, pralka) . Cena obejmuje miesięczny wynajem  mieszkania i parkingu podziemnego. Dodatkowo dochodzą koszty czynsz &#43; prąd &#61; oko ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 600 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168532016">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001687521350910468815909" data-criteoadid="168752135">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDI2WDY0MA==/z/A5QAAOSw3YNXa-0v/$_19.JPG?set_id=8800005007" alt=" 1800zł Mieszkanie dla 2-4 osób ul.Długa/ul.Szlak/ul.Karmelicka STARE MIASTO blisko NOWY KLEPARZ  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 9</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/1800z%C5%82-mieszkanie-dla-2+4-os%C3%B3b-ul-d%C5%82uga-ul-szlak-ul-karmelicka-stare-miasto-blisko-nowy-kleparz/1001687521350910468815909"> 1800zł Mieszkanie dla 2-4 osób ul.Długa/ul.Szlak/ul.Karmelicka STARE MIASTO blisko NOWY KLEPARZ </a>
                            
                        </div>

                        
                            <div class="description hidden" >Mieszkanie dla 4 osób STARE MIASTO ul.DługalLOKALIZACJA:Oferujemy Państwu do wynajęcia wygodne i funkcjonalne mieszkanie w spokojnej, dobrze skomunikowanej okolicy przy ulicy Krowoderskiej doskonałe połączenie z krakowskimi uczelniami, centrum miasta do Rynku Głównego 5 min pieszo. Mieszkanie jest świeżo po odmalowaniu.Mieszkanie jest świetnie zlokalizowane, na ul. Krowoderskiej, bliżej Aleji Słow ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 800 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168752135">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001686633390910472748409" data-criteoadid="168663339">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDUwWDgwMA==/z/cUsAAOSwNuxXatID/$_19.JPG?set_id=8800005007" alt="Do Wynajęcia 3 pokojowe Podgórze, Płaszów ul. Krzywda z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/do-wynaj%C4%99cia-3-pokojowe-podg%C3%B3rze-p%C5%82asz%C3%B3w-ul-krzywda/1001686633390910472748409">Do Wynajęcia 3 pokojowe Podgórze, Płaszów ul. Krzywda</a>
                            
                        </div>

                        
                            <div class="description hidden" >Mieszkanie 3-pokojowe mieszkanie dwupoziomowe o powierzchni: 65mkw. położone w zielonej i zacisznej okolicy na Płaszowie, niedaleko przystankuGromadzka. Lokal dostępny natychmiast. Piętro: 3. w bloku 2002W mieszkaniu - dolny poziom: salon, jasna kuchnia, sypialnia, łazienka i przedpokój.Górny poziom: sypialnia oraz garderoba.Wyposażenie: łóżko, kanapy, biurko, regały, szafy, lodówka, stół kuchenny ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168663339">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001688266640910911658609" data-criteoadid="168826664">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDYxWDYxNA==/z/xDYAAOSwbYZXbQGp/$_19.JPG?set_id=8800005007" alt="Mieszkanie nad Stawem koło KSW  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-nad-stawem-ko%C5%82o-ksw/1001688266640910911658609">Mieszkanie nad Stawem koło KSW </a>
                            
                        </div>

                        
                            <div class="description hidden" >Witam, mam do wynajęcia mieszkanie 70 m2, 3 pokojowe, (jeden pokój jednoosobowy, dwa pokoje dwuosobowe), osobna kuchnia, łazienka z kabiną prysznicową, pralką i dwoma umywalkami, kuchnia ze zmywarką i mikrofalówką, płytą indukcyjną i piekarnikiem. Mieszkanie 5-cio letnie, duży pokój z balkonem w kierunku Stawu Płaszowskiego. Cicha okolica, jednocześnie dobrze skomunikowana, 3 min. do przystanku tr ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 400 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168826664">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result " data-adid="1001665263100910949727009" data-criteoadid="166526310">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb ">
                        
                            <div class="icon-container"></div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/70m-dwupokojowe-podg%C3%B3rze-ul-p%C5%82aszowska-okolice-ksw-tandety-umeblowane/1001665263100910949727009">70m dwupokojowe PODGÓRZE ul. Płaszowska okolice KSW TANDETY umeblowane</a>
                            
                        </div>

                        
                            <div class="description hidden" >Wynajmę dwupokojowe, umeblowane mieszkanie 70 metrów. Jasna kuchnia, dwa duże pokoje, łazienka, balkon. Mieszkanie na pierwszym piętrze. Zainteresowanych proszę o kontakt 501_729_336.</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 000 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166526310">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001688394220910468992709" data-criteoadid="168839422">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDkzWDgwMA==/z/NzMAAOSwGIRXbRix/$_19.JPG?set_id=8800005007" alt="Stare Miasto, blisko centrum, komfortowe mieszkanie, 2 niezależne pokoje, wysoki standard  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/stare-miasto-blisko-centrum-komfortowe-mieszkanie-2-niezale%C5%BCne-pokoje-wysoki-standard/1001688394220910468992709">Stare Miasto, blisko centrum, komfortowe mieszkanie, 2 niezależne pokoje, wysoki standard </a>
                            
                        </div>

                        
                            <div class="description hidden" >
        Do wynajęcia od czerwca 2-pokojowe mieszkanie o
powierzchni 83m2 znajdujące się przy ul. Mazowieckiej w Krakowie. 

 

LOKALIZACJA: 

Mieszkanie znajduje się w pięknym, prestiżowym miejscu
blisko centrum miasta. O jego atrakcyjności decyduje położenie przy Alei Trzech
Wieszczów oraz bliskość Nowego Kleparza. Mieszkanie jest bardzo przestronne
oraz jasne, w pełni umeblowane. W najbliż ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 950 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168839422">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001672637170910739321109" data-criteoadid="167263717">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDIzWDY0MA==/z/gnIAAOSwMNxXV~4H/$_19.JPG?set_id=8800005007" alt="Mieszkanie Kraków Nowa Huta 57m2 (nr: 162466) z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krak%C3%B3w-nowa-huta-57m2-nr-162466/1001672637170910739321109">Mieszkanie Kraków Nowa Huta 57m2 (nr: 162466)</a>
                            
                        </div>

                        
                            <div class="description hidden" >Mieszkanie 3-pokojowe - Osiedle Krakowiaków. Do wynajęcia mieszkanie o powierzchni 57m2, znajdujące się na czwartym piętrze w dziesięciopiętrowym budynku z windą. Zadbana klatka schodowa. W jego skład wchodzą trzy pokoje o powierzchniach: 16m2, 14m2 i 10m2. Wszystkie pokoje oddzielne. Dodatkowo mamy jasną kuchnię - umeblowaną i wyposażoną, łazienkę oraz przestronny przedpokój z pojemną szafą w zab ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167263717">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001678592070910471056209" data-criteoadid="167859207">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/MzcyWDgwMA==/z/hbsAAOSwc1FXYARg/$_19.JPG?set_id=8800005007" alt="Mieszkanie 2-pokojowe w okolicy Ronda Matecznego z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 2</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-2+pokojowe-w-okolicy-ronda-matecznego/1001678592070910471056209">Mieszkanie 2-pokojowe w okolicy Ronda Matecznego</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia mieszkanie o powierzchni ok.45m2, znajduje się na I piętrze . Składa się z 2 pokoi w tym jeden z aneksem kuchennym, oddzielnej kuchni z , łazienki z WC oraz przedpokoju.Koszt wynajmu 1300 zł &#43; media wg. zużycia.Biurom Nieruchomości dziękujemy.</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 300 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167859207">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                       </ul>
                 </div>
             </div>
           

         
          <div class="vip-bottomBlock" >
              
               
    <div id="vip_bottombanner" style="margin:0 auto;width:320px"></div>

               <div class="vip-sponsoredads">
                        
        <div id="adcontainer1" class="googleAdContainer"></div>
    
               </div>
        </div>

        <input type='hidden' name='criteoadId' value='169136399' /> 
        <input type="hidden" name="NcatId" value="9008"/>
        <input type="hidden" name="NlocId" value="3200208" />
        <input type="hidden" name="NlocName" value="Krakow" />
        
    

    
    
    <div class="vip-gallery-preview" style='display:none'>
        <div class="gallerycontent">
            
                <div id="banner-container">
                    <div id="banner-preview-header" data-gtaid='7162/Gumtree_PL' data-catcanoname="Nieruchomości/mieszkania i domy do wynajęcia"></div>
                </div>
            
            <img id="preview-image" src="" alt="">
            <div id="vip-gallery-details">
                <div id="prd-title"></div>
                <div id="pict-count"></div>
            </div>
        </div>
        
        <a class="left" href="javascript:void(0)"><span class="icon-vip-popup-arrow-left"></span></a>
        <a class="right" href="javascript:void(0)"><span class="icon-vip-popup-arrow-right"></span></a>
        <div id="icon-close"></div>
    </div>
    



                        <div class="clear"></div>
                    </div>
                </section>
            </div>

           
             
            <div class="footer">
                <footer>
                    
<div class="footer-links clearfix">
    <div class="logo">
        <a href="http://www.gumtree.pl/">
               <img border="0"  src="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/logo.png" alt="Home"/>
        </a>
    </div>

    <div>
        <h3>Poznaj nas</h3>
        <ul>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/B-anf'>O Gumtree</span></li>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NMnfnql_Thzgerr'>Zasady zamieszczania</span></li>
            <li><a href="http://blog.gumtree.pl/">Gumtree Blog</a></li> 
        </ul>
    </div>

    <div>
        <h3>Zobacz więcej</h3>
        <ul>
            
             <li><a href="/t-wyszukiwarka-gory/mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208">Najpopularniejsze wyszukiwania</a></li>
             <li><a href="http://www.gumtree.pl/pages/zawartosc/">Tematy Gumtree</a></li>
             <li><a href="http://www.gumtree.pl/pages/lokalizacje/">Lokalizacje</a></li>
             <li><a href="http://www.gumtree.pl/pages/ceny-nieruchomosci">Ceny Nieruchomości</a></li>
   
        </ul>
    </div>
    
    <div class="rightColumn">
        <h3>Sprawy prawne</h3>
        <ul>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Mnfnql-xbemlfgnavn'>Zasady korzystania</span></li>
            <li><span class='sudo-link' data-o-uri="/cevinpl-cbyvpl" data-target="_self">Polityka Prywatności</span></li>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Pbbxvrf'>Informacje o Cookies</span></li>
        </ul>
    </div>
    
    <div class="rightColumn">
        <h3>Pomoc i porady</h3>
        <ul>
            <li><a href="http://pomoc.gumtree.pl/PL">Pomoc</a></li>
            <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NFnsrglCY'>Pozostań bezpiecznym</span></li>
            <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;ph=1&amp;sf=PbagnpgHfd=&amp;f='>Napisz do nas</span></li>
             <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NOnfvpfCY'>Promowanie ogłoszeń</span></li>
        </ul>
    </div>
</div>

<div class="social-links">



    <!--  social media -->
    <div class="social-media">
        <ul class="social-media-ul buttons">
            <li class="button"><a href="https://www.facebook.com/GumtreePolska" target="_blank"><span class="icon-seo-facebook sm-icons"></span></a></li>
            <li class="button"><a href="https://plus.google.com/103950977256553454134/posts" target="_blank"><span class="icon-seo-gmailplus sm-icons"></span></a></li>
            <li class="button"><a href="https://twitter.com/gumtreepolska" target="_blank"><span class="icon-seo-twitter sm-icons"></span></a></li>
            <li class="button"><a href="http://pinterest.com/gumtreepolska" target="_blank"><span class="icon-seo-pinterest sm-icons"></span></a></li>
            <li class="button"><a href="http://www.youtube.com/user/GumtreePolska" target="_blank"><span class="icon-seo-youtube sm-icons"></span></a></li>
        </ul>
    </div>
</div>
<div class="cpyrt">Copyright © 2014-2016 eBay.  Wszelkie Prawa zastrzeżone.</div>

                </footer>
            </div>
            
        </div>
        
    </div>
</div>



    
        




     


    


    
        
            <script type="text/javascript" src='http://inc.t9.classistatic.com/1.1.288/js/Main_pl_PL.min.js'></script>
        
    
        
            <script type="text/javascript" src='http://inc.t9.classistatic.com/1.1.288/js/SeoViewPage_pl_PL.min.js'></script>
        
    
    

    



    <script>

     var bP = {
             
             accId : ("/7162/Gumtree_PL/Nieruchomości/mieszkania i domy do wynajęcia").split(' ').join('_').replace(/\,|&_|'/g,""),
             
             dc_ref:window.location.href,
             kw: $('input[name=q]').val() || "no category",
             ptype: 'vip_r',
             loc: $('input[name=NlocName]').val(),
     };
     
     
    
         
        
              BOLT.displayBanner( $.extend({slotDim: [300, 250], slotId : 'div-vip-ad-banner',price :'1200', currency : 'PLN'},bP));
         
         

    
     

        
 


    </script>
    
    
        <script src="http://www.google.com/adsense/search/async-ads.js" type="text/javascript"></script>
        <script type="text/javascript" charset="utf-8">
            var x = {"desktopNumAdsTop":"0","desktopNumAdsBottom":"3","mobileNumAdsTop":"0","mobileNumAdsBottom":"3","numRepeated":"0","mobilePubId":"mobile-gumtree-pl","desktopPubId":"gumtree-pl-vip","longerHeadlines":false,"mobileSiteLinks":false,"desktopSiteLinks":true,"channel":"PL_VIP_r","query":"2 pok. 47 m2 na PŁASZOWSKIEJ DLA 3 OSÓB BLISKO RM GRZEGÓRZECKIEGO LINI TRAMWAJOWEJ  Kraków","hl":"pl","adtest":"off","adPage":"0","colorTitleLink":"#333","rolloverAdBackgroundColor":"#FFFFF0","mobileClickableBackground":false};
            
            var defaultBlock = {
                 'lines':'3',
                 'longerHeadlines': x.longerHeadlines,
                 'fontSizeTitle': '14',
                 'fontSizeDescription' : '14',
                 'lineHeightDescription' : 21,
                 'fontSizeDomainLink' : '14',
                 'lineHeightDomainLink' : 21,
                 'fontFamily' : 'tahoma',
                 'noTitleUnderline': true,
                 'colorTitleLink': x.colorTitleLink,
                 'colorDomainLink' : '#333333',
                 'colorText' : '#333333',
                 'colorAdSeparator':'#ffffff',
                  'colorAdBorder' : '#EEEEEE',
                  'adBorderSelections' : 'bottom',
                 'width' : '100%'
            };
            var defaultBlock_ext = {
                //defaultvalue
                'adIconUrl':'http://afs.googleusercontent.com/gumtree-pl/no-photo-pl.jpg',
                'adIconSpacingAbove' : 5,
                'adIconSpacingBefore' : 6,
                'adIconSpacingAfter' : 10,
                'adIconLocation' : 'ad-left'
            }
            
            var pageOptions = {
                'query': x.query,
                'hl': x.h1,
                'adtest' : x.adtest,
                'channel' : x.channel,
                'adPage' : x.adPage,
                'linkTarget' : '_blank',
                'numRepeated': x.numRepeated,
                'titleBold' : true,
                //new call back method through all the market
                'adLoadedCallback':function(containerName, adsLoaded) {
                    if (adsLoaded) {
                        if(containerName == 'adcontainer0'){
                            var exP0, newP;
                            newP = document.createElement("div");
                            newP.className='section-divider';
                            newP.innerHTML = 'Linki sponsorowane';
                            exP0 = document.getElementById('adcontainer0');
                            exP0.parentNode.insertBefore(newP,exP0);
                            $('.content #adcontainer0').css({'background-color':'#ffffff'});
                        };
                            
                        if(containerName == 'adcontainer1'){
                            var exP1, newP1;
                            newP1 = document.createElement("div");
                            newP1.className='section-divider';
                            newP1.innerHTML = 'Linki sponsorowane';
                            exP1 = document.getElementById('adcontainer1');
                            exP1.parentNode.insertBefore(newP1,exP1);
                            $('.content #adcontainer1').css("background-color", "#ffffff");
                        }
                    }
                }
                
            };
            
            function init(numAdsTop, numAdsBottom, siteLinks, pubId, clickableBackground, rolloverAdBackgroundColor, adIconW, adIconH){
                pageOptions.siteLinks = siteLinks;
                pageOptions.pubId = pubId;
                pageOptions.rolloverAdBackgroundColor = rolloverAdBackgroundColor;
                
                var targetArr = [];
                if(numAdsTop>0){
                    var adblock1 = {
                        'container': 'adcontainer0',
                        'maxTop': numAdsTop,
                        'clickableBackgrounds': clickableBackground,
                        'adIconWidth' : adIconW,
                        'adIconHeight' : adIconH
                    };
                    jQuery.extend(adblock1,defaultBlock);
                    if(adIconW)
                    {
                        jQuery.extend(adblock1,defaultBlock_ext);
                        
                    }
                    targetArr.push(adblock1);
                }
    
                if(numAdsBottom>0){
                    var adblock2 = {
                        'container': 'adcontainer1',
                        'number': numAdsBottom,
                        'clickableBackgrounds': clickableBackground,
                        'adIconWidth' : adIconW,
                        'adIconHeight' : adIconH
                    };
                    jQuery.extend(adblock2,defaultBlock);
                    if(adIconW)
                    {
                        jQuery.extend(adblock2,defaultBlock_ext);
                        
                    }
                    targetArr.push(adblock2);
                }
                new _googCsa('ads',pageOptions, targetArr);
            }
            
            
        
            if (matchMedia("tablet")){
                init(x.desktopNumAdsTop, x.desktopNumAdsBottom, x.desktopSiteLinks, x.desktopPubId, true, '#FFFFF0', 100, 67);
            } else {
                init(x.desktopNumAdsTop, x.desktopNumAdsBottom, x.desktopSiteLinks, x.desktopPubId, true, '#FFFFF0', 120, 80);
            }
        
    
        </script>
    
    



    



    
   













        <!--[if (lte IE 9)&!(IEMobile)]>
        <script src="http://inc.t9.classistatic.com/1.1.288/js//common/polyfills/placeholder.js"></script>
        <![endif]-->
    




    

    

    

    
</body>
</html>
"""

OFFER2_HTML = u"""



    
    
    
    

    

 









    
    
    
        
    
    









    
    

















    















<!DOCTYPE html>
<!--[if IEMobile 7]>
<html data-locale="pl_PL" lang="pl_PL" class="iem7 oldie VIP"><![endif]-->
<!--[if (IE 7)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie7 lt-ie8 lt-ie9 lt-ie10 oldie VIP"><![endif]-->
<!--[if (IE 8)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie8 lt-ie9 lt-ie10 oldie VIP"><![endif]-->
<!--[if (IE 9)&!(IEMobile)]>
<html data-locale="pl_PL" lang="pl_PL" class="ie9 lt-ie10 VIP"><![endif]-->
<!--[if (gt IE 9)|(gt IEMobile 7)]><!-->
<html data-locale="pl_PL" lang="pl_PL" xmlns="http://www.w3.org/1999/html" class="VIP"><!--<![endif]-->
<head>
    <title>Kawalerka, 30 m2, Śródmieście, ul. Dobrego Pasterza – Kraków – 169137755 | Gumtree</title>
    <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
    <meta name="description" content="Mieszkanie 1-pokojowe, atrakcyjna cena!  Do wynajęcia 2-pokojowe mieszkanie o powierzchni 30 m2 przy ul. Dobrego Pasterza (Prądnik Czerwony)...169137755"/>
    <meta name="robots" content="index,follow"/>
    <meta name="format-detection" content="telephone=no"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    
    
    

    
    

    
        <meta property="og:title" content="Kawalerka, 30 m2, Śródmieście, ul. Dobrego Pasterza – Kraków – 169137755 | Gumtree"/>
        <meta property="og:type" content="product"/>
        <meta property="og:image" content='http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/TxYAAOSwNuxXcYlD/$_20.JPG?set_id=8800005007'/>
        <meta property="og:url" content="http://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/kawalerka-30-m2-srodmiescie-ul-dobrego-pasterza/1001691377550910472310409"/>
        <meta property="og:site_name" content="Gumtree"/>
        <meta property="og:country-name" content="Poland"/>
        <meta property="og:description" content="Mieszkanie 1-pokojowe, atrakcyjna cena!  Do wynajęcia 2-pokojowe mieszkanie o powierzchni 30 m2 przy ul. Dobrego Pasterza (Prądnik Czerwony)...169137755"/>
        <meta property="og:locale" content="pl_PL"/>
    
    
    
    
    
        <link rel="stylesheet" type="text/css" href='http://inc.t9.classistatic.com/1.1.288/css/all/Gumtree/PL/pl_PL/Main.min.css'/>

    
        <link rel="stylesheet" type="text/css" href='http://inc.t9.classistatic.com/1.1.288/css/all/Gumtree/PL/pl_PL/SeoViewPage.min.css'/>

    
    <link rel="publisher" href="" />
    <link rel="shortcut icon" type="image/png" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="shortcut icon" type="image/x-icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="shortcut icon" type="image/vnd.microsoft.icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/shortcut.png"/>
    <link rel="apple-touch-icon" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-iphone.png"/>
    <link rel="apple-touch-icon" sizes="72x72" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-ipad.png"/>
    <link rel="apple-touch-icon" sizes="114x114" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-iphone-retina.png"/>
    <link rel="apple-touch-icon" sizes="144x144" href="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/touch-ipad-retina.png"/>



    
        <link rel="canonical" href="http://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/krakow/kawalerka-30-m2-srodmiescie-ul-dobrego-pasterza/1001691377550910472310409"/>
    
    
    
      
      
    
    <script>!function(e,t,n){function a(a){var m=o.document.createElement("link"),A=o.document.getElementsByTagName("script")[0],d=a&&r;m.rel="stylesheet",m.href=d?e:a?t:n,A.parentNode.insertBefore(m,A),d||(document.documentElement.className+=" no-svg")}if(3===arguments.length){var o=window,r=!(!o.document.createElementNS||!o.document.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect||!document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image","1.1")||window.opera&&-1===navigator.userAgent.indexOf("Chrome")),m=new o.Image;m.onerror=function(){a(!1)},m.onload=function(){a(1===m.width&&1===m.height)},m.src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="}}
    ("http://inc.t9.classistatic.com/1.1.288/css/icons.data.svg_pl_PL.css","http://inc.t9.classistatic.com/1.1.288/css/icons.data.png_pl_PL.css","http://inc.t9.classistatic.com/1.1.288/css/icons.fallback_pl_PL.css");</script>

    <noscript>
       <link href="http://inc.t9.classistatic.com/1.1.288/css/icons.fallback_pl_PL.css" rel="stylesheet">
       <style type="text/css">
            .jsOnly {display:none !important;}
            .nonJsOnlyInlineBlock{display:inline-block !important;}
            .nonJsOnlyBlock {display:block !important;}
            .nonJsOnlyInline {display:inline !important;}
       </style>
    </noscript>

    
    
      

            <script>
            var dataLayer = dataLayer || [];
            dataLayer.push({});(function(l) {
                var dl=l[0];
                dl["p"]={};
                     dl["p"]["t"] = "VIP";
                     dl["p"]["pl"] = "BOLT-RUI";
                     dl["p"]["v"] = "1.1.288";
                     dl["p"]["lng"] ="pl_PL";
                     
                dl["u"]={};
                dl["u"]["tg"]={};
                     
                     
                     
                     
                      
                     
                     
                     
                    
                dl["c"]={};
                dl["c"]["c"]={};
                      dl["c"]["c"]["id"] = "9008";
                     dl["c"]["l0"]={};dl["c"]["l0"]["id"]="0";
                     dl["c"]["l1"]={};dl["c"]["l1"]["id"]="2";
                     dl["c"]["l2"]={};dl["c"]["l2"]["id"]="9008";
                     
                     
                dl["l"]={};
                dl["l"]["c"]={};
                      dl["l"]["c"]["id"] = "3200208";
                     dl["l"]["l0"]={};dl["l"]["l0"]["id"]="202";
                     dl["l"]["l1"]={};dl["l"]["l1"]["id"]="3200003";
                     dl["l"]["l2"]={};dl["l"]["l2"]["id"]="3200208";
                     
                     

             
      dl["a"]={};
        dl["a"]["id"] ="169137755";  
        dl["a"]["cdt"] ="1467058516"; 
        dl["a"]["lpdt"] =""; 


            })(dataLayer);

                    //gtm script
                     (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push(
                             {'gtm.start': new Date().getTime(),event:'gtm.js'}
                     );var f=d.getElementsByTagName(s)[0],
                             j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                             '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                     })(window,document,'script','dataLayer','GTM-KSFR4N');
       </script>
      
    
    <script>
        var Bolt = Bolt || {};
        Bolt.BASEJSURL = "http://inc.t9.classistatic.com/1.1.288/js/";
        Bolt.BASECSSURL = "http://inc.t9.classistatic.com/1.1.288/css/";
        Bolt.BASEIMAGEURL = "http://inc.t9.classistatic.com/1.1.288/images/";
        Bolt.BRANDNAME = "Gumtree";
        Bolt.COUNTRY = "PL";
        Bolt.DECIMAL = ",";
        Bolt.PLACEHOLDER = ".";
        Bolt.LOCALE = "pl_PL";
        Bolt.LOCALIZEAPIROOTURL = "/rui-api/localize/rui/pl_PL";
    </script>
    
        <input id='ga-account' type='hidden' value='' />
        <input id='ga-domain' type='hidden' value='' />
        <script type="text/javascript">
            var _gaq = _gaq || [];
        
            
                _gaq.push(['siteTracker._setAccount', 'UA-9157637-1']);
                _gaq.push(['siteTracker._setAllowAnchor', true]);
                _gaq.push(['siteTracker._setDomainName', '.gumtree.pl']);
                
                    _gaq.push(['siteTracker._addIgnoredRef', 'gumtree.pl']);
                
                _gaq.push(['siteTracker._setSessionCookieTimeout', 1800000]);
                _gaq.push(['siteTracker._setCampaignCookieTimeout', 15768000000]);
                _gaq.push(['siteTracker._setVisitorCookieTimeout', 63072000000]);
                _gaq.push(['siteTracker._trackPageview']);

                (function() {
                    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
                    //ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                })();


            
        
        </script>
    

    

    

</head>
<body>
    
<div id="cookieWarning">
    <div class="messageContainer">
        Aby zapewnić najwyższą jakość usług i wygodne korzystanie z serwisu, używamy informacji zapisanych w przeglądarce za pomocą plików cookies (pol.: ciasteczek). Korzystając z serwisu wyrażasz zgodę na stosowanie plików <a href="http://pomoc.gumtree.pl/PL/articles/pl/KB_Article/Cookies" target="_blank">cookies</a>. W każdej chwili możesz je zablokować korzystając z ustawień swojej przeglądarki internetowej.
        <a class="accept icon-gl-message-close" style="width:15px;height:15px;margin-top:12px"></a>
    </div>
</div>

    
        <noscript>
            <iframe src="//www.googletagmanager.com/ns.html?id=GTM-KSFR4N"
              height="0" width="0" style="display:none;visibility:hidden">
            </iframe>
        </noscript>
    
     

    <noscript>
        <div class="js-message-error">
            <div>
                <span class="icon-warning-sign"></span>
                <div class="no-js pl_PL message"></div>
            </div>
        </div>
    </noscript>


    <div class="viewport" id="div-gpt-oop">

    <div class="header">
    <!-- mobile:false -->
    <header>
        <div class="wrap">
            <div class="elements">
                <div class="left">

                    
                    

<div class="logo">
    <a href="http://www.gumtree.pl/">
        
            
                <img class="logo" src="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/logo.png" alt='Darmowe Ogłoszenia' />
            
        
    </a>
</div>


                </div>
                <div class="right ">


                    


                    
                    
    <div class="post">
        <a class="sudo-link sudo-link post-btn postcommercial" data-gtm="pc|PostAdBegin" href="/post.html">
            <span>
                
                    Dodaj ogłoszenie
                
            </span>
        </a>
    </div>

                    

                    
                    


                    
                    
<div class="nav">
    <nav>




        
        




<div class="profile" aria-haspopup="true">
    <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nqf.ugzy">
        <span class="icon  "
              style="
               ">
            <span class="icon-header-profile-out"></span>
            <span class="icon-header-profile-over"></span>
        </span>
        <span class="label">Moje Gumtree</span>
    </span>
</div>
<div class="clear"></div>

        




        <ul>
            
            
                
                    <li>
                        <span class="sudo-link sudo-link-toConvert" data-o-uri="/ybtva.ugzy">Zaloguj się</span>
                    </li>
                
            

            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zljngpuyvfg.ugzy">Zachowane ogłoszenia</span>
            </li>

            
            
            
            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nyregf.ugzy">Moje powiadomienia</span>
            </li>

            
            <li>
                <span class="sudo-link menu-text sudo-link-toConvert" data-o-uri="/zl/nqf.ugzy">Moje ogłoszenia</span>
            </li>

            
            
                <li>
                    <span class="sudo-link menu-text sudo-link-toConvert"  data-gtm="pc|FeatureAdBegin"  data-o-uri="/zl/cebzbgr.ugzy">Wypromuj ogłoszenia</span>
                </li>
            

            

            
            

            
            

            
                <li>
                    <span class="sudo-link sudo-link-toConvert" data-o-uri="/ertvfgre.ugzy">Zarejestruj się</span>
                </li>
            

        </ul>
    </nav>
</div>
                    
                    
                    
    
        
            <div class="signin">
                <span class="sudo-link sudo-link-toConvert" data-o-uri="/ybtva.ugzy">Zaloguj się</span>
            </div>
        
    



                </div>
            </div>
        </div>
    </header>
</div>



<div class="postSection headerPost">
    <div class="header diff">
        <div class="right">
            <div class="post post-btn-wrap">
                <a class="sudo-link sudo-link post-btn postcommercial"  data-gtm="pc|PostAdBegin" href="/post.html">
                    <span class="long">Dodaj ogłoszenie</span>
                </a>
            </div>
        </div>
    </div>
    <div class="clear"></div>
</div>




    
    <div class="searchbar">
        <section role="search">
            <div class="wrap">


                <form action='/search.html?page=1' class="has-location-true"
                        data-instant-search="false"
                        data-clear-searches-message='Wyczyść'
                        data-saved-search="true"
                        data-auto-complete="true"
                        data-auto-complete-api="http://cache.gumtree.pl/rui-api/autocomplete/model/pl_PL/{catId}/{locId}/{value}">
                    <fieldset>


                        
                        <div class="keyword">
    <input tabindex="1" type="text" name="q" value="" placeholder='Czego szukasz?' autocomplete="off" />
</div>
                        


                        
                        <div class="category">
    <span class="icon main-icon">
        <span class='icon-header-categories'></span>
    </span>
    <input tabindex="2" type="text" data-all='Wszystkie kategorie' placeholder='Kategoria' value="" autocomplete="off" disabled="disabled" readonly="readonly" />
    <input type="hidden" name="catId" value="" />
    <!--[if (IE 8)&!(IEMobile)]>
        <span class="icon-caret-down"></span>
    <![endif]-->
    
        <script type="text/plain">{"children":[{"children":[{"children":[],"localizedName":"pokoje do wynajęcia","id":9000},{"children":[],"localizedName":"mieszkania i domy do wynajęcia","id":9008},{"children":[],"localizedName":"mieszkania i domy - sprzedam","id":9073},{"children":[],"localizedName":"działki","id":9194},{"children":[],"localizedName":"krótki termin i domki letniskowe","id":9074},{"children":[],"localizedName":"lokal i biuro","id":9072},{"children":[],"localizedName":"parking i garaż","id":9071},{"children":[],"localizedName":"kupię mieszkanie, dom, lokal, działkę","id":9772},{"children":[],"localizedName":"szukam mieszkania do wynajęcia","id":9773},{"children":[],"localizedName":"szukam pokoju do wynajęcia","id":9774}],"localizedName":"Nieruchomości","id":2},{"children":[{"children":[],"localizedName":"samochody osobowe","id":9026},{"children":[],"localizedName":"części i akcesoria samochodowe","id":9636},{"children":[],"localizedName":"samochody dostawcze","id":9027},{"children":[],"localizedName":"motocykle i skutery","id":9028},{"children":[],"localizedName":"części i akcesoria do motocykli","id":9634},{"children":[],"localizedName":"ciągniki i maszyny rolnicze","id":9154},{"children":[],"localizedName":"ciężki sprzęt","id":9622},{"children":[],"localizedName":"przyczepy i naczepy","id":9155},{"children":[],"localizedName":"quady, atv i inne","id":9621},{"children":[],"localizedName":"części i akcesoria do innych pojazdów","id":9635},{"children":[],"localizedName":"kupię samochód","id":9763},{"children":[],"localizedName":"kupię motocykl, skuter, pojazd","id":9764},{"children":[],"localizedName":"kupię części, akcesoria samochodowe","id":9765},{"children":[],"localizedName":"kupię części, akcesoria do innych pojazdów","id":9766}],"localizedName":"Motoryzacja","id":5},{"children":[{"children":[],"localizedName":"motorówki","id":9219},{"children":[],"localizedName":"skutery wodne","id":9222},{"children":[],"localizedName":"żaglówki","id":9221},{"children":[],"localizedName":"kajaki i pontony","id":9220},{"children":[],"localizedName":"silniki do łodzi","id":9223},{"children":[],"localizedName":"akcesoria do łodzi","id":9224},{"children":[],"localizedName":"inne pojazdy wodne","id":9225},{"children":[],"localizedName":"łodzie wiosłowe","id":9226},{"children":[],"localizedName":"kupię łódź, części, akcesoria","id":9787}],"localizedName":"Łodzie i Pojazdy wodne","id":9218},{"children":[{"children":[],"localizedName":"audio i hi-fi","id":9260},{"children":[],"localizedName":"cesje","id":9353},{"children":[],"localizedName":"fotografia i video","id":9281},{"children":[],"localizedName":"gry video i konsole","id":9265},{"children":[],"localizedName":"komputery i software","id":9238},{"children":[],"localizedName":"radiokomunikacja","id":9352},{"children":[],"localizedName":"tablety i bookreadery","id":9259},{"children":[],"localizedName":"telefony i akcesoria","id":9247},{"children":[],"localizedName":"telewizory i odtwarzacze","id":9276},{"children":[],"localizedName":"elektronika inne","id":9286},{"children":[],"localizedName":"kupię sprzęt elektroniczny","id":9767}],"localizedName":"Elektronika","id":9237},{"children":[{"children":[],"localizedName":"akwarystyka","id":9612},{"children":[],"localizedName":"koty i kocięta","id":9125},{"children":[],"localizedName":"psy i szczenięta","id":9131},{"children":[],"localizedName":"ptaki","id":9617},{"children":[],"localizedName":"inne zwierzaki","id":9126},{"children":[],"localizedName":"zwierzęta gospodarskie","id":9618},{"children":[],"localizedName":"zgubiono lub znaleziono","id":9128},{"children":[],"localizedName":"akcesoria dla zwierząt","id":9129},{"children":[],"localizedName":"usługi dla zwierząt","id":9130},{"children":[],"localizedName":"kupię zwierzaka","id":9775},{"children":[],"localizedName":"szukam akcesoriów, usług dla zwierząt","id":9776}],"localizedName":"Zwierzaki","id":9124},{"children":[{"children":[],"localizedName":"drobne pytania i hobby","id":9030},{"children":[],"localizedName":"sport, taniec i partnerzy do gry","id":9032},{"children":[],"localizedName":"zespoły i muzycy","id":9033},{"children":[],"localizedName":"wolontariat","id":9227},{"children":[],"localizedName":"wydarzenia lokalne","id":9228},{"children":[],"localizedName":"wymiana umiejętności","id":9035},{"children":[],"localizedName":"zgubiono lub znaleziono","id":9036},{"children":[],"localizedName":"przejazdy","id":9037},{"children":[],"localizedName":"podróże","id":9038},{"children":[],"localizedName":"dziękuję","id":9039},{"children":[],"localizedName":"wyznania","id":9084},{"children":[],"localizedName":"szukam starych przyjaciół","id":9132}],"localizedName":"Społeczność","id":6},{"children":[{"children":[],"localizedName":"AGD","id":9366},{"children":[],"localizedName":"meble","id":9376},{"children":[],"localizedName":"narzędzia i materiały budowlane","id":9384},{"children":[],"localizedName":"ogród","id":9398},{"children":[],"localizedName":"produkty żywnościowe i napoje","id":9407},{"children":[],"localizedName":"wyposażenie wnętrz","id":9408},{"children":[],"localizedName":"inne do domu i ogrodu","id":9023},{"children":[],"localizedName":"kupię do ogrodu","id":9784},{"children":[],"localizedName":"kupię do domu","id":9783}],"localizedName":"Dom i Ogród","id":4},{"children":[{"children":[],"localizedName":"karty kolekcjonerskie","id":9673},{"children":[],"localizedName":"książki i poligrafia","id":9674},{"children":[],"localizedName":"lampy, świeczniki i  lustra","id":9675},{"children":[],"localizedName":"meble zabytkowe","id":9676},{"children":[],"localizedName":"medale i odznaczenia","id":9677},{"children":[],"localizedName":"monety i banknoty","id":9678},{"children":[],"localizedName":"obrazy i rzeźby","id":9679},{"children":[],"localizedName":"rękodzieło","id":9680},{"children":[],"localizedName":"zastawy kuchenne","id":9681},{"children":[],"localizedName":"zabytkowe tekstylia i dekoracje","id":9682},{"children":[],"localizedName":"zegary","id":9683},{"children":[],"localizedName":"znaczki pocztowe","id":9684},{"children":[],"localizedName":"inne kolekcje","id":9685},{"children":[],"localizedName":"kupię antyki, kolekcje","id":9762}],"localizedName":"Antyki i kolekcje","id":9672},{"children":[{"children":[],"localizedName":"artykuły szkolne","id":9468},{"children":[],"localizedName":"bezpieczeństwo i zdrowie dziecka","id":9460},{"children":[],"localizedName":"buty dla dzieci","id":9461},{"children":[],"localizedName":"chrzciny i komunie","id":9469},{"children":[],"localizedName":"ciąża i karmienie","id":9464},{"children":[],"localizedName":"foteliki - nosidełka","id":9462},{"children":[],"localizedName":"kąpiel i zdrowie","id":9470},{"children":[],"localizedName":"kojce i chodziki","id":9471},{"children":[],"localizedName":"meble i wystrój pokoju","id":9463},{"children":[],"localizedName":"rowerki i inne pojazdy","id":9472},{"children":[],"localizedName":"odzież dziecięca","id":9465},{"children":[],"localizedName":"wózki dla dzieci","id":9466},{"children":[],"localizedName":"zabawki","id":9467},{"children":[],"localizedName":"inne dla dziecka","id":9489},{"children":[],"localizedName":"kupię ubranka, buty dla dziecka","id":9780},{"children":[],"localizedName":"kupię zabawki","id":9781},{"children":[],"localizedName":"kupię inne dla dziecka","id":9782}],"localizedName":"Dla Dziecka","id":9459},{"children":[{"children":[],"localizedName":"akcesoria i galanteria","id":9542},{"children":[],"localizedName":"biżuteria i zegarki","id":9563},{"children":[],"localizedName":"obuwie damskie","id":9596},{"children":[],"localizedName":"obuwie męskie","id":9604},{"children":[],"localizedName":"odzież damska","id":9565},{"children":[],"localizedName":"odzież męska","id":9584},{"children":[],"localizedName":"odzież i obuwie robocze","id":9660},{"children":[],"localizedName":"pasmanteria","id":9549},{"children":[],"localizedName":"torebki i torby","id":9551},{"children":[],"localizedName":"inne ubrania","id":9553},{"children":[],"localizedName":"walizki i plecaki","id":9552},{"children":[],"localizedName":"kupię ubrania, buty","id":9769},{"children":[],"localizedName":"kupię inne z działu mody","id":9768}],"localizedName":"Moda","id":9541},{"children":[{"children":[],"localizedName":"zdrowie","id":9691},{"children":[],"localizedName":"kosmetyki","id":9697},{"children":[],"localizedName":"perfumy i dezodoranty","id":9698},{"children":[],"localizedName":"kupię produkty zdrowotne, kosmetyki","id":9786}],"localizedName":"Zdrowie i Uroda","id":9690},{"children":[{"children":[],"localizedName":"fitness i siłownia","id":9745},{"children":[],"localizedName":"sport","id":9746},{"children":[],"localizedName":"karty i gadżety sportowe","id":9753},{"children":[],"localizedName":"sprzęt turystyczny","id":9756},{"children":[],"localizedName":"kupię sprzęt fitness, do siłowni","id":9771},{"children":[],"localizedName":"kupię sprzęt sportowy","id":9770}],"localizedName":"Sport i Fitness","id":9706},{"children":[{"children":[],"localizedName":"bilety","id":9491},{"children":[],"localizedName":"instrumenty i akcesoria muzyczne","id":9496},{"children":[],"localizedName":"komiksy i czasopisma","id":9497},{"children":[],"localizedName":"książki","id":9498},{"children":[],"localizedName":"CD, kasety i płyty","id":9514},{"children":[],"localizedName":"filmy i DVD","id":9513},{"children":[],"localizedName":"gry planszowe i puzzle","id":9515},{"children":[],"localizedName":"kupię instrument muzyczny","id":9777},{"children":[],"localizedName":"kupię bilet","id":9778},{"children":[],"localizedName":"kupię inne z działu muzyka i rozrywka","id":9779}],"localizedName":"Muzyka i Rozrywka","id":9490},{"children":[{"children":[],"localizedName":"bar, restauracja i gastronomia","id":9056},{"children":[],"localizedName":"biuro i administracja","id":9052},{"children":[],"localizedName":"praca na budowie i pracownicy fizyczni","id":9142},{"children":[],"localizedName":"fachowcy","id":9203},{"children":[],"localizedName":"finanse i księgowość","id":9050},{"children":[],"localizedName":"grafika i web design","id":9140},{"children":[],"localizedName":"hostessy, modele i aktorzy","id":9141},{"children":[],"localizedName":"hr, kadry i rekrutacja","id":9053},{"children":[],"localizedName":"inżynierowie, technicy i architekci","id":9094},{"children":[],"localizedName":"kierowcy i kurierzy","id":9097},{"children":[],"localizedName":"kontrola i inwentaryzacja","id":9208},{"children":[],"localizedName":"krawiectwo i moda","id":9204},{"children":[],"localizedName":"magazynier","id":9619},{"children":[],"localizedName":"marketing, media i pr","id":9048},{"children":[],"localizedName":"mlm","id":9532},{"children":[],"localizedName":"nauczyciele i edukacja","id":9060},{"children":[],"localizedName":"obsługa klienta i call center","id":9098},{"children":[],"localizedName":"ochrona","id":9200},{"children":[],"localizedName":"opiekunki i nianie","id":9059},{"children":[],"localizedName":"pielęgnacja i uroda","id":9054},{"children":[],"localizedName":"praca dla studentów","id":9206},{"children":[],"localizedName":"praca na produkcji","id":9620},{"children":[],"localizedName":"praca w hotelu","id":9058},{"children":[],"localizedName":"prawo i prokuratura","id":9049},{"children":[],"localizedName":"programiści, informatyka i internet","id":9005},{"children":[],"localizedName":"służba zdrowia i farmacja","id":9055},{"children":[],"localizedName":"spedycja","id":9205},{"children":[],"localizedName":"sport i fitness","id":9202},{"children":[],"localizedName":"sprzątanie i pomoc domowa","id":9138},{"children":[],"localizedName":"sprzedaż, handel  i praca w sklepie","id":9061},{"children":[],"localizedName":"turystyka","id":9207},{"children":[],"localizedName":"ulotki","id":9201},{"children":[],"localizedName":"weterynaria i rolnictwo","id":9095},{"children":[],"localizedName":"video i fotografia","id":9212},{"children":[],"localizedName":"praca inne","id":9099}],"localizedName":"Oferty Pracy","id":8},{"children":[{"children":[],"localizedName":"gastronomia","id":9291},{"children":[],"localizedName":"biuro i administracja","id":9292},{"children":[],"localizedName":"pracownicy fizyczni","id":9293},{"children":[],"localizedName":"specjaliści i technicy","id":9294},{"children":[],"localizedName":"kierowcy i kurierzy","id":9300},{"children":[],"localizedName":"marketing, reklama i PR","id":9304},{"children":[],"localizedName":"opiekunki i edukacja","id":9305},{"children":[],"localizedName":"ochrona","id":9306},{"children":[],"localizedName":"pielęgnacja i uroda","id":9308},{"children":[],"localizedName":"sprzedaż i praca w sklepie","id":9311},{"children":[],"localizedName":"szukam pracy studenckiej","id":9309},{"children":[],"localizedName":"turystyka","id":9312},{"children":[],"localizedName":"praca inne","id":9313}],"localizedName":"Szukający Zatrudnienia","id":9290},{"children":[{"children":[],"localizedName":"biura podróży","id":9150},{"children":[],"localizedName":"współpraca biznesowa","id":9325},{"children":[],"localizedName":"catering","id":9554},{"children":[],"localizedName":"usługi finansowe","id":9066},{"children":[],"localizedName":"fotografia i video","id":9146},{"children":[],"localizedName":"graficy i usługi IT","id":9234},{"children":[],"localizedName":"hurt i handel","id":9065},{"children":[],"localizedName":"komputery serwis i handel","id":9102},{"children":[],"localizedName":"usługi kurierskie","id":9337},{"children":[],"localizedName":"nauka i edukacja","id":9063},{"children":[],"localizedName":"mechanika, autoskup, pomoc drogowa","id":9145},{"children":[],"localizedName":"media i reklama","id":9217},{"children":[],"localizedName":"muzycy i artyści","id":9148},{"children":[],"localizedName":"ogrodnictwo","id":9214},{"children":[],"localizedName":"opieka i agencje niań","id":9152},{"children":[],"localizedName":"pielęgnacja i uroda","id":9064},{"children":[],"localizedName":"usługi prawne","id":9233},{"children":[],"localizedName":"przeprowadzki i transport towarów","id":9144},{"children":[],"localizedName":"przyjęcia, śluby, komunie","id":9104},{"children":[],"localizedName":"remont i budowa","id":9101},{"children":[],"localizedName":"serwis i montaż","id":9236},{"children":[],"localizedName":"sport i fitness","id":9151},{"children":[],"localizedName":"sprzątanie","id":9149},{"children":[],"localizedName":"taxi i przewozy osobowe","id":9147},{"children":[],"localizedName":"telefony","id":9341},{"children":[],"localizedName":"tłumaczenia i redakcja tekstu","id":9216},{"children":[],"localizedName":"utylizacja","id":9213},{"children":[],"localizedName":"wypożyczalnie","id":9215},{"children":[],"localizedName":"zdrowie","id":9235},{"children":[],"localizedName":"inne usługi","id":9105},{"children":[],"localizedName":"szukam usług finansowych","id":9759},{"children":[],"localizedName":"szukam usług budowlanych","id":9760},{"children":[],"localizedName":"szukam innych usług","id":9761},{"children":[],"localizedName":"szukam kursu, lekcji, korepetycji","id":9758}],"localizedName":"Usługi","id":9}],"localizedName":"Wszystkie kategorie","id":0}</script>
    
</div>
                        


                        
                        
    <div class="location">
        <span class="icon main-icon">
            <span class='icon-header-location-pin'></span>
        </span>
        <input tabindex="3" type="text" data-all='Polska' placeholder='Polska' value='Polska' autocomplete="off" disabled="disabled" readonly="readonly" />
        <input type="hidden" name="locId" value="" />
        <!--[if (IE 8)&!(IEMobile)]>
        <span class="icon-caret-down"></span>
        <![endif]-->
        
            <script type="text/plain">{"children":[{"children":[{"children":[],"localizedName":"Bardo","id":3200595},{"children":[],"localizedName":"Bielawa","id":3200085},{"children":[],"localizedName":"Bierutów","id":3200435},{"children":[],"localizedName":"Bogatynia","id":3200086},{"children":[],"localizedName":"Boguszów-Gorce","id":3200437},{"children":[],"localizedName":"Bolesławiec","id":3200087},{"children":[],"localizedName":"Bolków","id":3200436},{"children":[],"localizedName":"Brzeg Dolny","id":3200438},{"children":[],"localizedName":"Bystrzyca Kłodzka","id":3200439},{"children":[],"localizedName":"Chocianów","id":3200440},{"children":[],"localizedName":"Chojnów","id":3200441},{"children":[],"localizedName":"Długołęka","id":3200609},{"children":[],"localizedName":"Duszniki Zdrój","id":3200594},{"children":[],"localizedName":"Dzierżoniów","id":3200088},{"children":[],"localizedName":"Głogów","id":3200089},{"children":[],"localizedName":"Góra","id":3200090},{"children":[],"localizedName":"Gryfów Śląski","id":3200442},{"children":[],"localizedName":"Jawor","id":3200091},{"children":[],"localizedName":"Jelcz-Laskowice","id":3200443},{"children":[],"localizedName":"Jelenia Góra","id":3200092},{"children":[],"localizedName":"Kamienna Góra","id":3200093},{"children":[],"localizedName":"Karpacz","id":3200094},{"children":[],"localizedName":"Kąty Wrocławskie","id":3200621},{"children":[],"localizedName":"Kłodzko","id":3200095},{"children":[],"localizedName":"Kowary","id":3200444},{"children":[],"localizedName":"Kudowa-Zdrój","id":3200445},{"children":[],"localizedName":"Legnica","id":3200096},{"children":[],"localizedName":"Lubań","id":3200097},{"children":[],"localizedName":"Lubin","id":3200098},{"children":[],"localizedName":"Lubomierz","id":3200597},{"children":[],"localizedName":"Lwówek Śląski","id":3200099},{"children":[],"localizedName":"Marciszów","id":3200598},{"children":[],"localizedName":"Międzylesie","id":3200599},{"children":[],"localizedName":"Milicz","id":3200100},{"children":[],"localizedName":"Nowa Ruda","id":3200101},{"children":[],"localizedName":"Oborniki Śląskie","id":3200446},{"children":[],"localizedName":"Oleśnica","id":3200103},{"children":[],"localizedName":"Oława","id":3200102},{"children":[],"localizedName":"Piechowice","id":3200434},{"children":[],"localizedName":"Pieszyce","id":3200447},{"children":[],"localizedName":"Piława Górna","id":3200448},{"children":[],"localizedName":"Polanica-Zdrój","id":3200104},{"children":[],"localizedName":"Polkowice","id":3200105},{"children":[],"localizedName":"Sobótka","id":3200600},{"children":[],"localizedName":"Strzegom","id":3200449},{"children":[],"localizedName":"Strzelin","id":3200107},{"children":[],"localizedName":"Syców","id":3200450},{"children":[],"localizedName":"Szczawno-Zdrój","id":3200601},{"children":[],"localizedName":"Szklarska Poręba","id":3200106},{"children":[],"localizedName":"Środa Śląska","id":3200108},{"children":[],"localizedName":"Świdnica","id":3200109},{"children":[],"localizedName":"Świebodzice","id":3200110},{"children":[],"localizedName":"Trzebnica","id":3200111},{"children":[],"localizedName":"Wałbrzych","id":3200112},{"children":[],"localizedName":"Wołów","id":3200113},{"children":[],"localizedName":"Wrocław","id":3200114},{"children":[],"localizedName":"Ząbkowice Śląskie","id":3200115},{"children":[],"localizedName":"Zgorzelec","id":3200116},{"children":[],"localizedName":"Ziębice","id":3200451},{"children":[],"localizedName":"Złotoryja","id":3200117},{"children":[],"localizedName":"Żarów","id":3200452},{"children":[],"localizedName":"Żmigród","id":3200453}],"localizedName":"Dolnośląskie","id":3200007},{"children":[{"children":[],"localizedName":"Aleksandrów Kujawski","id":3200118},{"children":[],"localizedName":"Barcin","id":3200454},{"children":[],"localizedName":"Brodnica","id":3200119},{"children":[],"localizedName":"Bydgoszcz","id":3200120},{"children":[],"localizedName":"Chełmno","id":3200121},{"children":[],"localizedName":"Chełmża","id":3200455},{"children":[],"localizedName":"Ciechocinek","id":3200456},{"children":[],"localizedName":"Gniewkowo","id":3200457},{"children":[],"localizedName":"Golub-Dobrzyń","id":3200122},{"children":[],"localizedName":"Grudziądz","id":3200123},{"children":[],"localizedName":"Inowrocław","id":3200124},{"children":[],"localizedName":"Janikowo","id":3200458},{"children":[],"localizedName":"Koronowo","id":3200459},{"children":[],"localizedName":"Kruszwica","id":3200460},{"children":[],"localizedName":"Lipno","id":3200125},{"children":[],"localizedName":"Mogilno","id":3200126},{"children":[],"localizedName":"Nakło nad Notecią","id":3200127},{"children":[],"localizedName":"Radziejów","id":3200128},{"children":[],"localizedName":"Rypin","id":3200129},{"children":[],"localizedName":"Sępólno Krajeńskie","id":3200130},{"children":[],"localizedName":"Solec Kujawski","id":3200461},{"children":[],"localizedName":"Strzelno","id":3200462},{"children":[],"localizedName":"Szubin","id":3200463},{"children":[],"localizedName":"Świecie","id":3200131},{"children":[],"localizedName":"Toruń","id":3200132},{"children":[],"localizedName":"Tuchola","id":3200133},{"children":[],"localizedName":"Wąbrzeźno","id":3200134},{"children":[],"localizedName":"Więcbork","id":3200464},{"children":[],"localizedName":"Włocławek","id":3200135},{"children":[],"localizedName":"Żnin","id":3200136}],"localizedName":"Kujawsko - pomorskie","id":3200075},{"children":[{"children":[],"localizedName":"Bełżyce","id":3200465},{"children":[],"localizedName":"Biała Podlaska","id":3200137},{"children":[],"localizedName":"Biłgoraj","id":3200138},{"children":[],"localizedName":"Chełm","id":3200139},{"children":[],"localizedName":"Dęblin","id":3200466},{"children":[],"localizedName":"Hrubieszów","id":3200140},{"children":[],"localizedName":"Janów Lubelski","id":3200141},{"children":[],"localizedName":"Krasnystaw","id":3200142},{"children":[],"localizedName":"Kraśnik","id":3200143},{"children":[],"localizedName":"Lubartów","id":3200144},{"children":[],"localizedName":"Lublin","id":3200145},{"children":[],"localizedName":"Łęczna","id":3200146},{"children":[],"localizedName":"Łuków","id":3200147},{"children":[],"localizedName":"Międzyrzec Podlaski","id":3200467},{"children":[],"localizedName":"Opole Lubelskie","id":3200148},{"children":[],"localizedName":"Parczew","id":3200149},{"children":[],"localizedName":"Poniatowa","id":3200468},{"children":[],"localizedName":"Puławy","id":3200150},{"children":[],"localizedName":"Radzyń Podlaski","id":3200151},{"children":[],"localizedName":"Ryki","id":3200152},{"children":[],"localizedName":"Świdnik","id":3200153},{"children":[],"localizedName":"Terespol","id":3200469},{"children":[],"localizedName":"Tomaszów Lubelski","id":3200154},{"children":[],"localizedName":"Włodawa","id":3200155},{"children":[],"localizedName":"Zamość","id":3200156}],"localizedName":"Lubelskie","id":3200076},{"children":[{"children":[],"localizedName":"Drezdenko","id":3200158},{"children":[],"localizedName":"Gorzów Wielkopolski","id":3200157},{"children":[],"localizedName":"Gubin","id":3200159},{"children":[],"localizedName":"Kostrzyn nad Odrą","id":3200470},{"children":[],"localizedName":"Kożuchów","id":3200471},{"children":[],"localizedName":"Krosno Odrzańskie","id":3200160},{"children":[],"localizedName":"Lubsko","id":3200161},{"children":[],"localizedName":"Międzyrzecz","id":3200162},{"children":[],"localizedName":"Nowa Sól","id":3200163},{"children":[],"localizedName":"Rzepin","id":3200472},{"children":[],"localizedName":"Skwierzyna","id":3200473},{"children":[],"localizedName":"Słubice","id":3200164},{"children":[],"localizedName":"Strzelce Krajeńskie","id":3200165},{"children":[],"localizedName":"Sulechów","id":3200166},{"children":[],"localizedName":"Sulęcin","id":3200167},{"children":[],"localizedName":"Szprotawa","id":3200168},{"children":[],"localizedName":"Świebodzin","id":3200169},{"children":[],"localizedName":"Witnica","id":3200474},{"children":[],"localizedName":"Wschowa","id":3200170},{"children":[],"localizedName":"Zielona Góra","id":3200171},{"children":[],"localizedName":"Żagań","id":3200172},{"children":[],"localizedName":"Żary","id":3200173}],"localizedName":"Lubuskie","id":3200077},{"children":[{"children":[],"localizedName":"Aleksandrów Łódzki","id":3200174},{"children":[],"localizedName":"Andrespol","id":3200588},{"children":[],"localizedName":"Bełchatów","id":3200175},{"children":[],"localizedName":"Brzeziny","id":3200176},{"children":[],"localizedName":"Głowno","id":3200177},{"children":[],"localizedName":"Koluszki","id":3200475},{"children":[],"localizedName":"Konstantynów Łódzki","id":3200178},{"children":[],"localizedName":"Kutno","id":3200179},{"children":[],"localizedName":"Łask","id":3200180},{"children":[],"localizedName":"Łęczyca","id":3200181},{"children":[],"localizedName":"Łowicz","id":3200182},{"children":[],"localizedName":"Łódź","id":3200183},{"children":[],"localizedName":"Opoczno","id":3200184},{"children":[],"localizedName":"Ozorków","id":3200185},{"children":[],"localizedName":"Pabianice","id":3200186},{"children":[],"localizedName":"Pajęczno","id":3200187},{"children":[],"localizedName":"Piotrków Trybunalski","id":3200188},{"children":[],"localizedName":"Poddębice","id":3200189},{"children":[],"localizedName":"Radomsko","id":3200190},{"children":[],"localizedName":"Rawa Mazowiecka","id":3200191},{"children":[],"localizedName":"Sieradz","id":3200192},{"children":[],"localizedName":"Skierniewice","id":3200193},{"children":[],"localizedName":"Tomaszów Mazowiecki","id":3200194},{"children":[],"localizedName":"Tuszyn","id":3200476},{"children":[],"localizedName":"Wieluń","id":3200195},{"children":[],"localizedName":"Wieruszów","id":3200196},{"children":[],"localizedName":"Zduńska Wola","id":3200197},{"children":[],"localizedName":"Zelów","id":3200477},{"children":[],"localizedName":"Zgierz","id":3200198},{"children":[],"localizedName":"Żychlin","id":3200478}],"localizedName":"Łódzkie","id":3200004},{"children":[{"children":[],"localizedName":"Alwernia","id":3200610},{"children":[],"localizedName":"Andrychów","id":3200199},{"children":[],"localizedName":"Bochnia","id":3200200},{"children":[],"localizedName":"Brzesko","id":3200201},{"children":[],"localizedName":"Brzeszcze","id":3200479},{"children":[],"localizedName":"Bukowina Tatrzańska","id":3200202},{"children":[],"localizedName":"Bukowno","id":3200480},{"children":[],"localizedName":"Chełmek","id":3200481},{"children":[],"localizedName":"Chrzanów","id":3200203},{"children":[],"localizedName":"Czorsztyn","id":3200611},{"children":[],"localizedName":"Dąbrowa Tarnowska","id":3200204},{"children":[],"localizedName":"Gorlice","id":3200205},{"children":[],"localizedName":"Kęty","id":3200206},{"children":[],"localizedName":"Kocmyrzów","id":3200618},{"children":[],"localizedName":"Kościelisko","id":3200207},{"children":[],"localizedName":"Kraków","id":3200208},{"children":[],"localizedName":"Krościenko nad Dunajcem","id":3200491},{"children":[],"localizedName":"Krynica-Zdrój","id":3200209},{"children":[],"localizedName":"Krzeszowice","id":3200482},{"children":[],"localizedName":"Libiąż","id":3200483},{"children":[],"localizedName":"Limanowa","id":3200210},{"children":[],"localizedName":"Miechów","id":3200211},{"children":[],"localizedName":"Mszana Dolna","id":3200484},{"children":[],"localizedName":"Myślenice","id":3200212},{"children":[],"localizedName":"Niedzica","id":3200612},{"children":[],"localizedName":"Niepołomice","id":3200485},{"children":[],"localizedName":"Nowy Sącz","id":3200213},{"children":[],"localizedName":"Nowy Targ","id":3200214},{"children":[],"localizedName":"Olkusz","id":3200215},{"children":[],"localizedName":"Oświęcim","id":3200216},{"children":[],"localizedName":"Piwniczna-Zdrój","id":3200486},{"children":[],"localizedName":"Proszowice","id":3200217},{"children":[],"localizedName":"Rabka-Zdrój","id":3200487},{"children":[],"localizedName":"Skawina","id":3200218},{"children":[],"localizedName":"Słomniki","id":3200619},{"children":[],"localizedName":"Stary Sącz","id":3200488},{"children":[],"localizedName":"Sucha Beskidzka","id":3200219},{"children":[],"localizedName":"Szczawnica","id":3200220},{"children":[],"localizedName":"Tarnów","id":3200221},{"children":[],"localizedName":"Trzebinia","id":3200222},{"children":[],"localizedName":"Tuchów","id":3200489},{"children":[],"localizedName":"Wadowice","id":3200223},{"children":[],"localizedName":"Wieliczka","id":3200224},{"children":[],"localizedName":"Wolbrom","id":3200490},{"children":[],"localizedName":"Zakopane","id":3200225}],"localizedName":"Małopolskie","id":3200003},{"children":[{"children":[],"localizedName":"Pd - wsch powiaty","id":3200043},{"children":[],"localizedName":"Pd - zach powiaty","id":3200044},{"children":[],"localizedName":"Pn - wsch powiaty","id":3200036},{"children":[],"localizedName":"Pn - zach powiaty","id":3200041},{"children":[],"localizedName":"Południowe powiaty","id":3200042},{"children":[],"localizedName":"Północne powiaty","id":3200027},{"children":[],"localizedName":"Warszawa","id":3200008},{"children":[],"localizedName":"Wschodnie powiaty","id":3200045},{"children":[],"localizedName":"Zachodnie powiaty","id":3200046}],"localizedName":"Mazowieckie","id":3200001},{"children":[{"children":[],"localizedName":"Brzeg","id":3200226},{"children":[],"localizedName":"Głubczyce","id":3200227},{"children":[],"localizedName":"Grodków","id":3200526},{"children":[],"localizedName":"Kędzierzyn-Koźle","id":3200228},{"children":[],"localizedName":"Kluczbork","id":3200229},{"children":[],"localizedName":"Krapkowice","id":3200230},{"children":[],"localizedName":"Namysłów","id":3200231},{"children":[],"localizedName":"Niemodlin","id":3200527},{"children":[],"localizedName":"Nysa","id":3200232},{"children":[],"localizedName":"Olesno","id":3200233},{"children":[],"localizedName":"Opole","id":3200234},{"children":[],"localizedName":"Ozimek","id":3200528},{"children":[],"localizedName":"Paczków","id":3200529},{"children":[],"localizedName":"Praszka","id":3200530},{"children":[],"localizedName":"Prószków","id":3200593},{"children":[],"localizedName":"Prudnik","id":3200235},{"children":[],"localizedName":"Strzelce Opolskie","id":3200236},{"children":[],"localizedName":"Zawadzkie","id":3200531},{"children":[],"localizedName":"Zdzieszowice","id":3200532}],"localizedName":"Opolskie","id":3200078},{"children":[{"children":[],"localizedName":"Brzozów","id":3200237},{"children":[],"localizedName":"Cisna","id":3200607},{"children":[],"localizedName":"Dębica","id":3200238},{"children":[],"localizedName":"Jarosław","id":3200239},{"children":[],"localizedName":"Jasło","id":3200240},{"children":[],"localizedName":"Kolbuszowa","id":3200241},{"children":[],"localizedName":"Krosno","id":3200242},{"children":[],"localizedName":"Lesko","id":3200243},{"children":[],"localizedName":"Leżajsk","id":3200244},{"children":[],"localizedName":"Lubaczów","id":3200245},{"children":[],"localizedName":"Łańcut","id":3200246},{"children":[],"localizedName":"Mielec","id":3200247},{"children":[],"localizedName":"Nisko","id":3200248},{"children":[],"localizedName":"Nowa Dęba","id":3200533},{"children":[],"localizedName":"Przemyśl","id":3200249},{"children":[],"localizedName":"Przeworsk","id":3200250},{"children":[],"localizedName":"Ropczyce","id":3200251},{"children":[],"localizedName":"Rzeszów","id":3200252},{"children":[],"localizedName":"Sanok","id":3200253},{"children":[],"localizedName":"Sędziszów Małopolski","id":3200534},{"children":[],"localizedName":"Stalowa Wola","id":3200254},{"children":[],"localizedName":"Strzebowiska","id":3200608},{"children":[],"localizedName":"Strzyżów","id":3200255},{"children":[],"localizedName":"Tarnobrzeg","id":3200256},{"children":[],"localizedName":"Ustrzyki Dolne","id":3200257}],"localizedName":"Podkarpackie","id":3200079},{"children":[{"children":[],"localizedName":"Augustów","id":3200258},{"children":[],"localizedName":"Białystok","id":3200259},{"children":[],"localizedName":"Bielsk Podlaski","id":3200260},{"children":[],"localizedName":"Czarna Białostocka","id":3200535},{"children":[],"localizedName":"Dąbrowa Białostocka","id":3200536},{"children":[],"localizedName":"Grajewo","id":3200261},{"children":[],"localizedName":"Hajnówka","id":3200262},{"children":[],"localizedName":"Kolno","id":3200263},{"children":[],"localizedName":"Łapy","id":3200264},{"children":[],"localizedName":"Łomża","id":3200265},{"children":[],"localizedName":"Mońki","id":3200266},{"children":[],"localizedName":"Sejny","id":3200267},{"children":[],"localizedName":"Siemiatycze","id":3200268},{"children":[],"localizedName":"Sokółka","id":3200269},{"children":[],"localizedName":"Suwałki","id":3200270},{"children":[],"localizedName":"Wasilków","id":3200537},{"children":[],"localizedName":"Wysokie Mazowieckie","id":3200271},{"children":[],"localizedName":"Zambrów","id":3200272}],"localizedName":"Podlaskie","id":3200080},{"children":[{"children":[],"localizedName":"Bytów","id":3200407},{"children":[],"localizedName":"Chojnice","id":3200408},{"children":[],"localizedName":"Czersk","id":3200539},{"children":[],"localizedName":"Człuchów","id":3200409},{"children":[],"localizedName":"Gdańsk","id":3200072},{"children":[],"localizedName":"Gdynia","id":3200073},{"children":[],"localizedName":"Gniew","id":3200543},{"children":[],"localizedName":"Hel","id":3200410},{"children":[],"localizedName":"Jastarnia","id":3200411},{"children":[],"localizedName":"Jastrzębia Góra","id":3200412},{"children":[],"localizedName":"Kartuzy","id":3200413},{"children":[],"localizedName":"Karwia","id":3200414},{"children":[],"localizedName":"Kościerzyna","id":3200415},{"children":[],"localizedName":"Krynica Morska","id":3200416},{"children":[],"localizedName":"Kwidzyn","id":3200417},{"children":[],"localizedName":"Lębork","id":3200419},{"children":[],"localizedName":"Łeba","id":3200418},{"children":[],"localizedName":"Malbork","id":3200420},{"children":[],"localizedName":"Miastko","id":3200538},{"children":[],"localizedName":"Nowy Dwór Gdański","id":3200421},{"children":[],"localizedName":"Pelplin","id":3200541},{"children":[],"localizedName":"Pępowo","id":3200589},{"children":[],"localizedName":"Prabuty","id":3200540},{"children":[],"localizedName":"Pruszcz Gdański","id":3200422},{"children":[],"localizedName":"Puck","id":3200423},{"children":[],"localizedName":"Reda","id":3200424},{"children":[],"localizedName":"Rumia","id":3200425},{"children":[],"localizedName":"Skarszewy","id":3200542},{"children":[],"localizedName":"Słupsk","id":3200426},{"children":[],"localizedName":"Sopot","id":3200074},{"children":[],"localizedName":"Starogard Gdański","id":3200427},{"children":[],"localizedName":"Stegna","id":3200428},{"children":[],"localizedName":"Sztum","id":3200429},{"children":[],"localizedName":"Sztutowo","id":3200544},{"children":[],"localizedName":"Tczew","id":3200430},{"children":[],"localizedName":"Ustka","id":3200431},{"children":[],"localizedName":"Wejherowo","id":3200432},{"children":[],"localizedName":"Władysławowo","id":3200433},{"children":[],"localizedName":"Żukowo","id":3200590}],"localizedName":"Pomorskie","id":3200005},{"children":[{"children":[],"localizedName":"Będzin","id":3200273},{"children":[],"localizedName":"Bielsko-Biała","id":3200274},{"children":[],"localizedName":"Bieruń","id":3200275},{"children":[],"localizedName":"Blachownia","id":3200545},{"children":[],"localizedName":"Brenna","id":3200605},{"children":[],"localizedName":"Bytom","id":3200277},{"children":[],"localizedName":"Chorzów","id":3200278},{"children":[],"localizedName":"Cieszyn","id":3200279},{"children":[],"localizedName":"Czechowice-Dziedzice","id":3200546},{"children":[],"localizedName":"Czeladź","id":3200547},{"children":[],"localizedName":"Czerwionka-Leszczyny","id":3200548},{"children":[],"localizedName":"Częstochowa","id":3200280},{"children":[],"localizedName":"Dąbrowa Górnicza","id":3200281},{"children":[],"localizedName":"Gliwice","id":3200282},{"children":[],"localizedName":"Imielin","id":3200549},{"children":[],"localizedName":"Jastrzębie-Zdrój","id":3200283},{"children":[],"localizedName":"Jaworzno","id":3200284},{"children":[],"localizedName":"Kalety","id":3200550},{"children":[],"localizedName":"Katowice","id":3200285},{"children":[],"localizedName":"Kłobuck","id":3200286},{"children":[],"localizedName":"Knurów","id":3200551},{"children":[],"localizedName":"Korbielów","id":3200604},{"children":[],"localizedName":"Lędziny","id":3200552},{"children":[],"localizedName":"Lubliniec","id":3200287},{"children":[],"localizedName":"Łaziska Górne","id":3200553},{"children":[],"localizedName":"Mikołów","id":3200288},{"children":[],"localizedName":"Milówka","id":3200606},{"children":[],"localizedName":"Mysłowice","id":3200289},{"children":[],"localizedName":"Myszków","id":3200290},{"children":[],"localizedName":"Orzesze","id":3200554},{"children":[],"localizedName":"Piekary Śląskie","id":3200291},{"children":[],"localizedName":"Poręba","id":3200555},{"children":[],"localizedName":"Pszczyna","id":3200292},{"children":[],"localizedName":"Pszów","id":3200556},{"children":[],"localizedName":"Pyskowice","id":3200557},{"children":[],"localizedName":"Racibórz","id":3200293},{"children":[],"localizedName":"Radlin","id":3200558},{"children":[],"localizedName":"Radzionków","id":3200559},{"children":[],"localizedName":"Ruda Śląska","id":3200294},{"children":[],"localizedName":"Rybnik","id":3200295},{"children":[],"localizedName":"Rydułtowy","id":3200560},{"children":[],"localizedName":"Siemianowice Śląskie","id":3200296},{"children":[],"localizedName":"Siewierz","id":3200602},{"children":[],"localizedName":"Skoczów","id":3200561},{"children":[],"localizedName":"Sosnowiec","id":3200297},{"children":[],"localizedName":"Szczyrk","id":3200299},{"children":[],"localizedName":"Świerklaniec","id":3200603},{"children":[],"localizedName":"Świętochłowice","id":3200298},{"children":[],"localizedName":"Tarnowskie Góry","id":3200300},{"children":[],"localizedName":"Tychy","id":3200301},{"children":[],"localizedName":"Ustroń","id":3200562},{"children":[],"localizedName":"Wisła","id":3200302},{"children":[],"localizedName":"Wodzisław Śląski","id":3200303},{"children":[],"localizedName":"Wojkowice","id":3200563},{"children":[],"localizedName":"Zabrze","id":3200304},{"children":[],"localizedName":"Zawiercie","id":3200305},{"children":[],"localizedName":"Żory","id":3200306},{"children":[],"localizedName":"Żywiec","id":3200307}],"localizedName":"Śląskie","id":3200002},{"children":[{"children":[],"localizedName":"Busko-Zdrój","id":3200308},{"children":[],"localizedName":"Jędrzejów","id":3200309},{"children":[],"localizedName":"Kazimierza Wielka","id":3200310},{"children":[],"localizedName":"Kielce","id":3200311},{"children":[],"localizedName":"Końskie","id":3200312},{"children":[],"localizedName":"Opatów","id":3200313},{"children":[],"localizedName":"Ostrowiec Świętokrzyski","id":3200314},{"children":[],"localizedName":"Pińczów","id":3200315},{"children":[],"localizedName":"Połaniec","id":3200564},{"children":[],"localizedName":"Sandomierz","id":3200316},{"children":[],"localizedName":"Skarżysko-Kamienna","id":3200317},{"children":[],"localizedName":"Starachowice","id":3200318},{"children":[],"localizedName":"Staszów","id":3200319},{"children":[],"localizedName":"Suchedniów","id":3200565},{"children":[],"localizedName":"Włoszczowa","id":3200320}],"localizedName":"Świętokrzyskie","id":3200082},{"children":[{"children":[],"localizedName":"Barczewo","id":3200613},{"children":[],"localizedName":"Bartoszyce","id":3200321},{"children":[],"localizedName":"Biskupiec","id":3200322},{"children":[],"localizedName":"Braniewo","id":3200323},{"children":[],"localizedName":"Dobre Miasto","id":3200324},{"children":[],"localizedName":"Działdowo","id":3200325},{"children":[],"localizedName":"Elbląg","id":3200326},{"children":[],"localizedName":"Ełk","id":3200327},{"children":[],"localizedName":"Giżycko","id":3200328},{"children":[],"localizedName":"Gołdap","id":3200329},{"children":[],"localizedName":"Górowo Iławieckie","id":3200615},{"children":[],"localizedName":"Iława","id":3200330},{"children":[],"localizedName":"Kętrzyn","id":3200331},{"children":[],"localizedName":"Lidzbark Warmiński","id":3200332},{"children":[],"localizedName":"Lubawa","id":3200566},{"children":[],"localizedName":"Mikołajki","id":3200333},{"children":[],"localizedName":"Morąg","id":3200567},{"children":[],"localizedName":"Mrągowo","id":3200334},{"children":[],"localizedName":"Nidzica","id":3200335},{"children":[],"localizedName":"Nowe Miasto Lubawskie","id":3200336},{"children":[],"localizedName":"Olecko","id":3200337},{"children":[],"localizedName":"Olsztyn","id":3200338},{"children":[],"localizedName":"Olsztynek","id":3200568},{"children":[],"localizedName":"Orneta","id":3200569},{"children":[],"localizedName":"Ostróda","id":3200339},{"children":[],"localizedName":"Pasłęk","id":3200570},{"children":[],"localizedName":"Pieniężno","id":3200616},{"children":[],"localizedName":"Pisz","id":3200340},{"children":[],"localizedName":"Ruciane-Nida","id":3200617},{"children":[],"localizedName":"Szczytno","id":3200341},{"children":[],"localizedName":"Węgorzewo","id":3200342}],"localizedName":"Warmińsko-mazurskie","id":3200083},{"children":[{"children":[],"localizedName":"Buk","id":3200587},{"children":[],"localizedName":"Chodzież","id":3200343},{"children":[],"localizedName":"Czarnków","id":3200344},{"children":[],"localizedName":"Gniezno","id":3200345},{"children":[],"localizedName":"Gostyń","id":3200346},{"children":[],"localizedName":"Grodzisk Wielkopolski","id":3200347},{"children":[],"localizedName":"Jarocin","id":3200348},{"children":[],"localizedName":"Jastrowie","id":3200571},{"children":[],"localizedName":"Kalisz","id":3200349},{"children":[],"localizedName":"Kępno","id":3200350},{"children":[],"localizedName":"Koło","id":3200351},{"children":[],"localizedName":"Konin","id":3200352},{"children":[],"localizedName":"Kostrzyn","id":3200572},{"children":[],"localizedName":"Kościan","id":3200353},{"children":[],"localizedName":"Kórnik","id":3200573},{"children":[],"localizedName":"Krotoszyn","id":3200354},{"children":[],"localizedName":"Leszno","id":3200355},{"children":[],"localizedName":"Luboń","id":3200356},{"children":[],"localizedName":"Międzychód","id":3200357},{"children":[],"localizedName":"Mosina","id":3200358},{"children":[],"localizedName":"Murowana Goślina","id":3200359},{"children":[],"localizedName":"Nowy Tomyśl","id":3200360},{"children":[],"localizedName":"Oborniki","id":3200361},{"children":[],"localizedName":"Opalenica","id":3200574},{"children":[],"localizedName":"Ostrów Wielkopolski","id":3200362},{"children":[],"localizedName":"Ostrzeszów","id":3200363},{"children":[],"localizedName":"Piła","id":3200364},{"children":[],"localizedName":"Pleszew","id":3200365},{"children":[],"localizedName":"Pniewy","id":3200575},{"children":[],"localizedName":"Pobiedziska","id":3200576},{"children":[],"localizedName":"Poznań","id":3200366},{"children":[],"localizedName":"Puszczykowo","id":3200577},{"children":[],"localizedName":"Rawicz","id":3200367},{"children":[],"localizedName":"Rogoźno","id":3200578},{"children":[],"localizedName":"Słupca","id":3200368},{"children":[],"localizedName":"Swarzędz","id":3200369},{"children":[],"localizedName":"Szamotuły","id":3200370},{"children":[],"localizedName":"Śrem","id":3200371},{"children":[],"localizedName":"Środa Wielkopolska","id":3200372},{"children":[],"localizedName":"Trzcianka","id":3200373},{"children":[],"localizedName":"Trzemeszno","id":3200579},{"children":[],"localizedName":"Turek","id":3200374},{"children":[],"localizedName":"Wągrowiec","id":3200375},{"children":[],"localizedName":"Witkowo","id":3200580},{"children":[],"localizedName":"Wolsztyn","id":3200376},{"children":[],"localizedName":"Wronki","id":3200581},{"children":[],"localizedName":"Września","id":3200377},{"children":[],"localizedName":"Złotów","id":3200378}],"localizedName":"Wielkopolskie","id":3200006},{"children":[{"children":[],"localizedName":"Barlinek","id":3200379},{"children":[],"localizedName":"Białogard","id":3200380},{"children":[],"localizedName":"Cedynia","id":3200381},{"children":[],"localizedName":"Chojna","id":3200620},{"children":[],"localizedName":"Choszczno","id":3200382},{"children":[],"localizedName":"Czaplinek","id":3200586},{"children":[],"localizedName":"Darłowo","id":3200383},{"children":[],"localizedName":"Dębno","id":3200384},{"children":[],"localizedName":"Drawno","id":3200385},{"children":[],"localizedName":"Drawsko Pomorskie","id":3200386},{"children":[],"localizedName":"Goleniów","id":3200387},{"children":[],"localizedName":"Gryfice","id":3200388},{"children":[],"localizedName":"Gryfino","id":3200389},{"children":[],"localizedName":"Kamień Pomorski","id":3200390},{"children":[],"localizedName":"Kołobrzeg","id":3200391},{"children":[],"localizedName":"Koszalin","id":3200392},{"children":[],"localizedName":"Łobez","id":3200393},{"children":[],"localizedName":"Mielno","id":3200395},{"children":[],"localizedName":"Międzyzdroje","id":3200394},{"children":[],"localizedName":"Myślibórz","id":3200396},{"children":[],"localizedName":"Nowogard","id":3200397},{"children":[],"localizedName":"Police","id":3200398},{"children":[],"localizedName":"Połczyn-Zdrój","id":3200582},{"children":[],"localizedName":"Pyrzyce","id":3200399},{"children":[],"localizedName":"Sławno","id":3200400},{"children":[],"localizedName":"Stargard Szczeciński","id":3200401},{"children":[],"localizedName":"Szczecin","id":3200402},{"children":[],"localizedName":"Szczecinek","id":3200403},{"children":[],"localizedName":"Świdwin","id":3200404},{"children":[],"localizedName":"Świnoujście","id":3200405},{"children":[],"localizedName":"Trzebiatów","id":3200583},{"children":[],"localizedName":"Wałcz","id":3200406},{"children":[],"localizedName":"Wolin","id":3200584},{"children":[],"localizedName":"Złocieniec","id":3200585}],"localizedName":"Zachodniopomorskie","id":3200084}],"localizedName":"Polska","id":202}</script>
        
    </div>

                        


                        
                        <div class="button">
    <button tabindex="4">
        <span class="icon">
            <span class='icon-header-search-out'></span>
            <span class='icon-header-search-over'></span>
        </span>
        <span class="label">Szukaj</span>
    </button>
</div>
                        


                    </fieldset>


                    
                    
                    



                    
                    
                    


                </form>


            </div>
        </section>
    </div>


    




    


    <div class="containment">

        

        <div class="page extra" >


            


    

    

    
    
   
   





            
            
    <div class="breadcrumbs ">
            
                


    <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
        <a class="category" href="http://www.gumtree.pl/s-malopolskie/v1l3200003p1">
            <span class="microdata" itemprop="title">Małopolska</span>
        </a>
        <meta itemprop="url" content="http://www.gumtree.pl/s-malopolskie/v1l3200003p1" />
    </span>
    <span class="icon-chevron-right"></span>
    <span></span>





            
            
                


    <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
        <a class="category" href="http://www.gumtree.pl/s-nieruchomosci/krakow/v1c2l3200208p1">
            <span class="microdata" itemprop="title">Nieruchomości</span>
        </a>
        <meta itemprop="url" content="http://www.gumtree.pl/s-nieruchomosci/krakow/v1c2l3200208p1" />
    </span>
    <span class="icon-chevron-right"></span>
    <span></span>





            
        
            <span itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                <a class="category" href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1">
                    <span class="microdata" itemprop="title">
                        
                            mieszkania i domy do wynajęcia
                        
                        
                            | 
                            Kraków
                        
                    </span>
                </a>
                <meta itemprop="url" content="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1"/>
            </span>
            <span class="icon-chevron-right"></span>
            <span></span>
            <span class="title">ogłoszenie 169137755</span>
        
    </div>

<div class="clear"></div>





            

            <div class="content">
                <section role="content">
                    <div class="wrap">
                        
                        

    
       
       
        <div class="vip-controls">
            





        </div>

        <div id="seovip-left-column" class="vip-left-column vip-header-and-details hasImages">
            <div class="vip-content-header">
                <div class="vip-title clearfix">
                    <h1 class="item-title" >
                        <span class="myAdTitle">Kawalerka, 30 m2, Śródmieście, ul. Dobrego Pasterza</span>
                        
                    </h1>
                    <div class="price">


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">950 zł</span>
            
            
            
        </span>


</div>
                    
                </div>

                <div class="vip-gallery seoVip">
                    
    <div class="wrap has-thumbs" data-base-js-url="http://inc.t9.classistatic.com/1.1.288/js/">

        
            <div class="main-bg">
                <div class="main">
                    <span class="icon-vip-arrow-left"></span>
                    <span class='vertical-alignment-helper'></span><img  data-index="0" src = "http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/TxYAAOSwNuxXcYlD/$_20.JPG?set_id=8800005007" alt="Kawalerka, 30 m2, Śródmieście, ul. Dobrego Pasterza" />
                    
                    <span class="icon-vip-arrow-right"></span>
                    <span class="icon-zoom-image"></span>
                </div>
                
                    
    <div class="counter-pic"><span class="index"></span> z <span class="length"></span></div>

                
            </div>
        
        
        
        
        <script id="vip-gallery-data" type="text/x-bolt-json">
            {"small":"[http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/TxYAAOSwNuxXcYlD/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/T80AAOSwNuxXcYlG/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/vAoAAOSwZ1BXcYlI/$_19.JPG?set_id=8800005007, http://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/k90AAOSwepJXcYlU/$_19.JPG?set_id=8800005007]","medium":"[http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/TxYAAOSwNuxXcYlD/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/T80AAOSwNuxXcYlG/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/vAoAAOSwZ1BXcYlI/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/k90AAOSwepJXcYlU/$_20.JPG?set_id=8800005007]","large":"[http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/TxYAAOSwNuxXcYlD/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/T80AAOSwNuxXcYlG/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/vAoAAOSwZ1BXcYlI/$_20.JPG?set_id=8800005007, http://i.ebayimg.com/00/s/NjAwWDgwMA==/z/k90AAOSwepJXcYlU/$_20.JPG?set_id=8800005007]","alt-tags":"[Kawalerka 30 m2 Śródmieście ul. Dobrego Pasterza z Krakow zdjęcie: 1, Kawalerka 30 m2 Śródmieście ul. Dobrego Pasterza z Krakow zdjęcie: 2, Kawalerka 30 m2 Śródmieście ul. Dobrego Pasterza z Krakow zdjęcie: 3, Kawalerka 30 m2 Śródmieście ul. Dobrego Pasterza z Krakow zdjęcie: 4]"}
        </script>
    </div>

        
        



                   
 <div class='post-it-yourself'>
    <span class='sudo-link' data-gtm="pc|PostAdBegin|eventLabel|src=SimilarAd" data-o-uri='/cbfg.ugzy?fvzvyneNqVq=1001691377550910472310409'>Dodaj takie ogłoszenie!</span>
 </div>

                </div>
                
                
<!-- TODO: separate templates with different Locale  -->
<ul class="selMenu">

<li>
    <div class="attribute">
        <span class="name">Data dodania</span>
        <span class="value">
            
                27/06/2016
            
        </span>
        
    </div>
</li>

<li>
    <div class="attribute">
        <span class="name">Lokalizacja</span>
            <span class="value">
                
<div class="location" >
    
    
        <a href="http://www.gumtree.pl/s-krakow/v1l3200208p1" >Kraków</a>, 
    
    
        <a href="http://www.gumtree.pl/s-malopolskie/v1l3200003p1" >Małopolskie</a>
    
    
</div>

            </span>
    </div>
</li>

<!-- Vehicle -->





























































<!-- End Vehicle -->



<!-- Property -->



    
    <li>
        <div class="attribute">
            <span class="name">Do wynajęcia przez</span>
            <span class="value">Agencja</span>
        </div>
    </li>









    
    <li>
        <div class="attribute">
            <span class="name">Dostępny</span>
            <span class="value">27/06/2016</span>
        </div>
    </li>











    
    <li>
        <div class="attribute">
            <span class="name">Rodzaj nieruchomości</span>
            <span class="value">Mieszkanie</span>
        </div>
    </li>






















    
    <li>
        <div class="attribute">
            <span class="name">Liczba pokoi</span>
            <span class="value">Kawalerka lub garsoniera</span>
        </div>
    </li>








    
    <li>
        <div class="attribute">
            <span class="name">Liczba łazienek</span>
            <span class="value">1 łazienka</span>
        </div>
    </li>





    
    <li>
        <div class="attribute">
            <span class="name">Wielkość (m2)</span>
            <span class="value">30</span>
        </div>
    </li>







    
    <li>
        <div class="attribute">
            <span class="name">Parking</span>
            <span class="value">Ulica</span>
        </div>
    </li>













<!-- Baby, kids, pregnant -->


<!-- End Baby, kids, pregnant -->

<!-- Computers and Electronics -->











<!-- End Computers and Electronics -->

<!-- Courses, Workshops -->











<!-- End Courses, Workshops -->

<!-- Home/Fashion -->

















<!-- End Home Fashion -->

<!-- Services -->











<!-- End Services -->

<!-- Free time/leisure -->











<!-- End Free time -->

<!-- Pet -->









<!-- End Pet -->

<!-- Job -->






<!-- new for SG -->




































































































































































































































































































































































































































<li>

  

</li>
</ul>

                <div class="clear"></div>
            </div>
            <div class="vip-details seoVip">
                 
    <div class="description" >
        <span class="pre"
            
                
                style="font-family: inherit; white-space: pre-wrap;"
            
        ><p></p><p>Mieszkanie 1-pokojowe, atrakcyjna cena!</p>  <p>Do wynajęcia 2-pokojowe mieszkanie o powierzchni 30 m2 przy ul. Dobrego Pasterza (Prądnik Czerwony)</p>  <p>Mieszkanie składa się z komfortowego pokoju, aneksu kuchennego, łazienki oraz przedpokoju. W pokoju na podłodze zadbany parkiet dębowy, w kuchni i łazience terakota.</p>  <p>Mieszkanie częściowo umeblowane (możliwość uzupełnienia umeblowania na życzenie klienta), wyposażone w nowy markowy AGD (pralka, lodówka, płyta elektryczna). Bardzo dobry standard wykończenia.</p>  <p>Ogrzewanie centralne i ciepła woda wliczone w czynsz administracyjny.</p>  <p>Budynek położony w doskonałej lokalizacji. W niewielkiej odległości przystanków komunikacji miejskiej autobusowej. W okolicy liczne sklepy, apteka, przychodnia, TESCO. Do Centrum Handlowego Krokus, Aqua Parku, Multikina 2 przystanki autobusem.<br />Dojazd do centrum Miasta 15min. autobusem lub 10 min. samochodem.</p>  <p>Właściciel zastrzega, że wynajmie mieszkanie wyłącznie osobom bez małych dzieci oraz bez zwierząt. 1-2 spokojne osoby.</p>  <p>Czynsz najmu: 950 zł + czynsz administracyjny 250zł + prąd.</p>  <p>Kontakt do agenta:<br />Marek Wawrzynkiewicz<br />+48 503 588 845<br />marek2 at sadurscy. pl</p><p>Aby zobaczyć ofertę ponownie zapisz adres strony:</p><p>http://krakow.sadurscy.pl/mieszkania/wynajem/%C5%9Ar%C3%B3dmie%C5%9Bcie/Dobrego%20Pasterza/oferta-BS2-MW-169692/</p><p>Lub zapisz jej numer i wpisz w Google:</p><p>BS2-MW-169692</p><p>Kraków, ul. Dobrego Pasterza, Prądnik Czerwony, Grzegórzki, Śródmieście</p></span>
    </div>

    

             </div>



        </div>

        <div class="vip-right-column">
            <div class="vip-seller-forms-container">
                <div class="contact-wrapper ">
                    <div id="sm-share-cnt" class="clearfix">
                         <div id="sm-cnt">
                            
                               
    <div id="sm">
        <ul class="sm-ul buttons clearfix">
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-facebook sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-gmailplus sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span data-text='Sprawdź co dzieje się na Gumtree! {0}' class="icon-seo-twitter sm-icons"></span></a></li>
            <li class="button"><a href="#" target="_blank"><span class="icon-seo-pinterest sm-icons"></span></a></li>
            
            <li class="button last mailto"><a href="#"><span data-subject = 'To może Cię zainteresować! {0}' data-body = 'Witaj! Myślę, że to ogłoszenie na Gumtree może Cię zainteresować. {0} %0D%0ADołącz do społeczności Gumtree:%0D%0AFacebook: https://www.facebook.com/GumtreePolska %0D%0A Google+: https://plus.google.com/103950977256553454134/posts %0D%0A Twitter: https://twitter.com/gumtreepolska' class="icon-seo-mail sm-icons"></span></a></li>
        </ul>
    </div>

                            
                         </div>

                        <div id="share">
                         
    <div class="sharevisitInfo no-visit-0">
        
        
        
    </div>

                        </div>
                    </div>

                    <div class="abt1 vip-seller-container clearfix">

                        <div class="vip-seller clearfix">
                            




    <span class="icon-user"></span>


<span class="username">

    <a 

        
        href="/u-oferty-sprzedazy/m-wawrzynkiewicz/v1u104723104p1"
        

        >

        
            Marek Wawrzynkiewicz
        

        <span class="more-ads">(Zobacz więcej ogłoszeń)</span>
    </a>
</span>


    
        
    
        <span class="usersince">Użytkownik od 06-2015</span>
    

    




                        </div>

                        <div class="vip-usr-interactions clearfix">
                            
                            <div class="usr-interactions">
                                <div class="vip vip-contact">
                                    
                                    
<div class='reply_controls clearfix '>
    
    <a href="tel:503-588-845" class="button telephone">
    <span class="icon-phone-blue icon-phone-green"></span>
    <span class="icon-phone-white"></span>
    <span id='phone-number' class="label"  data-shortname-text='Połączenia' data-show-number-text='*** Pokaż numer telefonu'>503-588-845</span>
</a>
    
    <a href="javascript:void(0)" class="title other-country">
        <span class="icon-envelope-alt-green"></span>
        <span class="icon-envelope-alt-white"></span>
        <span class="label reply-label" data-shortname-text='E-mail'>E-mail</span>
    </a>
</div>

<form class="replyAd" data-attachment-size="2097152" data-gtm="npc|R2SEmailBegin"  data-success-msg='Twoja wiadomość została wysłana' method="post" action="/rui-api/page/reply/model/pl_PL" novalidate>
    <input name="machineId" type="hidden"/>
    <input name="rand" id="rand" type="hidden"/>
    <input name="fileName" id="fileName" type="hidden"/>

    
    <div class="gl-messages-replyAds-srp">
        <a href="javascript:void(0)" class="close_btn">
            <span class="icon-gl-message-close"></span>
        </a>
    </div>

    
    <label>
        <span class="label">Wiadomość</span>
    </label>
    

    
  
<div class="messageArea">
    
    <ul class="canned-responses">
        
         <li>
             <label class="checkbox-label">
                 <input type="checkbox" class="checkbox" />
                 <span data-i18n="vip.reply.canned.imInterested">Zainteresowała mnie ta oferta. Proszę o kontakt.</span>
             </label>
         </li>
         
         <li>
             <label class="checkbox-label">
                 <input type="checkbox" class="checkbox" />
                 <span data-i18n="vip.reply.canned.whenWhereICanSeeIt">Gdzie i kiedy mogę to zobaczyć?</span>
             </label>
         </li>
         
    </ul>
    
</div>



    
    <label>
        
        <textarea name="replyMessage"></textarea>
        
    </label>
    

    
    <label>
        <span class="label">Imię</span>
        
        <input name="buyerName" type="text" value=""/>
        
    </label>
    

    
    <label>
        <span class="label">E-mail</span>
        
        <input name="email" type="email" value=""/>
        
    </label>
    

    
    <label>
        <span class="phone label">Telefon (Opcjonalnie)</span>
        
        <input name="phoneNumber" type="text" value=""/>
        
    </label>
    

    

    
    <label class="checkbox-label">
        <input type="checkbox" name="isSendMeCopyEmail"  />
        <span class="label">Wyślij mi kopię e-maila</span>
    </label>
    



    <input type="hidden" name="adId" value="1001691377550910472310409"/>



    <button class="submit-reply" type="submit">Wyślij</button>

    
<div class="privacypolicy">
    Klikając "Wyślij", wyrażasz zgodę na nasze <span class=sudo-link data-o-uri="uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Mnfnql-xbemlfgnavn" data-target="_self"> Zasady korzystania</span> i <span class=sudo-link data-o-uri="/cevinpl-cbyvpl" data-target="_self">Politykę prywatności</span> oraz zgadzasz się na otrzymywanie naszych newsletterów i ofert promocyjnych.
</div>

</form>
<form name="fileAttachmentForm" id="fileAttachmentForm" target="uploadedFile" method="post" action="/fileattachmentuploader" enctype="multipart/form-data">
    <input type="hidden" name="adId" value="1001691377550910472310409"/>
</form>



                                </div>
                            </div>
                            
                        </div>

                    </div>
                </div>
                
                
                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL"  data-adid="169137755">
                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                    <span class="label" data-toggle-text='Dodane do Zachowanych'>Dodaj do Zachowanych</span>
                </div>
                
                
                <div class="vip-seller-form-details">
                    
                        
                            <div class="vip vip-flagad">
                                
    <label class="reported-ad is-title-disabled hide">
        
        <span class="icon-warning-sign"></span>
        
        <span>Ogłoszenie zgłoszone</span>
    </label>
    <div class="unreported-ad flagad-container">
        
    <span class="sudo-link security-tips"  data-target="_blank">
    <span class="icon-lock"></span>
        <span class="security-tips-text">Porady Bezpieczeństwa</span> <span>- Twoje bezpieczeństwo jest dla nas ważne, zachęcamy do zachowania czujności.</span>
        <span data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NFnsrglCY' data-target="_blank"  >Dowiedz się więcej</span>
        
    </span>
    

        <a class="title" href="javascript:void(0)">
            
            <span class="icon-warning-sign"></span>
            
            <span class="label">Zgłoś ogłoszenie</span>
            <span class="caret-icon-area icon-caret-right"></span>
        </a>
        <form class="flagAd tallForm"  data-flagad-success='Dziękujemy za zgłoszenie. Sprawdzimy tę ofertę najszybciej jak to możliwe. '
            method="post" action="/rui-api/page/flag/confirm/pl_PL" novalidate>
            <label>
                <span class="label ">Powód</span>
            </label>
            <div>
                <input type="hidden" name="adId" value="1001691377550910472310409" />
                <input type="hidden" name="captchaToken" value="Q0FQVENIQTozMTQ5OjE0NjcwNTkzODEyODc6NDgzMWFlZGViNjJiN2I3NjdiZjc1MjcyYWVkNDE5NDg0ZWVjMDM5MA==" />                
                <ul>
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="InappropriateContent"   checked="checked" /><label>Nieodpowiednia treść</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>InappropriateContent=Nieodpowiednia treść</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="DuplicateSpam"   /><label>Duplikat/Spam</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>DuplicateSpam=Duplikat/Spam</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="PossibleFraud"   /><label>Możliwe oszustwo</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>PossibleFraud=Możliwe oszustwo</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="NotRelevant"   /><label>Nieaktualne</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>NotRelevant=Nieaktualne</label></li> -->
                
                        <li><input type="radio" class="radio-btn" name="flagAdType" value="WrongCategory"   /><label>Zła kategoria</label></li>                     
                     <!--  <li><input type="radio" class="radio-btn" name="flagAdType" value="" /><label>WrongCategory=Zła kategoria</label></li> -->
                
                </ul>
            </div>
            <label>
                <span class="label">E-mail</span>
                                
                    <input type="email" name="email" value=""  />
                
                <!--  handle error -->
            </label>
               <label>
                <span class="label">Komentarz&nbsp;<span class="optional">(Opcjonalnie)</span></span>
                <textarea name="comments"></textarea>
                <!--  handle error -->
            </label>
            <label>
                <span class="label">Wpisz numer</span>
                <div>            
                    <img class="imageAlign" name="captchaTokenImg" width="75" height="50" border="0" src="/captcha/image?token=Q0FQVENIQTozMTQ5OjE0NjcwNTkzODEyODc6NDgzMWFlZGViNjJiN2I3NjdiZjc1MjcyYWVkNDE5NDg0ZWVjMDM5MA==" alt='Włącz zdjęcia' />
                    <!--
                    <embed src="/captcha/audio?token=Q0FQVENIQTozMTQ5OjE0NjcwNTkzODEyODc6NDgzMWFlZGViNjJiN2I3NjdiZjc1MjcyYWVkNDE5NDg0ZWVjMDM5MA==" width="100%" height="60">
                        <noembed>
                              <img src="yourimage.gif" >
                           </noembed>
                    </embed>
                    -->
                    <input class="textAlign" type="text" name="captchaValue" value=""/>
                </div>
                <br class="clear" />                
            </label>        
            <label class='privacypolicy'>Wysyłając Zgłoszenie, wyrażasz zgodę na nasze <a href="http://pomoc.gumtree.pl/PL/articles/pl/KB_Article/Zasady-korzystania"> Zasady korzystania</a> z Gumtree.</label>
            <div class="button-area">
                <button class="action-button" type="submit">Zgłoś</button>
                <button class="action-button cancel" type="button" name="cancel">Anuluj</button>
            </div>
        </form>
    </div>






                            </div>
                        

                        
    <div class="map">
        <div class="wrapper">
            
                
                    <span class="google-maps-link" data-target="GoogleMaps" data-uri="http://maps.google.com/maps?q=50.0646501,19.9449799">
                        <img src="http://maps.googleapis.com/maps/api/staticmap?center=50.0646501,19.9449799&zoom=13&size=300x300&sensor=false&gme-marktplaats&markers=color:orange%7C50.0646501,19.9449799" />
                    </span>
                
            
            
                <h5 class="full-address">
                    <span class="icon-map-marker"></span>
                    <span class="address">Kraków, ul. Dobrego Pasterza, Prądnik Czerwony, Grzegórzki, Śródmieście</span>
                </h5>
            
        </div>
    </div>


                                 
                    
                </div>
            </div>

            <input type='hidden' id='adId' value='1001691377550910472310409' />  
        </div>




         <div class="vip-seller-form-details seoVip_banner">
                <div>
                     
                     
                     
                    
                        

 


             <div class="moreSearches">
                <div class="titleContainer">
                    <span>Popularne</span>
                </div>
                <ul class="resultsContainer relSearchMenu">
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/krakow/v1c9008l3200208q0p1">krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/kawalerka+krakow/v1c9008l3200208q0p1">kawalerka krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/mieszkanie+krakow/v1c9008l3200208q0p1">mieszkanie krakow</a>
                    </li>
                    
                    <li>
                        <a href="/s-mieszkania-i-domy-do-wynajecia/krak%C3%B3w/mieszkanie+do+wynajecia/v1c9008l3200208q0p1">mieszkanie do wynajecia</a>
                    </li>
                    
                </ul>
               </div> 

                           
                     
                     
                    
                    <div class="suggestedSearch">
                     
                     

 


             <div class="moreSearches">
                <div class="titleContainer">
                    <span>Proponowane</span>
                </div>
                <ul class="resultsContainer relSearchMenu">
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/rzeszow/mieszkania+do+wynajecia+rzeszow/v1c9008l3200252q0p1">mieszkania do wynajęcia rzeszów</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/pd-+-zach-powiaty/mieszkania+do+wynajecia+pruszkow/v1c9008l3200044q0p1">mieszkania do wynajęcia pruszków</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/wynajem+domow+i+mieszkan/v1c9008q0p1?priceType=free">wynajem domów i mieszkań</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/szczecin/mieszkania+do+wynajecia+szczecin/v1c9008l3200402q0p1">mieszkania do wynajęcia szczecin</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/katowice/mieszkania+do+wynajecia+katowice/v1c9008l3200285q0p1">mieszkania do wynajęcia katowice</a>
                    </li>
                    
                    <li>
                        <a href="http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/poznan/mieszkania+wynajem+poznan/v1c9008l3200366q0p1">mieszkania wynajem poznań</a>
                    </li>
                    
                </ul>
               </div> 

                      
                    </div>
                     
                     
              </div>
              
              <div>
                     
                           
    <div style="margin-top:10px;">
        <div class="rightbanner">
            <div id="div-vip-ad-banner" class="vipbanner"></div>
        </div>
    </div>
    
                     
              </div>
         </div>
         
       
          
             <div class="seo_similar results list-view">
                 <div class="section-divider">Podobne ogłoszenia, które mogą Cię zainteresować.</div>
                 <div class="view">
                     <ul>
                        
                               
        <li class="result pictures" data-adid="1001672654610910672916909" data-criteoadid="167265461">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NjAwWDgwMA==/z/0foAAOSwOVpXWATG/$_19.JPG?set_id=8800005007" alt="4 pokojowy apartament | Taras | Prądnik Czerwony  z Krakow, zobacz zdjęcie" class="thumbM"/>
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/4-pokojowy-apartament-taras-pr%C4%85dnik-czerwony/1001672654610910672916909">4 pokojowy apartament | Taras | Prądnik Czerwony </a>
                            
                        </div>

                        
                            <div class="description hidden" >LuxHome Group – mieszkania do wynajęciaLuxHome Group poleca nowy 4 pokojowy apartament z widokowym 160 m2 tarasem przy ulicy Dobrego Pasterza – Prądnik Czerwony.* Prądnik Czerwony * Dobrego Pasterza * Opolska * Lublańska * Rondo Barei * Młyńska * Centrum biurowe Vinci * O3 Business Campus * Capgemini * Krokus * Obi * Norauto * Park Wodny * Multikino *Oferowane mieszkanie o powierzchni 87 m2 usytuo ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">6 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167265461">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001688592140910468995109" data-criteoadid="168859214">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDk2WDgwMA==/z/hWgAAOSw-4BXbUg~/$_19.JPG?set_id=8800005007" alt="[Eng] Apartament 3 sypialnie | Taras 163 m2 | ul. Dobrego Pasterza | **Apartamenty Kaskada** z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/eng-apartament-3-sypialnie-taras-163-m2-ul-dobrego-pasterza-apartamenty-kaskada/1001688592140910468995109">[Eng] Apartament 3 sypialnie | Taras 163 m2 | ul. Dobrego Pasterza | **Apartamenty Kaskada**</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia nowoczesne, nigdy niezamieszkane mieszkanie w prestiżowej inwestycji Apartamenty Kaskada przy ul. Dobrego Pasterza na Prądniku Czerwonym.ENGLISH VERSION BELOW!LOKALIZACJA:W sercu biznesowego centrum Krakowa znajduje się prestiżowa inwestycja realizowana przez Super Krak - Apartamenty Kaskada. Kompleks usytuowany jest w północnej części Krakowa - Prądnik Czerwony, ul. Dobrego Pasterza. ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">6 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168859214">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001662633620910739320809" data-criteoadid="166263362">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDIzWDY0MA==/z/QXoAAOSwagdXSvkO/$_19.JPG?set_id=8800005007" alt="Mieszkanie Kraków Prądnik Czerwony 51m2 (nr: 157789) z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krak%C3%B3w-pr%C4%85dnik-czerwony-51m2-nr-157789/1001662633620910739320809">Mieszkanie Kraków Prądnik Czerwony 51m2 (nr: 157789)</a>
                            
                        </div>

                        
                            <div class="description hidden" >Nowe 2-pokojowe, atrakcyjna cena, dobrze wyposażone!Do wynajęcia 2-pokojowe mieszkanie o powierzchni 50 m2 przy ul. Dobrego Pasterza (Prądnik Czerwony)Mieszkanie składa się z przestronnego pokoju, komfortowej sypialni, dużej osobnej i jasnej kuchni, łazienki oraz przedpokoju. Z salonu wyjście balkon. W pokojach na podłodze nowe wysokiej jakości panele, w kuchni, przedpokoju i łazience terakota. W  ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166263362">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001677583710910470344609" data-criteoadid="167758371">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/MTIwMFgxNjAw/z/koAAAOSwvg9XXs1Z/$_19.JPG?set_id=8800005007" alt="4 POKOJE, UL. DOBREGO PASTERZA, PRĄDNIK CZERWONY z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/4-pokoje-ul-dobrego-pasterza-pr%C4%85dnik-czerwony/1001677583710910470344609">4 POKOJE, UL. DOBREGO PASTERZA, PRĄDNIK CZERWONY</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia od zaraz nowe dwupokojowe mieszkanie, ul. Dobrego Pasterza - dzielnica Prądnik Czerwony. Doskonała propozycja zarówno dla osoby pracującej, pary jak i rodziny z dziećmi. Zaledwie 3 km od Rynku Głównego, 900m od Opolskiej Estakady. W pobliżu Centrum Biurowe Quattro Business Park - Grupy Buma. MIESZKANIEZnajduje się na 9 piętrze w 10 piętrowym nowym bloku mieszkalnym. Składa się z: czte ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">6 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167758371">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001670658780910947199909" data-criteoadid="167065878">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDgwWDY0MA==/z/KvsAAOSwMNxXVZIu/$_19.JPG?set_id=8800005007" alt="2 niezależne pokoje, umeblowane, wolne od 1 lipca - Prądnik Czerwony! z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-niezale%C5%BCne-pokoje-umeblowane-wolne-od-1-lipca-+-pr%C4%85dnik-czerwony/1001670658780910947199909">2 niezależne pokoje, umeblowane, wolne od 1 lipca - Prądnik Czerwony!</a>
                            
                        </div>

                        
                            <div class="description hidden" >Victoria Estate prezentuje dwupokojowe mieszkanie zlokalizowane na ul. Dobrego Pasterza wolne od 1 lipca!Nieruchomość:Mieszkanie znajduje się przy ul. Dobrego Pasterza, na pierwszym piętrze w trzypiętrowym bloku. Składa się z dwóch niezależnych pokoi, kuchni, łazienki, korytarza. Częściowo umeblowane: kuchnia- meble, lodówka, kuchenka gazowa, okap, stół, krzesła; 1 pokój - łóżko, półki; 2 pokój -  ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 000 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167065878">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001690810720910969921409" data-criteoadid="169081072">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NjgwWDEwMjQ=/z/goEAAOSwbYZXcQTt/$_19.JPG?set_id=2?set_id=6172554881" alt="2 pokojowe, Prądnik Czerwony, ul. Dobrego Pasterza z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-pokojowe-pr%C4%85dnik-czerwony-ul-dobrego-pasterza/1001690810720910969921409">2 pokojowe, Prądnik Czerwony, ul. Dobrego Pasterza</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia OD 15 SIEPRNIA 2 pokojowe mieszkanie o powierzchni 60 m2, ul. Dobrego PasterzaLOKALIZACJA:Mieszkanie znajduje się w bardzo dogodnej lokalizacji umożliwiającej szybki dojazd do centrum o każdej porze dnia i nocy. Budynek znajduje się przy ul. Dobrego Pasterza.Budynek znajduje się w bezpośrednim sąsiedztwie Ronda Stanisława Barei. Dojazd do centrum miasta (Galerii Krakowskej)zajmuje 10- ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="169081072">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001690057610910515735309" data-criteoadid="169005761">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDgwWDY0MA==/z/rFcAAOSwepJXcAPC/$_19.JPG?set_id=8800005007" alt="2 pokojowe mieszkanie w nowym budynku (2014) na Prądniku Czerwonym z miejscem postojowym z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 11</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-pokojowe-mieszkanie-w-nowym-budynku-2014-na-pr%C4%85dniku-czerwonym-z-miejscem-postojowym/1001690057610910515735309">2 pokojowe mieszkanie w nowym budynku (2014) na Prądniku Czerwonym z miejscem postojowym</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia od 01.07.2016 2 pokojowe MIESZKANIE o powierzchni 35m2 w NOWYM budynku (2014) z MIEJSCEM POSTOJOWYM w podziemnym garażu w dzielnicy Prądnik Czerwony w Krakowie. Budynek znajduje się na ul. Łepkowskiego (blisko al. 29 Listopada oraz ul. Dobrego Pasterza). Prądnik Czerwony to Dzielnica Krakowa oddalona od centrum miasta o około 3 km. Dojazd autobusem miejskim do Rynku zajmuje około 10 m ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="169005761">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001679155190910510768709" data-criteoadid="167915519">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDUwWDYwMA==/z/ggoAAOSwepJXYPam/$_19.JPG?set_id=8800005007" alt="2 POK. 34 M2 BLISKO AL. 29 LISTOPADA, DOBREGO PASTERZA z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2-pok-34-m2-blisko-al-29-listopada-dobrego-pasterza/1001679155190910510768709">2 POK. 34 M2 BLISKO AL. 29 LISTOPADA, DOBREGO PASTERZA</a>
                            
                        </div>

                        
                            <div class="description hidden" >PRZYTULNE 2-POKOJOWE MIESZKANKO Z DUŻYM BALKONEM. KAMERALNE ZAMKNIĘTE OSIEDLE NA PRĄDNIKU CZERWONYM.LOKALIZACJA:- Prądnik Czerwony, ul. Rezedowa- blisko do al. 29 Listopada oraz ul. Dobrego Pasterza- bezproblemowy dostęp do komunikacji miejskiej- ok. 15 minut zajmuje dojazd do centrum miasta- w pobliżu cała infrastruktura handlowo-usługowa- niedaleko Park Wodny, Multikino, hipermarket Real, C.H. K ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 200 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167915519">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001685312830910469913709" data-criteoadid="168531283">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDY4WDc2MA==/z/1WsAAOSw3YNXaUMz/$_19.JPG?set_id=8800005007" alt="Prądnik Czerwony, Dobrego Pasterza, blisko Quattro 2 sypialnie + salon / Nice flat near Quattro BP z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/pr%C4%85dnik-czerwony-dobrego-pasterza-blisko-quattro-2-sypialnie-%2B-salon-nice-flat-near-quattro-bp/1001685312830910469913709">Prądnik Czerwony, Dobrego Pasterza, blisko Quattro 2 sypialnie &#43; salon / Nice flat near Quattro BP</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia od zaraz 3-pokojowe mieszkanie o powierzchni 55m2 znajdujące się przy ul. Bohomolca / Dobrego Pasterza w Krakowie.LOKALIZACJAPrądnik Czerwony - tu warto zamieszkać!Lokalizacja inwestycji doskonale łączy w sobie trzy ważne aspekty życia codziennego - dobrze rozwiniętą komunikację, bezpieczeństwo i komfort wypoczynku oraz szeroki dostęp do infrastruktury handlowo-usługowej. Te niezaprze ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168531283">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001691379600910955766109" data-criteoadid="169137960">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NTMzWDgwMA==/z/5s4AAOSwFwpXcYpr/$_19.JPG?set_id=8800005007" alt="3-pok 52 m2, Prądnik Czerwony, ul. Słoneckiego z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 4</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/3+pok-52-m2-pr%C4%85dnik-czerwony-ul-s%C5%82oneckiego/1001691379600910955766109">3-pok 52 m2, Prądnik Czerwony, ul. Słoneckiego</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia mieszkanie 3 pokojowe o powierzchni 52m2 na ulicy Słoneckiego.Mieszkanie znajduje się na wysokim parterze w 13-pietrowym bloku. Składa się z 3 osobnych pokoi, oddzielnej kuchni, przedpokoju, łazienki, osobne WC, balkonu i piwnicy. Mieszkanie umeblowane i wyposażone w niezbędny sprzęt. Ogrzewanie i ciepła woda miejskie rozliczane według liczników.Bardzo dobra lokalizacja praktycznie na ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="169137960">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001681894710910730614209" data-criteoadid="168189471">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/ODAwWDUzNQ==/z/pVEAAOSwvg9XZGCn/$_19.JPG?set_id=8800005007" alt="Mieszkanie dwupokojowe Dobrego Pasterza - super lokalizacja z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 11</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-dwupokojowe-dobrego-pasterza-+-super-lokalizacja/1001681894710910730614209">Mieszkanie dwupokojowe Dobrego Pasterza - super lokalizacja</a>
                            
                        </div>

                        
                            <div class="description hidden" >WitamOferuję do wynajęcia mieszkanie dwupokojowe w dzielnicy Prądnik Czerwony - ulica Dobrego Pasterza.Super lokalizacja: przystanek 1 min z mieszkania - linia 105, 139, 184, 439, 169 (autobusem do rynku 10 min, pieszo 40 pod kościół Mariacki) W pobliżu:sklepy - 2x Biedronka, Tesco, Lidl, Auchan, Obipoczta; kościół; plac Imbramowski krakowskie uczelnie: UE, PK, UR (linia 105), AGH (linia 139, 439, ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168189471">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001675555740910910876109" data-criteoadid="167555574">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDIzWDY0MA==/z/DtgAAOSwGIRXaqK3/$_19.JPG?set_id=8800005007" alt="LOFT HOUSE Dobrego Pasterza Prądnik Czerwony z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 8</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/loft-house-dobrego-pasterza-pr%C4%85dnik-czerwony/1001675555740910910876109">LOFT HOUSE Dobrego Pasterza Prądnik Czerwony</a>
                            
                        </div>

                        
                            <div class="description hidden" >LOFT HOUSE Nieruchomości prezentuje do wynajęcia mieszkanie w bardzo dobrym standardzie o powierzchni 33 m2 z 1 niezależnym pokojem i osobną, jasną kuchnią.LOKALIZACJA:Mieszkanie zlokalizowane jest w spokojnej, dobrze skomunikowanej okolicy przy ulicy Dobrego Pasterza w dzielnicy Prądnik Czerwony. Doskonałe połączenie z krakowskimi uczelniami, centrum miasta.BUDYNEK:Mieszkanie położone jest na 10  ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167555574">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001672506590910468471909" data-criteoadid="167250659">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/ODAwWDYwMA==/z/iOwAAOSw9eVXV-lr/$_19.JPG?set_id=8800005007" alt="Okazja! Mieszkanie w podwyższonym standardzie z miejscem postojowym/4pok/86m2/Dobrego Pasterza z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 12</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/okazja-mieszkanie-w-podwy%C5%BCszonym-standardzie-z-miejscem-postojowym-4pok-86m2-dobrego-pasterza/1001672506590910468471909">Okazja! Mieszkanie w podwyższonym standardzie z miejscem postojowym/4pok/86m2/Dobrego Pasterza</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia mieszkanie z miejscem postojowym w cenie w super lokalizacji Prądnik Czerwony okolice Dobrego Pasterza.Oferujemy do wynajęcia 4 pokojowe mieszkanie o powierzchni 86m2 w pełni umeblowane i wyposażone.Mieszkanie znajduje się na 1 piętrze 3 piętrowego bloku z 2006r.Nieruchomość składa się z 3 niezależnych sypialni, salonu połączonego z aneksem kuchennym, 2 łazienek z wc, przedpokoju.Z ka ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 300 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="167250659">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001691348800910493764009" data-criteoadid="169134880">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NjAwWDQ1MA==/z/MBoAAOSwepJXcYAl/$_19.JPG?set_id=8800005007" alt="3-pok 86 m2, 2000 rok, Mistrzejowice, os. Oświecenia z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 7</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/3+pok-86-m2-2000-rok-mistrzejowice-os-o%C5%9Bwiecenia/1001691348800910493764009">3-pok 86 m2, 2000 rok, Mistrzejowice, os. Oświecenia</a>
                            
                        </div>

                        
                            <div class="description hidden" >Do wynajęcia od połowy grudnia przestronne, trzypokojowe mieszkanie o powierzchni 86 m2, położone na 6 piętrze w nowym, 8-piętrowym bloku z windą.  Lokalizacja:  Mieszkanie położone w atrakcyjnej okolicy na osiedlu Oświecenia (w pobliżu ulicy Dobrego Pasterza). Osiedle charakteryzuje się dobrze rozwiniętą lokalną infrastrukturą, w pobliżu wiele sklepów (m. in. Real, Biedronka), Park Wodny, Multiki ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 900 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="169134880">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001681761850910972314309" data-criteoadid="168176185">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NjE1WDQ1OQ==/z/iBUAAOSwnNBXZB5c/$_19.JPG?set_id=8800005007" alt="Nowe 3 pok; Dobrego Pasterza - Śródmieście/Prądnik Czerwony - do negocjacji z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 9</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/nowe-3-pok-dobrego-pasterza-+-%C5%9Br%C3%B3dmie%C5%9Bcie-pr%C4%85dnik-czerwony-+-do-negocjacji/1001681761850910972314309">Nowe 3 pok; Dobrego Pasterza - Śródmieście/Prądnik Czerwony - do negocjacji</a>
                            
                        </div>

                        
                            <div class="description hidden" >Prosperity Nieruchomości prezentuje nowoczesne 3-pokojowe mieszkanie w niedalekiej odległości od centrum - Śródmieście/Prądnik CzerwonyNIERUCHOMOŚĆ:Mieszkanie umiejscowione jest na pierwszym piętrze w prestiżowej i nowoczesnej inwestycji w niedalekiej odległości od centrum Krakowa przy ul. Bohomolca. Składa się z przestronnego salonu z otwartą kuchnią, dwóch sypialni, łazienki, przedpokoju i balko ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168176185">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001667981460910471914009" data-criteoadid="166798146">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/ODAwWDUzMw==/z/uNIAAOSwepJXUXln/$_19.JPG?set_id=8800005007" alt="dwa nieprzechodnie pokoje PRĄDNIK CZERWONY, balkon, osobno wc, obok Ronda Barei z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 8</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/dwa-nieprzechodnie-pokoje-pr%C4%85dnik-czerwony-balkon-osobno-wc-obok-ronda-barei/1001667981460910471914009">dwa nieprzechodnie pokoje PRĄDNIK CZERWONY, balkon, osobno wc, obok Ronda Barei</a>
                            
                        </div>

                        
                            <div class="description hidden" >
oferta bezpośrednio od właściciela -
bez kosztów prowizji dla pośredników oplaty: 1500 zl za miesiąc,
dodatkowo czynsz: woda, ogrzewanie miejskie !! ( tj. 300 zł.) &#43; prąd
i gaz wg zużycia 



przy ulicy Dobrego Pasterza (kolo Ronda
Barei), 45 m, 4 pietro w wieżowcu z windą, 2 samodzielne pokoje,
kuchnia, łazienka z wanną, osobne wc z umywalką, duży balkon,
piwnica, domofon, mieszkanie  ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166798146">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001604353360910734417109" data-criteoadid="160435336">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NTMzWDgwMA==/z/bXwAAOSwJQdW-ixs/$_19.JPG?set_id=8800005007" alt="2-pokojowe Prądnik Czerwony dla spokojnej pary 1400 zł + prąd i woda z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/2+pokojowe-pr%C4%85dnik-czerwony-dla-spokojnej-pary-1400-z%C5%82-%2B-pr%C4%85d-i-woda/1001604353360910734417109">2-pokojowe Prądnik Czerwony dla spokojnej pary 1400 zł &#43; prąd i woda</a>
                            
                        </div>

                        
                            <div class="description hidden" >Wynajmę mieszkanie: dwa pokoje z aneksem kuchennym i łazienką na Prądniku Czerwonym. Dla spokojnej niepalącej pary. Mieszkanie jest na parterze w domu wolnostojącym w całości przeznaczonym na najem - właściciel mieszka osobno. Mieszkanie po remoncie (wymiana paneli, malowanie, wymiana drzwi, wymiana mebli kuchennych, zlewu, okapu, oświetlenia). Wyposażone: pralka, lodówka i kuchenka, w kuchni komp ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 400 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="160435336">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001666600960910468702809" data-criteoadid="166660096">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/MzM0WDUwMA==/z/UVEAAOSwMNxXT~Pm/$_19.JPG?set_id=8800005007" alt="INDEPRO poleca - mieszkanie, Dobrego Pasterza, 127m2, 3 pokoje z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 8</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/indepro-poleca-+-mieszkanie-dobrego-pasterza-127m2-3-pokoje/1001666600960910468702809">INDEPRO poleca - mieszkanie, Dobrego Pasterza, 127m2, 3 pokoje</a>
                            
                        </div>

                        
                            <div class="description hidden" >Trzypokojowe, dwupoziomowe mieszkanie o powierzchni całkowitej 
127 m2 (użytkowej 80m2) położone przy ul. Dobrego Pasterza (Prądnik 
Czerwony).

Mieszkanie znajduje się na pierwszym piętrze w jednopiętrowym  
dwurodzinnym domku szeregowym, ocieplonym i odnowionym (1999 r., cegła) 
 na kameralnym osiedlu w sąsiedztwie niskiej zabudowy. Teren domu  
monitorowany. 

Mieszkanie w dobrym stani ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="166660096">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001681577000910940061109" data-criteoadid="168157700">
            
                
                    <div class="result-link  ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/NDY5WDc2MQ==/z/EksAAOSwMNxXY-p8/$_19.JPG?set_id=8800005007" alt="Nowa kawalerka z miejscem postojowym, Dobrego Pasterza, Prądnik Czerwony, Quattro Business Park z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/nowa-kawalerka-z-miejscem-postojowym-dobrego-pasterza-pr%C4%85dnik-czerwony-quattro-business-park/1001681577000910940061109">Nowa kawalerka z miejscem postojowym, Dobrego Pasterza, Prądnik Czerwony, Quattro Business Park</a>
                            
                        </div>

                        
                            <div class="description hidden" >o wynajęcia kawalerka o powierzchni 33 m2 znajdująca się w 10-piętrowym boku przy ulicy Dobrego Pasterza.LOKALIZACJA: Mieszkanie znajduje się w budynku z 2015 r., w dzielnicy Prądnik Czerwony.Zlokalizowane jest w bliskiej okolicy Parku Wodnego, Multikina, Centrum Handlowego Krokus, OBI, Quattro Business Park . Mieszkanie zostało zakupione od dewelopera i jest dostępne od 15.06.2016r w pełni umeblo ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">1 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168157700">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                               
        <li class="result pictures" data-adid="1001680847200910552984909" data-criteoadid="168084720">
            
                
                    <div class="result-link highlight ">
                
            
            


                  <div class="thumb shrtHght">
                        
                            <div id="img-cnt">
                            
                                 <img src="http://inc.t9.classistatic.com/1.1.288/images//loading.gif" data-src="http://img.classistatic.com/crop/75x50/i.ebayimg.com/00/s/Mzk4WDYwMA==/z/fvMAAOSw-4BXYuhF/$_19.JPG?set_id=8800005007" alt="Mieszkanie 55m2 3 pokoje Dobrego Pasterza/Bohomolca  z Krakow, zobacz zdjęcie"  class="thumbM"/>
                                
                             
                            
                            <div id="pht-cnt">Zdjęć: 10</div>
                            </div>
                        
                    </div>


                    <div class="container" data-telopt="" data-cannedkeys="">

                        <div class="title">
                                                    
                            <a class="href-link" href="/a-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-55m2-3-pokoje-dobrego-pasterza-bohomolca/1001680847200910552984909">Mieszkanie 55m2 3 pokoje Dobrego Pasterza/Bohomolca </a>
                            
                        </div>

                        
                            <div class="description hidden" >For English please call.Ładne i przestronne mieszkanie, 3 pokoje 55 m2, Prądnik Czerwony Prezentowana nieruchomość to bardzo ładnie urządzone mieszkanie o powierzchni 55 m2,
usytuowane na pierwszym piętrze w sześciopiętrowym bloku. Do dyspozycji w
mieszkaniu mamy hol, kuchnię wraz z salonem, 2 pokoje, łazienkę z WC.
Ogrzewanie i ciepła woda są miejskie. Nieruchomość jest nowa, jest urządzona, w ...</div>
                        
                        <div class=attributes-ctnr>
                            
                                
                            
                        </div>
                        
                        
                        <div class="info">
                            <div class="price">
                                


    

    

        





    
    
        <span class="value">
    
        
            <span class="amount">2 500 zł</span>
            
            
            
        </span>



                            </div>

                            
                        </div>  
                        
                         <div class="category-location">
                         
                               
                                 <span class="locationName city">Krakow</span>
                                
                               
                           
                       </div>
                         
                        
                        <div class="meta-info"></div>
                        
                             

                            <div class="reply-action">
                                <div class="addAdTofav " data-synchurl = "http://www.gumtree.pl/rui-api/synchwatchlist/model/synch/pl_PL" data-adid="168084720">
                                    <span class="starIcon icon-star-icon-gray-line" data-toggle-class="icon-star-icon-gray-line icon-star-icon"></span>
                                </div>

                                
                            </div>
                        </div>

                    
                </div>
            </li>

                           
                       </ul>
                 </div>
             </div>
           

         
          <div class="vip-bottomBlock" >
              
               
    <div id="vip_bottombanner" style="margin:0 auto;width:320px"></div>

               <div class="vip-sponsoredads">
                        
        <div id="adcontainer1" class="googleAdContainer"></div>
    
               </div>
        </div>

        <input type='hidden' name='criteoadId' value='169137755' /> 
        <input type="hidden" name="NcatId" value="9008"/>
        <input type="hidden" name="NlocId" value="3200208" />
        <input type="hidden" name="NlocName" value="Krakow" />
        
    

    
    
    <div class="vip-gallery-preview" style='display:none'>
        <div class="gallerycontent">
            
                <div id="banner-container">
                    <div id="banner-preview-header" data-gtaid='7162/Gumtree_PL' data-catcanoname="Nieruchomości/mieszkania i domy do wynajęcia"></div>
                </div>
            
            <img id="preview-image" src="" alt="">
            <div id="vip-gallery-details">
                <div id="prd-title"></div>
                <div id="pict-count"></div>
            </div>
        </div>
        
        <a class="left" href="javascript:void(0)"><span class="icon-vip-popup-arrow-left"></span></a>
        <a class="right" href="javascript:void(0)"><span class="icon-vip-popup-arrow-right"></span></a>
        <div id="icon-close"></div>
    </div>
    



                        <div class="clear"></div>
                    </div>
                </section>
            </div>

           
             
            <div class="footer">
                <footer>
                    
<div class="footer-links clearfix">
    <div class="logo">
        <a href="http://www.gumtree.pl/">
               <img border="0"  src="http://inc.t9.classistatic.com/1.1.288/images/pl_PL/logo.png" alt="Home"/>
        </a>
    </div>

    <div>
        <h3>Poznaj nas</h3>
        <ul>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/B-anf'>O Gumtree</span></li>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NMnfnql_Thzgerr'>Zasady zamieszczania</span></li>
            <li><a href="http://blog.gumtree.pl/">Gumtree Blog</a></li> 
        </ul>
    </div>

    <div>
        <h3>Zobacz więcej</h3>
        <ul>
            
             <li><a href="/t-wyszukiwarka-gory/mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208">Najpopularniejsze wyszukiwania</a></li>
             <li><a href="http://www.gumtree.pl/pages/zawartosc/">Tematy Gumtree</a></li>
             <li><a href="http://www.gumtree.pl/pages/lokalizacje/">Lokalizacje</a></li>
             <li><a href="http://www.gumtree.pl/pages/ceny-nieruchomosci">Ceny Nieruchomości</a></li>
   
        </ul>
    </div>
    
    <div class="rightColumn">
        <h3>Sprawy prawne</h3>
        <ul>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Mnfnql-xbemlfgnavn'>Zasady korzystania</span></li>
            <li><span class='sudo-link' data-o-uri="/cevinpl-cbyvpl" data-target="_self">Polityka Prywatności</span></li>
            <li><span class='sudo-link' data-o-uri='uggc://cbzbp.thzgerr.cy/CY/negvpyrf/cy/XO_Negvpyr/Pbbxvrf'>Informacje o Cookies</span></li>
        </ul>
    </div>
    
    <div class="rightColumn">
        <h3>Pomoc i porady</h3>
        <ul>
            <li><a href="http://pomoc.gumtree.pl/PL">Pomoc</a></li>
            <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NFnsrglCY'>Pozostań bezpiecznym</span></li>
            <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;ph=1&amp;sf=PbagnpgHfd=&amp;f='>Napisz do nas</span></li>
             <li><span class="sudo-link" data-o-uri='uggc://cbzbp.thzgerr.cy/CY?ynat=cy&amp;y=cy&amp;p=CXO%3NOnfvpfCY'>Promowanie ogłoszeń</span></li>
        </ul>
    </div>
</div>

<div class="social-links">



    <!--  social media -->
    <div class="social-media">
        <ul class="social-media-ul buttons">
            <li class="button"><a href="https://www.facebook.com/GumtreePolska" target="_blank"><span class="icon-seo-facebook sm-icons"></span></a></li>
            <li class="button"><a href="https://plus.google.com/103950977256553454134/posts" target="_blank"><span class="icon-seo-gmailplus sm-icons"></span></a></li>
            <li class="button"><a href="https://twitter.com/gumtreepolska" target="_blank"><span class="icon-seo-twitter sm-icons"></span></a></li>
            <li class="button"><a href="http://pinterest.com/gumtreepolska" target="_blank"><span class="icon-seo-pinterest sm-icons"></span></a></li>
            <li class="button"><a href="http://www.youtube.com/user/GumtreePolska" target="_blank"><span class="icon-seo-youtube sm-icons"></span></a></li>
        </ul>
    </div>
</div>
<div class="cpyrt">Copyright © 2014-2016 eBay.  Wszelkie Prawa zastrzeżone.</div>

                </footer>
            </div>
            
        </div>
        
    </div>
</div>



    
        




     


    


    
        
            <script type="text/javascript" src='http://inc.t9.classistatic.com/1.1.288/js/Main_pl_PL.min.js'></script>
        
    
        
            <script type="text/javascript" src='http://inc.t9.classistatic.com/1.1.288/js/SeoViewPage_pl_PL.min.js'></script>
        
    
    

    



    <script>

     var bP = {
             
             accId : ("/7162/Gumtree_PL/Nieruchomości/mieszkania i domy do wynajęcia").split(' ').join('_').replace(/\,|&_|'/g,""),
             
             dc_ref:window.location.href,
             kw: $('input[name=q]').val() || "no category",
             ptype: 'vip_r',
             loc: $('input[name=NlocName]').val(),
     };
     
     
    
         
        
              BOLT.displayBanner( $.extend({slotDim: [300, 250], slotId : 'div-vip-ad-banner',price :'950', currency : 'PLN'},bP));
         
         

    
     

        
 


    </script>
    
    
        <script src="http://www.google.com/adsense/search/async-ads.js" type="text/javascript"></script>
        <script type="text/javascript" charset="utf-8">
            var x = {"desktopNumAdsTop":"0","desktopNumAdsBottom":"3","mobileNumAdsTop":"0","mobileNumAdsBottom":"3","numRepeated":"0","mobilePubId":"mobile-gumtree-pl","desktopPubId":"gumtree-pl-vip","longerHeadlines":false,"mobileSiteLinks":false,"desktopSiteLinks":true,"channel":"PL_VIP_r","query":"Kawalerka, 30 m2, Śródmieście, ul. Dobrego Pasterza  Kraków","hl":"pl","adtest":"off","adPage":"0","colorTitleLink":"#333","rolloverAdBackgroundColor":"#FFFFF0","mobileClickableBackground":false};
            
            var defaultBlock = {
                 'lines':'3',
                 'longerHeadlines': x.longerHeadlines,
                 'fontSizeTitle': '14',
                 'fontSizeDescription' : '14',
                 'lineHeightDescription' : 21,
                 'fontSizeDomainLink' : '14',
                 'lineHeightDomainLink' : 21,
                 'fontFamily' : 'tahoma',
                 'noTitleUnderline': true,
                 'colorTitleLink': x.colorTitleLink,
                 'colorDomainLink' : '#333333',
                 'colorText' : '#333333',
                 'colorAdSeparator':'#ffffff',
                  'colorAdBorder' : '#EEEEEE',
                  'adBorderSelections' : 'bottom',
                 'width' : '100%'
            };
            var defaultBlock_ext = {
                //defaultvalue
                'adIconUrl':'http://afs.googleusercontent.com/gumtree-pl/no-photo-pl.jpg',
                'adIconSpacingAbove' : 5,
                'adIconSpacingBefore' : 6,
                'adIconSpacingAfter' : 10,
                'adIconLocation' : 'ad-left'
            }
            
            var pageOptions = {
                'query': x.query,
                'hl': x.h1,
                'adtest' : x.adtest,
                'channel' : x.channel,
                'adPage' : x.adPage,
                'linkTarget' : '_blank',
                'numRepeated': x.numRepeated,
                'titleBold' : true,
                //new call back method through all the market
                'adLoadedCallback':function(containerName, adsLoaded) {
                    if (adsLoaded) {
                        if(containerName == 'adcontainer0'){
                            var exP0, newP;
                            newP = document.createElement("div");
                            newP.className='section-divider';
                            newP.innerHTML = 'Linki sponsorowane';
                            exP0 = document.getElementById('adcontainer0');
                            exP0.parentNode.insertBefore(newP,exP0);
                            $('.content #adcontainer0').css({'background-color':'#ffffff'});
                        };
                            
                        if(containerName == 'adcontainer1'){
                            var exP1, newP1;
                            newP1 = document.createElement("div");
                            newP1.className='section-divider';
                            newP1.innerHTML = 'Linki sponsorowane';
                            exP1 = document.getElementById('adcontainer1');
                            exP1.parentNode.insertBefore(newP1,exP1);
                            $('.content #adcontainer1').css("background-color", "#ffffff");
                        }
                    }
                }
                
            };
            
            function init(numAdsTop, numAdsBottom, siteLinks, pubId, clickableBackground, rolloverAdBackgroundColor, adIconW, adIconH){
                pageOptions.siteLinks = siteLinks;
                pageOptions.pubId = pubId;
                pageOptions.rolloverAdBackgroundColor = rolloverAdBackgroundColor;
                
                var targetArr = [];
                if(numAdsTop>0){
                    var adblock1 = {
                        'container': 'adcontainer0',
                        'maxTop': numAdsTop,
                        'clickableBackgrounds': clickableBackground,
                        'adIconWidth' : adIconW,
                        'adIconHeight' : adIconH
                    };
                    jQuery.extend(adblock1,defaultBlock);
                    if(adIconW)
                    {
                        jQuery.extend(adblock1,defaultBlock_ext);
                        
                    }
                    targetArr.push(adblock1);
                }
    
                if(numAdsBottom>0){
                    var adblock2 = {
                        'container': 'adcontainer1',
                        'number': numAdsBottom,
                        'clickableBackgrounds': clickableBackground,
                        'adIconWidth' : adIconW,
                        'adIconHeight' : adIconH
                    };
                    jQuery.extend(adblock2,defaultBlock);
                    if(adIconW)
                    {
                        jQuery.extend(adblock2,defaultBlock_ext);
                        
                    }
                    targetArr.push(adblock2);
                }
                new _googCsa('ads',pageOptions, targetArr);
            }
            
            
        
            if (matchMedia("tablet")){
                init(x.desktopNumAdsTop, x.desktopNumAdsBottom, x.desktopSiteLinks, x.desktopPubId, true, '#FFFFF0', 100, 67);
            } else {
                init(x.desktopNumAdsTop, x.desktopNumAdsBottom, x.desktopSiteLinks, x.desktopPubId, true, '#FFFFF0', 120, 80);
            }
        
    
        </script>
    
    



    



    
   













        <!--[if (lte IE 9)&!(IEMobile)]>
        <script src="http://inc.t9.classistatic.com/1.1.288/js//common/polyfills/placeholder.js"></script>
        <![endif]-->
    




    

    

    

    
</body>
</html>

"""