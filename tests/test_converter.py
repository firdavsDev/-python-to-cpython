# tests/test_converter.py
import unittest
import module

class TestPythonToCPython(unittest.TestCase):
    
    def test_add_function(self):
        result = module.add(2, 3)
        self.assertEqual(result, 5)
    
    # Add more tests here for other functions or code snippets
    
if __name__ == '__main__':
    unittest.main()
