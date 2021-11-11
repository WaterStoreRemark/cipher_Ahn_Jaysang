from cipher_ja3549 import cipher_ja3549
import pytest




def test_cipher_singleword():
    example = 'dog'
    expected = 'eph'
    result = cipher(example, 1, True)
    assert result == expected
