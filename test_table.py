import unittest
import my_table
class MyTableTest(unittest.TestCase):

    def setUp(self):
        self.my_table = my_table.MyTable('DEMO', 'DEMO')
        self.my_table.set_pk('DEMO_ID')

    def test(self):
       self.my_table.add_col('COL_CODE', 'COL_NAME', '', 'this is a test')
       print(self.my_table.build_table())

if __name__ == '__main__':
    unittest.main()
