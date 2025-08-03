# test_neosphere.py
"""
Tests for NeoSphere module.
"""

import unittest
from neosphere import NeoSphere

class TestNeoSphere(unittest.TestCase):
    """Test cases for NeoSphere class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoSphere()
        self.assertIsInstance(instance, NeoSphere)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoSphere()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
