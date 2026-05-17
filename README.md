# 💊 Gerenciador de Medicamentos

## 📝 Descrição do Projeto
Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida para auxiliar pacientes e cuidadores na organização de cronogramas de medicação.

## 🎯 Relevância e Impacto Real
A falta de preocupação ao tratamento medicamentoso é uma deficiência de saúde pública. Erros na dosagem ou esquecimento de horários podem prejudicar a recuperação de pacientes crônicos e idosos. 
Este gerenciador visa reduzir esses riscos através de:
- **Validação de Dosagem:** Impede o registro de doses negativas ou inválidas.
- **Organização de Horários:** Centraliza o agendamento em uma interface simples.

## 🚀 Como Executar
1. Certifique se o Python está instalado.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Rode a aplicação:

Bash
python app/main.py

## 🧪 Como Rodar os Testes
Para garantir que a lógica de validação está funcionando, execute:

Bash
py -m pytest

## 🛠️ Tecnologias Utilizadas
Python 3.x

Pytest (Testes unitários)

Flake8 (Análise estática de código)

GitHub Actions (Integração Contínua)

## 🚀 Novas Funcionalidades (Entrega Intermediária)

Nesta etapa, o projeto evoluiu de um gerenciador local para uma aplicação integrada e testada:

- **Busca Automática de CEP:** Integração com a API pública do **ViaCEP** para autocompletar e validar o endereço do local de retirada do medicamento de forma dinâmica.
- **Validação de Dosagem:** Garante que nenhum medicamento seja cadastrado com dosagens inválidas ou negativas.
- **Qualidade de Código (Linting):** Código 100% adequado às normas de estilo **PEP 8** utilizando o **Flake8**.
- **Testes Automatizados:** Implementação de testes de integração com **Pytest** para garantir o funcionamento correto das rotas e do consumo da API.
- **Integração Contínua (CI):** Configuração do **GitHub Actions** para rodar a esteira de testes automaticamente a cada Pull Request.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Requests:** Para consumo da API HTTP do ViaCEP.
- **Pytest:** Para a estrutura de testes automatizados.
- **Flake8:** Para garantir os padrões de formatação de código.
- **GitHub Actions:** Para automação de testes na nuvem.

## 🧪 Como Rodar os Testes Localmente

Caso queira executar os testes criados no seu ambiente local, certifique-se de ter as dependências instaladas e execute:

```bash
# Instalar os requisitos (caso não tenha feito)
pip install requests pytest flake8

# Rodar o verificador de estilo
flake8 app/

# Rodar os testes de integração
pytest




