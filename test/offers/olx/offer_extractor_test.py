# -*- coding: utf-8 -*-

'''
Created on 24-01-2015

@author: mateusz
'''
import unittest
from src.offersource.olx.offer_extractor import OfferExtractor

class OfferExtractorTest(unittest.TestCase):

    def test_extract_price(self):
        ACTUAL_PRICE = u"1 400 zł"
        price = OfferExtractor.extract(OFFER_HTML)["price"]
        self.assertEquals(ACTUAL_PRICE, price)

    def test_extract_date(self):
        ACTUAL_DATE = u"14 Stycznia 2015"
        date = OfferExtractor.extract(OFFER_HTML)["date"]
        self.assertEquals(ACTUAL_DATE, date)
        
    def test_extract_title(self):
        ACTUAL_TITLE = u"OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol"
        title = OfferExtractor.extract(OFFER_HTML)["title"]
        self.assertEquals(ACTUAL_TITLE, title)
        
    def test_extract_address(self):
        ACTUAL_ADDRESS = u"Kraków, Podgórze"
        address = OfferExtractor.extract(OFFER_HTML)["address_section"]
        self.assertEquals(ACTUAL_ADDRESS, address)
        
    def test_extract_description(self):
        ACTUAL_DESCRIPTION = u"""Do wynajęcia od zaraz 2-pokojowe w pełni wyposażone mieszkanie o powierzchni 51 m2.

LOKALIZACJA: Budynek położony jest przy ulicy Chmieleniec, w zacisznej części Ruczaju. Wokoło dużo zieleni, sąsiedztwo lasu. Młody kompleks budynków w nowoczesnej zabudowie. W pobliżu przystanek autobusowy i tramwajowy (11, 18, 23, 52, 194, 609) - komfortowy dojazd co centrum bez przesiadek, regularne kursy również w godzinach nocnych. Osiedle posiada wiele sklepów oraz punktów usługowych w tym dentysta, zakład opieki zdrowotnej, restauracje, fryzjer, salon kosmetyczny, kwiaciarnia, przedszkole, Pasaż 33 - sklepy Lewiatan, Rossmann oraz inne niezbędne na co dzień. Kilka kroków od budynku znajduje się także plac zabaw. Bezpośredni dojazd co centrum komunikacją miejską - 20 minut.

Film o okolicy: 

https://www.youtube.com/embed/LtnRfloZ3zQ

BUDYNEK: Niski, 3-piętrowy blok z 2006 wyposażony parking podziemny i parking naziemny. Parking naziemny dostępny bez dodatkowych opłat wyłącznie dla mieszkańców budynku. W budynku znajduje się także dostępna dla mieszkańców wózkownia, do mieszkania przynależy piwnica.

MIESZKANIE: 2-pokojowe mieszkanie o powierzchni 51 m2 położone jest na 4 piętrze i składa się z dużego salonu, otwartej na salon kuchni, sypialni, garderoby, holu i łazienki. Mieszkanie posiada  balkon o powierzchni 6 m2. Aneks kuchenny wyposażony w meble w zabudowie kuchennej, chłodziarko-zamrażalkę, piekarnik, płytę grzewczą elektryczną, zlewozmywak, okap oraz mikrofalówkę. W salonie znajduje się komplet wypocznykowy, komoda, stół jadalny z 4 krzesłąmi oraz drewniany stolik. W sypialni znajduje się duże podwójne łóżko oraz szafa garderobiana. Łazienka wyposażona w wannę, pralkę, WC, grzejnik drabinkowy oraz umywalkę. 
W cenie najmu dodatkowo miejsce postojowe w garażu podziemnym.

WIRTUALNA WIZYTA:"""
        description = OfferExtractor.extract(OFFER_HTML)["description"]
        self.assertEquals(ACTUAL_DESCRIPTION, description)
        
    def test_extract_summary(self):
        ACTUAL_SUMMARY = u"""Do wynajęcia od zaraz 2-pokojowe w pełni wyposażone mieszkanie o powierzchni 51 m2.

LOKALIZACJA: Budynek położony jest przy ulicy Chmieleniec, w zacisznej części Ruczaju. Wokoło dużo zieleni, sąsie..."""
        summary = OfferExtractor.extract(OFFER_HTML)["summary"]
        self.assertEquals(ACTUAL_SUMMARY, summary)

    def test_extract_image_url(self):
        ACTUAL_URL = u"http://img20.olx.pl/images_tablicapl/214959355_1_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg"
        url = OfferExtractor.extract(OFFER_HTML)["image_url"]
        self.assertEquals(ACTUAL_URL, url)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    

