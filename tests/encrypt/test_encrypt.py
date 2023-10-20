import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("abcde", 1) == "a_edcb"
    assert encrypt_message("abcde", 2) == "edc_ba"
    assert encrypt_message("abc", 9) == "cba"
    assert encrypt_message("accb", 2) == "bc_ca"
    with pytest.raises(TypeError):
        encrypt_message(123, 1)
