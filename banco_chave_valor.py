
import shelve
import json

ARQUIVO_BANCO = "banco_alunos"


def cadastrar():
    chave = input("Digite a matrícula do aluno: ")

    with shelve.open(ARQUIVO_BANCO) as banco:
        if chave in banco:
            print("Já existe um aluno com essa matrícula!")
            return

        nome = input("Digite o nome: ")
        curso = input("Digite o curso: ")
        idade = input("Digite a idade: ")

        aluno = {
            "nome": nome,
            "curso": curso,
            "idade": idade
        }

        banco[chave] = aluno

    print("Aluno cadastrado com sucesso!")


def consultar():
    chave = input("Digite a matrícula do aluno: ")

    with shelve.open(ARQUIVO_BANCO) as banco:
        if chave in banco:
            print("\nDados do aluno:")
            print(json.dumps(
                banco[chave],
                indent=4,
                ensure_ascii=False
            ))
        else:
            print("Aluno não encontrado!")


def excluir():
    chave = input("Digite a matrícula do aluno: ")

    with shelve.open(ARQUIVO_BANCO) as banco:
        if chave in banco:
            del banco[chave]
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não encontrado!")


def listar():
    with shelve.open(ARQUIVO_BANCO) as banco:
        if not banco:
            print("Nenhum aluno cadastrado.")
            return

        print("\n--- ALUNOS CADASTRADOS ---")

        for chave, aluno in banco.items():
            print(f"\nMatrícula: {chave}")
            print(f"Nome: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Idade: {aluno['idade']}")


def menu():
    while True:
        print("\n===== BANCO DE DADOS CHAVE-VALOR =====")
        print("1 - Cadastrar aluno")
        print("2 - Consultar aluno")
        print("3 - Excluir aluno")
        print("4 - Listar alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            listar()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()