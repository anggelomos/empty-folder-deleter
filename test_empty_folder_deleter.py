import unittest
import os
from empty_folder_deleter import folder_deleter

class EmptyFolderDeleterTest(unittest.TestCase):

    def test_folder_deleter_1(self):
        folder_deleter("test_files/test_01", verbose_mode=False)
        testcase = "test_01" not in os.listdir("test_files")
        self.assertTrue(testcase)
        os.mkdir("test_files/test_01")

    def test_folder_deleter_2(self):
        folder_deleter("test_files/test_02", verbose_mode=False)
        testcase = "test_02" in os.listdir("test_files")
        self.assertTrue(testcase)

    def test_folder_deleter_3(self):
        folder_deleter("test_files/test_03", verbose_mode=False)
        testcase = "test_03" in os.listdir("test_files")
        self.assertTrue(testcase)

    def test_folder_deleter_4(self):
        folder_deleter("test_files/test_04", verbose_mode=False)
        testcase = "test_04" in os.listdir("test_files")
        self.assertTrue(testcase)

if __name__ == "__main__":
    unittest.main()