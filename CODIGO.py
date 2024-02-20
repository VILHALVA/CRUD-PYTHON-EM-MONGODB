from pymongo import MongoClient
from time import sleep

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class GerenciadorUsuarios:
    def __init__(self):
        try:
            self.cliente = MongoClient('localhost', 27017)
            self.db = self.cliente['cadastro']
            self.collection = self.db['usuarios']
            print("🚀CONEXÃO AO BANCO DE DADOS ESTABELECIDA COM SUCESSO!")
        except Exception as e:
            print(f"😡ERRO AO CONECTAR AO BANCO DE DADOS: {e}")

    def adicionar_usuario(self, nome, idade):
        try:
            usuario = {"nome": nome, "idade": idade}
            self.collection.insert_one(usuario)
            print("😎USUÁRIO ADICIONADO COM SUCESSO!")
        except Exception as e:
            print(f"😡ERRO AO ADICIONAR USUÁRIO: {e}")

    def listar_usuarios(self):
        try:
            usuarios = list(self.collection.find())

            if len(usuarios) > 0:
                print("=" * 100)
                print("LISTA DE USUÁRIOS:")
                print("-" * 100)
                for usuario in usuarios:
                    print("*" * 100)
                    print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
                    print("*" * 100)
                print("=" * 100)
            else:
                print("😡NENHUM USUÁRIO CADASTRADO.")
        except Exception as e:
            print(f"😡ERRO AO LISTAR USUÁRIOS: {e}")

    def atualizar_usuario(self, nome_antigo, novo_nome, nova_idade):
        try:
            query = {"nome": nome_antigo}
            new_values = {"$set": {"nome": novo_nome, "idade": nova_idade}}
            self.collection.update_one(query, new_values)
            print("😙USUÁRIO ATUALIZADO COM SUCESSO!")
        except Exception as e:
            print(f"😡ERRO AO ATUALIZAR USUÁRIO: {e}")

    def excluir_usuario(self, nome):
        try:
            query = {"nome": nome}
            self.collection.delete_one(query)
            print("🗑USUÁRIO EXCLUÍDO COM SUCESSO!")
        except Exception as e:
            print(f"😡ERRO AO EXCLUIR USUÁRIO: {e}")

def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. SAIR")

def main():
    gerenciador = GerenciadorUsuarios()

    while True:
        exibir_menu()
        opcao = input("😎ESCOLHA UMA OPÇÃO:\n>>>")

        if opcao == "1":
            nome = input("😎DIGITE O NOME:\n>>>")
            idade = input("😎DIGITE A IDADE:\n>>>")
            gerenciador.adicionar_usuario(nome, idade)
        elif opcao == "2":
            gerenciador.listar_usuarios()
        elif opcao == "3":
            nome_antigo = input("😎DIGITE O NOME A SER ATUALIZADO:\n>>>")
            novo_nome = input("😎DIGITE O NOVO NOME:\n>>>")
            nova_idade = input("😎DIGITE A NOVA IDADE:\n>>>")
            gerenciador.atualizar_usuario(nome_antigo, novo_nome, nova_idade)
        elif opcao == "4":
            nome = input("😎DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
            gerenciador.excluir_usuario(nome)
        elif opcao == "5":
            print("🚀SAINDO...")
            sleep(3)
            break
        else:
            print("😡OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
