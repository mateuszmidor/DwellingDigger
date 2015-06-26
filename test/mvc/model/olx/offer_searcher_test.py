# -*- coding: UTF-8 -*-

'''
Created on 24-01-2015

@author: mateusz
'''
import unittest
from src.mvc.model.olx.offer_searcher import OfferSearcher

class WebDocumentFetcherStub():
    """This guy is used in OfferSearcher.search to return predefined html content"""

    @staticmethod
    def fetch(url):
        """Returns fixed HTML string representing olx offer search result"""
        PAGES = {"http://SEARCH_QUERY_URL?&page=1" : SEARCH_RESULT_PAGE1,
                 "http://SEARCH_QUERY_URL?&page=2" : SEARCH_RESULT_PAGE2} 
        return PAGES[url]
    
    
class OfferSearcherTest(unittest.TestCase):

    def test_get_urls(self):
        """Check if we can get all 6 offer urls that reside in 2 predefined olx offer search result pages"""
        OFFER_URLS = ["http://olx.pl/offer1",
                      "http://olx.pl/offer2",
                      "http://olx.pl/offer3",
                      "http://olx.pl/offer4",
                      "http://olx.pl/offer5",
                      "http://olx.pl/offer6"]

        SEARCH_QUERY = "http://SEARCH_QUERY_URL?"
        
        for url in OfferSearcher.search(SEARCH_QUERY, 6, WebDocumentFetcherStub):
            self.assertTrue(url in OFFER_URLS, "Unexpected offer url fetched: %s" % url)
            OFFER_URLS.remove(url)
               
        self.assertEquals(0, len(OFFER_URLS), "Not all offer urls fetched: %s" % OFFER_URLS)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
