''' Suite de casos de prueba para la funcion calculaPrecio.
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
        
    # Prueba del minimo tiempo que se puede reservar en dia de semana   
    def testTiempoMinimo(self):
        tarif = Tarifa(1.50, 5)
        tiempo = [datetime(2015, 4, 22, 9, 0), datetime(2015, 4, 22, 9, 15)]
        self.assertEqual(calcularPrecio(tarif, tiempo), 1.50)
    
    # Prueba de funcionalidad basica para los dias de fin de semana 
    def testTarifaEnRangoDiaFinSemana(self):
        tarif = Tarifa(1, 3)
        tiempo = (datetime(2015, 4, 25, 9, 30), datetime(2015, 4, 25, 10, 30))
        self.assertEqual(calcularPrecio(tarif,tiempo), 3.00) 

    # Prueba de redondeo de la tarifa durante dias de fin de semana
    # prueba si se cobra la fraccion como una hora completa
    def testTarifaRedondeoFinSemana(self):
        tarif = Tarifa(1, 2)
        tiempo = (datetime(2015, 4, 25, 9, 0), datetime(2015, 4, 25, 10, 1))
        self.assertEqual(calcularPrecio(tarif, tiempo), 4.00)
        
    # Prueba para la tarifa minima: 0 bs con 1 centimo.
    # tarifa no entera
    def testTarifaMinimaFrontera(self):
        tarif = Tarifa(1, 0.1)
        tiempo = (datetime(2015, 4, 25, 13, 0), datetime(2015, 4, 25, 13, 15))
        self.assertEqual(calcularPrecio(tarif, tiempo), 0.10)
    
    '''Datos no permitidos'''
        
    # Prueba del mayor de los menores tiempos invalidos en dia de semana
    def testTiempoInvalidoMenor(self):
        tarif = Tarifa(1, 0)
        tiempo = [datetime(2015, 4, 21, 10, 0), datetime(2015, 4, 21, 10, 14)]
        self.assertRaises(Exception, calcularPrecio, tarif, tiempo)
    
    # Prueba del menor de los mayores tiempos invalidos
    def testTiempoInvalidoMayor(self):
        tarif = Tarifa(2, 3)
        tiempo = [datetime(2015, 4, 21, 10, 0), datetime(2015, 4, 28, 10, 1)]
        self.assertRaises(Exception, calcularPrecio, tarif, tiempo)
    
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