from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
    
    #Testes de erro

    def test4(self): #Erro de dia da semana que não corresponde a data
        result = "Error!"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 21Feb2009(sun), 28Mar2009(sat)"))

    def test5(self): #Erro de dia que não existe no mês dado
        result = "Error!"
        self.assertEqual(result, get_cheapest_hotel("Regular: 26Mar2009(thur), 32Jun2009(sun), 28Mar2009(sat)"))

    def test6(self): #Erro do mês escrito de maneira errada
        result = "Error!"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 22Fev2009(sun), 28Mar2009(sat)"))
    
    def test7(self): #Erro de tipo de hospedagem não valida
        result = "Error!"
        self.assertEqual(result, get_cheapest_hotel("Sócio: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))
    