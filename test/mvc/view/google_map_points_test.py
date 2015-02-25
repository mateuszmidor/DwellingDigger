'''
Created on 23-02-2015

@author: mateusz
'''
import unittest
from src.mvc.view.google_map_points import GoogleMapPoints
import re
from datetime import datetime


class GoogleMapPointsTest(unittest.TestCase):
    OFFER1 = {"address" :   "Wielicka, Krakow, Polska",
              "address_section" :   "Wielicka",
              "title"   :   "OFFER1",
              "date"    :   datetime(2000, 1, 1),
              "price"   :   "1000 ZL",
              "url"     :   "www.OFFER1.pl",
              "summary" :   "Tanie mieszkanie na wielickiej",
              "longlatt":   [1, 1]}
    
    OFFER2 = {"address" :   "Kurdwanow, Krakow, Polska",
              "address_section" :   "osiedle Kurdwanow",
              "title"   :   "OFFER2",
              "date"    :   datetime(2000, 1, 2),
              "price"   :   "2000 ZL",
              "url"     :   "www.OFFER2.pl",
              "summary" :   "Niezbyt tanie mieszkanie, kurdwanow",
              "longlatt":   [2, 2]}        

    OFFER3 = {"address" :   "Wielicka, Krakow, Polska",
              "address_section" :   "ul wielicka",
              "title"   :   "OFFER3",
              "date"    :   datetime(2000, 1, 3),
              "price"   :   "3000 ZL",
              "url"     :   "www.OFFER3.pl",
              "summary" :   "Absolutnie nietanie mieszkanie, kurdwanow",
              "longlatt":   [1, 1]}  

    def test_from_offers(self):
        points = GoogleMapPoints.from_offers([GoogleMapPointsTest.OFFER1, 
                                              GoogleMapPointsTest.OFFER2, 
                                              GoogleMapPointsTest.OFFER3]).points
        
        # 2 distinct addresses should result in 2 points
        self.assertEqual(len(points), 2)
        
        # now investigate the points 
        point1 = points[0]
        
        # check point has all properties [longitude, latitude, description, icon_name]
        self.assertEqual(len(point1), 4)
        
        # check longitude
        longitude = point1[0]
        self.assertEqual(longitude, 1)
        
        # check latitude
        latitude = point1[1]
        self.assertEqual(latitude, 1)
        
        # check point description
        descr = point1[2]
        self.assertTrue("OFFER1" in descr)
        self.assertTrue("www.OFFER1.pl" in descr)
        self.assertTrue("Tanie mieszkanie na wielickiej" in descr)
        
        self.assertTrue("OFFER3" in descr)
        self.assertTrue("www.OFFER3.pl" in descr)
        self.assertTrue("Absolutnie nietanie mieszkanie, kurdwanow" in descr)
        
        
        point2 = points[1]
 
        # check point has [longitude, latitude, description, icon_name]
        self.assertEqual(len(point2), 4)
        
        # check longitude
        longitude = point2[0]
        self.assertEqual(longitude, 2)
        
        # check latitude
        latitude = point2[1]
        self.assertEqual(latitude, 2)
        
        # check point description
        descr = point2[2]
        self.assertTrue("OFFER2" in descr)
        self.assertTrue("www.OFFER2.pl" in descr)
        self.assertTrue("Niezbyt tanie mieszkanie, kurdwanow" in descr)
        
        
    def test_as_java_script(self):
        google_map_points = GoogleMapPoints.from_offers([GoogleMapPointsTest.OFFER1, 
                                                         GoogleMapPointsTest.OFFER2, 
                                                         GoogleMapPointsTest.OFFER3])
        
        java_string = google_map_points.as_java_script()
        
        # java_string is sth like: [[1.0, 1.0, 'description', icon1], [2.0, 2.0, 'description', icon2]]
        # take off outer square brackets to get what follows:
        # 1.0, 1.0, 'description', icon1], [2.0, 2.0, 'description', icon2
        points_string = java_string[2:-2]
        
        # split points into
        # 1.0, 1.0, 'description', icon1
        # 2.0, 2.0, 'description', icon2
        points = points_string.split("], [")
        
        # make sure there are 2 points as we have 2 distinct addresses present
        self.assertEqual(len(points), 2)
        
        # check each point is built from 4 components:
        # float, float, 'string', string
        # float can be 1, -1, 1.98, -1.98
        FOUR_COMPONENTS = r"-?\d+(?:\.\d+)?, -?\d+(?:\.\d+)?, '.+', .+"
        for point in points:
            self.assertTrue(re.match(FOUR_COMPONENTS, point), "google_map_point doesnt seem to be in proper format [float, float, 'string', string]")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()