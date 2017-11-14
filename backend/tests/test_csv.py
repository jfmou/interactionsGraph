import unittest
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
try:
    from api.commons import Utils
except Exception as e:
    print("import.except: %s" % e)


utils = Utils()

class TestCSV(unittest.TestCase):

    def setUp(self):
        self.csv_file = "tests/static/data-inter.csv"
        self.file_hash = "d91995ed297bd4158472d1a5f4def72e"
        
    def test_read_csv(self):
        ''' Test csv reader works '''
        csv_data = utils.read_csv_file(self.csv_file)
        self.assertNotEqual(0, len(csv_data))

    def test_file_hash(self):
        ''' Calculate tests/static/data-inter.csv md5sum '''
        file_hash = utils.get_uploaded_file_hash("tests/static", self.csv_file.split('/')[-1])
        self.assertEqual(self.file_hash, file_hash)


if __name__ == "__main__":
    unittest.main(verbosity=2)
