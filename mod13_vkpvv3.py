import unittest
import datetime

test_stock = "AAPL"
test_chart = 1
test_time_series = 1
test_date1 = "2022-03-22"
test_date2 = "2023-03-22"


class TestStockSymbol(unittest.TestCase):
    def test(self): 
        fixed_stock = test_stock.upper()[:7] #set variable to be uppercase, length 1-7
        self.assertEqual(test_stock, fixed_stock) #if they're the same, that means the test was already uppercase and length 1-7

class TestChartType(unittest.TestCase):
    def test(self):
        if test_chart == 1 or test_chart == 2:
            return True
        return False

class TestTimeSeries(unittest.TestCase):
    def test(self):
        if test_time_series in [1,2,3,4]:
            return True
        return False

class TestDates(unittest.TestCase):
    def test(self):
        date_format = "%Y-%m-%d"
        try: #this determines if it can even be converted to a date
            test_date1 = datetime.strptime(test_date1, date_format).date()
            test_date2 = datetime.strptime(test_date2, date_format).date()
            if test_date1 < test_date2: #then tests if date1 is before than date2
                return True
            return False
        except:
            return False

if __name__ == "__main__":
    unittest.main()
