
import pytest
from unittest.mock import patch
from src.main import *


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    assert not result


def test_update_estudante_positivo():
    result = update_estudante(5)
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(5)
    assert result