OFFER_HTML = u"""
    <!DOCTYPE html>
<html xmlns:og="http://ogp.me/ns#" xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków Podgórze • OLX.pl (dawniej Tablica.pl)</title>
                        <meta name="robots" content="index, follow" />        <link rel="canonical" href="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" />        <link rel="alternate" media="handheld" href="http://olx.pl/m/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" />
<link rel="alternate" media="only screen and (max-width: 640px)" href="http://olx.pl/i2/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" />        <meta http-equiv="Content-Language" content="pl" />
        <meta name="description" content="1 400 zł: Do wynajęcia od zaraz 2-pokojowe w pełni wyposażone mieszkanie o powierzchni 51 m2.

LOKALIZACJA: Budynek położony jest przy ulicy Chmieleniec, w zacisznej części Ruczaju. Wokoło dużo zieleni, sąsie..." />
                            <meta property="og:title" content="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol"/>
                    <meta property="og:description" content="1 400 zł: Do wynajęcia od zaraz 2-pokojowe w pełni wyposażone mieszkanie o powierzchni 51 m2.

LOKALIZACJA: Budynek położony jest przy ulicy Chmieleniec, w zacisznej części Ruczaju. Wokoło dużo zieleni, sąsie..."/>
                    <meta property="og:type" content="other"/>
                    <meta property="og:url" content="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html"/>
                    <meta property="og:site_name" content="OLX.pl (dawniej Tablica.pl)"/>
                    <meta property="fb:app_id" content="121167521293285"/>
                    <meta property="og:image" content="http://img20.olx.pl/images_tablicapl/214959355_1_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg"/>
                            <link rel="icon" type="image/x-icon" href="http://s2.olx.pl/static/olxpl/external/olxpl/img/favicon.ico?v=3">
                                            <script type="text/javascript">
                var _adblock = true;
            </script>
            <script type="text/javascript" src="http://s2.olx.pl/static/olxpl/external/base/js/advertising.js"></script>
                                                                                        <link rel="stylesheet" type="text/css" href="http://s1.olx.pl/static/olxpl/packed/sw737207f83cf86243fcc9d41775ff06d0.css">
                                                                                                            <link rel="stylesheet" type="text/css" href="http://s2.olx.pl/static/olxpl/packed/sw300f31d6e96e223ef465bfb3e425a6a5.css">
                                                                                                        <!--[if lte IE 8]>                        <link rel="stylesheet" type="text/css" href="http://s2.olx.pl/static/olxpl/packed/swa6b5e165ba558334a65995311c9502a6.css">
                    <![endif]-->                                            <script type="text/javascript">
            window.suggestmeyes_loaded = true;
                            var action='ad';
                            var method='index';
                            var user_logged=0;
                            var www_base='http://olx.pl';
                            var www_base_no_namespace='http://olx.pl';
                            var www_base_ajax='http://olx.pl/ajax';
                            var static_files_www_base='http://s1.olx.pl/static/olxpl/';
                            var external_static_files_www_base='http://s2.olx.pl/static/olxpl/external/olxpl/';
                            var session_domain='olx.pl';
                            var decimal_separator=',';
                            var thousands_separator=' ';
                            var sitecode='olxpl';
                            var defaultCurrency='PLN';
                            var config_currency='zł';
                            var useExternalScripts=1;
                            var lang='pl';
                            var module_adding_refactor=1;
                            var module_answers_filters_fraud=1;
                            var module_at_addingform_track=1;
                            var module_automotive_supiscious_parameters=1;
                            var module_category_change_with_pay_to_post_ad=1;
                            var module_comperiabox=1;
                            var module_connection_port=1;
                            var module_controlpanel2=1;
                            var module_dogs=1;
                            var module_einvoice_olxpl=1;
                            var module_facebook_login=1;
                            var module_fraud_contact_data=1;
                            var module_fraud_detection=1;
                            var module_fraud_detector_queue=1;
                            var module_gg_integration=1;
                            var module_googleplus=1;
                            var module_hashtags=1;
                            var module_i2_payment=1;
                            var module_invoiceform=1;
                            var module_kredyt_hipoteczny=1;
                            var module_mms_images=1;
                            var module_mobile_app=1;
                            var module_multiacc=1;
                            var module_new_einvoice=1;
                            var module_otokredyt=1;
                            var module_paid_for_post=1;
                            var module_paid_limits=1;
                            var module_paidads=1;
                            var module_payupl_bank_accounts=1;
                            var module_payupl_response=1;
                            var module_pdlaenau=1;
                            var module_refactorized_stats=1;
                            var module_sms_notification=1;
                            var module_trusted_changes=1;
                            var module_zendesk_schedule=1;
                            var mapkey='AIzaSyCZwXJXvszIPYtHv_WtLIgWekvYaSp5Nzs';
                            var fb_connect_url='http://connect.facebook.net/pl_PL/all.js#xfbml=1&amp;appId=121167521293285';
                            var fb_app_id='121167521293285';
                            var region_id='4';
                            var subregion_id='102';
                            var city_id='8959';
                            var cat_path='nieruchomosci/mieszkania/wynajem';
                            var saveFavLink="http://olx.pl/konto/?origin=observepopup&ref%5B0%5D%5Bdocument%5D=okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html&ref%5B0%5D%5Baction%5D=ad&ref%5B0%5D%5Bmethod%5D=index";
                            var marker_default='http://s1.olx.pl/static/olxpl/external/olxpl/img/maps/marker_default.png';
                            var marker_zone='http://s1.olx.pl/static/olxpl/external/base/img/maps/marker_zone.png';
                            var adID='125968309';
                            var equal_address_provided='0';
                            var messageSent='';
                            var map_show_detailed='1';
                            var regionName="Ma\u0142opolskie";
                            var subregionName="Krak\u00f3w";
                            var category_id='15';
                            var categoryName="Wynajem";
                            var categoryCode="wynajem";
                            var categoryAdsenseText=null;
                            var root_category_id='3';
                            var rootCategoryName="Nieruchomo\u015bci";
                            var rootCategoryCode="nieruchomosci";
                            var rootCategoryAdsenseText=null;
                            var setSeoPageName="Og\u0142oszenia ";
                            var gemius_identifier=new String('nGiaeIyDmyR6bLq7yxiMT8RqnIR_WjA9.HzcpV.kcBb.H7');
                        function __(txt) {
                if (typeof translations == 'object') {
                    if (translations[txt] == undefined) {
                        return txt;
                    } else {
                        return translations[txt];
                    }
                }
                return txt;
            }
        </script>
        <!--[if lt IE 9]>
            <script type="text/javascript" src="http://s2.olx.pl/static/olxpl/js/scripts/html5shiv.min.js"></script>
        <![endif]-->
        <link href="https://plus.google.com/113406265199615974663" rel="publisher" />
            <!-- Criteo cookie -->
        <script type="text/javascript">
        function crtg_getCookie(c_name){ var i,x,y,ARRCookies=document.cookie.split(";");for(i=0;i<ARRCookies.length;i++){x=ARRCookies[i].substr(0,ARRCookies[i].indexOf("="));y=ARRCookies[i].substr(ARRCookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);} }return'';} var crtg_content = crtg_getCookie('crtg_rta');    (function(){var crtg_nid = '2859';var crtg_cookiename = 'crtg_rta';var crtg_varname = 'crtg_content';var crtg_url=location.protocol+'//rtax.criteo.com/delivery/rta/rta.js?netId='+escape(crtg_nid)+'&cookieName='+escape(crtg_cookiename)+'&rnd='+Math.floor(Math.random()*99999999999)+'&varName=' + escape(crtg_varname);var crtg_script=document.createElement('script');crtg_script.type='text/javascript';crtg_script.src=crtg_url;crtg_script.async=true;if(document.getElementsByTagName("head").length>0)document.getElementsByTagName("head")[0].appendChild(crtg_script);else if(document.getElementsByTagName("body").length>0)document.getElementsByTagName("body")[0].appendChild(crtg_script);})();
        var AdoVars = [];
                        AdoVars['master'] = {
                id: 'V9Or1trQqOllnolYqJpfoQbtsMnQeoLkd8WQ0s3oDN3.M7',
                server: 'gg.adocean.pl',
                keys: ['region:malopolskie','city:krakow' ,'cat:nieruchomosci' ,'cat:mieszkania' ,'cat:wynajem']
                                , vars: '&price=1400'
                                };
                                </script>
        
        </head>
    <body class="detailpage">
        <script>
    dataLayer = [];
</script>

<!-- Google Tag Manager -->
    <noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5Q8C6P"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-5Q8C6P');</script>
<!-- End Google Tag Manager -->                <div id="innerLayout">
    <header id="header-container">
    <div class="navi">
        <div class="wrapper clr rel">
                        <a href="http://olx.pl" id="headerLogo" class="abs icon website big" title="Ogłoszenia - Sprzedam, kupię na OLX.pl (dawniej Tablica.pl)">Ogłoszenia - Sprzedam, kupię na OLX.pl (dawniej Tablica.pl)</a>
                                                <span class="icon prevpagelanding"></span>
                                                                    <a id="postNewAdLink" class="postnewlink fbold tdnone" href="http://olx.pl/nowe-ogloszenie/">
                    <span>Dodaj ogłoszenie</span>
                </a>
                                                <script type="text/javascript">
    observedNC = [];
    observedNC['ads'] = [];
    observedNC['searches'] = [];
    observedNC['toSynchronize'] = '';
</script>
<ul class="userbox fright marginleft10">
    <li class="hidden inlblk nowrap rel vtop" id="observed-counter">
        <a href="http://olx.pl/obserwowane/" class="tdnone inlblk hidden" id="observed-ads-link" title="Obserwowane">
            <span class="icon inlblk favin vtop"></span>
            <strong class="counter"></strong>
        </a>
        <a href="http://olx.pl/obserwowane/wyszukiwania/" class="tdnone inlblk hasObservedAds?'hidden':''}" id="observed-search-link" title="Obserwowane">
            <span class="icon inlblk favin vtop"></span>
            <strong class="counter"></strong>
        </a>
    </li>
    <li class="inlblk nowrap vtop noslash" id="my-account-link">
        <div class="inlblk rel">
            <a href="http://olx.pl/mojolx/"
                class="tdnone" id="topLoginLink">
                <span class="icon inlblk accountshape vtop"></span>
                <span class="link inlblk"><strong>Mój OLX</strong></span>
                    </a>
                        </div>
    </li>
</ul>
        </div>
    </div>
    </header>    <section id="body-container">
    <div class="wrapper">
        <div class="content" id="offer_active">
            
<div class="rel breadcrumbbox">
    <table width="100%" cellpadding="0" cellspacing="0" class="breadcrumb small" id="breadcrumbTop">
        <tr>
            <td width="20" class="nowrap hidden left" valign="middle">
                <a href="http://olx.pl/oferty/prev/" class="inlblk hidden nowrap prev-link mini tdnone small small back arrowsup" rel="nofollow">
                    <span class="inlblk link"><span>&laquo;  Wróć</span></span>
                </a>
            </td>
            <td valign="top" class="middle">
                <ul>
                    <li class="inline nowrap">
                        <a class="link" href="http://olx.pl/krakow/"><span>Ogłoszenia Kraków</span></a>
                    </li>
                                        <li class="inline">
                        <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/krakow/" class="link nowrap"><span>Nieruchomości Kraków</span></a>
                    </li>
                                        <li class="inline">
                        <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/mieszkania/krakow/" class="link nowrap"><span>Mieszkania Kraków</span></a>
                    </li>
                                        <li class="inline">
                        <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/" class="link nowrap"><span>Wynajem Kraków</span></a>
                    </li>
                                    </ul>
            </td>
            <td width="20" class="nowrap hidden right" valign="middle">
                <a href="http://olx.pl/oferty/next/" class="inlblk hidden nowrap next-link mini tdnone small next arrowsup" rel="nofollow">
                    <span class="inlblk link"><span>Następne ogłoszenie &raquo;</span></span>
                                        <span class="cloud br5 hidden">
                        <img class="hidden">
                        <span class="title-label"></span>
                        <span class="link overh hn"><span></span></span>
                    </span>
                                    </a>
            </td>
        </tr>
    </table>
</div>


            


            

            <div class="clr offerbody">
                <div class="offercontent fleft rel ">
                    <div class="offercontentinner">
                        
<div class="clr offerheadinner pding15 pdingright20">
    <h1 class="brkword lheight28">
        
        OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol    </h1>
    <p class="x-large clr margintop10">
        <span class="fleft block clr pdingright10">
            <span class="icon markerloc vmiddle inlblk"></span>
            <span class="show-map-link link gray cpointer">
            <strong class="c2b small">
                Kraków, Podgórze            </strong>
        </span>
        </span>
            <small class="small c62 lheight22">
                <span class="pdingleft10 brlefte5">
                                            Dodane                                        o 16:23, 14 Stycznia 2015, <span class="nowrap">ID ogłoszenia: <span class="rel inlblk">125968309                    </span></span>
                </span>
            </small>
        </p>
        </div>

                                                                        <div class="offerdescription clr" id="offerdescription">
                            
<div class="clr">
        <div class="rel zi2 marginbott10 gallery firstimage">
                    <a href="#" class="{id:125968309} observe-link abs zi3 block tdnone tcenter cfff layerlink br5 offerobserve" data-statkey="ad.observed.bigstar">
            <span class="inlblk icon observe4 observed-125968309">&nbsp;</span> <span class="observed-txt block pdingtop10 normal">Obserwuj</span>
        </a>
                <div class="gallery_img tcenter img-item">
            <div class="photo-glow">
                <div class="photo-handler rel inlblk">
                                        <img src="http://img20.olx.pl/images_tablicapl/214959355_1_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg" class="vtop bigImage {nr:1}"
                        alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 1">
                    <a id="enlargephoto" class="layerlink br5 abs tcenter tdnone hidden" href="#">
                        <span class="icon enlargephoto inlblk">&nbsp;</span> <span class="block xx-large cfff margintop10">Galeria</span>
                    </a>
                                    </div>
            </div>
        </div>
    </div>
    </div>

                            <div class="clr descriptioncontent marginbott20">
                                
<table class="details fixed marginbott20 margintop5" width="609" cellpadding="0" cellspacing="0">
        <tr class="brbottdashc8">
                    <td class="" width="203">
            <div class="pding5_10">
                Oferta od:
                <strong class="block">
                                                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bprivate_business%5D=business" title="Biura nieruchomości - Kraków">
                                        Biura nieruchomości                                        </a>
                                                    </strong>
            </div>
        </td>
                            <td class="" width="203">
            <div class="pding5_10">
                Poziom:
                <strong class="block">
                                                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_4" title="4 - Kraków">
                                        4                                        </a>
                                                    </strong>
            </div>
        </td>
                            <td class="" width="203">
            <div class="pding5_10">
                Umeblowane:
                <strong class="block">
                                                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bfilter_enum_furniture%5D%5B0%5D=yes" title="Tak - Kraków">
                                        Tak                                        </a>
                                                    </strong>
            </div>
        </td>
                </tr>
    <tr>
        <td class="space" height="0" colspan="3"></td>
    </tr>
        <tr class="brbottdashc8">
                    <td class="" width="203">
            <div class="pding5_10">
                Liczba pokoi:
                <strong class="block">
                                                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bfilter_enum_rooms%5D%5B0%5D=two" title="2 pokoje - Kraków">
                                        2 pokoje                                        </a>
                                                    </strong>
            </div>
        </td>
                            <td class="" width="203">
            <div class="pding5_10">
                Powierzchnia:
                <strong class="block">
                                                        51 m<sup>2</sup>                                                    </strong>
            </div>
        </td>
                            <td class="" width="203">
            <div class="pding5_10">
                Rodzaj zabudowy:
                <strong class="block">
                                                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bfilter_enum_builttype%5D%5B0%5D=blok" title="Blok - Kraków">
                                        Blok                                        </a>
                                                    </strong>
            </div>
        </td>
                </tr>
    <tr>
        <td class="space" height="0" colspan="3"></td>
    </tr>
    </table>


                                <div class="clr" id="textContent">
                                    <p class="pding10 lheight20 large">
                                        Do wynajęcia od zaraz 2-pokojowe w pełni wyposażone mieszkanie o powierzchni 51 m2.<br />
<br />
LOKALIZACJA: Budynek położony jest przy ulicy Chmieleniec, w zacisznej części Ruczaju. Wokoło dużo zieleni, sąsiedztwo lasu. Młody kompleks budynków w nowoczesnej zabudowie. W pobliżu przystanek autobusowy i tramwajowy (11, 18, 23, 52, 194, 609) - komfortowy dojazd co centrum bez przesiadek, regularne kursy również w godzinach nocnych. Osiedle posiada wiele sklepów oraz punktów usługowych w tym dentysta, zakład opieki zdrowotnej, restauracje, fryzjer, salon kosmetyczny, kwiaciarnia, przedszkole, Pasaż 33 - sklepy Lewiatan, Rossmann oraz inne niezbędne na co dzień. Kilka kroków od budynku znajduje się także plac zabaw. Bezpośredni dojazd co centrum komunikacją miejską - 20 minut.<br />
<br />
Film o okolicy: <br />
<br />
https://www.youtube.com/embed/LtnRfloZ3zQ<br />
<br />
BUDYNEK: Niski, 3-piętrowy blok z 2006 wyposażony parking podziemny i parking naziemny. Parking naziemny dostępny bez dodatkowych opłat wyłącznie dla mieszkańców budynku. W budynku znajduje się także dostępna dla mieszkańców wózkownia, do mieszkania przynależy piwnica.<br />
<br />
MIESZKANIE: 2-pokojowe mieszkanie o powierzchni 51 m2 położone jest na 4 piętrze i składa się z dużego salonu, otwartej na salon kuchni, sypialni, garderoby, holu i łazienki. Mieszkanie posiada  balkon o powierzchni 6 m2. Aneks kuchenny wyposażony w meble w zabudowie kuchennej, chłodziarko-zamrażalkę, piekarnik, płytę grzewczą elektryczną, zlewozmywak, okap oraz mikrofalówkę. W salonie znajduje się komplet wypocznykowy, komoda, stół jadalny z 4 krzesłąmi oraz drewniany stolik. W sypialni znajduje się duże podwójne łóżko oraz szafa garderobiana. Łazienka wyposażona w wannę, pralkę, WC, grzejnik drabinkowy oraz umywalkę. <br />
W cenie najmu dodatkowo miejsce postojowe w garażu podziemnym.<br />
<br />
WIRTUALNA WIZYTA:                                    </p>
                                </div>
                                

                            </div>
                            


                            

                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img21.olx.pl/images_tablicapl/214959355_2_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-dodaj-zdjecia.jpg" class="vtop bigImage {nr:2}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 2">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img20.olx.pl/images_tablicapl/214959355_3_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-wynajem.jpg" class="vtop bigImage {nr:3}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 3">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img19.olx.pl/images_tablicapl/214959355_4_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-nieruchomosci.jpg" class="vtop bigImage {nr:4}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 4">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img19.olx.pl/images_tablicapl/214959355_5_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-malopolskie.jpg" class="vtop bigImage {nr:5}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 5">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img20.olx.pl/images_tablicapl/214959355_6_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vtop bigImage {nr:6}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 6">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img20.olx.pl/images_tablicapl/214959355_7_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vtop bigImage {nr:7}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 7">
                                </div>
                            </div>
                                                            <div class="tcenter img-item">
                                <div class="photo-glow">
                                    <img src="http://img21.olx.pl/images_tablicapl/214959355_8_644x461_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vtop bigImage {nr:8}" alt="OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol Kraków - image 8">
                                </div>
                            </div>
                                                        
<div id="offerbottombar" class="pding15">
    <div class="clr pdingbott10 small">
            <a href="http://olx.pl/oferty/next/" id="next-link" class="next-link fright tdnone hidden">
            <span class="link inlblk"><span>Następne ogłoszenie</span></span><span class="icon inlblk vtop nextsmall marginleft10 margintop1 fright">&nbsp;</span>
        </a>
        <a href="http://olx.pl/oferty/prev/" id="prev-link" class="prev-link fleft tdnone hidden">
            <span class="icon inlblk vtop prevsmall marginright10 margintop1">&nbsp;</span><span class="link inlblk"><span>Wróć</span></span>
        </a>
        </div>
    <div class="clr pdingtop10 brtop-1 rel zi5">
        
<div class="fleft ad-share marginright15">
            <div class="fleft marginright10">
<div id="fb-root" class="{id:  125968309} "></div>
    <div class="fleft fb_detailpage" id="fb_offerLikeButton">
        <iframe src="//www.facebook.com/plugins/like.php?locale=pl_PL&amp;href=http%3A%2F%2Folx.pl%2Foferta%2Fokazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html&amp;width=195&amp;layout=button_count&amp;action=like&amp;show_faces=false&amp;share=true&amp;height=21" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:195px; height:21px;" allowTransparency="true"></iframe>
    </div>
</div>
                
<a href="#sendmailContent" title="Wyślij przez e-mail" id="sendmail" class="fleft button sec mini4 br3 marginleft10 marginright10 small ffarial sendinemail">
    <span class="icon inlblk mini inbox vtop">&nbsp;</span><span class="inlblk">Wyślij</span>
</a>
<div id="sendmailContent" class="hidden">
    <div class="pding20 tcenter large fbold" id="sendmailSuccess" style="display: none">
        <div></div>
    </div>
    <form class="default sendmail margintop15" action="#">
        <fieldset>
            <div class="fblock clr">
                <div class="fleft label tright">
                    <label class="fbold c000">Twoje imię<span class="cc914">*</span></label>
                </div>
                <div class="area clr">
                    <div class="fleft rel focusbox">
                        <input type="text" class="text light br4 x-normal long" value="" name="name"> <span class="status icon vmiddle inlblk dnone">&nbsp;</span>
                    </div>
                </div>
            </div>
            <div class="fblock clr">
                <div class="fleft label tright">
                    <label class="fbold c000">Twój e-mail<span class="cc914">*</span></label>
                </div>
                <div class="area clr">
                    <div class="fleft rel focusbox">
                        <input type="text" class="text light br4 x-normal long" value="" name="email"> <span class="status icon vmiddle inlblk dnone">&nbsp;</span>
                    </div>
                </div>
            </div>
            <div class="fblock clr">
                <div class="fleft label tright">
                    <label class="fbold c000">Adres e-mail znajomego<span class="cc914">*</span></label>
                </div>
                <div class="area clr">
                    <div class="fleft rel focusbox">
                        <input type="text" class="text light br4 x-normal long" value="" name="friendsEmail"> <span class="status icon vmiddle inlblk dnone">&nbsp;</span>
                    </div>
                </div>
            </div>
            <div class="fblock clr margintop5">
                <div class="area clr">
                    <p class="tcenter">
                        <span class="button big br3 vtop"><input type="submit" class="cfff" value="Wyślij" id="submit-contact"></span>
                        <a class="button big br3 c000 rel gray vtop" id="sendmailClose">
                            <span class="inlblk">Anuluj</span>
                        </a>
                    </p>
                    <div class="margintop20 clr">
                        <span class="icon info2 marginright10 fleft margintop-2">&nbsp;</span>
                        <div class="overh small lheight14 color-6">Po kliknięciu Wyślij Twój znajomy otrzyma link do tego ogłoszenia</div>
                    </div>
                </div>
            </div>
        </fieldset>
        <input type="hidden" name="adID" value="125968309" />
    </form>
</div>

            </div>


    </div>
    <div class="pdingtop10">
                    Wyświetleń:<strong>84</strong>
            </div>
</div>

                        </div>
                    </div>
                    


                                                                
                                                                
<div class="offercontentinner margintop7">
    <form enctype="multipart/form-data" class="default quickcontact" id="contact-form" method="post" action="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html">
        <fieldset>
            <h3 class="x-large fbold">Skontaktuj się z ogłoszeniodawcą</h3>
            <div class="inner rel">
                <div class="fblock clr">
                    <ul id="contact_methods_below" class="form">
                                                <li class="link-phone clr rel margintop10 {'path':'phone', 'id':'8vy6W', 'id_raw': '125968309'} atClickTracking contact-a cpointer" data-rel="phone">
                            <div class="fleft">
                                <span class="icon vtop inlblk mobile2">&nbsp;</span>
                            </div>
                            <div class="overh fleft marginleft10 brkword contactitem">
                                                                <strong class="fnormal xx-large">57x xxx xxx</strong>
                                <span class="link spoiler small nowrap">
                                    <span>Pokaż</span>
                                </span>
                                                            </div>
                        </li>
                                                                                            </ul>
                </div>
                                                <div class="fblock clr marginbott15">
                    <div class="focusbox fleft rel smallshadow">
                        <input type="text" title="Twój e-mail..." value="" class="defval light br3 xx-long x-normal" id="ask-email" name="contact[email]">
                        <p class="desc errorboxContainer">
                            <small class="ca6 lheight24" id="se_emailError"></small>
                        </p>
                    </div>
                </div>
                                <div class="fblock clr">
                    <div class="focusbox fleft rel smallshadow">
                        <textarea title="Treść wiadomości..." id="ask-text"
                            class="defval light lheight18 br3 x-normal"
                            name="contact[txt]"></textarea>
                        <p class="desc errorboxContainer">
                            <small class="ca6 lheight24" id="se_messageError"></small>
                        </p>
                    </div>
                </div>
                
                <div class="fblock clr pding10">
                    <div class="clr">
                        <div class="fleft">
                            <span class="tdnone lheight28 cpointer" id="upload-a" title="Dodaj załącznik"><span class="icon vmiddle inlblk attch">&nbsp;</span> <span class="link"><span>Dodaj załącznik</span></span></span>
                            <p class="x-small color-1 lheight14 attachmentinfo marginleft14">
                                Dopuszczalne typy plików: jpg, jpeg, png, doc, pdf, gif, zip, rar, tar, html, swf, txt, xls, docx, xlsx                                <span class="block">Maksymalny rozmiar pliku to 2 MB</span>
                            </p>
                        </div>
                        <span class="button br3 fright send3"><span class="icon inlblk vtop b_send3">&nbsp;</span><input type="submit" value="Wyślij" class="cfff"></span>
                    </div>
                                    </div>
                <div id="upload-div" style="display: none" class="fblock clr">
                <div class="fblock" id="safariWarning" style="display: none;">
                    Wygląda na to że korzystasz z przeglądarki "Mobile Safari", która nie wspiera wysyłania plików. Dodanie zdjęć nie będzie możliwe. Przykro nam.                </div>
                                                                <p class="clr marginbott5">
                    <input type="file" id="attachment0" name="attachment[0]" size="39" class="attachment fleft"> 
                    <input type="button" class="removeAtachment fright" value="usuń"> 
                    <input type="hidden" name="attachment[0]" value="file">
                </p>
                                <p class="clr marginbott5">
                    <input type="file" id="attachment1" name="attachment[1]" size="39" class="attachment fleft"> 
                    <input type="button" class="removeAtachment fright" value="usuń"> 
                    <input type="hidden" name="attachment[1]" value="file">
                </p>
                                <p class="clr marginbott5">
                    <input type="file" id="attachment2" name="attachment[2]" size="39" class="attachment fleft"> 
                    <input type="button" class="removeAtachment fright" value="usuń"> 
                    <input type="hidden" name="attachment[2]" value="file">
                </p>
                                <p class="clr marginbott5">
                    <input type="file" id="attachment3" name="attachment[3]" size="39" class="attachment fleft"> 
                    <input type="button" class="removeAtachment fright" value="usuń"> 
                    <input type="hidden" name="attachment[3]" value="file">
                </p>
                                <p class="clr marginbott5">
                    <input type="file" id="attachment4" name="attachment[4]" size="39" class="attachment fleft"> 
                    <input type="button" class="removeAtachment fright" value="usuń"> 
                    <input type="hidden" name="attachment[4]" value="file">
                </p>
                                </div>
                                <input type="hidden" id="token" name="contact[token]" value="c1232c00Ul5nvXpoQ4hoA3XyYZYj+7IOHzkc35LOBqY09ILDocM=" /> <input type="hidden" id="token2" name="contact[debug]" value="7" />
                        <span class="icon scissors abs hidden">&nbsp;</span>
                            <a href="http://olx.pl/bezpieczenstwo/" target="_blank" id="securitylabel" class="icon securitylabel abs zi3">Zasady bezpiecznej transakcji</a>
                        </div>
        </fieldset>
    </form>
</div>

                                                            <div class="offercontentinner margintop7">
                        <div class="similarads" id="similarads">
                                    <a href="http://olx.pl/oferty/uzytkownik/1ywAj/" class="fright link alluserads"><span>Wszystkie ogłoszenia tego użytkownika</span></a>
                            <h2 class="normal lheight16 pding7 bgfff">
            Ogłoszenia użytkownika Krzysztof        </h2>
        <div>
                <table width="100%" cellpadding="0" cellspacing="0" class="marginbott10 fixed">
                        <tr>
                <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" summary="Ogłoszenie" class="fixed breakword">
                    <tbody>
                        <tr>
                            <td width="85" class="tcenter" height="85">
                                <p>wczoraj<br/>14:39</p>
                            </td>
                            <td width="120">
                                <span class="rel inlblk detailcloudbox clr">
                                    <a title="Okazja! 3 pokojowe mieszkanie 75m2, Ruczaj, Taras 40 m2, Garaż" href="http://olx.pl/oferta/okazja-3-pokojowe-mieszkanie-75m2-ruczaj-taras-40-m2-garaz-CID3-ID8DNpR.html" class="thumb vtop inlblk rel tdnone scale4">
                                        <img alt="Okazja! 3 pokojowe mieszkanie 75m2, Ruczaj, Taras 40 m2, Garaż" src="http://img32.olx.pl/images_tablicapl/218074205_1_261x203_okazja-3-pokojowe-mieszkanie-75m2-ruczaj-taras-40-m2-garaz-krakow.jpg" class="fleft">
                                    </a>
                                </span>
                            </td>
                                                                                    <td>
                                <h3 class="large lheight20 clr">
                                    <a class="link" title="Okazja! 3 pokojowe mieszkanie 75m2, Ruczaj, Taras 40 m2, Garaż Kraków" href="http://olx.pl/oferta/okazja-3-pokojowe-mieszkanie-75m2-ruczaj-taras-40-m2-garaz-CID3-ID8DNpR.html">
                                        <span>Okazja! 3 pokojowe mieszkanie 75m2, Ruczaj, Taras 40 m2, Garaż</span>
                                    </a>
                                    
                                </h3>
                                <p class="clr">
                                    <small class="breadcrumb small">
                                    Wynajem                                    </small>
                                </p>
                                    </td>
                                    <td width="170" class="wwnormal tright">
                                                                    <div class="space">
                                            <p class="price large marginright15">
                                                <strong class="c000 ">1 800 zł</strong>
                                            </p>
                                                                                                                      </div>
                                                                </td>
                                </tr>
                            </tbody>
                        </table>
                                    </td>
                </tr>
                        <tr>
                <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" summary="Ogłoszenie" class="fixed breakword">
                    <tbody>
                        <tr>
                            <td width="85" class="tcenter" height="85">
                                <p>20  sty</p>
                            </td>
                            <td width="120">
                                <span class="rel inlblk detailcloudbox clr">
                                    <a title="OKAZJA! 3 pokojowe mieszkanie 64 m2. Wys. standard, Dębniki, Kapelanka" href="http://olx.pl/oferta/okazja-3-pokojowe-mieszkanie-64-m2-wys-standard-debniki-kapelanka-CID3-ID8Bp4f.html" class="thumb vtop inlblk rel tdnone scale4">
                                        <img alt="OKAZJA! 3 pokojowe mieszkanie 64 m2. Wys. standard, Dębniki, Kapelanka" src="http://img19.olx.pl/images_tablicapl/217026485_1_261x203_okazja-3-pokojowe-mieszkanie-64-m2-wys-standard-debniki-kapelanka-krakow.jpg" class="fleft">
                                    </a>
                                </span>
                            </td>
                                                                                    <td>
                                <h3 class="large lheight20 clr">
                                    <a class="link" title="OKAZJA! 3 pokojowe mieszkanie 64 m2. Wys. standard, Dębniki, Kapelanka Kraków" href="http://olx.pl/oferta/okazja-3-pokojowe-mieszkanie-64-m2-wys-standard-debniki-kapelanka-CID3-ID8Bp4f.html">
                                        <span>OKAZJA! 3 pokojowe mieszkanie 64 m2. Wys. standard, Dębniki, Kapelanka</span>
                                    </a>
                                    
                                </h3>
                                <p class="clr">
                                    <small class="breadcrumb small">
                                    Wynajem                                    </small>
                                </p>
                                    </td>
                                    <td width="170" class="wwnormal tright">
                                                                    <div class="space">
                                            <p class="price large marginright15">
                                                <strong class="c000 ">2 200 zł</strong>
                                            </p>
                                                                                                                      </div>
                                                                </td>
                                </tr>
                            </tbody>
                        </table>
                                    </td>
                </tr>
                        <tr>
                <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" summary="Ogłoszenie" class="fixed breakword">
                    <tbody>
                        <tr>
                            <td width="85" class="tcenter" height="85">
                                <p>20  sty</p>
                            </td>
                            <td width="120">
                                <span class="rel inlblk detailcloudbox clr">
                                    <a title="Okazja! Mieszkanie o pow 40 m2. Konstelacja, Dębniki, Miłkowskiego" href="http://olx.pl/oferta/okazja-mieszkanie-o-pow-40-m2-konstelacja-debniki-milkowskiego-CID3-ID8B78z.html" class="thumb vtop inlblk rel tdnone scale4">
                                        <img alt="Okazja! Mieszkanie o pow 40 m2. Konstelacja, Dębniki, Miłkowskiego" src="http://img22.olx.pl/images_tablicapl/216898939_1_261x203_okazja-mieszkanie-o-pow-40-m2-konstelacja-debniki-milkowskiego-krakow.jpg" class="fleft">
                                    </a>
                                </span>
                            </td>
                                                                                    <td>
                                <h3 class="large lheight20 clr">
                                    <a class="link" title="Okazja! Mieszkanie o pow 40 m2. Konstelacja, Dębniki, Miłkowskiego Kraków" href="http://olx.pl/oferta/okazja-mieszkanie-o-pow-40-m2-konstelacja-debniki-milkowskiego-CID3-ID8B78z.html">
                                        <span>Okazja! Mieszkanie o pow 40 m2. Konstelacja, Dębniki, Miłkowskiego</span>
                                    </a>
                                    
                                </h3>
                                <p class="clr">
                                    <small class="breadcrumb small">
                                    Wynajem                                    </small>
                                </p>
                                    </td>
                                    <td width="170" class="wwnormal tright">
                                                                    <div class="space">
                                            <p class="price large marginright15">
                                                <strong class="c000 ">1 500 zł</strong>
                                            </p>
                                                                                                                      </div>
                                                                </td>
                                </tr>
                            </tbody>
                        </table>
                                    </td>
                </tr>
                        <tr>
                <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" summary="Ogłoszenie" class="fixed breakword">
                    <tbody>
                        <tr>
                            <td width="85" class="tcenter" height="85">
                                <p>14  sty</p>
                            </td>
                            <td width="120">
                                <span class="rel inlblk detailcloudbox clr">
                                    <a title="OKAZJA! Do wynajęcia dom o pow 170 m2. Kobierzyńska, Dębniki" href="http://olx.pl/oferta/okazja-do-wynajecia-dom-o-pow-170-m2-kobierzynska-debniki-CID3-ID8vyrb.html" class="thumb vtop inlblk rel tdnone scale4">
                                        <img alt="OKAZJA! Do wynajęcia dom o pow 170 m2. Kobierzyńska, Dębniki" src="http://img23.olx.pl/images_tablicapl/214961569_1_261x203_okazja-do-wynajecia-dom-o-pow-170-m2-kobierzynska-debniki-krakow.jpg" class="fleft">
                                    </a>
                                </span>
                            </td>
                                                                                    <td>
                                <h3 class="large lheight20 clr">
                                    <a class="link" title="OKAZJA! Do wynajęcia dom o pow 170 m2. Kobierzyńska, Dębniki Kraków" href="http://olx.pl/oferta/okazja-do-wynajecia-dom-o-pow-170-m2-kobierzynska-debniki-CID3-ID8vyrb.html">
                                        <span>OKAZJA! Do wynajęcia dom o pow 170 m2. Kobierzyńska, Dębniki</span>
                                    </a>
                                    
                                </h3>
                                <p class="clr">
                                    <small class="breadcrumb small">
                                    Wynajem                                    </small>
                                </p>
                                    </td>
                                    <td width="170" class="wwnormal tright">
                                                                    <div class="space">
                                            <p class="price large marginright15">
                                                <strong class="c000 ">4 200 zł</strong>
                                            </p>
                                                                                                                      </div>
                                                                </td>
                                </tr>
                            </tbody>
                        </table>
                                    </td>
                </tr>
                        <tr>
                <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" summary="Ogłoszenie" class="fixed breakword">
                    <tbody>
                        <tr>
                            <td width="85" class="tcenter" height="85">
                                <p>14  sty</p>
                            </td>
                            <td width="120">
                                <span class="rel inlblk detailcloudbox clr">
                                    <a title="Okazja!!! 2 pokojowe mieszkanie 42 m2. Miłkowskiego, Dębniki" href="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-42-m2-milkowskiego-debniki-CID3-ID8vydn.html" class="thumb vtop inlblk rel tdnone scale4">
                                        <img alt="Okazja!!! 2 pokojowe mieszkanie 42 m2. Miłkowskiego, Dębniki" src="http://img20.olx.pl/images_tablicapl/214960093_1_261x203_okazja-2-pokojowe-mieszkanie-42-m2-milkowskiego-debniki-krakow.jpg" class="fleft">
                                    </a>
                                </span>
                            </td>
                                                                                    <td>
                                <h3 class="large lheight20 clr">
                                    <a class="link" title="Okazja!!! 2 pokojowe mieszkanie 42 m2. Miłkowskiego, Dębniki Kraków" href="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-42-m2-milkowskiego-debniki-CID3-ID8vydn.html">
                                        <span>Okazja!!! 2 pokojowe mieszkanie 42 m2. Miłkowskiego, Dębniki</span>
                                    </a>
                                    
                                </h3>
                                <p class="clr">
                                    <small class="breadcrumb small">
                                    Wynajem                                    </small>
                                </p>
                                    </td>
                                    <td width="170" class="wwnormal tright">
                                                                    <div class="space">
                                            <p class="price large marginright15">
                                                <strong class="c000 ">1 800 zł</strong>
                                            </p>
                                                                                                                      </div>
                                                                </td>
                                </tr>
                            </tbody>
                        </table>
                                    </td>
                </tr>
                    </table>
                        <table width="100%" cellpadding="0" cellspacing="0" class="marginbott10">
            <tr>
                <td>
                    
<div id="google-ads-container1"></div>

                </td>
            </tr>
        </table>
            </div>
</div>
<div class="actionbar">
    <div class="showall x-large lheight20 tcenter">
                Pokaż pozostałe <a href="http://olx.pl/oferty/uzytkownik/1ywAj/" class="link"><strong>ogłoszenia tego użytkownika</strong></a>
            </div>
</div>
                    </div>
                                    </div>
                                <div class="offerbox fright rel zi2" id="offerbox">
                    <div class="offeractions" id="offeractions">
                        <div class="pdingbott20">
                                                        
<div class="ab_test_contact ab0">
    
<div class="pricelabel tcenter">
        <strong class="xxxx-large margintop7 block not-arranged">1 400 zł</strong>
    </div>

            <h3 class="lheight40 color-5 tcenter x-large">Skontaktuj się:</h3>
    

    
    <div class="contactbox innerbox br3 bgfff rel">
            <ul class="hidden ab6_show contact_methods full marginbott10 ">
            <li class="link-phone clr rel {'path':'phone', 'id':'8vy6W', 'id_raw': '125968309'} atClickTracking contact-a cpointer" data-rel="phone">
                <div class="fleft">
                    <span class="icon vmiddle inlblk mobile2">&nbsp;</span>
                </div>
                <div class="clr fleft marginleft15 contactitem">
                                <strong class="brkword xx-large lheight20 fnormal">57x xxx xxx</strong>
                <span class="link spoiler small nowrap">
                    <span>Pokaż</span>
                </span>
                                </div>
            </li>
        </ul>
                    <div class="tcenter">
        <a href="http://olx.pl/oferta/kontakt/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" class="ab4_hide ab5_hide full button send2 big br3 cfff large marginleft-1 rel button-email {'id_raw': '125968309'} atClickTracking" >
            <span class="icon inlblk vtop b_send4">&nbsp;</span> <span class="inlblk message rel ab3_hide">Napisz wiadomość</span> <span class="inlblk message rel hidden x-large ab3_show">Chcesz kupić?</span> <span class="shadow pding0 abs"></span>
        </a>
                
<form class="hidden ab5_show tleft default quick-contact full" enctype="multipart/form-data" method="post" id="contact-form2" action="http://olx.pl/oferta/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html">
    <h4 class="hidden">Email Seller</h4>
    <div class="fblock clr">
        <div class="focusbox smallshadow">
            <textarea class="defval light lheight18 br3 x-normal" title="Treść wiadomości..." name="contact[txt]" rows="8" id="ask-text2"></textarea>
        </div>
    </div>
        <div class="fblock clr email-field hidden">
        <div class="focusbox smallshadow">
            <input class="defval light br3" type="text" name="contact[email]" title="Twój e-mail..." value=""  id="ask-email2" />
        </div>
    </div>
            
    <div class="fblock submit clr">
        <span class="button big br3">
            <span class="icon inlblk vtop b_send4"></span>
            <input type="submit" class="cfff large" value="Wyślij">
        </span>
    </div>
</form>

            </div>
        <div class="rel">
        <ul id="contact_methods" class="brbott-12">
                            <li class="hidden ab4_show full marginbott10 button big br3 cfff large link-phone rel {'path':'phone', 'id':'8vy6W', 'id_raw': '125968309'} atClickTracking contact-a cpointer" data-rel="phone">
                    <span class="icon inlblk vtop b_phone4">&nbsp;</span>
                    <span class="inlblk message rel brkword">
                                                    <strong class="xx-large">57x xxx xxx</strong>
                            <span class="link spoiler small nowrap">
                                <span>Pokaż</span>
                            </span>
                                            </span>
                </li>
                                        <li class="clr rel hidden ab4_show">
                    <div class="fleft">
                        <span class="icon vmiddle inlblk mail2">&nbsp;</span>
                    </div>
                    <div class="clr fleft marginleft15 contactitem">
                        <a href="http://olx.pl/oferta/kontakt/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" class="xx-large lheight20 button-email {'id_raw': '125968309'} atClickTracking" >
                            Napisz wiadomość                        </a>
                    </div>
                </li>
                        
<li class="ab4_hide ab6_hide link-phone clr rel {'path':'phone', 'id':'8vy6W', 'id_raw': '125968309'} atClickTracking contact-a cpointer" data-rel="phone">
    <div class="fleft">
        <span class="icon vmiddle inlblk mobile2">&nbsp;</span>
    </div>
    <div class="clr fleft marginleft15 contactitem brkword">
        <strong class="xx-large lheight20 fnormal">57x xxx xxx</strong>
    <span class="link spoiler small nowrap">
        <span>Pokaż</span>
    </span>
        </div>
</li>

            

            

        </ul>
    </div>
</div>

<div class="locationbox innerbox br3 bgfff clr margintop7">
    <div class="clr">
        <span class="icon markerloc2 fleft margintop5 marginleft5"></span>
        <div class="address fleft marginleft15">
            <p class="block normal brkword">
                Kraków, Małopolskie                                , Podgórze                            </p>
                            <span id="showMap" class="show-map-link link lheight22 cpointer"> <span class="">Pokaż na mapie</span>
            </span>
                    </div>
    </div>
</div>


    
 
<div class="userbox clr rel zi2 margintop10">
    <span class="icon user fleft"></span>
    <p class="userdetails fleft marginleft15">
        <span class="block color-5 brkword xx-large">Krzysztof</span>
                    <span class="block color-5 normal margintop5 sinceline">Na OLX.pl od cze 2014</span>
                        <span class="block">
                        <a href="http://olx.pl/oferty/uzytkownik/1ywAj/" class="link lheight22 normal" id="linkUserAds">
                            <span>Ogłoszenia użytkownika</span>
            </a>
        </span>
        </p>
</div>

</div>

                                                        

<div class="adoptions clr margintop5">
    <span class="icon flag2 fleft"></span>
    <ul class="fleft normal lheight18 marginleft15">
        <li>
            <a href="#" class="{id:125968309} observe-link-2 link" data-statkey="ad.observed.right" rel="nofollow">
                <span>Obserwuj</span>
            </a>
        </li>
        <li>
            <a href="http://olx.pl/drukuj/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" id="printOffer" title="Drukuj" class="printOffer link" rel="nofollow" target="_blank">
                <span>Drukuj</span>
            </a>
        </li>
        <li>
                            <a rel="nofollow" href="http://olx.pl/nowe-ogloszenie/edit/125968309/?back=ad" title="Edytuj" class="link">
                    <span>Edytuj</span>
                </a>
            
        </li>
        
        <li class="">
            <span class="link report report-links cpointer" id="reportMe" title="Zgłoś naruszenie"> <span>Zgłoś naruszenie</span></span>
            <noindex>
                <div id="report-data">
                <div id="report-form" style="display: none;">
                    <div id="reportInnerHeight">
                        <form action="" method="post" class="rel default report" id="report-form-fill" autocomplete="off">
                            <fieldset class="pding0_20 margintop10 marginbott10 overh">
                                                                         <div class="fblock clr">
                                    <input type="radio" class="radio vmiddle inlblk" name="report[reason]" value="spam" id="reason-spam" autocomplete="off"> <label class="inlblk vmiddle" for="reason-spam"><strong
                                        class="inlblk ">Spam</strong></label>
                                </div>
                                                                        <div class="fblock clr">
                                    <input type="radio" class="radio vmiddle inlblk" name="report[reason]" value="badCategory" id="reason-badCategory" autocomplete="off"> <label class="inlblk vmiddle" for="reason-badCategory"><strong
                                        class="inlblk ">Niewłaściwa kategoria</strong></label>
                                </div>
                                                                        <div class="fblock clr">
                                    <input type="radio" class="radio vmiddle inlblk" name="report[reason]" value="violation" id="reason-violation" autocomplete="off"> <label class="inlblk vmiddle" for="reason-violation"><strong
                                        class="inlblk ">Inne naruszenie zasad</strong></label>
                                </div>
                                                                        <div class="fblock clr">
                                    <input type="radio" class="radio vmiddle inlblk" name="report[reason]" value="outofdate" id="reason-outofdate" autocomplete="off"> <label class="inlblk vmiddle" for="reason-outofdate"><strong
                                        class="inlblk ">Ogłoszenie nieaktualne</strong></label>
                                </div>
                                                                        <div id="report_form_description_field" class="hidden">
                                    <div class="fblock clr margin10_0">
                                            W polu poniżej opisz dlaczego ogłoszenie narusza nasze zasady:                                        </div>
                                                                        <div class="fblock clr margin10_0">
                                        <div class="fleft">
                                            <div class="focusbox">
                                                <textarea class="x-normal light required c73 br4 do-not-validate" id="report-textarea" name="report[content]" autocomplete="off" defaultval="<Podaj dodatkowe informacje, które ułatwią nam sprawdzenie Twojego zgłoszenia>"></textarea>
                                            </div>
                                            <p class="small margintop10">Pozostało znaków: <b class="report-countdown">1000</b>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </fieldset>
                            <div class="fblock brtop-1 clr pding20">
                                <span class="button br3 fright"><input type="submit" class="submit cfff {id: '8vy6W'}" value="Wyślij" id="report-submit"></span>
                            </div>
                        </form>
                        <div id="report-form-confirmation" style="display: none">
                            
<h4>Dziękujemy za zgłoszenie.</h4>
<div class="pding30_10">
    <p>Sprawdzimy czy ogłoszenie narusza nasze zasady. Ponieważ otrzymujemy wiele zgłoszeń nie możemy na nie odpowiadać. 
    Jeśli chcesz się z nami skontaktować skorzystaj z formularza dostępnego <a href="http://olx.pl/kontakt/">tutaj</a>.</p>
</div>
<div class="tcenter brtop-1 pding20_0">
    <a href="#" class="link close"><span>Zamknij</span></a>
</div>

                        </div>
                    </div>
                </div>
            </div>
            </noindex>
        </li>
    </ul>
</div>

                        </div>
                        
            <div class="margintop10">
            <div id="adoceanggppkhppdpkn"></div>
            <script type="text/javascript">
            (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggppkhppdpkn'] = {myMaster: 'V9Or1trQqOllnolYqJpfoQbtsMnQeoLkd8WQ0s3oDN3.M7'};
            </script>
        </div>
    
                    </div>
                </div>
                            </div>
                        <div id="mapcontainer"
                class="bgfff hidden br-1 vtop mapcontainer {zoom: '13', lat: '50.03979000', lon: '19.97714000', rad: '2000'}">
                <div class="googlemap" id="googlemap" style="height: 564px; width: 874px;"></div>
            </div>
                    </div>
    </div>
    
</section>



<div class="overgallery fix normal hidden" id="bigImageContent">
    <div class="layermax">
        <div class="horizontal">
            <div class="vertical">
                <div class="tleft">
                    <div class="layertitle cfff">
                        <div class="pding5 clr">
                            <a href="#" class="icon layerclose fright marginright5" id="overgalleryclose">&nbsp;</a>
                            <p class="xx-large fbold lheight26 pdingtop10">OKAZJA!!! 2 pokojowe mieszkanie 51m2. Chmieleniec, Ruczaj, Ericpol</p>
                            <p class="small">
                                <span class="fleft block clr pdingright10">
                                    <span class="icon markerloc gray vmiddle inlblk"></span>
                                    <strong class="marginleft5 lheight24">
                                        Kraków                                                                                    , Podgórze                                                                            </strong>
                                </span>
                                <span class="pdingleft10 lheight24 brlefte5">
                                                                            Dodane o                                                                        16:23, 14 Stycznia 2015, <span class="nowrap">ID ogłoszenia: 125968309</span>
                                </span>
                            </p>
                        </div>
                    </div>
                    <div class="clr">
                        
<div class="fright optionsbar">
            <div class="pricelabel tcenter">
                                            <strong class="xxxx-large margintop7 block not-arranged">1 400 zł</strong>
                                    </div>
        <h3 class="margintop10 cfff tcenter x-large">Skontaktuj się:</h3>
    <div class="optionsbarinner">
                    <div class="tcenter">
                <a href="http://olx.pl/oferta/kontakt/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" class="full button send2 big br3 cfff large marginleft-1 rel button-email {'id_raw': '125968309'} atClickTracking">
                    <span class="icon inlblk vtop b_send4">&nbsp;</span> <span class="inlblk message rel">Napisz wiadomość</span> <span class="shadow pding0 abs"></span>
                </a>
            </div>
                <div class="contactbox">
            <div class="rel">
                <ul id="contact_methodsBigImage" class="margintop20">
                                            <li class="clr rel link-phone {'path':'phone', 'id':'8vy6W', 'id_raw': '125968309'} atClickTracking contact-a cpointer" data-rel="phone">
                            <div class="fleft">
                                <span class="icon vmiddle inlblk mobile2 gray">&nbsp;</span>
                            </div>
                            <div class="clr fleft marginleft10 contactitem brkword">
                                                                <strong class="xx-large lheight20 fnormal">57x xxx xxx</strong>
                                <span class="link spoiler small nowrap">
                                    <span>Pokaż</span>
                                </span>
                                                                                            </div>
                        </li>
                                                                            </ul>
            </div>
        </div>
                        
<div class="locationbox innerbox br3 bgfff clr margintop7">
    <div class="clr">
        <span class="icon markerloc2 fleft margintop5 marginleft5"></span>
        <div class="address fleft marginleft15">
            <p class="block normal brkword">
                Kraków, Małopolskie                                , Podgórze                            </p>
                            <span id="showMapLayer" class=" link lheight22 cpointer"> <span class="">Pokaż na mapie</span>
            </span>
                    </div>
    </div>
</div>


                <div class="userbox clr">
            <span class="icon user gray fleft"></span>
            <p class="userdetails fleft marginleft10">
                <span class="block brkword xx-large">Krzysztof</span>
                <span class="block normal margintop5">
                    Na OLX.pl od cze 2014                </span>
                                    <span class="block">
                                            <a href="http://olx.pl/oferty/uzytkownik/1ywAj/" class="link lheight22 normal" id="linkUserAds">
                                                <span>Ogłoszenia użytkownika</span>
                        </a>
                    </span>
                            </p>
        </div>
    </div>
</div>

                        <div class="viewspace">
                            <div class="photospace rel" id="bigImage">
                                                                <a href="#" class="{id:125968309} observe-link abs zi3 block tdnone tcenter cfff layerlink br5 offerobserve" data-statkey="ad.observed.overgallery">
                                    <span class="inlblk icon observe4 observed-125968309">&nbsp;</span> <span class="observed-txt block pdingtop10 normal">Obserwuj</span>
                                </a>
                                                                                                <div class="lshowprev abs cpointer bigImagePrev">
                                    <a href="#" class="lprev block br5 abs">
                                        <span class="icon block">&nbsp;</span>
                                    </a>
                                </div>
                                <div class="lshownext abs cpointer bigImageNext">
                                    <a href="#" class="lnext block br5 abs">
                                        <span class="icon block">&nbsp;</span>
                                    </a>
                                </div>
                                                                <a href="#" class="lbutton abs type2 tdnone br5" id="showOnlyImage" target="_blank">
                                    <span class="block icon">&nbsp;</span> <span class="suggesttitle small top abs zi2 br3 c000 hidden">
                                        Pokaż sam obrazek                                        <span class="target abs icon">&nbsp;</span>
                                    </span>
                                </a>
                                <div class="loadinginfo icon hidden abs br5"></div>
                            </div>
                            <div class="photosbar">
                                <ul class="overh" id="bigGallery">
                                                                        <li class="fleft">
                                        <a href="http://img19.olx.pl/images_tablicapl/214959355_1_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_1_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg" class="block br5 {nr:1}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img19.olx.pl/images_tablicapl/214959355_2_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-dodaj-zdjecia.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_2_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-dodaj-zdjecia.jpg" class="block br5 {nr:2}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img19.olx.pl/images_tablicapl/214959355_3_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-wynajem.jpg" rel="http://img19.olx.pl/images_tablicapl/214959355_3_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-wynajem.jpg" class="block br5 {nr:3}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img21.olx.pl/images_tablicapl/214959355_4_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-nieruchomosci.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_4_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-nieruchomosci.jpg" class="block br5 {nr:4}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img21.olx.pl/images_tablicapl/214959355_5_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-malopolskie.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_5_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-malopolskie.jpg" class="block br5 {nr:5}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img19.olx.pl/images_tablicapl/214959355_6_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_6_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="block br5 {nr:6}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img20.olx.pl/images_tablicapl/214959355_7_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" rel="http://img20.olx.pl/images_tablicapl/214959355_7_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="block br5 {nr:7}"></a>
                                    </li>
                                                                        <li class="fleft">
                                        <a href="http://img19.olx.pl/images_tablicapl/214959355_8_1000x700_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" rel="http://img21.olx.pl/images_tablicapl/214959355_8_94x72_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="block br5 {nr:8}"></a>
                                    </li>
                                                                        
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>



<div id="printOfferDiv" class="hidden">
    <div id="printCaption" style="display: none;">
        <p class="block clr large lheight22 marginleft10">Drukuj</p>
    </div>
    <form class="default" action="http://olx.pl/drukuj/okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-CID3-ID8vy6W.html" method="post" target="_blank">
        <div class="inner tcenter">
            <div class="large lheight18">
                <fieldset class="tleft margintop10">
                    <p class="marginbott15">
                        <input checked="checked" type="radio" name="print-option" id="print-opt-1" value="print-opt-1"><label for="print-opt-1" class="marginleft10">wydrukuj całe ogłoszenie</label>
                    </p>
                    <p class="marginbott15">
                        <input type="radio" name="print-option" id="print-opt-2" value="print-opt-2"><label for="print-opt-2" class="marginleft10">drukuj z wybranymi zdjęciami</label>
                    </p>
                    <div class="hidden" id="printOfferPhotos">
                        <ul class="clr printphotoselect">
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-0"><img src="http://img20.olx.pl/images_tablicapl/214959355_1_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-krakow.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="0" class="abs {renderformClass: 'abs'}" id="photoprint-0">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-1"><img src="http://img20.olx.pl/images_tablicapl/214959355_2_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-dodaj-zdjecia.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="1" class="abs {renderformClass: 'abs'}" id="photoprint-1">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-2"><img src="http://img21.olx.pl/images_tablicapl/214959355_3_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-wynajem.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="2" class="abs {renderformClass: 'abs'}" id="photoprint-2">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-3"><img src="http://img20.olx.pl/images_tablicapl/214959355_4_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-nieruchomosci.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="3" class="abs {renderformClass: 'abs'}" id="photoprint-3">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-4"><img src="http://img19.olx.pl/images_tablicapl/214959355_5_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-malopolskie.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="4" class="abs {renderformClass: 'abs'}" id="photoprint-4">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-5"><img src="http://img19.olx.pl/images_tablicapl/214959355_6_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="5" class="abs {renderformClass: 'abs'}" id="photoprint-5">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-6"><img src="http://img19.olx.pl/images_tablicapl/214959355_7_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="6" class="abs {renderformClass: 'abs'}" id="photoprint-6">
                            </li>
                                                        <li class="fleft rel tcenter">
                                <label class="block br4" for="photoprint-7"><img src="http://img20.olx.pl/images_tablicapl/214959355_8_261x203_okazja-2-pokojowe-mieszkanie-51m2-chmieleniec-ruczaj-ericpol-.jpg" class="vmiddle"></label><input type="checkbox" checked="checked"
                                    name="selectedImages[]" value="7" class="abs {renderformClass: 'abs'}" id="photoprint-7">
                            </li>
                                                    </ul>
                    </div>
                </fieldset>
            </div>
        </div>
        <div class="tcenter brtop-1 clr pding10">
            <p class="margin15_0">
                <span class="button big3 br3 circleshadow large"><input id="printButton" type="submit" class="cfff" value="Drukuj"></span>
            </p>
        </div>
    </form>
</div>



    <footer id="footer-container">
        <div class="wrapper small" id="lastwrapper">
        <div class="margintop15 clr rel">
            <div class="fleft">
                                    <p>
                    <a href="http://olx.pl" class="tdnone" title="OLX.pl (dawniej Tablica.pl)">
                        <span class="icon websitegray inlblk vtop">&nbsp;</span>
                    </a>
                    </p>
                            </div>
            <div class="boxindent">
                <div class="clr">
                    
<div class="static box fleft">
    <ul class="small lheight16">
        
        <li class="block">
            <a id="footerLinkMobileApps" class="link gray" title="Aplikacje mobilne OLX.pl (dawniej Tablica.pl)" href="http://olx.pl/mobilne/">
                <span>Aplikacje mobilne OLX.pl</span>
            </a>
        </li>
        <li class="block">
            <a href="http://olx.pl/pomoc/" class="link gray" title="Pomoc">
                <span>Pomoc</span>
            </a>
        </li>
                        <li class="block">
                    <a class="link gray" title="Wyróżnione ogłoszenia" href="http://olx.pl/platnosci/dlaczego-warto-promowac/">
                        <span>Wyróżnione ogłoszenia</span>
                    </a>
                </li>
                <li class="block">
    <a href="http://blog.olx.pl" class="link gray" title="Blog Olx.pl" target="_blank">
        <span>Blog</span>
    </a>
</li>
        <li class="block">
            <a href="http://olx.pl/zasady/" class="link gray" title="Regulamin OLX.pl">
                <span>Regulamin OLX.pl</span>
            </a>
        </li>
        <li class="block">
            <a href="#" class="tdnone link spoiler graydot" id="footerPartners">
                <span class="inlblk">Partnerzy</span><span class="icon mini inlblk vtop margintop6 marginleft5 down4">&nbsp;</span>
            </a>
        </li>
    </ul>
</div>
<div class="static box fleft">
    <ul class="small lheight16">
        <li class="block">
            <a href="http://olx.pl/jak-dziala-olx/" title="Jak działa OLX.pl (dawniej Tablica.pl)" class="link gray nowrap" title="Jak działa OLX.pl (dawniej Tablica.pl)">
                <span>Jak działa OLX.pl (dawniej Tablica.pl)</span>
            </a>
        </li>
        <li class="block">
            <a href="http://olx.pl/bezpieczenstwo/" title="Zasady bezpieczeństwa" class="link gray">
                <span>Zasady bezpieczeństwa</span>
            </a>
        </li>
        <li class="block">
            <a href="http://olx.pl/sitemap/" class="link gray" title="Mapa kategorii">
                <span>Mapa kategorii</span>
            </a>
        </li>
        <li class="block">
            <a href="http://olx.pl/sitemap/regions/" class="link gray" title="Mapa miejscowości">
                <span>Mapa miejscowości</span>
            </a>
        </li>
                            <li class="block">
                <a href="http://olx.pl/popularne/" class="link gray" title="Popularne wyszukiwania">
                    <span>Popularne wyszukiwania</span>
                </a>
            </li>
                
        <li class="block">
            <a href="http://olx.pl/kontakt/" class="link gray" title="Kontakt z OLX.pl">
                <span>Kontakt z OLX.pl</span>
            </a>
        </li>
                    </ul>
</div>
                                            <div class="footerapps fright rel tcenter">
    <a href="http://ad-x.co.uk/API/click/olxplnd230914jda/am554b643d90169e&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" id="footerAppAndroid" target="_blank" class="inlblk">
        <span class="icon block googleplay"> w Google Play</span>
        <span class="tag-line tleft hidden">
            Do pobrania w            <strong class="block">Google Play</strong>
        </span>
    </a>
    <a href="http://ad-x.co.uk/API/click/olxplnd230914jda/am554b644ea7b60c>" id="footerAppIphone" target="_blank" class="inlblk">
        <span class="icon block appstore"> w AppStore</span>
        <span class="tag-line hidden">
            Pobierz w            <strong class="block">AppStore</strong>
        </span>
    </a>
    <a href="http://www.windowsphone.com/pl-pl/store/app/olx-pl/cfb57b0c-bc3e-4d00-9373-fa351f8c5f0c" id="footerAppIphone" target="_blank" class="inlblk">
        <span class="icon block windowsstore"> w WindowsStore</span>
        <span class="tag-line tright hidden">
            Dostępne dla            <strong class="block">Windows Phone</strong>
        </span>
    </a>
    <p class="tag-line">Darmowa aplikacja na Twój telefon</p>
</div>
                                    </div>
                <div class="partners box margin10_0 hidden" id="footerPartnersContainer">
    <ul class="clr">
                        <li class="part25 fleft">
                <a href="http://olx.bg" target="_blank" class="link gray">
                    <span class="icon fleft flag hitarpetarbg">&nbsp;</span><span>OLX.bg</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://olx.hu" target="_blank" class="link gray">
                    <span class="icon fleft flag olxhu">&nbsp;</span><span>OLX.hu</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://olx.ro" target="_blank" class="link gray">
                    <span class="icon fleft flag olxro">&nbsp;</span><span>OLX.ro</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://www.skelbiu.lt" target="_blank" class="link gray">
                    <span class="icon fleft flag skelbiult">&nbsp;</span><span>Skelbiu.lt</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://olx.ua/" target="_blank" class="link gray">
                    <span class="icon fleft flag olxua">&nbsp;</span><span>OLX.ua</span>
                </a>
            </li>
                </ul>
</div>
            </div>
            
                            <div id="mobileAppsbadge" class="fix hidden">
                    <a href="http://olx.pl/mobilne/" class="icon tdnone abs"></a>
                    <a href="#" id="mobileAppsbadgeClose" class="tdnone abs" title="Zamknij"></a>
                </div>
                 <ul id="mobile_change" class="breaklist version tcenter margintop15" style="display: none">
                    <li class="inline">
                        <a href="http://olx.pl/disable/m/" rel="nofollow">Wersja mobilna</a>
                    </li>
                    <li class="inline">
                        <a href="http://olx.pl/disable/i/" rel="nofollow">Wersja dotykowa</a>
                    </li>
                    <li class="inline">
                        <span>Wersja pełna</span>
                    </li>
                </ul>
                    </div>
    </div>
</footer>
<div id="message_system" style="display: none">
    <div class="inner">
        <div class="tleft x-normal lheight20 rel messagesystem ">
            <p>
                <span class="fleft icon status">&nbsp;</span>
                <span class="msg block overh"></span>
            </p>
        </div>
    </div>
</div>
<div id="dialogMessage" class="hidden">
    <div class="inner"></div>
</div>
<div id="saveFavDiv" class="hidden">
    <div class="inner tcenter">
        <div class="large lheight18">
            <p class="marginbott15 margintop10 typeSearch hidden">
                <strong>Wyszukiwanie zostało dodane do obserwowanych</strong>
            </p>
            <p class="marginbott15 margintop10 typeOffer hidden">
                <strong>Ogłoszenie dodane do obserwowanych</strong>
            </p>
            <p class="margin5_0">Zaloguj się do OLX.pl aby zapamiętać je na "stałe"</p>
            <p class="margintop25 marginbott25">
                <a class="button big3 br3 circleshadow" href="http://olx.pl/konto/?origin=observepopup">
                    <span class="cfff large">Zaloguj się</span>
                </a>
            </p>
            <p class="margin5_0">lub <a href="http://olx.pl/konto/rejestracja/" class="link">
                    <span>Utwórz konto</span>
                </a>
            </p>
        </div>
    </div>
    <div class="tcenter brtop-1 clr pding10">
        <p class="margin20_0 large lheight18">
            <a href="#" class="link" onclick="$.fancybox.close(); return false;">
                <span>Nie, dziękuję</span>
            </a>
        </p>
    </div>
</div>
<div id="synchroFavDiv" class="hidden">
    <div class="inner"></div>
    <div class="tcenter brtop-1 clr pding10">
        <p class="margin10_0">
            <a class="button big br3" href="#" id="synchronizeObservedConfirm">
                <span class="cfff large">Zapisz w Obserwowanych</span>
            </a>
        </p>
        <p class="margin5_0">
            <a href="#" class="link" id="synchronizeObservedCancel">
                <span>Nie, dziękuję</span>
            </a>
        </p>
    </div>
</div>
<div class="topinfo rel hidden" id="cookiesBar">
    <a href="javascript:void(0);" class="cookiesBarClose abs link icon close"></a>
    <p class="normal cfff">
        Strona korzysta z plików cookies w celu realizacji usług i zgodnie z 
        <a href="http://olx.pl/zasady/" target="_blank" class="link tdnone cookiesBarClose">Polityką Plików Cookies</a>. 
        Możesz określić warunki przechowywania lub dostępu do plików cookies w Twojej przeglądarce.
    </p>
</div> 

<div id="layer-apps" class="layer-apps  hidden">
    <div class="layer-content">
        <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'Close']);" class="layerapps-close icon close abs" href="#"></a>
        <span class="header iblblk abs"></span>
        <div class="buttons-box">
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'AppStore']);" class="inlblk icon appstore" href="http://ad-x.co.uk/API/click/olxplnd230914jda/am554b644ea7b60c" target="_blank">OLX.pl AppStore</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'GooglePlay']);" class="inlblk icon googleplay" href="http://ad-x.co.uk/API/click/olxplnd230914jda/am554b643d90169e&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" target="_blank">OLX.pl GooglePlay</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'WindowsStore']);" class="inlblk icon windowsstore" href="http://www.windowsphone.com/pl-pl/store/app/olx-pl/cfb57b0c-bc3e-4d00-9373-fa351f8c5f0c" target="_blank">OLX.pl WindowsStore</a>
        </div>
    </div>
</div> </div>            
            <script type="text/javascript">
          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-7409099-1']);
          _gaq.push(['_setDomainName', 'olx.pl']);
          _gaq.push(['_trackPageview']);
          
          (function(){
           var ga, s;
           if ( !_adblock ) {
              ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
              s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
           } else {
              ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
           }})();
        </script>
        
        
        
                <script type="text/javascript">
    <!--
    xtnv = document;
    xtsd = "http://LOGC269"
    xtsite = "507462";
    xtcustom = {"page_name":"adpage","action_type":"loaded","ad_id":"125968309","poster_id":"23000903","ad_photo":8,"poster_type":"business","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","provinces":"malopolskie","cities":"krakow","user_status":"unlogged_user"};
    //-->
</script>
<noscript>
    <img width="1" height="1" alt="" src="http://LOGC269.xiti.com/hit.xiti?s=507462&stc={"page_name":"adpage","action_type":"loaded","ad_id":"125968309","poster_id":"23000903","ad_photo":8,"poster_type":"business","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","provinces":"malopolskie","cities":"krakow","user_status":"unlogged_user"}" >
</noscript>
                                    <script type="text/javascript" src="http://s1.olx.pl/static/olxpl/packed/sw74dbe9ec6d2d49cb65e8f50fb9437003.js"></script>
                                                <script type="text/javascript" src="http://s2.olx.pl/static/olxpl/packed/sw2ec272cfee08dc515edecd83ffcc3946.js"></script>
                                        <script type="text/javascript">
                $LAB
                                .script('http://cdn.optimizely.com/js/572110902.js')
                            </script>
                            <script type="text/javascript">
        $(function(){
            if(typeof GoogleObj != 'undefined') {
                setTimeout(function() {
                    var conversions = GoogleObj.getConversions();
                    for(k in conversions) {
                        var data = conversions[k];
                        window['google_conversion_id'] = data.id;
                        window['google_conversion_language'] = data.language;
                        window['google_conversion_format'] = data.format;
                        window['google_conversion_color'] = data.color;
                        window['google_conversion_label'] = data.label;
                        window['google_conversion_value'] = data.value;
                        oldWrite = document.write;
                        document.write = (function(params)
                        {
                            $(document.body).append(params);
                        });
                        $.getScript(document.location.protocol + "//www.googleadservices.com/pagead/conversion.js", function(){
                            document.write = oldWrite;
                        });
                    }
                }, 10);
            };
    
            if(typeof GoogleObj != 'undefined') {
                setTimeout(function() {
                    var adsDetails = GoogleObj.getAdsDetails();
                    if(typeof adsDetails[0] != 'undefined') {
                        GoogleObj.loadGoogleAds(adsDetails[0]);
                    }
                }, 100);
            }
        });
    </script>
        <script type="text/javascript">
    function loadAdocean() {
        var additinalKeys = [];
        if(typeof crtg_content != 'undefined') {
            var ckeys = crtg_content.split(';');
            if(ckeys.length) {
                for(i in ckeys) {
                    if(ckeys[i].indexOf('gata') === 0) {
                        additinalKeys.push(ckeys[i].split('=')[0] + ':' + ckeys[i].split('=')[1]);
                    }
                }
            }
        }
                
        if(typeof AdoVars != 'undefined') {
            if(typeof ado!=="object"){ado={};ado.config=ado.preview=ado.placement=ado.master=ado.slave=function(){};}
            ado.config({mode: "new", xml: false, characterEncoding: true});
            ado.preview({enabled: true, emiter: "gg.adocean.pl", id: "JOcK7gzdoyrcIT2176iLzhCz8UoPOGcT6Y1ax8FNTPf.l7"});
            if(typeof AdoVars['master'] != 'undefined') {
                if(typeof AdoVars['master']['keys'] != 'undefined') {
                    AdoVars['master']['keys'] = additinalKeys.concat(AdoVars['master']['keys']);
                } else {
                    AdoVars['master']['keys'] = additinalKeys;
                }
                ado.master(AdoVars['master']);

                if(typeof AdoVars['slave'] != 'undefined') {
                    for(key in AdoVars['slave']) {
                        ado.slave(key, AdoVars['slave'][key]);
                    }
                };
            }
        }
    };
    $(function(){
        setTimeout(loadAdocean ,300);
    });
    </script>
    
        <!--APP R3NDR olx.pl--><!--B4CK3ND OK-->
    </body>
</html>
<!-- tablica-06 -->
"""