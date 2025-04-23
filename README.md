Sistema de Gerenciamento de Biblioteca em Python
📚 Visão Geral
Este sistema permite gerenciar o acervo de uma biblioteca com operações como cadastro, busca, empréstimo e devolução de livros, além de persistência dos dados em arquivo JSON.

🛠️ Requisitos
Python 3.6+

Nenhuma dependência externa necessária

🔧 Instalação
Clone o repositório:

Execute o sistema:

bash
python biblioteca.

📋 Funcionalidades

Requisitos Funcionais

RF01	Cadastrar novos livros (título, autor, ISBN)
RF02	Buscar livros por título, autor ou ISBN
RF03	Listar todos os livros ou apenas disponíveis
RF04	Emprestar livros (marcar como indisponível)
RF05	Devolver livros (marcar como disponível)
RF06	Salvar e carregar dados em arquivo JSON

Requisitos Não Funcionais

Desenvolvido em Python com POO (2 classes, 6+ métodos)
Interface via terminal com menu interativo
Armazenamento persistente em JSON

🧪 Testes

Testes Manuais (Interface)

Caso 1: Cadastro e Listagem

Adicione: "Dom Casmurro", "Machado de Assis", "123"
Liste livros (opção 3)
Esperado: Confirmação de cadastro e livro listado como "Disponível"

Caso 2: Empréstimo e Devolução

Empreste livro (opção 5, ISBN "456")
Liste disponíveis (opção 4)
Devolva livro (opção 6, ISBN "456")
Esperado:
Status "Emprestado" após empréstimo
Livro não aparece nos disponíveis
Status "Disponível" após devolução

Caso 3: Persistência

Salve dados (opção 7)
Reinicie o programa
Carregue dados (opção 8)
Esperado: Livros mantidos após recarregar

Testes Automatizados (Pytest)
Como executar:

pytest test_biblioteca.py -v