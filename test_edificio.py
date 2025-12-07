#!/usr/bin/env python3
"""
Tests for the Edificio (Building) class
"""

import unittest
from edificio import Edificio, Nivel


class TestNivel(unittest.TestCase):
    """Test cases for Nivel class"""
    
    def test_nivel_creation(self):
        """Test creating a level"""
        nivel = Nivel(5, altura=3.0)
        self.assertEqual(nivel.numero, 5)
        self.assertEqual(nivel.altura, 3.0)
        self.assertEqual(nivel.desplazamiento, 0.0)
        self.assertEqual(nivel.danio, 0)
    
    def test_nivel_default_altura(self):
        """Test default height for a level"""
        nivel = Nivel(0)
        self.assertEqual(nivel.altura, 3.0)


class TestEdificio(unittest.TestCase):
    """Test cases for Edificio class"""
    
    def test_edificio_creation(self):
        """Test creating an 11-level building"""
        edificio = Edificio()
        self.assertEqual(edificio.num_niveles, 11)
        self.assertEqual(len(edificio.niveles), 11)
    
    def test_edificio_niveles(self):
        """Test that building has correct number of levels"""
        edificio = Edificio()
        for i in range(11):
            self.assertEqual(edificio.niveles[i].numero, i)
    
    def test_altura_total(self):
        """Test total building height calculation"""
        edificio = Edificio()
        # 11 levels * 3.0 meters each = 33.0 meters
        self.assertEqual(edificio.get_altura_total(), 33.0)
    
    def test_estado_inicial(self):
        """Test initial building state"""
        edificio = Edificio()
        self.assertEqual(edificio.get_estado(), "Intacto")
    
    def test_aplicar_terremoto(self):
        """Test applying earthquake to building"""
        edificio = Edificio()
        edificio.aplicar_terremoto(5.0)
        
        # After earthquake, building should not be intact
        self.assertNotEqual(edificio.get_estado(), "Intacto")
        
        # Higher levels should have more displacement
        self.assertGreater(
            edificio.niveles[10].desplazamiento,
            edificio.niveles[0].desplazamiento
        )
    
    def test_terremoto_intensidad_cero(self):
        """Test earthquake with zero intensity"""
        edificio = Edificio()
        edificio.aplicar_terremoto(0.0)
        
        # Building should remain intact
        for nivel in edificio.niveles:
            self.assertEqual(nivel.desplazamiento, 0.0)
    
    def test_edificio_nombre(self):
        """Test building name"""
        nombre = "Mi Edificio Test"
        edificio = Edificio(nombre)
        self.assertEqual(edificio.nombre, nombre)


if __name__ == '__main__':
    unittest.main()
