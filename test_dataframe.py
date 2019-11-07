"""Homework 4 is making homework 3 PEP8 compliant"""
import unittest
import pandas as pd
import numpy as np
import hw2


# url = 'https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/resource/' \
#       'ef734bd0-0aff-4687-9b8a-fc69b937be63/download/userssharedsdfratebrthsyaw1819raceet' \
#       'hncty20002012.csv'
# dataframe = hw2.read_function(url)
# column_names = dataframe.columns.values.tolist()

DATA = pd.DataFrame(np.arange(200).reshape(20, 10),
                    index=list('abcdefghijklmnopqrst'),
                    columns=list('abcdefghij'))

DATA.loc['a', 'd'] = None
COLUMN_NAMES = DATA.columns.values.tolist()


class TestModule(unittest.TestCase):
    """implement test through unittest"""
    # 　hw2 test
    def test_data_frame(self):
        """Create a test that replicates what was done in item(2) for HW2."""
        self.assertTrue(hw2.test_create_dataframe(DATA, COLUMN_NAMES))

    # Check that all columns have values of the correct type.
    def test_type(self):
        """Create a test that checks that all columns have values of the correct type."""
        for i in range(len(list(DATA.dtypes))):
            for j in range(list(DATA.count())[i]):
                if type(DATA.iloc[j, i]) != type(DATA.iloc[0, i]):
                    raise ValueError('Type of value is not correct')

    # Check for nan values.
    def test_nan(self):
        """Creates a test that checks for nan values in data_frame"""
        for i in list(DATA.columns):
            self.assertTrue(not pd.isnull(DATA[i]).any())

    # Verify that the data has at least one row.
    def test_row(self):
        """Creates a test that checks that the data_frame has at least one row"""
        for i in DATA.count():
            self.assertTrue(int(i) >= 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
