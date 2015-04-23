''' Suite de casos de prueba para la funcion calculaPrecio
creado el 21/04/2015
Equipo: PyTech
Autores: 
Carlos Noria 10-10498
Dayana Rodrigues 10-10615
'''

import unittest
from datetime import datetime
from calcularPrecio import calcularPrecio, Tarifa
from decimal import Decimal

class Test(unittest.TestCase):

    '''Datos Permitidos'''
    
    # Pruba de tarifa en rango normal por una semana entera, el maximo tiempo posible
    def testTarifaEnRango(self):
        tarif = Tarifa(1, 2)
        tiempo = [datetime(2015, 4, 21, 23, 0), datetime(2015, 4, 28, 23, 0)]
        self.assertEqual(calcularPrecio(tarif, tiempo), 216)

    '''Datos Invalidos'''  
        
    # Prueba de la tarifa invalida del dia de semana  
    def testTarifaInvalida(self):
        tarif = Tarifa(-1, 0)
        tiempo = [datetime(2015, 4, 21, 10, 0), datetime(2015, 4, 21, 11, 0)]
        self.assertRaises(Exception, calcularPrecio, tarif, tiempo)
       
    # Prueba reservacion de menos de 15 minutos
    def testTiempoMinimoInv(self):
        tarif = Tarifa(1, 2)
        tiempo = (datetime(2015, 4, 25, 9, 0), datetime(2015, 4, 25, 9, 14))
        self.assertRaises(Exception, calcularPrecio, tarif, tiempo)
        
    # Prueba para tarifas invalidas: un numero negativo.
    def testTarifaInvalidaFS(self):
        tarif = Tarifa(1, -1)
        tiempo = (datetime(2015, 4, 25, 0, 1), datetime(2015, 4, 25, 2, 1))
        self.assertRaises(Exception, calcularPrecio, tarif, tiempo)

    '''Datos Maliciosos'''
        
    # Prueba de una hora con el ultimo minuto de un dia de semana y los otros 59 en un fin de semana    
    def testDiaSemanaDiaFinSemana(self):
        tarif = Tarifa(1, 2)
        tiempo = [datetime(2015, 4, 24, 23, 59), datetime(2015, 4, 25, 0, 59)]
        self.assertEqual(calcularPrecio(tarif, tiempo), Decimal('1.98')) 
        
    #Prueba de la tarifa en la frontera entre el fin de semana y dias de semana
    def testTarifaTerminaFinSemana(self):
        tarif = Tarifa(1, 2)
        tiempo = (datetime(2015, 4, 26, 23, 59), datetime(2015, 4, 27, 0, 59))
        self.assertEqual(calcularPrecio(tarif, tiempo), Decimal('1.02'))  

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()