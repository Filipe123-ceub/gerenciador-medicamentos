import sys
import os
import pytest

# Garante que o Python encontre a pasta 'app'
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, base_path)

from app.core import validar_dosagem, cadastrar_medicamento, buscar_endereco_por_cep  # noqa: E402


def test_dosagem_valida():
    assert validar_dosagem(100) is True


def test_dosagem_invalida():
    assert validar_dosagem(-10) is False


def test_nome_vazio_gera_erro():
    msg = "O nome do medicamento não pode estar vazio."
    with pytest.raises(ValueError, match=msg):
        cadastrar_medicamento("", "08:00", 500)


# --- TESTES DE INTEGRAÇÃO (API PÚBLICA VIA CEP) ---

def test_busca_cep_sucesso_integracao():
    """Valida a integração real consultando o CEP da Praça da Sé/SP"""
    endereco = buscar_endereco_por_cep("01001000")
    assert endereco is not None
    assert "Praça da Sé" in endereco


def test_busca_cep_invalido():
    """Valida que um CEP com formato incorreto retorna None"""
    endereco = buscar_endereco_por_cep("99999999")
    assert endereco is None