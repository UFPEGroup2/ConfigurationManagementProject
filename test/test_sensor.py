import sys
file = sys.path.insert(1,'C:/Git/ProjectConfigurationManagement/ConfigurationManagementProject/test')
import unittest
from file import readSensor

def  test_readSensor(self):
       
    def setUp(self): # Preparation code that run before each Test.
        self.obj = read()
    
    def tearDown(self): # Clean-up all the registry and modification after each test completes
        self.obj= readSensor()
     
    def test_read(self):
        actual =  self.obj.readSensor()
        expected = TRUE
        self.assertEqual(actual, expected)  # Assert is the method of class that do the TesCase

if __name__ == '__main__':
    unittest.main (verbosity=2)