import sys
import os
import pytest

# Garante que o Python encontre a pasta 'app'
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, base_path)

from app.core import validar_dosagem, cadastrar_medicamento  # noqa: E402


def test_dosagem_valida():
    assert validar_dosagem(100) is True


def test_dosagem_invalida():
    assert validar_dosagem(-10) is False


def test_nome_vazio_gera_erro():
    msg = "O nome do medicamento não pode estar vazio."
    with pytest.raises(ValueError, match=msg):
        cadastrar_medicamento("", "08:00", 500)