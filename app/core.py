def validar_dosagem(dosagem):
    """Verifica se a dosagem é um número positivo."""
    return dosagem > 0


def cadastrar_medicamento(nome, horario, dosagem):
    """Valida e retorna os dados do medicamento."""
    if not nome.strip():
        raise ValueError("O nome do medicamento não pode estar vazio.")
    if not validar_dosagem(dosagem):
        raise ValueError("A dosagem deve ser um valor positivo.")

    return {
        "nome": nome,
        "horario": horario,
        "dosagem": dosagem
    }
