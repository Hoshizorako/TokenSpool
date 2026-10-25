# test_tokenspool.py
"""
Tests for TokenSpool module.
"""

import unittest
from tokenspool import TokenSpool

class TestTokenSpool(unittest.TestCase):
    """Test cases for TokenSpool class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenSpool()
        self.assertIsInstance(instance, TokenSpool)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenSpool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