# First SEARCH_RESULT_PAGE with 3 prepared offer urls
SEARCH_RESULT_PAGE1 = u"""
    <!DOCTYPE html>
<html xmlns:og="http://ogp.me/ns#" xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl)</title>
                            <link rel="next" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2" />
                <meta name="robots" content="index, follow" />        <link rel="canonical" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />        <link rel="alternate" media="handheld" href="http://olx.pl/m/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />
<link rel="alternate" media="only screen and (max-width: 640px)" href="http://olx.pl/i2/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />
<link rel="alternate" href="android-app://pl.tablica/http/olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />        <meta http-equiv="Content-Language" content="pl" />
        <meta name="description" content="Ruczaj w Kraków najnowsze ogłoszenia na OLX.pl (dawniej Tablica.pl) w Kraków" />
                            <meta property="og:title" content="Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl)"/>
                    <meta property="og:description" content="Ruczaj w Kraków najnowsze ogłoszenia na OLX.pl (dawniej Tablica.pl) w Kraków"/>
                    <meta property="og:url" content="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/"/>
                    <meta property="fb:app_id" content="121167521293285"/>
                    <meta property="og:image" content="http://s7.olx.pl/static/olxpl/external/olxpl/img/fb/fb-image200x200.png?t=15-06-26"/>
                    <meta property="og:type" content="website"/>
                    <meta property="og:site_name" content="OLX.pl (dawniej Tablica.pl)"/>
                            <link rel="icon" type="image/x-icon" href="http://s8.olx.pl/static/olxpl/external/olxpl/img/favicon.ico?v=3">
                                    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/rss/q-ruczaj/" />
                                                        <script type="text/javascript">
                    var _adblock = true;
            </script>
            <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/external/base/js/advertising.js"></script>
                                                                                                <link rel="stylesheet" type="text/css" href="http://s7.olx.pl/static/olxpl/packed/sweb45af5fa50c07d56be5994ade79367a.css">
                                                                                                        <!--[if lte IE 8]>                        <link rel="stylesheet" type="text/css" href="http://s7.olx.pl/static/olxpl/packed/sw219069a4faf339926afcad6163516c59.css">
                    <![endif]-->                                                        <script type="text/javascript">
                window.suggestmeyes_loaded = true;
                                        var action='ads';
                                        var method='index';
                                        var user_logged=0;
                                        var www_base='http://olx.pl/krakow';
                                        var www_base_no_namespace='http://olx.pl/krakow';
                                        var www_base_ajax='http://olx.pl/ajax/krakow';
                                        var static_files_www_base='http://s7.olx.pl/static/olxpl/';
                                        var external_static_files_www_base='http://s8.olx.pl/static/olxpl/external/olxpl/';
                                        var session_domain='olx.pl';
                                        var decimal_separator=',';
                                        var thousands_separator=' ';
                                        var sitecode='olxpl';
                                        var defaultCurrency='PLN';
                                        var config_currency='zł';
                                        var useExternalScripts=1;
                                        var lang='pl';
                                        var hasRwd=0;
                                        var module_store_image_sizes_db=1;
                                        var module_store_image_sizes=1;
                                        var module_new_design=1;
                                        var module_paidads=1;
                                        var module_facebook_login=1;
                                        var module_gg_integration=1;
                                        var module_mms_images=1;
                                        var module_sms_notification=1;
                                        var module_mobile_app=1;
                                        var module_otokredyt=1;
                                        var module_invoiceform=1;
                                        var module_paid_limits=1;
                                        var module_connection_port=1;
                                        var module_multiacc=1;
                                        var module_fraud_detection=1;
                                        var module_dogs=1;
                                        var module_googleplus=1;
                                        var module_trusted_changes=1;
                                        var module_kredyt_hipoteczny=1;
                                        var module_einvoice_olxpl=1;
                                        var module_comperiabox=1;
                                        var module_payupl_response=1;
                                        var module_payupl_bank_accounts=1;
                                        var module_controlpanel2=1;
                                        var module_i2_payment=1;
                                        var module_pdlaenau=1;
                                        var module_zendesk_schedule=1;
                                        var module_hashtags=1;
                                        var module_answers_filters_fraud=1;
                                        var module_fraud_contact_data=1;
                                        var module_refactorized_stats=1;
                                        var module_fraud_detector_queue=1;
                                        var module_paid_for_post=1;
                                        var module_category_change_with_pay_to_post_ad=1;
                                        var module_adding_refactor=1;
                                        var module_automotive_supiscious_parameters=1;
                                        var module_at_addingform_track=1;
                                        var module_m_promote=1;
                                        var module_invoice_exporter=1;
                                        var module_einvoice_ap_poland=1;
                                        var module_rest_api=1;
                                        var module_old_payment_tables=1;
                                        var module_redis_hash=1;
                                        var module_js_stacktrace=1;
                                        var module_hermes_migration=1;
                                        var module_hermes_history=1;
                                        var module_prevent_fraud_stats=1;
                                        var module_history_extra_info_alter=1;
                                        var module_solr_cloud=1;
                                        var module_solr_improvement=1;
                                        var region_id='4';
                                        var regionName="Ma\u0142opolskie";
                                        var subregion_id='102';
                                        var subregionName="Krak\u00f3w";
                                        var category_id='15';
                                        var is_search_category='';
                                        var categoryName="Wynajem";
                                        var categoryCode="wynajem";
                                        var categoryAdsenseText=null;
                                        var root_category_id='3';
                                        var second_category_id='1307';
                                        var second_category_code="mieszkania";
                                        var rootCategoryName="Nieruchomo\u015bci";
                                        var rootCategoryCode="nieruchomosci";
                                        var rootCategoryAdsenseText=null;
                                        var setSeoPageName="Mieszkania wynajm\u0119, mieszkania na wynajem Krak\u00f3w";
                                        var q="ruczaj";
                                        var city_id='8959';
                                        var regionCode='malopolskie';
                                        var cityCode='krakow';
                                        var is_archive='';
                                        var geoData={"category":"15","locationName":"Krak\u00f3w, Ma\u0142opolskie","region":"4","params":{"q":"ruczaj"}};
                                        var geoAjaxGet='http://olx.pl/ajax/krakow/geo/get/';
                                        var geoAjaxClose='http://olx.pl/ajax/krakow/geo/close/';
                                        var isSearch='1';
                                        var saveFavLink="http://olx.pl/konto/?origin=observepopup&ref%5B0%5D%5Baction%5D=ads&ref%5B0%5D%5Bmethod%5D=index&ref%5B0%5D%5Bparams%5D%5Bq%5D=ruczaj&ref%5B0%5D%5Bcategory%5D=15&ref%5B0%5D%5Bregion%5D=4&ref%5B0%5D%5Bsubregion%5D=102&ref%5B0%5D%5Bcity%5D=8959";
                                        var xtClickCategoryID='9';
                                        var totalAds='131';
                                        var isUserSearch='';
                                        var categoriesStats={"1307":"294","3":"214","0":"206","15":"131","11":"43","4":"33","124":"30","619":"23","711":"22","751":"18","710":"16","14":"16","1313":"15","130":"12","333":"11","1435":"9","127":"8","368":"8","64":"6","443":"6","1437":"5","297":"5","625":"4","82":"4","1449":"3","306":"3","1213":"3","1209":"3","321":"3","99":"3","1399":"2","522":"2","65":"2","62":"2","1309":"2","767":"2","453":"2","5":"2","1159":"1","628":"1","329":"1","88":"1","461":"1","230":"1","164":"1","100":"1","53":"1","282":"1","523":"1","324":"1","20":"1","1421":"1","326":"1"};
                                        var gemius_identifier=new String('ApI65iOBi_V74WSAbF.5DNUoDmwZEdr0JULbeXtukR7.Y7');
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
            <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/js/scripts/html5shiv.min.js"></script>
        <![endif]-->
        <link href="https://plus.google.com/113406265199615974663" rel="publisher" />
            <!-- Criteo cookie -->
        <script type="text/javascript">
        function crtg_getCookie(c_name){ var i,x,y,ARRCookies=document.cookie.split(";");for(i=0;i<ARRCookies.length;i++){x=ARRCookies[i].substr(0,ARRCookies[i].indexOf("="));y=ARRCookies[i].substr(ARRCookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);} }return'';} var crtg_content = crtg_getCookie('crtg_rta');    (function(){var crtg_nid = '2859';var crtg_cookiename = 'crtg_rta';var crtg_varname = 'crtg_content';var crtg_url=location.protocol+'//rtax.criteo.com/delivery/rta/rta.js?netId='+escape(crtg_nid)+'&cookieName='+escape(crtg_cookiename)+'&rnd='+Math.floor(Math.random()*99999999999)+'&varName=' + escape(crtg_varname);var crtg_script=document.createElement('script');crtg_script.type='text/javascript';crtg_script.src=crtg_url;crtg_script.async=true;if(document.getElementsByTagName("head").length>0)document.getElementsByTagName("head")[0].appendChild(crtg_script);else if(document.getElementsByTagName("body").length>0)document.getElementsByTagName("body")[0].appendChild(crtg_script);})();
        var AdoVars = [];
                        AdoVars['master'] = {
                id: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
                server: 'gg.adocean.pl',
                characterEncoding: true,
                keys: ['region:malopolskie','city:krakow' ,'cat:nieruchomosci' ,'cat:mieszkania' ,'cat:wynajem', 'ruczaj']
                                };
                                </script>
        
        </head>
    <body class="offersview standard">
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
<!-- End Google Tag Manager -->                        <div id="innerLayout">
    
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
    <div id="searchbox">
    <div class="wrapper">
        <form method="POST" action="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/" class="search clr" id="mainTopSearch">
            <a href="http://olx.pl" class="abs icon website hidden">OLX.pl (dawniej Tablica.pl)</a>
                        <input type="hidden" name="view" value="" />
                        <input type="hidden" name="min_id" value="" />
                        <fieldset>
                <div class="clr rel pdingbott5" id="withshowbox">
                    <noindex>
                    <table width="100%" cellpadding="0" cellspacing="0" id="withshowboxTable">
                        <tr>
                            
<td valign="top" width="251">
    
<div class="clearbox clr rel">
    <input autocomplete="off" id="search-text" type="text"
           class="br3 light large fleft with-x-clear-button ca2 fbold autosuggest-input defaultval {suggesturl: 'http://olx.pl/ajax/nieruchomosci/mieszkania/wynajem/krakow/suggest/get/'}"
           name="q" value="ruczaj" defaultval="Szukaj..." style="margin: 0px;">
    <div id="autosuggest-div">
        <!-- via ajax -->
    </div>
    <a class="icon cleartext3 abs clear-input-button hidden" id="clearQ" href="#">X</a>
</div>

</td>
<td valign="top">
    
<div class="locationrequest smallBox has-dist-picker" id="locationBox">
    <div class="clr rel">
        <div class="rel fleft input-container">
                        <input id="cityField" autocomplete="off" type="text" defaultval="Cała Polska"
                defaultalternative="Miejscowość lub kod" value="Kraków" class="with-x-clear-button fleft defaultval light ca2 cityfield bold">
            <div class="cityfield" id="cityFieldGray">
                <span class="fbold vishid">Kraków</span><span class="color-9">, Małopolskie</span>
            </div>
            <a href="#" class="icon cleartext3 abs clear-input-button ">X</a>
            <div class="distanceseparator abs"></div>
            <label class="icon locmarker2 abs" for="cityField">&nbsp;</label>
            <div class="proposals hidden" id="proposalContainer">
                <div class="lastbox">
                    <p>Ostatnio wybrane:</p>
                    <ul id="last-locations-ul">
                    </ul>
                </div>
                <div class="abs categorySelectContainer">
                    <ul class="categorySelectList regionsList">
                        <!-- utaj umiescic -->
                    </ul>
                </div>
            </div>
            <input class="autosuggest-geo-input" type="hidden" name="search[city_id]" value="8959" />
            <input class="autosuggest-geo-input-region" type="hidden" name="search[region_id]" value="4" />
            <input class="autosuggest-geo-district-input" type="hidden" name="search[district_id]" value="0" />
            
                            <input class="autosuggest-geo-dist-input" type="hidden" name="search[dist]" value="0" />
                        
            <div class="autosuggest-geo-div suggestmain">
                <!-- via ajax -->
            </div>
            <div id="geo-suggestions" class="chooselocation br3 hidden">
                <div class="icon target abs"></div>
                <a id="geo-suggestions-close" href="#" class="close icon abs">X</a>
                <p>Wybierz lokalizację:</p>
                <div id="geo-suggestions-options" class="items"></div>
            </div>
        </div>
                    <dl class="distancelist fleft bold " id="distanceSelect">
                                <dt>
                    <a href="#" class="topLink">
                        <span class="label">+ 0 km</span>
                        <span class="value">0</span>
                    </a>
                </dt>
                <dd>
                    <ul style="display: none;">
                                                <li class="">
                            <a href="#" class="dist">+ 0 km<span class="value">0</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 5 km<span class="value">5</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 10 km<span class="value">10</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 15 km<span class="value">15</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 30 km<span class="value">30</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 50 km<span class="value">50</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 75 km<span class="value">75</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 100 km<span class="value">100</span>
                            </a>
                        </li>
                                            </ul>
                </dd>
            </dl>
            </div>
        <p id="cityFieldError" class="margintop3 small lheight16 marginbott-5" style="display: none;">Niepoprawne miasto lub kod pocztowy</p>
    </div>
</td>

                            <td valign="top" width="150">
                                <div class="rel combospace">
    <a href="" class="block select fbold a-category-3 rel nowrap tdnone overh" id="choosecat">
        <span class="icon caticongray abs">&nbsp;</span>
        <span class="block overh">
                                                 <span id="main-category-choose-label" class="c000">Mieszkania</span>
                                    </span>
    </a>
    <div class="abs categorySelectContainer">
        <ul class="categorySelectList" id="categorySelectList" style="display: none;"></ul>
    </div>
</div>
                            </td>
                        </tr>
                    </table>
                    </noindex>
                </div>
            </fieldset>
            <noindex>
            <fieldset id="paramsListOpt">
                <div class="checkboxsepa clr">
                    <div class="fblock fleft">
                        <input  type="checkbox" id="title-desc" class=" checkbox {renderformClass: 'fleft marginright5 '}"
                                name="search[description]" value="1"> <label class=" small" for="title-desc">szukaj również w opisach</label>
                    </div>
                    <div class="fblock fleft">
                        <input  type="checkbox" id="photo-only" class="checkbox {renderformClass: 'fleft marginright5'}"
                            name="search[photos]" value="1" /> <label class="small" for="photo-only">tylko ze zdjęciem</label>
                    </div>
                                    </div>
            </fieldset>
               <fieldset class="paramsList rel clr" id="paramsList">
    <ul class="clr multifilters subSelectActive">
                <li class="grid-li">
            <ul class="grid-ul grid-1" id="param-grid-1">
                                                                                                                                                            
<li class="subcategory" id="param_subcat">
    <div class="filter-item rel category-item">
        <div class="subSelect hidden abs zi2" id="">
            Wybierz kategorię        </div>
        <a href="javascript:void(0);" class="button gray block category rel zi3 clr fbold">
                        <span class="3rd-category-choose-label header block" data-default-label="Wynajem">
                Wynajem            </span> 
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs hidden subcategories">
            <li class="clr brbottdash-2">
                <a id="all-categories" class="tdnone block value c000 category-choose search-choose {name: 'search[category_id]', value: '1307'}" href="#">Wszystkie</a>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<li class="param paramSelect " data-name="search[filter_enum_rooms][]" data-key="rooms" data-param-id="165" id="param_rooms">
    <div class="filter-item rel filter-item-rooms">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Liczba pokoi">Liczba pokoi</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_rooms_25">
                    <input maxlength="13" id="f-all-filter_enum_rooms_25" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                
<li class="param paramSelect " data-name="search[filter_enum_builttype][]" data-key="builttype" data-param-id="157" id="param_builttype">
    <div class="filter-item rel filter-item-builttype">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Rodzaj zabudowy">Rodzaj zabudowy</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_builttype_27">
                    <input maxlength="13" id="f-all-filter_enum_builttype_27" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-2" id="param-grid-2">
                                                                                
<li class="param paramFloat " data-name="search[filter_float_price][]" data-key="price" data-param-id="1" id="param_price">
    <div class="filter-both-item">
                    <div class="filter-item filter-item-from rel numeric-item price ">
            <a href="javascript:void(0);" class="button button-from numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Cena od">
                    Cena od                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="13" value="" type="text" class="defaultval {name: 'search[filter_float_price:from]'} small vtop min-value-input from" defaultval="od..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="zł"></ul>
        </div>
                    <div class="filter-item filter-item-to rel numeric-item price ">
            <a href="javascript:void(0);" class="button button-to numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Cena do">
                    Cena do                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="13" value="" type="text" class="defaultval {name: 'search[filter_float_price:to]'} small vtop max-value-input to" defaultval="do..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="zł"></ul>
        </div>
            </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-3" id="param-grid-3">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<li class="param paramFloat " data-name="search[filter_float_m][]" data-key="m" data-param-id="163" id="param_m">
    <div class="filter-both-item">
                    <div class="filter-item filter-item-from rel numeric-item  ">
            <a href="javascript:void(0);" class="button button-from numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Pow. od">
                    Pow. od                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="8" value="" type="text" class="defaultval {name: 'search[filter_float_m:from]'} small vtop min-value-input from" defaultval="od..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="m<sup>2</sup>"></ul>
        </div>
                    <div class="filter-item filter-item-to rel numeric-item  ">
            <a href="javascript:void(0);" class="button button-to numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Pow. do">
                    Pow. do                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="8" value="" type="text" class="defaultval {name: 'search[filter_float_m:to]'} small vtop max-value-input to" defaultval="do..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="m<sup>2</sup>"></ul>
        </div>
            </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-4" id="param-grid-4">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<li class="param paramSelect " data-name="search[filter_enum_floor_select][]" data-key="floor_select" data-param-id="151" id="param_floor_select">
    <div class="filter-item rel filter-item-floor_select">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Poziom">Poziom</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_floor_select_22">
                    <input maxlength="13" id="f-all-filter_enum_floor_select_22" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                
<li class="param paramSelect " data-name="search[filter_enum_furniture][]" data-key="furniture" data-param-id="155" id="param_furniture">
    <div class="filter-item rel filter-item-furniture">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Umeblowane">Umeblowane</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_furniture_24">
                    <input maxlength="13" id="f-all-filter_enum_furniture_24" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-5" id="param-grid-5">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                <li class="line"></li>
                    <li class="grid-li">
            <ul class="grid-ul grid-6" id="param-grid-6">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-7" id="param-grid-7">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-8" id="param-grid-8">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-9" id="param-grid-9">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-10" id="param-grid-10">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                </ul>
</fieldset>
<fieldset class="clr " id="searchList">
    <div class="checkboxsepa small">
        <div class="fblock fright">
            <a id="clear-params" href="#" class="fleft option-search-clear tdnone hidden">
                <span class="icon block fleft cleartext6"></span>
                <span class="pdingleft5 link hn">
                    <span>Wyczyść filtry</span>
                </span>
            </a>
            <div class="fblock fleft option-search-criteria">
                <a href="#" class="tdnone inlblk selected" id="cancelSearchCriteriaTop" style="display: none" title="Usuń z obserwowanych">
                    <span class="icon favsearch2 inlblk vtop"></span>
                    <span class="link hn">
                        <span>Usuń z obserwowanych</span>
                    </span>
                </a>
                <a href="#" class="tdnone inlblk rel normal" id="saveSearchCriteriaTop" title="Obserwuj wyszukiwanie">
                    <span class="icon favsearch2 inlblk vtop"></span>
                    <span class="link hn">
                        <span>Obserwuj wyszukiwanie</span>
                    </span>
                </a>
            </div>
            <div class="fleft rel option-search-submit">
                <span class="button search submit normal zi3 inlblk marginleft7 circleshadow active ">
                    <span class="icon inlblk vtop margintop6 marginleft10 b_search2">&nbsp;</span>
                    <input type="submit" class="margintop-1 cfff {clickerID:'search_loop'} tiptip" id="search-submit" value="Szukaj">
                </span>
            </div>
        </div>
    </div>
</fieldset>

            </noindex>
            <input type="hidden" name="search[category_id]" id="searchFormCatID" value="15" />
        </form>
    </div>
</div>
<a name="ending-search-ads"></a></header>    
<div id="listContainer">
    <div id="tabs-container">
    <div class="wrapper clr">
        
<div class="view-lists">
        <ul class="order-select-gallery" id="order-select-gallery">
        <li class="list-label">
            Sortuj:
        </li>
        <li>
            <a href="#" class="link selected" data-type="created_at:desc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Border%5D=created_at%3Adesc"><span>Najnowsze</span></a>
        </li>
                                    <li>
                    <a href="#" class="link " data-type="filter_float_price:asc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Border%5D=filter_float_price%3Aasc"><span>Najtańsze</span></a>
                </li>
                                        <li>
                    <a href="#" class="link " data-type="filter_float_price:desc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Border%5D=filter_float_price%3Adesc"><span>Najdroższe</span></a>
                </li>
                        </ul>
            <ul class="view" id="viewSelector">
        <li class="list-label">Widok:</li>
                <li>
                            <span>Lista</span>
                    </li>
                <li>
                            <a class="topTabView link" data-type="galleryWide" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?view=galleryWide" rel="nofollow"><span>Galeria</span></a>
                    </li>
            </ul>
        </div>

                                                <ul class="tabs offerseek clr large fleft tohide rel zi3">
                                                                                        <li class="fleft">
                                                            <span class="fleft tab selected"> <span class="fbold">Wszystkie</span>
                                                                            <span class="color-2 normal indexed-int">131</span>
                                                                    </span>
                                                    </li>
                                                                                            <li class="fleft">
                                                                                                <a class="fleft tab tdnone topTabOffer" data-type="private" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bprivate_business%5D=private">
                                        <span class="fbold link"><span>Prywatne</span></span> <span class="color-2 normal indexed-int">54</span>
                                    </a>
                                                                                    </li>
                                                                                            <li class="fleft">
                                                                                                <a class="fleft tab tdnone topTabOffer" data-type="business" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bprivate_business%5D=business">
                                        <span class="fbold link"><span>Agencje</span></span> <span class="color-2 normal indexed-int">77</span>
                                    </a>
                                                                                    </li>
                                                            </ul>
                        </div>
</div>    

    
                    <div id="adoceanggmpohhkfufu"></div>
    <script type="text/javascript">
    /* (c)AdOcean 2003-2015, GaduGadu.Tablica.pl (olx.pl).Listings.screening */
    (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggmpohhkfufu'] = {
        myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
    };
    setTimeout(function(){
        typeof window.ads.initScreening == 'function' && window.ads.initScreening();
    }, 2500);
    </script>
 
    <section id="body-container" class="container" data-facets='{"offer_seek":{"offer":131},"private_business":{"business":77,"private":54,"all":131},"categories":{"1307":294,"3":214,"0":206,"15":131,"11":43,"4":33,"124":30,"619":23,"711":22,"751":18,"710":16,"14":16,"1313":15,"130":12,"333":11,"1435":9,"127":8,"368":8,"64":6,"443":6,"1437":5,"297":5,"625":4,"82":4,"1449":3,"306":3,"1213":3,"1209":3,"321":3,"99":3,"1399":2,"522":2,"65":2,"62":2,"1309":2,"767":2,"453":2,"5":2,"1159":1,"628":1,"329":1,"88":1,"461":1,"230":1,"164":1,"100":1,"53":1,"282":1,"523":1,"324":1,"20":1,"1421":1,"326":1},"categoriesParent":[]}' data-showfacets="1" data-pagetitle="Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl)" data-ajaxurl="" data-searchid="">
        <div class="wrapper">
            <div class="content">
                
    <div class="clr offersnav rel margin0_10">
        <div class="pdingtop6"><ul class="breadcrumb offerslist clr marginbott5 small xxxx">
        <li class="marginright7 abs homelink">
        <a href="http://olx.pl" class="tdnone">
            <span class="icon inlblk home"></span>
                    </a>
        <span class="slash">&raquo;</span>
    </li>
                            <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Kraków</span>
                </a>
            </li>
                                <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Nieruchomości</span>
                </a>
            </li>
                                <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/mieszkania/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Mieszkania</span>
                </a>
            </li>
                                <li class="inline selected">
                    <span class="slash">&raquo;</span>
                    <h1 class="small fnormal inline lheight18">Mieszkania wynajmę, mieszkania na wynajem Kraków - OLX.pl - ruczaj</h1>
            </li>
            </ul>
</div>
            </div>
<div id="topmessages"></div>

                                                
<div class="clr tcenter">
    <div class="rel billboard750x100 overh zi2" id="billboard750x100">
        <div id="adoceanggppioipntwd"></div>
    </div>
    <script type="text/javascript">
        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggppioipntwd'] = {
            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
        };
    </script>
</div>

                                <div class="rel listHandler ">
                    
        <div class="rel zi3">
        <div class="abs rightBranding">
            <div id="skycraper" style="top:0px">
                <div class="skyflex rel">
                    <div class="abs deco" id="skyflexdeco" style="display:none;"></div>
                    <div id="adoceanggtchrmukrtx" class="box"></div>
                    <script type="text/javascript">
                        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggtchrmukrtx'] = {
                            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
                            onServerEmission: function(){
                                document.getElementById('skyflexdeco').style.display = 'block';
                            }};
                    </script>
                </div>
            </div>
        </div>
    </div>
    
                                            


<table width="100%" cellspacing="0" cellpadding="0" class="fixed offers breakword" summary="">
    <caption></caption>
    <tbody>
        <tr>
            <td>
                <div class="section clr">
                    <h2>Wyróżnione ogłoszenia</h2>
                    <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bpaidads_listing%5D=1" class="link">
                        <span>Zobacz wszystkie</span>
                    </a>
                </div>
            </td>
        </tr>
        
<div id="adoceanggvgrringnqx"></div>
<script type="text/javascript">
    (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggvgrringnqx'] = {
        myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
        onServerEmission: function(){
            document.getElementById('adoceanggvgrringnqx').style.margin = '10px 0';
        }
    };
</script>


                        
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword promoted-list ad_idaCXrT" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "
                            href="http://olx.pl/offer1" title="">
                                                        <img class="fleft" src="http://img19.staticclassifieds.com/images_tablicapl/267144981_3_261x203_3-poknowe-mieszkanie-ruczaj-wynajem_rev002.jpg" alt="3-Pok.NOWE Mieszkanie RUCZAJ">
                                                                                        <span class="inlblk icon paid type2 abs zi2" title="Ogłoszenie wyróżnione"></span>
                                                    </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/3-pok-nowe-mieszkanie-ruczaj-CID3-IDaCXrT.html#d0dba6ec99;promoted" class="marginright5 link linkWithHash detailsLinkPromoted">
                                    <strong>3-Pok.NOWE Mieszkanie RUCZAJ</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 000 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                22  cze                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:157048349} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-157048349">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>


                
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword promoted-list ad_idayvXn" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "
                            href="http://olx.pl/offer2" title="">
                                                        <img class="fleft" src="http://img19.staticclassifieds.com/images_tablicapl/265397489_5_261x203_mieszkanie-2-pokojowe-na-ul-chmieleniec-ruczaj-wynajem-malopolskie_rev012.jpg" alt="Mieszkanie 2 pokojowe na ul. Chmieleniec - Ruczaj - WYNAJEM">
                                                                                        <span class="inlblk icon paid type2 abs zi2" title="Ogłoszenie wyróżnione"></span>
                                                    </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/mieszkanie-2-pokojowe-na-ul-chmieleniec-ruczaj-wynajem-CID3-IDayvXn.html#d0dba6ec99;promoted" class="marginright5 link linkWithHash detailsLinkPromoted">
                                    <strong>Mieszkanie 2 pokojowe na ul. Chmieleniec - Ruczaj - WYNAJEM</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 400 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                17  cze                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:155993201} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-155993201">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>


                
    </tbody>
</table>
<style type="text/css">
.hasPromoted {
    display: block
}
.dontHasPromoted {
    display: none
}
</style>
                                                            

<table width="100%" cellspacing="0" cellpadding="0" id="offers_table" class="fixed offers breakword" summary="">
    <tbody>
        
<tr>
    <td>
                
<div class="hasPromoted section clr">
    <h2>Pozostałe ogłoszenia</h2>
    <p class="color-2">Znaleziono 131 ogłoszeń</p>
</div>

<div class="dontHasPromoted section clr rel">
        <h2>Znaleziono 131 ogłoszeń</h2>
    <p class="color-2">Twoje ogłoszenie na górze listy? <a href="http://olx.pl/krakow/platnosci/dlaczego-warto-promowac/" target="_blank" id="whyPromoteListLink" class="link"><span>Wyróżnij!</span></a></p>
    </div>

            </td>
</tr>

                     

            
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword  ad_idaaqxp" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink "
                            href="http://olx.pl/offer3" title="">
                                                        <img class="fleft" src="http://img06.staticclassifieds.com/images_tablicapl/255926909_1_261x203_w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowaruczaj-krakow.jpg" alt="W pełni umeblowane mieszkanie do wynajęcia od ZARAZ, ul Obozowa,Ruczaj">
                                                                                </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowa-ruczaj-CID3-IDaaqxp.html#d0dba6ec99" class="marginright5 link linkWithHash detailsLink">
                                    <strong>W pełni umeblowane mieszkanie do wynajęcia od ZARAZ, ul Obozowa,Ruczaj</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 800 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                dzisiaj 12:45                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:150248655} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-150248655">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>
              
<tr class="adcontainer-tr">
    <td class="offer">
        <table cellspacing="0" cellpadding="0" width="100%" class="fixed breakword" summary="Ogłoszenie">
            <tbody>
                <tr>
                    <td width="200" class="tcenter"></td>
                    <td width="1"></td>
                    <td>
                        <div id="adcontainer3"></div>
                    </td>
                    <td width="1" class="wwnormal tright"></td>
                    <td width="1" class="tright small"></td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>

        
        

       </tbody>
</table>                                        

                                </div>
                <div class="pager rel clr">
            <span class="item fleft">
                <span class="block br3 c41 large tdnone lheight24 current"> <span>1</span>
    </span>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2">
            <span>2</span>
        </a>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=3">
            <span>3</span>
        </a>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=4">
            <span>4</span>
        </a>
            </span>
        <span class="fbold next abs large">
                <a class="link pageNextPrev {page:2}" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2">
            <span>następna &raquo;</span>
        </a>
            </span>
    </div>                <div id="skycraperMax"></div>
                
    <div class="seo-suggestions brtop-1 large">
        <h4>Podobne wyszukiwania:</h4>
        <div class="columns">
            <ul class="column">
                                                        <li><a href="http://olx.pl/nieruchomosci/mieszkania/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Mieszkania</span></li>
                                                        <li><a href="http://olx.pl/nieruchomosci/stancje-pokoje/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Stancje i Pokoje</span></li>
                                                        <li><a href="http://olx.pl/nieruchomosci/garaze-parkingi/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Garaże i Parkingi</span></li>
                            </ul>
        </div>
    </div>

                

                                    
<div class="tcenter pding20_0 color-10 brtop-1 large favsearchbox" id="searchCriteriaSave">
    <div class="margintop15">
        <span class="lheight20 inlblk">Czy chcesz zapisać aktualne kryteria wyszukiwania?</span>
        <span id="saveSearchCriteriaLink" class="favsearchlink inlblk vtop rel cpointer">
            <span class="icon favsearch inlblk vtop" id="saveSearchCriteriaStar"></span>
        </span>
        <span class="link tdnone lheight35 inlblk cpointer fbold">
            <span id="saveSearchCriteria">Zapisz wyszukiwanie</span>
        </span>
        <span class="seeAllSaved">
            <span class="slash inlblk vmiddle margin0_10"></span> <a href="http://olx.pl/krakow/obserwowane/wyszukiwania/" class="link gray small">
                <span>Zobacz zapisane</span>
            </a>
        </span>
    </div>
</div>
<div class="tcenter pding20_0 color-10 brtop-1 large favsearchbox" id="searchCriteriaSaved" style="display: none">
    <div class="margintop15">
        <span class="lheight20 inlblk">Aktualne kryteria wyszukiwania są zapisane</span>
        <span id="cancelSearchCriteriaLink" class="favsearchlink inlblk vtop rel cpointer selected">
            <span class="icon favsearch inlblk vtop" id="cancelSearchCriteriaStar"></span>
        </span>
        <span class="link tdnone lheight35 inlblk cpointer fbold">
            <span id="cancelSearchCriteria">Usuń</span>
        </span>
        <span class="seeAllSaved">
            <span class="slash inlblk vmiddle margin0_10"></span>
            <a href="http://olx.pl/krakow/obserwowane/wyszukiwania/" class="link gray small">
                <span>Zobacz zapisane</span>
            </a>
        </span>
    </div>
</div>
<div id="searchCriteria" style="display: none">tFU/Mq7qJDo8bgnFJ3sl++EtOeu6LRgmWOhCfdDPEeAs0r4iNCMA4ZGgWQWBdAfjBSt6xEJ7EEflorRxfHkQD7ywxwF7jm2rqpc4TVvkX2+mcZX3AK/4HwyIH/4IMEUmSuStXRy/0BEEmv4Qt/jJwjKhIaKkCL88MzbCrPxqffs4VmySH5BmPEWHhJW0cUO9NJTyk/B2Ujt8XPRFIFY9dA==</div>


                                
<div class="clr tcenter margintop10">
    <div class="rel billboard750x200" id="billboard750x200" >
        <div id="adoceanggwbqkjxqmyc"></div>
    </div>
    <script type="text/javascript">
        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggwbqkjxqmyc'] = {
            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
        };
    </script>
</div>
<div class="margintop10 hidden " id="favoritesGalleryBox">
    <div class="wrapper">
        <ul class="tabsfav tohide clr cpointer">
            <li class="fleft lastSeen hidden ">
                <span class="fleft tab"> <span class="fbold">Ostatnio przeglądane</span>
                </span>
            </li>
            <li class="fleft observedAds hidden">
                <span class="fleft tab"> <span class="fbold">Obserwowane ogłoszenia</span> <span class="color-2 normal">(<span class="counter">0</span>)
                </span>
                </span>
            </li>
            <li class="fleft observedSearches hidden">
                <span class="fleft tab"> <span class="fbold">Obserwowane wyszukiwania</span> <span class="color-2 normal">(<span class="counter">0</span>)
                </span>
                </span>
            </li>
        </ul>
    </div>
    <div class="favbottombox">
        <div class="tab-lastSeen initialized hidden" id="tab-lastSeen">
            <div class="wrapper">
                <ul class="clr favgallerybox">
                                </ul>
            </div>
        </div>
        <div class="tab-observedAds hidden"></div>
        <div class="tab-observedSearches hidden"></div>
    </div>
</div>
            </div>
        </div>
        
            </section>
    

</div>
<div id="ad-not-available-box" class="pding10_20 clr br5 margin10 headinfobox hidden" style="display: none">
    <div class="icon info7 fleft marginright20"></div>
    <div class="overh">
        <h3 class="lheight20 large cfff">
            <strong>To ogłoszenie nie jest już dostępne</strong>
        </h3>
        <p class="cfff">Wybierz coś dla siebie z podobnych, które znaleźliśmy.</p>
    </div>
</div>
   
    <footer id="footer-container">
        <div id="footerTop" class="wrapper rel small overh brbott-12">
    <div class="content brbott-5">
        <div id="categoryLinksHeader">
    <ul class="breaklist small lheight16 brbott-1 pding15_0">
    <li id="linksCat0" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie główne Kraków</span></span>
        </li>
    <li id="linksCat3" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie podobne do "Nieruchomości" Kraków</span></span>
        </li>
    <li id="linksCat1307" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie podobne do "Mieszkania" Kraków</span></span>
        </li>
</ul>
</div>

<div id="categoryLinksSections">
            <div id="linksCat0Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie główne Kraków:</h3>
                                                <a href="http://olx.pl/motoryzacja/krakow/" title="Motoryzacja Kraków" class="link gray2 tunder">
            <span>Motoryzacja Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/krakow/" title="Nieruchomości Kraków" class="link gray2 tunder">
            <span>Nieruchomości Kraków</span>
        </a>,                                                                <a href="http://olx.pl/praca/krakow/" title="Praca Kraków" class="link gray2 tunder">
            <span>Praca Kraków</span>
        </a>,                                                                <a href="http://olx.pl/dom-ogrod/krakow/" title="Dom i Ogród Kraków" class="link gray2 tunder">
            <span>Dom i Ogród Kraków</span>
        </a>,                                                                <a href="http://olx.pl/elektronika/krakow/" title="Elektronika Kraków" class="link gray2 tunder">
            <span>Elektronika Kraków</span>
        </a>,                                                                <a href="http://olx.pl/moda/krakow/" title="Moda Kraków" class="link gray2 tunder">
            <span>Moda Kraków</span>
        </a>,                                                                <a href="http://olx.pl/rolnictwo/krakow/" title="Rolnictwo Kraków" class="link gray2 tunder">
            <span>Rolnictwo Kraków</span>
        </a>,                                                                <a href="http://olx.pl/zwierzeta/krakow/" title="Zwierzęta Kraków" class="link gray2 tunder">
            <span>Zwierzęta Kraków</span>
        </a>,                                                                <a href="http://olx.pl/dla-dzieci/krakow/" title="Dla Dzieci Kraków" class="link gray2 tunder">
            <span>Dla Dzieci Kraków</span>
        </a>,                                                                <a href="http://olx.pl/sport-hobby/krakow/" title="Sport i Hobby Kraków" class="link gray2 tunder">
            <span>Sport i Hobby Kraków</span>
        </a>,                                                                <a href="http://olx.pl/muzyka-edukacja/krakow/" title="Muzyka i Edukacja Kraków" class="link gray2 tunder">
            <span>Muzyka i Edukacja Kraków</span>
        </a>,                                                                <a href="http://olx.pl/uslugi-firmy/krakow/" title="Usługi i Firmy Kraków" class="link gray2 tunder">
            <span>Usługi i Firmy Kraków</span>
        </a>,                                                                <a href="http://olx.pl/oddam-za-darmo/krakow/" title="Oddam za darmo Kraków" class="link gray2 tunder">
            <span>Oddam za darmo Kraków</span>
        </a>,                                                                <a href="http://olx.pl/zamienie/krakow/" title="Zamienię Kraków" class="link gray2 tunder">
            <span>Zamienię Kraków</span>
        </a>                                    </div>
                <div id="linksCat3Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie podobne do "Nieruchomości" Kraków:</h3>
                                                <a href="http://olx.pl/nieruchomosci/mieszkania/krakow/" title="Mieszkania Kraków" class="link gray2 tunder">
            <span>Mieszkania Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/domy/krakow/" title="Domy Kraków" class="link gray2 tunder">
            <span>Domy Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/dzialki/krakow/" title="Działki Kraków" class="link gray2 tunder">
            <span>Działki Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/biura-lokale/krakow/" title="Biura i Lokale Kraków" class="link gray2 tunder">
            <span>Biura i Lokale Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/garaze-parkingi/krakow/" title="Garaże i Parkingi Kraków" class="link gray2 tunder">
            <span>Garaże i Parkingi Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/noclegi/krakow/" title="Noclegi Kraków" class="link gray2 tunder">
            <span>Noclegi Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/stancje-pokoje/krakow/" title="Stancje i Pokoje Kraków" class="link gray2 tunder">
            <span>Stancje i Pokoje Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/hale-magazyny/krakow/" title="Hale i Magazyny Kraków" class="link gray2 tunder">
            <span>Hale i Magazyny Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/pozostale-nieruchomosci/krakow/" title="Pozostałe nieruchomości Kraków" class="link gray2 tunder">
            <span>Pozostałe nieruchomości Kraków</span>
        </a>                                    </div>
                <div id="linksCat1307Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie podobne do "Mieszkania" Kraków:</h3>
                                                <span class="c73">Wynajem Kraków</span>,                                                                <a href="http://olx.pl/nieruchomosci/mieszkania/sprzedaz/krakow/" title="Sprzedaż Kraków" class="link gray2 tunder">
            <span>Sprzedaż Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/mieszkania/zamiana/krakow/" title="Zamiana Kraków" class="link gray2 tunder">
            <span>Zamiana Kraków</span>
        </a>                                    </div>
    </div>
                    <div id="locationLinks">
                <div class="static clr lheight16 c73 brbott-1 pding15_0">
                    <ul class="breadcrumb">
                                                    <li class="inline nowrap">
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/q-ruczaj/"><span>Polska</span></a>
                            </li>
                                                    <li class="inline nowrap">
                                                                    <span class="slash">&raquo;</span>
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/malopolskie/q-ruczaj/"><span>Małopolskie</span></a>
                            </li>
                                                    <li class="inline nowrap">
                                                                    <span class="slash">&raquo;</span>
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/"><span>Kraków</span></a>
                            </li>
                                            </ul>
                    <div class="locationlinks margintop10">
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=261"><span>Dębniki</span></a>&nbsp;(99)</li>
                                                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=279"><span>Grzegórzki</span></a>&nbsp;(1)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=263"><span>Podgórze</span></a>&nbsp;(13)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=265"><span>Łagiewniki-Borek Fałęcki</span></a>&nbsp;(9)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=255"><span>Krowodrza</span></a>&nbsp;(3)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bdistrict_id%5D=273"><span>Stare Miasto</span></a>&nbsp;(2)</li>
                                                                                    </ul>
                    </div>
                                    </div>
            </div>
                <div id="categoryLinksSuggestions" class="small lheight16 pding15_0">
        <p class="c73">Mieszkania do wynajęcia na OLX.pl (dawniej Tablica.pl) Kraków, oferty bezpośrednie i od agencji nieruchomości. Mieszkanie wynajmę Kraków - sprawdź nasze ogłoszenia.</p>
    </div>    </div>
</div>
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
            <a href="http://pomoc.olx.pl" class="link gray" title="Pomoc">
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
            <a href="http://olx.pl/zasady/" class="link gray inlblk rel" title="Regulamin OLX.pl">
                <span>Regulamin OLX.pl</span>
                            </a>
        </li>
                    <li>
                <a href="http://s7.olx.pl/static/olxpl/external/olxpl/pdf/cennik_reklam_OLX.pdf" class="link gray" title="Cennik reklam">
                    <span>Cennik reklam</span>
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
                <a href="http://olx.pl/nieruchomosci/krakow/popularne/" class="link gray" title="Popularne wyszukiwania w Nieruchomości">
                    <span>Popularne wyszukiwania w Nieruchomości</span>
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
    <a href="https://play.google.com/store/apps/details?id=pl.tablica&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" id="footerAppAndroid" target="_blank" class="inlblk">
        <span class="icon block googleplay"> w Google Play</span>
        <span class="tag-line tleft hidden">
            Do pobrania w            <strong class="block">Google Play</strong>
        </span>
    </a>
    <a href="https://itunes.apple.com/pl/app/olx.pl-darmowe-og-oszenia/id531717763?l=pl&ls=1&mt=8" id="footerAppIphone" target="_blank" class="inlblk">
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
                    <span class="icon fleft flag olxbg">&nbsp;</span><span>OLX.bg</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://olx.ro" target="_blank" class="link gray">
                    <span class="icon fleft flag olxro">&nbsp;</span><span>OLX.ro</span>
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
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'AppStore']);" class="inlblk icon appstore" href="https://itunes.apple.com/pl/app/olx.pl-darmowe-og-oszenia/id531717763?l=pl&ls=1&mt=8" target="_blank">OLX.pl AppStore</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'GooglePlay']);" class="inlblk icon googleplay" href="https://play.google.com/store/apps/details?id=pl.tablica&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" target="_blank">OLX.pl GooglePlay</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'WindowsStore']);" class="inlblk icon windowsstore" href="http://www.windowsphone.com/pl-pl/store/app/olx-pl/cfb57b0c-bc3e-4d00-9373-fa351f8c5f0c" target="_blank">OLX.pl WindowsStore</a>
        </div>
    </div>
</div>
</div>                    
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
    xtcustom = {"page_name":"listing","keyword":"ruczaj","page_nb":"1","provinces":"malopolskie","cities":"krakow","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","user_status":"unlogged_user"};
    //-->
</script>
<noscript>
    <img width="1" height="1" alt="" src="http://LOGC269.xiti.com/hit.xiti?s=507462&stc={"page_name":"listing","keyword":"ruczaj","page_nb":"1","provinces":"malopolskie","cities":"krakow","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","user_status":"unlogged_user"}" >
</noscript>
                                    <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/packed/sw1320019e5ecaacfb81789395e9b12bab.js"></script>
                                                <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/packed/sw262e3acc54ab15d86d656bf5dfe6c736.js"></script>
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
                    <script type="text/javascript" charset="utf-8">
              (function(G,o,O,g,L,e){G[g]=G[g]||function(){(G[g]['q']=G[g]['q']||[]).push(
              arguments)},G[g]['t']=1*new Date;L=o.createElement(O),e=o.getElementsByTagName(
              O)[0];L.async=1;L.src='//www.google.com/adsense/search/async-ads.js';
              e.parentNode.insertBefore(L,e)})(window,document,'script','_googCsa');
            </script>
                                <script type="text/javascript">
        function loadAdocean(ajax) {
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
                    
                    if (ajax)
                    {
                        var keys = [];
                        var cat = [];
                        if (categoryCode != rootCategoryCode){
                            cat=['cat:'+categoryCode,'cat:'+rootCategoryCode];
                            if (category_id != second_category_id && second_category_code != undefined)
                            {
                                cat.push('cat:'+second_category_code);
                            }
                        } else {
                            cat=['cat:'+categoryCode];
                        }
                        
                        if (regionCode != '') {
                            cat.push('region:'+regionCode);
                        } else {
                            cat.push('region:none');
                        }
                        if (cityCode != '') {
                            cat.push('city:'+cityCode);
                        } else {
                            cat.push('city:none');
                        }
                        for (var i=0; i < AdoVars['master']['keys'].length;i++)
                        {   
                            //str.indexOf
                            if (AdoVars['master']['keys'][i].indexOf('cat:')== -1 && AdoVars['master']['keys'][i].indexOf('city:')== -1 && AdoVars['master']['keys'][i].indexOf('region:')== -1)
                            {
                                keys.push(AdoVars['master']['keys'][i]);
                            }
                        }
                        AdoVars['master']['keys'] = keys.concat(cat);
                        
                        
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
<!-- tablica-dc4-110 -->
    
"""

