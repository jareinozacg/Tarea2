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
        
    # Prueba de la minima tarifa de dia de semana sobre la minima hora inexacta    
    def testTarifaMinimaHoraInexacta(self):
        tarif = Tarifa(0.01, 2)
        tiempo = [datetime(2015, 4, 22, 9, 0), datetime(2015, 4, 22, 10, 1)]
        self.assertEqual(calcularPrecio(tarif, tiempo), 0.02)
    
    # Prueba de la tarifa nula del dia de semana    
    def testTarifaCero(self):
        tarif = Tarifa(0, 1)
        tiempo = [datetime(2015, 4, 21, 22, 0), datetime(2015, 4, 22, 23, 0)]
        self.assertEqual(calcularPrecio(tarif, tiempo), 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()