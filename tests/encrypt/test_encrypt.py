from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("olá", "oi")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)
    assert encrypt_message("bola", 5) == "alob"
    assert encrypt_message("padaria", 3) == "dap_aira"
    assert encrypt_message("urso", 2) == "os_ru"