# second SEARCH_RESULT_PAGE with 3 prepared offer urls
SEARCH_RESULT_PAGE2 = u"""
    <!DOCTYPE html>
<html xmlns:og="http://ogp.me/ns#" xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl) - strona 2</title>
                    <link rel="prev" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />
                            <link rel="next" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=3" />
                <meta name="robots" content="index, follow" />        <link rel="canonical" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />        <link rel="alternate" media="handheld" href="http://olx.pl/m/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />
<link rel="alternate" media="only screen and (max-width: 640px)" href="http://olx.pl/i2/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />
<link rel="alternate" href="android-app://pl.tablica/http/olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/" />        <meta http-equiv="Content-Language" content="pl" />
        <meta name="description" content="Ruczaj w Kraków najnowsze ogłoszenia na OLX.pl (dawniej Tablica.pl) w Kraków" />
                            <meta property="og:title" content="Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl) - strona 2"/>
                    <meta property="og:description" content="Ruczaj w Kraków najnowsze ogłoszenia na OLX.pl (dawniej Tablica.pl) w Kraków"/>
                    <meta property="og:url" content="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2"/>
                    <meta property="fb:app_id" content="121167521293285"/>
                    <meta property="og:image" content="http://s7.olx.pl/static/olxpl/external/olxpl/img/fb/fb-image200x200.png?t=15-06-26"/>
                    <meta property="og:type" content="website"/>
                    <meta property="og:site_name" content="OLX.pl (dawniej Tablica.pl)"/>
                            <link rel="icon" type="image/x-icon" href="http://s8.olx.pl/static/olxpl/external/olxpl/img/favicon.ico?v=3">
                                    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/rss/q-ruczaj/" />
                                                        <script type="text/javascript">
                    var _adblock = true;
            </script>
            <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/external/base/js/advertising.js"></script>
                                                                                                <link rel="stylesheet" type="text/css" href="http://s7.olx.pl/static/olxpl/packed/sweb45af5fa50c07d56be5994ade79367a.css">
                                                                                                        <!--[if lte IE 8]>                        <link rel="stylesheet" type="text/css" href="http://s7.olx.pl/static/olxpl/packed/sw219069a4faf339926afcad6163516c59.css">
                    <![endif]-->                                                        <script type="text/javascript">
                window.suggestmeyes_loaded = true;
                                        var action='ads';
                                        var method='index';
                                        var user_logged=0;
                                        var www_base='http://olx.pl/krakow';
                                        var www_base_no_namespace='http://olx.pl/krakow';
                                        var www_base_ajax='http://olx.pl/ajax/krakow';
                                        var static_files_www_base='http://s7.olx.pl/static/olxpl/';
                                        var external_static_files_www_base='http://s8.olx.pl/static/olxpl/external/olxpl/';
                                        var session_domain='olx.pl';
                                        var decimal_separator=',';
                                        var thousands_separator=' ';
                                        var sitecode='olxpl';
                                        var defaultCurrency='PLN';
                                        var config_currency='zł';
                                        var useExternalScripts=1;
                                        var lang='pl';
                                        var hasRwd=0;
                                        var module_store_image_sizes_db=1;
                                        var module_store_image_sizes=1;
                                        var module_new_design=1;
                                        var module_paidads=1;
                                        var module_facebook_login=1;
                                        var module_gg_integration=1;
                                        var module_mms_images=1;
                                        var module_sms_notification=1;
                                        var module_mobile_app=1;
                                        var module_otokredyt=1;
                                        var module_invoiceform=1;
                                        var module_paid_limits=1;
                                        var module_connection_port=1;
                                        var module_multiacc=1;
                                        var module_fraud_detection=1;
                                        var module_dogs=1;
                                        var module_googleplus=1;
                                        var module_trusted_changes=1;
                                        var module_kredyt_hipoteczny=1;
                                        var module_einvoice_olxpl=1;
                                        var module_comperiabox=1;
                                        var module_payupl_response=1;
                                        var module_payupl_bank_accounts=1;
                                        var module_controlpanel2=1;
                                        var module_i2_payment=1;
                                        var module_pdlaenau=1;
                                        var module_zendesk_schedule=1;
                                        var module_hashtags=1;
                                        var module_answers_filters_fraud=1;
                                        var module_fraud_contact_data=1;
                                        var module_refactorized_stats=1;
                                        var module_fraud_detector_queue=1;
                                        var module_paid_for_post=1;
                                        var module_category_change_with_pay_to_post_ad=1;
                                        var module_adding_refactor=1;
                                        var module_automotive_supiscious_parameters=1;
                                        var module_at_addingform_track=1;
                                        var module_m_promote=1;
                                        var module_invoice_exporter=1;
                                        var module_einvoice_ap_poland=1;
                                        var module_rest_api=1;
                                        var module_old_payment_tables=1;
                                        var module_redis_hash=1;
                                        var module_js_stacktrace=1;
                                        var module_hermes_migration=1;
                                        var module_hermes_history=1;
                                        var module_prevent_fraud_stats=1;
                                        var module_history_extra_info_alter=1;
                                        var module_solr_cloud=1;
                                        var module_solr_improvement=1;
                                        var region_id='4';
                                        var regionName="Ma\u0142opolskie";
                                        var subregion_id='102';
                                        var subregionName="Krak\u00f3w";
                                        var category_id='15';
                                        var is_search_category='';
                                        var categoryName="Wynajem";
                                        var categoryCode="wynajem";
                                        var categoryAdsenseText=null;
                                        var root_category_id='3';
                                        var second_category_id='1307';
                                        var second_category_code="mieszkania";
                                        var rootCategoryName="Nieruchomo\u015bci";
                                        var rootCategoryCode="nieruchomosci";
                                        var rootCategoryAdsenseText=null;
                                        var setSeoPageName="Mieszkania wynajm\u0119, mieszkania na wynajem Krak\u00f3w";
                                        var q="ruczaj";
                                        var city_id='8959';
                                        var regionCode='malopolskie';
                                        var cityCode='krakow';
                                        var is_archive='';
                                        var geoData={"category":"15","locationName":"Krak\u00f3w, Ma\u0142opolskie","region":"4","params":{"page":"2","q":"ruczaj"}};
                                        var geoAjaxGet='http://olx.pl/ajax/krakow/geo/get/';
                                        var geoAjaxClose='http://olx.pl/ajax/krakow/geo/close/';
                                        var isSearch='1';
                                        var saveFavLink="http://olx.pl/konto/?origin=observepopup&ref%5B0%5D%5Baction%5D=ads&ref%5B0%5D%5Bmethod%5D=index&ref%5B0%5D%5Bparams%5D%5Bpage%5D=2&ref%5B0%5D%5Bparams%5D%5Bq%5D=ruczaj&ref%5B0%5D%5Bcategory%5D=15&ref%5B0%5D%5Bregion%5D=4&ref%5B0%5D%5Bsubregion%5D=102&ref%5B0%5D%5Bcity%5D=8959";
                                        var xtClickCategoryID='9';
                                        var totalAds='131';
                                        var isUserSearch='';
                                        var categoriesStats={"1307":"294","3":"214","0":"206","15":"131","11":"43","4":"33","124":"30","619":"23","711":"22","751":"18","710":"16","14":"16","1313":"15","130":"12","333":"11","1435":"9","127":"8","368":"8","64":"6","443":"6","1437":"5","297":"5","625":"4","82":"4","1449":"3","306":"3","1213":"3","1209":"3","321":"3","99":"3","1399":"2","522":"2","65":"2","62":"2","1309":"2","767":"2","453":"2","5":"2","1159":"1","628":"1","329":"1","88":"1","461":"1","230":"1","164":"1","100":"1","53":"1","282":"1","523":"1","324":"1","20":"1","1421":"1","326":"1"};
                                        var gemius_identifier=new String('ApI65iOBi_V74WSAbF.5DNUoDmwZEdr0JULbeXtukR7.Y7');
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
            <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/js/scripts/html5shiv.min.js"></script>
        <![endif]-->
        <link href="https://plus.google.com/113406265199615974663" rel="publisher" />
            <!-- Criteo cookie -->
        <script type="text/javascript">
        function crtg_getCookie(c_name){ var i,x,y,ARRCookies=document.cookie.split(";");for(i=0;i<ARRCookies.length;i++){x=ARRCookies[i].substr(0,ARRCookies[i].indexOf("="));y=ARRCookies[i].substr(ARRCookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);} }return'';} var crtg_content = crtg_getCookie('crtg_rta');    (function(){var crtg_nid = '2859';var crtg_cookiename = 'crtg_rta';var crtg_varname = 'crtg_content';var crtg_url=location.protocol+'//rtax.criteo.com/delivery/rta/rta.js?netId='+escape(crtg_nid)+'&cookieName='+escape(crtg_cookiename)+'&rnd='+Math.floor(Math.random()*99999999999)+'&varName=' + escape(crtg_varname);var crtg_script=document.createElement('script');crtg_script.type='text/javascript';crtg_script.src=crtg_url;crtg_script.async=true;if(document.getElementsByTagName("head").length>0)document.getElementsByTagName("head")[0].appendChild(crtg_script);else if(document.getElementsByTagName("body").length>0)document.getElementsByTagName("body")[0].appendChild(crtg_script);})();
        var AdoVars = [];
                        AdoVars['master'] = {
                id: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
                server: 'gg.adocean.pl',
                characterEncoding: true,
                keys: ['region:malopolskie','city:krakow' ,'cat:nieruchomosci' ,'cat:mieszkania' ,'cat:wynajem', 'ruczaj']
                                };
                                </script>
        
        </head>
    <body class="offersview standard">
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
<!-- End Google Tag Manager -->                        <div id="innerLayout">
    
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
    <div id="searchbox">
    <div class="wrapper">
        <form method="POST" action="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/" class="search clr" id="mainTopSearch">
            <a href="http://olx.pl" class="abs icon website hidden">OLX.pl (dawniej Tablica.pl)</a>
                        <input type="hidden" name="view" value="" />
                        <input type="hidden" name="min_id" value="" />
                        <fieldset>
                <div class="clr rel pdingbott5" id="withshowbox">
                    <noindex>
                    <table width="100%" cellpadding="0" cellspacing="0" id="withshowboxTable">
                        <tr>
                            
<td valign="top" width="251">
    
<div class="clearbox clr rel">
    <input autocomplete="off" id="search-text" type="text"
           class="br3 light large fleft with-x-clear-button ca2 fbold autosuggest-input defaultval {suggesturl: 'http://olx.pl/ajax/nieruchomosci/mieszkania/wynajem/krakow/suggest/get/'}"
           name="q" value="ruczaj" defaultval="Szukaj..." style="margin: 0px;">
    <div id="autosuggest-div">
        <!-- via ajax -->
    </div>
    <a class="icon cleartext3 abs clear-input-button hidden" id="clearQ" href="#">X</a>
</div>

</td>
<td valign="top">
    
<div class="locationrequest smallBox has-dist-picker" id="locationBox">
    <div class="clr rel">
        <div class="rel fleft input-container">
                        <input id="cityField" autocomplete="off" type="text" defaultval="Cała Polska"
                defaultalternative="Miejscowość lub kod" value="Kraków" class="with-x-clear-button fleft defaultval light ca2 cityfield bold">
            <div class="cityfield" id="cityFieldGray">
                <span class="fbold vishid">Kraków</span><span class="color-9">, Małopolskie</span>
            </div>
            <a href="#" class="icon cleartext3 abs clear-input-button ">X</a>
            <div class="distanceseparator abs"></div>
            <label class="icon locmarker2 abs" for="cityField">&nbsp;</label>
            <div class="proposals hidden" id="proposalContainer">
                <div class="lastbox">
                    <p>Ostatnio wybrane:</p>
                    <ul id="last-locations-ul">
                    </ul>
                </div>
                <div class="abs categorySelectContainer">
                    <ul class="categorySelectList regionsList">
                        <!-- utaj umiescic -->
                    </ul>
                </div>
            </div>
            <input class="autosuggest-geo-input" type="hidden" name="search[city_id]" value="8959" />
            <input class="autosuggest-geo-input-region" type="hidden" name="search[region_id]" value="4" />
            <input class="autosuggest-geo-district-input" type="hidden" name="search[district_id]" value="0" />
            
                            <input class="autosuggest-geo-dist-input" type="hidden" name="search[dist]" value="0" />
                        
            <div class="autosuggest-geo-div suggestmain">
                <!-- via ajax -->
            </div>
            <div id="geo-suggestions" class="chooselocation br3 hidden">
                <div class="icon target abs"></div>
                <a id="geo-suggestions-close" href="#" class="close icon abs">X</a>
                <p>Wybierz lokalizację:</p>
                <div id="geo-suggestions-options" class="items"></div>
            </div>
        </div>
                    <dl class="distancelist fleft bold " id="distanceSelect">
                                <dt>
                    <a href="#" class="topLink">
                        <span class="label">+ 0 km</span>
                        <span class="value">0</span>
                    </a>
                </dt>
                <dd>
                    <ul style="display: none;">
                                                <li class="">
                            <a href="#" class="dist">+ 0 km<span class="value">0</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 5 km<span class="value">5</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 10 km<span class="value">10</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 15 km<span class="value">15</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 30 km<span class="value">30</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 50 km<span class="value">50</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 75 km<span class="value">75</span>
                            </a>
                        </li>
                                                <li class="">
                            <a href="#" class="dist">+ 100 km<span class="value">100</span>
                            </a>
                        </li>
                                            </ul>
                </dd>
            </dl>
            </div>
        <p id="cityFieldError" class="margintop3 small lheight16 marginbott-5" style="display: none;">Niepoprawne miasto lub kod pocztowy</p>
    </div>
</td>

                            <td valign="top" width="150">
                                <div class="rel combospace">
    <a href="" class="block select fbold a-category-3 rel nowrap tdnone overh" id="choosecat">
        <span class="icon caticongray abs">&nbsp;</span>
        <span class="block overh">
                                                 <span id="main-category-choose-label" class="c000">Mieszkania</span>
                                    </span>
    </a>
    <div class="abs categorySelectContainer">
        <ul class="categorySelectList" id="categorySelectList" style="display: none;"></ul>
    </div>
</div>
                            </td>
                        </tr>
                    </table>
                    </noindex>
                </div>
            </fieldset>
            <noindex>
            <fieldset id="paramsListOpt">
                <div class="checkboxsepa clr">
                    <div class="fblock fleft">
                        <input  type="checkbox" id="title-desc" class=" checkbox {renderformClass: 'fleft marginright5 '}"
                                name="search[description]" value="1"> <label class=" small" for="title-desc">szukaj również w opisach</label>
                    </div>
                    <div class="fblock fleft">
                        <input  type="checkbox" id="photo-only" class="checkbox {renderformClass: 'fleft marginright5'}"
                            name="search[photos]" value="1" /> <label class="small" for="photo-only">tylko ze zdjęciem</label>
                    </div>
                                    </div>
            </fieldset>
               <fieldset class="paramsList rel clr" id="paramsList">
    <ul class="clr multifilters subSelectActive">
                <li class="grid-li">
            <ul class="grid-ul grid-1" id="param-grid-1">
                                                                                                                                                            
<li class="subcategory" id="param_subcat">
    <div class="filter-item rel category-item">
        <div class="subSelect hidden abs zi2" id="">
            Wybierz kategorię        </div>
        <a href="javascript:void(0);" class="button gray block category rel zi3 clr fbold">
                        <span class="3rd-category-choose-label header block" data-default-label="Wynajem">
                Wynajem            </span> 
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs hidden subcategories">
            <li class="clr brbottdash-2">
                <a id="all-categories" class="tdnone block value c000 category-choose search-choose {name: 'search[category_id]', value: '1307'}" href="#">Wszystkie</a>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<li class="param paramSelect " data-name="search[filter_enum_rooms][]" data-key="rooms" data-param-id="165" id="param_rooms">
    <div class="filter-item rel filter-item-rooms">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Liczba pokoi">Liczba pokoi</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_rooms_25">
                    <input maxlength="13" id="f-all-filter_enum_rooms_25" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                
<li class="param paramSelect " data-name="search[filter_enum_builttype][]" data-key="builttype" data-param-id="157" id="param_builttype">
    <div class="filter-item rel filter-item-builttype">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Rodzaj zabudowy">Rodzaj zabudowy</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_builttype_27">
                    <input maxlength="13" id="f-all-filter_enum_builttype_27" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-2" id="param-grid-2">
                                                                                
<li class="param paramFloat " data-name="search[filter_float_price][]" data-key="price" data-param-id="1" id="param_price">
    <div class="filter-both-item">
                    <div class="filter-item filter-item-from rel numeric-item price ">
            <a href="javascript:void(0);" class="button button-from numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Cena od">
                    Cena od                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="13" value="" type="text" class="defaultval {name: 'search[filter_float_price:from]'} small vtop min-value-input from" defaultval="od..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="zł"></ul>
        </div>
                    <div class="filter-item filter-item-to rel numeric-item price ">
            <a href="javascript:void(0);" class="button button-to numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Cena do">
                    Cena do                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="13" value="" type="text" class="defaultval {name: 'search[filter_float_price:to]'} small vtop max-value-input to" defaultval="do..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="zł"></ul>
        </div>
            </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-3" id="param-grid-3">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<li class="param paramFloat " data-name="search[filter_float_m][]" data-key="m" data-param-id="163" id="param_m">
    <div class="filter-both-item">
                    <div class="filter-item filter-item-from rel numeric-item  ">
            <a href="javascript:void(0);" class="button button-from numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Pow. od">
                    Pow. od                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="8" value="" type="text" class="defaultval {name: 'search[filter_float_m:from]'} small vtop min-value-input from" defaultval="od..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="m<sup>2</sup>"></ul>
        </div>
                    <div class="filter-item filter-item-to rel numeric-item  ">
            <a href="javascript:void(0);" class="button button-to numeric gray block fnormal rel zi3 clr">
                <span class="header block" data-default-label="Pow. do">
                    Pow. do                </span>
                <span class="icon down abs"></span>
            </a>
            <label class="num-input block rel hidden">
                <input maxlength="8" value="" type="text" class="defaultval {name: 'search[filter_float_m:to]'} small vtop max-value-input to" defaultval="do..." />
            </label>
                <ul class="small suggestinput numeric-suggest bgfff lheight20 br-3 abs range hidden" data-unit="m<sup>2</sup>"></ul>
        </div>
            </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-4" id="param-grid-4">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<li class="param paramSelect " data-name="search[filter_enum_floor_select][]" data-key="floor_select" data-param-id="151" id="param_floor_select">
    <div class="filter-item rel filter-item-floor_select">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Poziom">Poziom</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_floor_select_22">
                    <input maxlength="13" id="f-all-filter_enum_floor_select_22" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                
<li class="param paramSelect " data-name="search[filter_enum_furniture][]" data-key="furniture" data-param-id="155" id="param_furniture">
    <div class="filter-item rel filter-item-furniture">
        <a href="javascript:void(0);" class="button gray block fnormal rel zi3 clr">
            <span class="header block" data-default-label="Umeblowane">Umeblowane</span>
            <span class="icon down abs"></span>
        </a>
        <ul class="small suggestinput bgfff lheight20 br-3 abs select hidden">
            <li class="clr brbottdash-2">
                <label class="block value c000 lheight18" for="f-all-filter_enum_furniture_24">
                    <input maxlength="13" id="f-all-filter_enum_furniture_24" type="checkbox" class="inlblk all-checkbox {renderformClass: 'inlblk vtop margintop3 marginright5'}" />Wszystkie                </label>
            </li>
        </ul>
    </div>
</li>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-5" id="param-grid-5">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                <li class="line"></li>
                    <li class="grid-li">
            <ul class="grid-ul grid-6" id="param-grid-6">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-7" id="param-grid-7">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-8" id="param-grid-8">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-9" id="param-grid-9">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                    <li class="grid-li">
            <ul class="grid-ul grid-10" id="param-grid-10">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            </ul>
        </li>
                </ul>
</fieldset>
<fieldset class="clr " id="searchList">
    <div class="checkboxsepa small">
        <div class="fblock fright">
            <a id="clear-params" href="#" class="fleft option-search-clear tdnone hidden">
                <span class="icon block fleft cleartext6"></span>
                <span class="pdingleft5 link hn">
                    <span>Wyczyść filtry</span>
                </span>
            </a>
            <div class="fblock fleft option-search-criteria">
                <a href="#" class="tdnone inlblk selected" id="cancelSearchCriteriaTop" style="display: none" title="Usuń z obserwowanych">
                    <span class="icon favsearch2 inlblk vtop"></span>
                    <span class="link hn">
                        <span>Usuń z obserwowanych</span>
                    </span>
                </a>
                <a href="#" class="tdnone inlblk rel normal" id="saveSearchCriteriaTop" title="Obserwuj wyszukiwanie">
                    <span class="icon favsearch2 inlblk vtop"></span>
                    <span class="link hn">
                        <span>Obserwuj wyszukiwanie</span>
                    </span>
                </a>
            </div>
            <div class="fleft rel option-search-submit">
                <span class="button search submit normal zi3 inlblk marginleft7 circleshadow active ">
                    <span class="icon inlblk vtop margintop6 marginleft10 b_search2">&nbsp;</span>
                    <input type="submit" class="margintop-1 cfff {clickerID:'search_loop'} tiptip" id="search-submit" value="Szukaj">
                </span>
            </div>
        </div>
    </div>
</fieldset>

            </noindex>
            <input type="hidden" name="search[category_id]" id="searchFormCatID" value="15" />
        </form>
    </div>
</div>
<a name="ending-search-ads"></a></header>    
<div id="listContainer">
    <div id="tabs-container">
    <div class="wrapper clr">
        
<div class="view-lists">
        <ul class="order-select-gallery" id="order-select-gallery">
        <li class="list-label">
            Sortuj:
        </li>
        <li>
            <a href="#" class="link selected" data-type="created_at:desc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Border%5D=created_at%3Adesc"><span>Najnowsze</span></a>
        </li>
                                    <li>
                    <a href="#" class="link " data-type="filter_float_price:asc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Border%5D=filter_float_price%3Aasc"><span>Najtańsze</span></a>
                </li>
                                        <li>
                    <a href="#" class="link " data-type="filter_float_price:desc" data-url="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Border%5D=filter_float_price%3Adesc"><span>Najdroższe</span></a>
                </li>
                        </ul>
            <ul class="view" id="viewSelector">
        <li class="list-label">Widok:</li>
                <li>
                            <span>Lista</span>
                    </li>
                <li>
                            <a class="topTabView link" data-type="galleryWide" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&view=galleryWide" rel="nofollow"><span>Galeria</span></a>
                    </li>
            </ul>
        </div>

                                                <ul class="tabs offerseek clr large fleft tohide rel zi3">
                                                                                        <li class="fleft">
                                                            <span class="fleft tab selected"> <span class="fbold">Wszystkie</span>
                                                                            <span class="color-2 normal indexed-int">131</span>
                                                                    </span>
                                                    </li>
                                                                                            <li class="fleft">
                                                                                                <a class="fleft tab tdnone topTabOffer" data-type="private" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bprivate_business%5D=private">
                                        <span class="fbold link"><span>Prywatne</span></span> <span class="color-2 normal indexed-int">54</span>
                                    </a>
                                                                                    </li>
                                                                                            <li class="fleft">
                                                                                                <a class="fleft tab tdnone topTabOffer" data-type="business" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bprivate_business%5D=business">
                                        <span class="fbold link"><span>Agencje</span></span> <span class="color-2 normal indexed-int">77</span>
                                    </a>
                                                                                    </li>
                                                            </ul>
                        </div>
</div>    

    
                    <div id="adoceanggmpohhkfufu"></div>
    <script type="text/javascript">
    /* (c)AdOcean 2003-2015, GaduGadu.Tablica.pl (olx.pl).Listings.screening */
    (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggmpohhkfufu'] = {
        myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
    };
    setTimeout(function(){
        typeof window.ads.initScreening == 'function' && window.ads.initScreening();
    }, 2500);
    </script>
 
    <section id="body-container" class="container" data-facets='{"offer_seek":{"offer":131},"private_business":{"business":77,"private":54,"all":131},"categories":{"1307":294,"3":214,"0":206,"15":131,"11":43,"4":33,"124":30,"619":23,"711":22,"751":18,"710":16,"14":16,"1313":15,"130":12,"333":11,"1435":9,"127":8,"368":8,"64":6,"443":6,"1437":5,"297":5,"625":4,"82":4,"1449":3,"306":3,"1213":3,"1209":3,"321":3,"99":3,"1399":2,"522":2,"65":2,"62":2,"1309":2,"767":2,"453":2,"5":2,"1159":1,"628":1,"329":1,"88":1,"461":1,"230":1,"164":1,"100":1,"53":1,"282":1,"523":1,"324":1,"20":1,"1421":1,"326":1},"categoriesParent":[]}' data-showfacets="1" data-pagetitle="Ruczaj - Wynajem w Kraków - OLX.pl (dawniej Tablica.pl) - strona 2" data-ajaxurl="" data-searchid="">
        <div class="wrapper">
            <div class="content">
                
    <div class="clr offersnav rel margin0_10">
        <div class="pdingtop6"><ul class="breadcrumb offerslist clr marginbott5 small xxxx">
        <li class="marginright7 abs homelink">
        <a href="http://olx.pl" class="tdnone">
            <span class="icon inlblk home"></span>
                    </a>
        <span class="slash">&raquo;</span>
    </li>
                            <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Kraków</span>
                </a>
            </li>
                                <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Nieruchomości</span>
                </a>
            </li>
                                <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/mieszkania/krakow/" class="link" itemprop="url">
                    <span itemprop="title">...</span>
                </a>
            </li>
                                <li class="inline" itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
                    <span class="slash">&raquo;</span>
                        <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/" class="link" itemprop="url">
                    <span itemprop="title">Wynajem</span>
                </a>
            </li>
                                <li class="inline selected">
                    <span class="slash">&raquo;</span>
                    <h1 class="small fnormal inline lheight18">Mieszkania wynajmę, mieszkania na wynajem Kraków - OLX.pl - ruczaj</h1>
            </li>
            </ul>
</div>
            </div>
<div id="topmessages"></div>

                                                
<div class="clr tcenter">
    <div class="rel billboard750x100 overh zi2" id="billboard750x100">
        <div id="adoceanggppioipntwd"></div>
    </div>
    <script type="text/javascript">
        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggppioipntwd'] = {
            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
        };
    </script>
</div>

                                <div class="rel listHandler ">
                    
        <div class="rel zi3">
        <div class="abs rightBranding">
            <div id="skycraper" style="top:0px">
                <div class="skyflex rel">
                    <div class="abs deco" id="skyflexdeco" style="display:none;"></div>
                    <div id="adoceanggtchrmukrtx" class="box"></div>
                    <script type="text/javascript">
                        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggtchrmukrtx'] = {
                            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
                            onServerEmission: function(){
                                document.getElementById('skyflexdeco').style.display = 'block';
                            }};
                    </script>
                </div>
            </div>
        </div>
    </div>
    
                                            


<table width="100%" cellspacing="0" cellpadding="0" class="fixed offers breakword" summary="">
    <caption></caption>
    <tbody>
        <tr>
            <td>
                <div class="section clr">
                    <h2>Wyróżnione ogłoszenia</h2>
                    <a href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?search%5Bpaidads_listing%5D=1" class="link">
                        <span>Zobacz wszystkie</span>
                    </a>
                </div>
            </td>
        </tr>
        
<div id="adoceanggvgrringnqx"></div>
<script type="text/javascript">
    (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggvgrringnqx'] = {
        myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7',
        onServerEmission: function(){
            document.getElementById('adoceanggvgrringnqx').style.margin = '10px 0';
        }
    };
</script>


                        
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword promoted-list ad_idaCXrT" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "
                            href="http://olx.pl/offer4" title="">
                                                        <img class="fleft" src="http://img19.staticclassifieds.com/images_tablicapl/267144981_3_261x203_3-poknowe-mieszkanie-ruczaj-wynajem_rev002.jpg" alt="3-Pok.NOWE Mieszkanie RUCZAJ">
                                                                                        <span class="inlblk icon paid type2 abs zi2" title="Ogłoszenie wyróżnione"></span>
                                                    </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/3-pok-nowe-mieszkanie-ruczaj-CID3-IDaCXrT.html#dd03f42874;promoted" class="marginright5 link linkWithHash detailsLinkPromoted">
                                    <strong>3-Pok.NOWE Mieszkanie RUCZAJ</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 000 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                22  cze                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:157048349} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-157048349">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>


                
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword promoted-list ad_idayvXn" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "
                            href="http://olx.pl/offer5" title="">
                                                        <img class="fleft" src="http://img19.staticclassifieds.com/images_tablicapl/265397489_5_261x203_mieszkanie-2-pokojowe-na-ul-chmieleniec-ruczaj-wynajem-malopolskie_rev012.jpg" alt="Mieszkanie 2 pokojowe na ul. Chmieleniec - Ruczaj - WYNAJEM">
                                                                                        <span class="inlblk icon paid type2 abs zi2" title="Ogłoszenie wyróżnione"></span>
                                                    </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/mieszkanie-2-pokojowe-na-ul-chmieleniec-ruczaj-wynajem-CID3-IDayvXn.html#dd03f42874;promoted" class="marginright5 link linkWithHash detailsLinkPromoted">
                                    <strong>Mieszkanie 2 pokojowe na ul. Chmieleniec - Ruczaj - WYNAJEM</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 400 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                17  cze                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:155993201} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-155993201">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>


                
    </tbody>
</table>
<style type="text/css">
.hasPromoted {
    display: block
}
.dontHasPromoted {
    display: none
}
</style>
                                                            

<table width="100%" cellspacing="0" cellpadding="0" id="offers_table" class="fixed offers breakword" summary="">
    <tbody>
        
<tr>
    <td>
                
<div class="hasPromoted section clr">
    <h2>Pozostałe ogłoszenia</h2>
    <p class="color-2">Znaleziono 131 ogłoszeń</p>
</div>

<div class="dontHasPromoted section clr rel">
        <h2>Znaleziono 131 ogłoszeń</h2>
    <p class="color-2">Twoje ogłoszenie na górze listy? <a href="http://olx.pl/krakow/platnosci/dlaczego-warto-promowac/" target="_blank" id="whyPromoteListLink" class="link"><span>Wyróżnij!</span></a></p>
    </div>

            </td>
</tr>

                     

            
<tr>
    <td class="offer ">
                <table width="100%" cellspacing="0" cellpadding="0" class="fixed breakword  ad_idaDUiB" summary="Ogłoszenie">
            <tbody>
                <tr>                    
                    <td width="168" rowspan="2">
                        <a
                            class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink "
                            href="http://olx.pl/offer6" title="">
                                                        <img class="fleft" src="http://img28.staticclassifieds.com/images_tablicapl/267548815_1_261x203_przytulna-kawalerka-na-osiedlu-pychowice-ruczaj-bezposrednio-krakow.jpg" alt="przytulna kawalerka na osiedlu Pychowice / Ruczaj - bezpośrednio">
                                                                                </a>
                    </td>
                                                            <td valign="top">
                        <div class="space rel">
                            <h3 class="x-large lheight20 margintop5">
                                                                <a href="http://olx.pl/oferta/przytulna-kawalerka-na-osiedlu-pychowice-ruczaj-bezposrednio-CID3-IDaDUiB.html#dd03f42874" class="marginright5 link linkWithHash detailsLink">
                                    <strong>przytulna kawalerka na osiedlu Pychowice / Ruczaj - bezpośrednio</strong>
                                </a>
                                
                            </h3>
                            <p class="color-9 lheight16 margintop5">
                                <small class="breadcrumb x-normal">
                                                                    Mieszkania » Wynajem
                                                                </small>
                            </p>
                        </div>
                    </td>
                    <td width="170" class="wwnormal tright td-price" valign="top">
                        <div class="space rel">
                                                    <p class="price">
                                <strong>1 000 zł</strong>
                            </p>
                                                                                                                                </div>
                    </td>
                </tr>
                <tr>
                    <td valign="bottom">
                        <div class="space rel">
                            <p class="color-9 lheight16 marginbott5">
                                <small class="breadcrumb x-normal">
                                    <span>Kraków</span>
                                </small>
                            </p>
                            <p class="color-9 lheight16 marginbott5 x-normal">
                                23  cze                            </p>
                        </div>
                    </td>
                    <td width="85" class="tright" valign="bottom">
                        <div class="space rel">
                                                        <div class="rel observelinkinfo inlblk zi3">
                                <a href="#" class="{id:157274569} observe-link inlblk lheight16 tdnone tcenter margintop5 vishid " data-statkey="ad.observed.list">
                                    <span class="icon inlblk observe2 observed-157274569">&nbsp;</span>
                                    <span class="link x-small gray2 block lheight14">
                                        <span>  </span>
                                    </span>
                                </a>
                                <div class="suggesttitleright small top abs zi2 br4 hidden">
                                    <p></p>
                                    <div class="target abs icon"></div>
                                </div>
                            </div>
                                                    </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>


                                 



                                 

    
<tr class="adcontainer-tr">
    <td class="offer">
        <table cellspacing="0" cellpadding="0" width="100%" class="fixed breakword" summary="Ogłoszenie">
            <tbody>
                <tr>
                    <td width="200" class="tcenter"></td>
                    <td width="1"></td>
                    <td>
                        <div id="adcontainer3"></div>
                    </td>
                    <td width="1" class="wwnormal tright"></td>
                    <td width="1" class="tright small"></td>
                </tr>
            </tbody>
        </table>
    </td>
</tr>

        
        

       </tbody>
</table>                                        

                                </div>
                <div class="pager rel clr">
            <span class="fbold prev abs large">
                <a class="link pageNextPrev {page:1}" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/">
            <span>&laquo; poprzednia</span>
        </a>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/">
            <span>1</span>
        </a>
            </span>
        <span class="item fleft">
                <span class="block br3 c41 large tdnone lheight24 current"> <span>2</span>
    </span>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=3">
            <span>3</span>
        </a>
            </span>
        <span class="item fleft">
                <a class="block br3 brc8 large tdnone lheight24" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=4">
            <span>4</span>
        </a>
            </span>
        <span class="fbold next abs large">
                <a class="link pageNextPrev {page:3}" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=3">
            <span>następna &raquo;</span>
        </a>
            </span>
    </div>                <div id="skycraperMax"></div>
                
    <div class="seo-suggestions brtop-1 large">
        <h4>Podobne wyszukiwania:</h4>
        <div class="columns">
            <ul class="column">
                                                        <li><a href="http://olx.pl/nieruchomosci/mieszkania/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Mieszkania</span></li>
                                                        <li><a href="http://olx.pl/nieruchomosci/stancje-pokoje/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Stancje i Pokoje</span></li>
                                                        <li><a href="http://olx.pl/nieruchomosci/garaze-parkingi/q-ruczaj/" class="link"><span>ruczaj</span></a> w kategorii <span class="fbold">Garaże i Parkingi</span></li>
                            </ul>
        </div>
    </div>

                

                                    
<div class="tcenter pding20_0 color-10 brtop-1 large favsearchbox" id="searchCriteriaSave">
    <div class="margintop15">
        <span class="lheight20 inlblk">Czy chcesz zapisać aktualne kryteria wyszukiwania?</span>
        <span id="saveSearchCriteriaLink" class="favsearchlink inlblk vtop rel cpointer">
            <span class="icon favsearch inlblk vtop" id="saveSearchCriteriaStar"></span>
        </span>
        <span class="link tdnone lheight35 inlblk cpointer fbold">
            <span id="saveSearchCriteria">Zapisz wyszukiwanie</span>
        </span>
        <span class="seeAllSaved">
            <span class="slash inlblk vmiddle margin0_10"></span> <a href="http://olx.pl/krakow/obserwowane/wyszukiwania/" class="link gray small">
                <span>Zobacz zapisane</span>
            </a>
        </span>
    </div>
</div>
<div class="tcenter pding20_0 color-10 brtop-1 large favsearchbox" id="searchCriteriaSaved" style="display: none">
    <div class="margintop15">
        <span class="lheight20 inlblk">Aktualne kryteria wyszukiwania są zapisane</span>
        <span id="cancelSearchCriteriaLink" class="favsearchlink inlblk vtop rel cpointer selected">
            <span class="icon favsearch inlblk vtop" id="cancelSearchCriteriaStar"></span>
        </span>
        <span class="link tdnone lheight35 inlblk cpointer fbold">
            <span id="cancelSearchCriteria">Usuń</span>
        </span>
        <span class="seeAllSaved">
            <span class="slash inlblk vmiddle margin0_10"></span>
            <a href="http://olx.pl/krakow/obserwowane/wyszukiwania/" class="link gray small">
                <span>Zobacz zapisane</span>
            </a>
        </span>
    </div>
</div>
<div id="searchCriteria" style="display: none">tFU/Mq7qJDo8bgnFJ3sl++EtOeu6LRgmWOhCfdDPEeAs0r4iNCMA4ZGgWQWBdAfjBSt6xEJ7EEflorRxfHkQD7ywxwF7jm2rqpc4TVvkX2+mcZX3AK/4HwyIH/4IMEUmSuStXRy/0BEEmv4Qt/jJwjKhIaKkCL88MzbCrPxqffs4VmySH5BmPEWHhJW0cUO9NJTyk/B2Ujt8XPRFIFY9dA==</div>


                                
<div class="clr tcenter margintop10">
    <div class="rel billboard750x200" id="billboard750x200" >
        <div id="adoceanggwbqkjxqmyc"></div>
    </div>
    <script type="text/javascript">
        (AdoVars['slave'] = AdoVars['slave'] || [])['adoceanggwbqkjxqmyc'] = {
            myMaster: 'BQ.xB.CSDKoJHrE7HNDWLlHCnlEP43t6Rz04kdqCin3.y7'
        };
    </script>
</div>
<div class="margintop10 " id="favoritesGalleryBox">
    <div class="wrapper">
        <ul class="tabsfav tohide clr cpointer">
            <li class="fleft lastSeen ">
                <span class="fleft tab"> <span class="fbold">Ostatnio przeglądane</span>
                </span>
            </li>
            <li class="fleft observedAds hidden">
                <span class="fleft tab"> <span class="fbold">Obserwowane ogłoszenia</span> <span class="color-2 normal">(<span class="counter">0</span>)
                </span>
                </span>
            </li>
            <li class="fleft observedSearches hidden">
                <span class="fleft tab"> <span class="fbold">Obserwowane wyszukiwania</span> <span class="color-2 normal">(<span class="counter">0</span>)
                </span>
                </span>
            </li>
        </ul>
    </div>
    <div class="favbottombox">
        <div class="tab-lastSeen initialized " id="tab-lastSeen">
            <div class="wrapper">
                <ul class="clr favgallerybox">
                                    <li class="fleft rel  " id="lastSeen-150248655">
                        <div class="card tcenter br4">
                            <div class="mheight tcenter">
                                <a class="thumb tdnone scale4 detailsLink linkWithHash " href="http://olx.pl/oferta/w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowa-ruczaj-CID3-IDaaqxp.html" title="W pełni umeblowane mieszkanie do wynajęcia od ZARAZ, ul Obozowa,Ruczaj">
                                                                            <img src="http://img06.staticclassifieds.com/images_tablicapl/255926909_1_261x203_w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowaruczaj-krakow.jpg" alt="http://olx.pl/oferta/w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowa-ruczaj-CID3-IDaaqxp.html">
                                                                                                        </a>
                            </div>
                            <div class="inner pding5 br4">
                                <h4 class="small lheight14">
                                    <a class="link" title="W pełni umeblowane mieszkanie do wynajęcia od ZARAZ, ul Obozowa,Ruczaj" href="http://olx.pl/oferta/w-pelni-umeblowane-mieszkanie-do-wynajecia-od-zaraz-ul-obozowa-ruczaj-CID3-IDaaqxp.html">
                                        <span class="fbold">W pełni umeblowane mieszkanie do wynajęcia od ZARAZ, ul Obozowa,Ruczaj</span>
                                    </a>
                                </h4>
                                <div class="lheight12 onhoverin">
                                    <small class="breadcrumb">Wynajem<br>Kraków</small>
                                </div>
                            </div>
                                                        <div class="price">
                                1 800 zł                                                                                            </div>
                                                                                    <span class="favtab br3 abs zi3 observelinkgallery hidden">
                                <a href="#" class="inlblk lheight16 tdnone observeChange {adId: 150248655}">
                                    <span class="icon inlblk observe2 vtop "></span>
                                </a>
                                <span class="suggesttitle small top abs zi2 br4 hidden">
                                    <span class="txt">Obserwuj</span>
                                    <span class="target abs icon"></span>
                                </span>
                            </span>
                                                    </div>
                    </li>
                                </ul>
            </div>
        </div>
        <div class="tab-observedAds hidden"></div>
        <div class="tab-observedSearches hidden"></div>
    </div>
</div>
            </div>
        </div>
        
            </section>
    

</div>
<div id="ad-not-available-box" class="pding10_20 clr br5 margin10 headinfobox hidden" style="display: none">
    <div class="icon info7 fleft marginright20"></div>
    <div class="overh">
        <h3 class="lheight20 large cfff">
            <strong>To ogłoszenie nie jest już dostępne</strong>
        </h3>
        <p class="cfff">Wybierz coś dla siebie z podobnych, które znaleźliśmy.</p>
    </div>
</div>
   
    <footer id="footer-container">
        <div id="footerTop" class="wrapper rel small overh brbott-12">
    <div class="content brbott-5">
        <div id="categoryLinksHeader">
    <ul class="breaklist small lheight16 brbott-1 pding15_0">
    <li id="linksCat0" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie główne Kraków</span></span>
        </li>
    <li id="linksCat3" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie podobne do "Nieruchomości" Kraków</span></span>
        </li>
    <li id="linksCat1307" class="inline">
            <span class="link gray"><span class="cpointer">Kategorie podobne do "Mieszkania" Kraków</span></span>
        </li>
</ul>
</div>

<div id="categoryLinksSections">
            <div id="linksCat0Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie główne Kraków:</h3>
                                                <a href="http://olx.pl/motoryzacja/krakow/" title="Motoryzacja Kraków" class="link gray2 tunder">
            <span>Motoryzacja Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/krakow/" title="Nieruchomości Kraków" class="link gray2 tunder">
            <span>Nieruchomości Kraków</span>
        </a>,                                                                <a href="http://olx.pl/praca/krakow/" title="Praca Kraków" class="link gray2 tunder">
            <span>Praca Kraków</span>
        </a>,                                                                <a href="http://olx.pl/dom-ogrod/krakow/" title="Dom i Ogród Kraków" class="link gray2 tunder">
            <span>Dom i Ogród Kraków</span>
        </a>,                                                                <a href="http://olx.pl/elektronika/krakow/" title="Elektronika Kraków" class="link gray2 tunder">
            <span>Elektronika Kraków</span>
        </a>,                                                                <a href="http://olx.pl/moda/krakow/" title="Moda Kraków" class="link gray2 tunder">
            <span>Moda Kraków</span>
        </a>,                                                                <a href="http://olx.pl/rolnictwo/krakow/" title="Rolnictwo Kraków" class="link gray2 tunder">
            <span>Rolnictwo Kraków</span>
        </a>,                                                                <a href="http://olx.pl/zwierzeta/krakow/" title="Zwierzęta Kraków" class="link gray2 tunder">
            <span>Zwierzęta Kraków</span>
        </a>,                                                                <a href="http://olx.pl/dla-dzieci/krakow/" title="Dla Dzieci Kraków" class="link gray2 tunder">
            <span>Dla Dzieci Kraków</span>
        </a>,                                                                <a href="http://olx.pl/sport-hobby/krakow/" title="Sport i Hobby Kraków" class="link gray2 tunder">
            <span>Sport i Hobby Kraków</span>
        </a>,                                                                <a href="http://olx.pl/muzyka-edukacja/krakow/" title="Muzyka i Edukacja Kraków" class="link gray2 tunder">
            <span>Muzyka i Edukacja Kraków</span>
        </a>,                                                                <a href="http://olx.pl/uslugi-firmy/krakow/" title="Usługi i Firmy Kraków" class="link gray2 tunder">
            <span>Usługi i Firmy Kraków</span>
        </a>,                                                                <a href="http://olx.pl/oddam-za-darmo/krakow/" title="Oddam za darmo Kraków" class="link gray2 tunder">
            <span>Oddam za darmo Kraków</span>
        </a>,                                                                <a href="http://olx.pl/zamienie/krakow/" title="Zamienię Kraków" class="link gray2 tunder">
            <span>Zamienię Kraków</span>
        </a>                                    </div>
                <div id="linksCat3Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie podobne do "Nieruchomości" Kraków:</h3>
                                                <a href="http://olx.pl/nieruchomosci/mieszkania/krakow/" title="Mieszkania Kraków" class="link gray2 tunder">
            <span>Mieszkania Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/domy/krakow/" title="Domy Kraków" class="link gray2 tunder">
            <span>Domy Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/dzialki/krakow/" title="Działki Kraków" class="link gray2 tunder">
            <span>Działki Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/biura-lokale/krakow/" title="Biura i Lokale Kraków" class="link gray2 tunder">
            <span>Biura i Lokale Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/garaze-parkingi/krakow/" title="Garaże i Parkingi Kraków" class="link gray2 tunder">
            <span>Garaże i Parkingi Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/noclegi/krakow/" title="Noclegi Kraków" class="link gray2 tunder">
            <span>Noclegi Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/stancje-pokoje/krakow/" title="Stancje i Pokoje Kraków" class="link gray2 tunder">
            <span>Stancje i Pokoje Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/hale-magazyny/krakow/" title="Hale i Magazyny Kraków" class="link gray2 tunder">
            <span>Hale i Magazyny Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/pozostale-nieruchomosci/krakow/" title="Pozostałe nieruchomości Kraków" class="link gray2 tunder">
            <span>Pozostałe nieruchomości Kraków</span>
        </a>                                    </div>
                <div id="linksCat1307Section" class="static clr lheight16 c73 brbott-1 pding15_0">
        <h3 class="lheight16 c73 fbold inline">Kategorie podobne do "Mieszkania" Kraków:</h3>
                                                <span class="c73">Wynajem Kraków</span>,                                                                <a href="http://olx.pl/nieruchomosci/mieszkania/sprzedaz/krakow/" title="Sprzedaż Kraków" class="link gray2 tunder">
            <span>Sprzedaż Kraków</span>
        </a>,                                                                <a href="http://olx.pl/nieruchomosci/mieszkania/zamiana/krakow/" title="Zamiana Kraków" class="link gray2 tunder">
            <span>Zamiana Kraków</span>
        </a>                                    </div>
    </div>
                    <div id="locationLinks">
                <div class="static clr lheight16 c73 brbott-1 pding15_0">
                    <ul class="breadcrumb">
                                                    <li class="inline nowrap">
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/q-ruczaj/?page=2"><span>Polska</span></a>
                            </li>
                                                    <li class="inline nowrap">
                                                                    <span class="slash">&raquo;</span>
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/malopolskie/q-ruczaj/?page=2"><span>Małopolskie</span></a>
                            </li>
                                                    <li class="inline nowrap">
                                                                    <span class="slash">&raquo;</span>
                                                                <a class="link gray nowrap" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2"><span>Kraków</span></a>
                            </li>
                                            </ul>
                    <div class="locationlinks margintop10">
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=261"><span>Dębniki</span></a>&nbsp;(99)</li>
                                                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=279"><span>Grzegórzki</span></a>&nbsp;(1)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=263"><span>Podgórze</span></a>&nbsp;(13)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=265"><span>Łagiewniki-Borek Fałęcki</span></a>&nbsp;(9)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=255"><span>Krowodrza</span></a>&nbsp;(3)</li>
                                                                                    </ul>
                        <ul>
                                                                                                <li><a class="link gray" href="http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-ruczaj/?page=2&search%5Bdistrict_id%5D=273"><span>Stare Miasto</span></a>&nbsp;(2)</li>
                                                                                    </ul>
                    </div>
                                    </div>
            </div>
                <div id="categoryLinksSuggestions" class="small lheight16 pding15_0">
        <p class="c73">Mieszkania do wynajęcia na OLX.pl (dawniej Tablica.pl) Kraków, oferty bezpośrednie i od agencji nieruchomości. Mieszkanie wynajmę Kraków - sprawdź nasze ogłoszenia.</p>
    </div>    </div>
</div>
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
            <a href="http://pomoc.olx.pl" class="link gray" title="Pomoc">
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
            <a href="http://olx.pl/zasady/" class="link gray inlblk rel" title="Regulamin OLX.pl">
                <span>Regulamin OLX.pl</span>
                            </a>
        </li>
                    <li>
                <a href="http://s7.olx.pl/static/olxpl/external/olxpl/pdf/cennik_reklam_OLX.pdf" class="link gray" title="Cennik reklam">
                    <span>Cennik reklam</span>
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
                <a href="http://olx.pl/nieruchomosci/krakow/popularne/" class="link gray" title="Popularne wyszukiwania w Nieruchomości">
                    <span>Popularne wyszukiwania w Nieruchomości</span>
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
    <a href="https://play.google.com/store/apps/details?id=pl.tablica&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" id="footerAppAndroid" target="_blank" class="inlblk">
        <span class="icon block googleplay"> w Google Play</span>
        <span class="tag-line tleft hidden">
            Do pobrania w            <strong class="block">Google Play</strong>
        </span>
    </a>
    <a href="https://itunes.apple.com/pl/app/olx.pl-darmowe-og-oszenia/id531717763?l=pl&ls=1&mt=8" id="footerAppIphone" target="_blank" class="inlblk">
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
                    <span class="icon fleft flag olxbg">&nbsp;</span><span>OLX.bg</span>
                </a>
            </li>
                                <li class="part25 fleft">
                <a href="http://olx.ro" target="_blank" class="link gray">
                    <span class="icon fleft flag olxro">&nbsp;</span><span>OLX.ro</span>
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
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'AppStore']);" class="inlblk icon appstore" href="https://itunes.apple.com/pl/app/olx.pl-darmowe-og-oszenia/id531717763?l=pl&ls=1&mt=8" target="_blank">OLX.pl AppStore</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'GooglePlay']);" class="inlblk icon googleplay" href="https://play.google.com/store/apps/details?id=pl.tablica&referrer=utm_source%3Dolx.pl%26utm_medium%3Dcpc%26utm_campaign%3Dandroid-app-footer" target="_blank">OLX.pl GooglePlay</a>
            <a onclick="_gaq.push(['_trackEvent', 'AppPromo', 'MyOLX', 'WindowsStore']);" class="inlblk icon windowsstore" href="http://www.windowsphone.com/pl-pl/store/app/olx-pl/cfb57b0c-bc3e-4d00-9373-fa351f8c5f0c" target="_blank">OLX.pl WindowsStore</a>
        </div>
    </div>
</div>
</div>                    
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
    xtcustom = {"page_name":"listing","keyword":"ruczaj","page_nb":"2","provinces":"malopolskie","cities":"krakow","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","user_status":"unlogged_user"};
    //-->
</script>
<noscript>
    <img width="1" height="1" alt="" src="http://LOGC269.xiti.com/hit.xiti?s=507462&stc={"page_name":"listing","keyword":"ruczaj","page_nb":"2","provinces":"malopolskie","cities":"krakow","category":"nieruchomosci","subcategory":"mieszkania","subsubcategory":"wynajem","user_status":"unlogged_user"}" >
</noscript>
                                    <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/packed/sw1320019e5ecaacfb81789395e9b12bab.js"></script>
                                                <script type="text/javascript" src="http://s8.olx.pl/static/olxpl/packed/sw262e3acc54ab15d86d656bf5dfe6c736.js"></script>
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
                    <script type="text/javascript" charset="utf-8">
              (function(G,o,O,g,L,e){G[g]=G[g]||function(){(G[g]['q']=G[g]['q']||[]).push(
              arguments)},G[g]['t']=1*new Date;L=o.createElement(O),e=o.getElementsByTagName(
              O)[0];L.async=1;L.src='//www.google.com/adsense/search/async-ads.js';
              e.parentNode.insertBefore(L,e)})(window,document,'script','_googCsa');
            </script>
                                <script type="text/javascript">
        function loadAdocean(ajax) {
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
                    
                    if (ajax)
                    {
                        var keys = [];
                        var cat = [];
                        if (categoryCode != rootCategoryCode){
                            cat=['cat:'+categoryCode,'cat:'+rootCategoryCode];
                            if (category_id != second_category_id && second_category_code != undefined)
                            {
                                cat.push('cat:'+second_category_code);
                            }
                        } else {
                            cat=['cat:'+categoryCode];
                        }
                        
                        if (regionCode != '') {
                            cat.push('region:'+regionCode);
                        } else {
                            cat.push('region:none');
                        }
                        if (cityCode != '') {
                            cat.push('city:'+cityCode);
                        } else {
                            cat.push('city:none');
                        }
                        for (var i=0; i < AdoVars['master']['keys'].length;i++)
                        {   
                            //str.indexOf
                            if (AdoVars['master']['keys'][i].indexOf('cat:')== -1 && AdoVars['master']['keys'][i].indexOf('city:')== -1 && AdoVars['master']['keys'][i].indexOf('region:')== -1)
                            {
                                keys.push(AdoVars['master']['keys'][i]);
                            }
                        }
                        AdoVars['master']['keys'] = keys.concat(cat);
                        
                        
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
<!-- tablica-dc4-100 -->
"""