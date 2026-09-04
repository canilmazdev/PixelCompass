# test_pixelcompass.py
"""
Tests for PixelCompass module.
"""

import unittest
from pixelcompass import PixelCompass

class TestPixelCompass(unittest.TestCase):
    """Test cases for PixelCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelCompass()
        self.assertIsInstance(instance, PixelCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
