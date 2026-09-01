# test_nftstudiomax.py
"""
Tests for NFTStudioMax module.
"""

import unittest
from nftstudiomax import NFTStudioMax

class TestNFTStudioMax(unittest.TestCase):
    """Test cases for NFTStudioMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTStudioMax()
        self.assertIsInstance(instance, NFTStudioMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTStudioMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
