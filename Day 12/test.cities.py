import unittest
from city_functions import formatted_city_country
class TestCities(unittest.TestCase):
    def test_formatted_city_country(self):
        formatted_string = formatted_city_country("santiago" , "chile" , "100000")
        self.assertEqual(formatted_string , "Santiago, Chile, 100000")
unittest.main()