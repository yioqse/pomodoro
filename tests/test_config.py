from unittest.mock import patch
from config.manager import get_positive_value, DEFAULT_CONFIG

def test_get_positive_value_defaults():
    with patch('builtins.input', return_value=''):
        val = get_positive_value("Prompt", 25.0)
        assert val == 25.0

def test_get_positive_value_valid_input():
    with patch('builtins.input', side_effect=['30']):
        val = get_positive_value("Prompt", 25.0)
        assert val == 30.0

def test_get_positive_value_invalid_then_valid():
    with patch('builtins.input', side_effect=['-5', 'abc', '10']):
        val = get_positive_value("Prompt", 25.0)
        assert val == 10.0
