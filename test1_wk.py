
import unittest 
import moj_program_wk

class Test1TDD(unittest.TestCase):
    def test_100(self):
        wynik = moj_program_wk.zwroc_100()
        self.assertEqual(100, wynik)
    def test_zwroc_parmetr(self):
        ret = moj_program_wk.zwroc_parametr('olek')
        self.assertEqual(ret , 'olek')
        
    

if __name__ == '__main__':
    unittest.main()

