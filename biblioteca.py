import json
from typing import List, Dict, Optional

class Livro:
    """
    Classe que representa um livro na biblioteca
    """
    def __init__(self, titulo: str, autor: str, isbn: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel
    
    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - {status}"
    
    def emprestar(self) -> bool:
        """Tenta emprestar o livro, retorna True se bem-sucedido"""
        if self.disponivel:  # Controle de fluxo: if
            self.disponivel = False
            return True
        return False
    
    def devolver(self) -> None:
        """Marca o livro como disponível"""
        self.disponivel = True


class Biblioteca:
    """
    Classe principal que gerencia o acervo de livros
    """
    def __init__(self):
        self.acervo: Dict[str, Livro] = {}  # Dicionário ISBN -> Livro
    
    def adicionar_livro(self, livro: Livro) -> None:
        """Adiciona um novo livro ao acervo"""
        if livro.isbn in self.acervo:  # Controle de fluxo: if
            print(f"Livro com ISBN {livro.isbn} já existe no acervo.")
        else:
            self.acervo[livro.isbn] = livro
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")
    
    def buscar_livro(self, termo: str) -> List[Livro]:
        """
        Busca livros por título, autor ou ISBN
        Retorna uma lista de livros que correspondem ao termo
        """
        resultados = []
        termo = termo.lower()
        
        # Controle de fluxo: loop for
        for livro in self.acervo.values():
            if (termo in livro.titulo.lower() or 
                termo in livro.autor.lower() or 
                termo == livro.isbn.lower()):
                resultados.append(livro)
        
        return resultados
    
    def listar_livros(self, apenas_disponiveis: bool = False) -> None:
        """Lista todos os livros ou apenas os disponíveis"""
        print("\n=== LIVROS NA BIBLIOTECA ===")
        
        if not self.acervo:  # Controle de fluxo: if
            print("Nenhum livro cadastrado.")
            return
        
        # Controle de fluxo: loop for
        for livro in self.acervo.values():
            if not apenas_disponiveis or livro.disponivel:
                print(livro)
    
    def emprestar_livro(self, isbn: str) -> bool:
        """Tenta emprestar um livro pelo ISBN"""
        livro = self.acervo.get(isbn)
        if livro:
            return livro.emprestar()
        print(f"Livro com ISBN {isbn} não encontrado.")
        return False
    
    def devolver_livro(self, isbn: str) -> None:
        """Devolve um livro pelo ISBN"""
        livro = self.acervo.get(isbn)
        if livro:
            livro.devolver()
            print(f"Livro '{livro.titulo}' devolvido com sucesso.")
        else:
            print(f"Livro com ISBN {isbn} não encontrado.")
    
    def salvar_para_arquivo(self, arquivo: str = "biblioteca.json") -> None:
        """Salva o acervo em um arquivo JSON"""
        dados = []
        for livro in self.acervo.values():
            dados.append({
                'titulo': livro.titulo,
                'autor': livro.autor,
                'isbn': livro.isbn,
                'disponivel': livro.disponivel
            })
        
        with open(arquivo, 'w') as f:
            json.dump(dados, f)
        print(f"Dados salvos em {arquivo}")
    
    def carregar_de_arquivo(self, arquivo: str = "biblioteca.json") -> None:
        """Carrega o acervo de um arquivo JSON"""
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
            
            self.acervo = {}
            for item in dados:
                livro = Livro(
                    item['titulo'],
                    item['autor'],
                    item['isbn'],
                    item['disponivel']
                )
                self.acervo[livro.isbn] = livro
            print(f"Dados carregados de {arquivo}")
        
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado. Iniciando com acervo vazio.")


def mostrar_menu() -> None:
    """Exibe o menu de opções para o usuário"""
    print("\n=== MENU ===")
    print("1. Adicionar livro")
    print("2. Buscar livro")
    print("3. Listar todos os livros")
    print("4. Listar livros disponíveis")
    print("5. Emprestar livro")
    print("6. Devolver livro")
    print("7. Salvar dados")
    print("8. Carregar dados")
    print("0. Sair")


def obter_opcao() -> int:
    """Obtém a opção do usuário com tratamento de erro"""
    while True:  # Controle de fluxo: loop while
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Por favor, digite um número válido.")


def main() -> None:
    """Função principal que executa o programa"""
    biblioteca = Biblioteca()
    
    # Menu principal usando switch-like com dicionário (controle de fluxo)
    while True:
        mostrar_menu()
        opcao = obter_opcao()
        
        if opcao == 0:
            print("Saindo do sistema...")
            break
        elif opcao == 1:
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            isbn = input("ISBN do livro: ")
            livro = Livro(titulo, autor, isbn)
            biblioteca.adicionar_livro(livro)
        elif opcao == 2:
            termo = input("Digite título, autor ou ISBN para busca: ")
            resultados = biblioteca.buscar_livro(termo)
            if resultados:
                print("\nResultados da busca:")
                for livro in resultados:
                    print(livro)
            else:
                print("Nenhum livro encontrado.")
        elif opcao == 3:
            biblioteca.listar_livros()
        elif opcao == 4:
            biblioteca.listar_livros(apenas_disponiveis=True)
        elif opcao == 5:
            isbn = input("Digite o ISBN do livro a ser emprestado: ")
            if biblioteca.emprestar_livro(isbn):
                print("Livro emprestado com sucesso!")
        elif opcao == 6:
            isbn = input("Digite o ISBN do livro a ser devolvido: ")
            biblioteca.devolver_livro(isbn)
        elif opcao == 7:
            biblioteca.salvar_para_arquivo()
        elif opcao == 8:
            biblioteca.carregar_de_arquivo()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()