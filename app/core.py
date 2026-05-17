import requests


def validar_dosagem(dosagem):
    """Verifica se a dosagem é um número positivo."""
    return dosagem > 0


def buscar_endereco_por_cep(cep):
    """Consome a API pública do ViaCEP para buscar dados de endereço."""
    cep_limpo = str(cep).strip().replace("-", "").replace(".", "")
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        return None

    try:
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                logradouro = dados.get('logradouro', '')
                bairro = dados.get('bairro', '')
                localidade = dados.get('localidade', '')
                uf = dados.get('uf', '')
                return f"{logradouro}, {bairro} - {localidade}/{uf}"
    except requests.RequestException:
        return None
    return None


def cadastrar_medicamento(nome, horario, dosagem, cep=None):
    """Valida e retorna os dados do medicamento com o local de retirada."""
    if not nome.strip():
        raise ValueError("O nome do medicamento não pode estar vazio.")
    if not validar_dosagem(dosagem):
        raise ValueError("A dosagem deve ser um valor positivo.")

    endereco = "Não informado"
    if cep:
        endereco_api = buscar_endereco_por_cep(cep)
        if endereco_api:
            endereco = endereco_api
        else:
            raise ValueError("CEP inválido ou não encontrado.")

    return {
        "nome": nome,
        "horario": horario,
        "dosagem": dosagem,
        "local_retirada": endereco
    }