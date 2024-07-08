from scripts.sentiment_analysis import analyze_sentiment
from scripts.technical_analysis import calculate_moving_average
import pandas as pd
import unittest


class TestTradingTool(unittest.TestCase):
    def test_analyze_sentiment(self):
        self.assertEqual(analyze_sentiment("Market is going up"), 1)
        self.assertEqual(analyze_sentiment("Market is stable"), 0)
        self.assertEqual(analyze_sentiment("Market is going down"), -1)

    def test_calculate_moving_average(self):
        data = pd.Series([1, 2, 3, 4, 5])
        ma = calculate_moving_average(data, 2)
        self.assertEqual(ma.iloc[1], 1.5)
        self.assertEqual(ma.iloc[2], 2.5)

if __name__ == "__main__":
    unittest.main()
