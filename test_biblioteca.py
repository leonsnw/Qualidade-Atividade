import pytest
from biblioteca import Livro, Biblioteca 

#para rodar o teste, digite "pytest test_biblioteca.py -v" no terminal !!!

# Fixture para criar uma biblioteca de teste com dados iniciais
@pytest.fixture
def biblioteca_teste():
    bib = Biblioteca()
    bib.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", "123"))
    bib.adicionar_livro(Livro("1984", "George Orwell", "456"))
    return bib

# Testes para a classe Livro
def test_livro_emprestar():
    livro = Livro("Python Guide", "Autor X", "789")
    assert livro.disponivel == True  # Livro começa disponível
    assert livro.emprestar() == True  # Empréstimo bem-sucedido
    assert livro.disponivel == False  # Agora está emprestado

def test_livro_emprestar_indisponivel():
    livro = Livro("Python Guide", "Autor X", "789", disponivel=False)
    assert livro.emprestar() == False  # Falha ao emprestar (já emprestado)

# Testes para a classe Biblioteca
def test_buscar_livro_existente(biblioteca_teste):
    resultados = biblioteca_teste.buscar_livro("Dom")
    assert len(resultados) == 1
    assert resultados[0].titulo == "Dom Casmurro"

def test_emprestar_livro_disponivel(biblioteca_teste):
    assert biblioteca_teste.emprestar_livro("123") == True  # ISBN do "Dom Casmurro"
    assert biblioteca_teste.acervo["123"].disponivel == False  # Agora emprestado

def test_salvar_e_carregar_arquivo(tmp_path, biblioteca_teste):
    arquivo = tmp_path / "teste_biblioteca.json"
    biblioteca_teste.salvar_para_arquivo(arquivo)
    
    nova_bib = Biblioteca()
    nova_bib.carregar_de_arquivo(arquivo)
    assert len(nova_bib.acervo) == 2  # Verifica se os 2 livros foram carregados