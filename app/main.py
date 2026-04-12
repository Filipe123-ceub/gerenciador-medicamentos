from core import cadastrar_medicamento


def menu():
    print("\n" + "="*30)
    print("  GERENCIADOR DE MEDICAMENTOS")
    print("="*30)

    try:
        nome = input("Nome do Medicamento: ")
        horario = input("Horário (ex: 08:00): ")
        dosagem_str = input("Dosagem em mg (ex: 500): ")
        dosagem = float(dosagem_str)

        med = cadastrar_medicamento(nome, horario, dosagem)

        print("\n✅ Sucesso! Medicamento agendado:")
        msg = f"Nome: {med['nome']} | Hora: {med['horario']} | Dose: {med['dosagem']}mg"
        print(msg)

    except ValueError as e:
        print(f"\n❌ Erro de entrada: {e}")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    menu()
