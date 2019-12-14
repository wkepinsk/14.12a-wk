import unittest 
import kalkulator

class testy_kalkulator(unittest.TestCase):
    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik ,2)
        wynik = kalkulator.dodaj(-2, 3)
        self.assertEqual(wynik, 1)
        wynik = kalkulator.dodaj(5,3*5)
        self.assertEqual(wynik, 20)
    def test_odejmowanie(self):
        wynik = kalkulator.odejmij(3,3)
        self.assertEqual(wynik, 0)
    def test_mnozenie(self):
        wnik = kalkulator.pomnoz(2,3)
        self.assertEqual(wynik, 6)
    def test_dzielenie(self):
        wynik = kalkulator.dziel(9,3)
        self.assertEqual(wynik, 3)


if __name__ == '__main__':
    unittest.main()