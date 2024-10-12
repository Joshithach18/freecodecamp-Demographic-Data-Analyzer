# test_module.py

from demographic_data_analyzer import demographic_data_analyzer
import unittest

class TestDemographicAnalyzer(unittest.TestCase):
    def setUp(self):
        self.result = demographic_data_analyzer()

    def test_race_count(self):
        expected = 5  # Adjust based on your dataset's actual races
        self.assertEqual(len(self.result['race_count']), expected)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.result['average_age_men'], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.result['percentage_bachelors'], 16.4, places=1)

    def test_higher_education_rich(self):
        self.assertAlmostEqual(self.result['higher_education_rich'], 46.5, places=1)

    def test_lower_education_rich(self):
        self.assertAlmostEqual(self.result['lower_education_rich'], 17.4, places=1)

    def test_min_work_hours(self):
        self.assertEqual(self.result['min_work_hours'], 1)

    def test_rich_min_workers_percentage(self):
        self.assertAlmostEqual(self.result['rich_min_workers_percentage'], 10.0, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(self.result['highest_earning_country'], 'United-States')

    def test_highest_earning_country_percentage(self):
        self.assertAlmostEqual(self.result['highest_earning_country_percentage'], 39.3, places=1)

    def test_top_IN_occupation(self):
        self.assertEqual(self.result['top_IN_occupation'], 'Prof-specialty')

def run_tests():
    unittest.main(exit=False)
