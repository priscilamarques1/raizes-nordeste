# Raízes do Nordeste

 1. Descrição do projeto

Projeto acadêmico desenvolvido para o estudo de caso Raízes do Nordeste, no âmbito da disciplina Projeto: Desenvolvimento Back-End.

Conforme a orientação da professora, o desenvolvimento foi concentrado em um módulo do sistema. A área de maior ênfase escolhida para o trabalho foi **Quality Assurance (QA)**, por meio do planejamento, execução e documentação de testes de software.

 2. Objetivo

Desenvolver um módulo funcional de API REST para gerenciamento de produtos e criação de pedidos, utilizando práticas de QA para verificar o comportamento da aplicação, validar regras de negócio e identificar falhas.

 3. Tecnologias utilizadas

- Python 3.11.9
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Swagger/OpenAPI para documentação e execução de testes manuais

 4. Módulo implementado

O módulo principal é o gerenciamento de produtos, com operações CRUD:

- Create: cadastrar produtos.
- Read: consultar a lista de produtos e buscar um produto pelo identificador.
-Update: atualizar informações de produtos.
-Delete: excluir produtos.

Também foi implementado um endpoint para criação de pedidos, com validações de quantidade, cadastro e disponibilidade do produto, além do cálculo automático do valor total.

5. Atividades de QA

Foram realizados testes manuais utilizando o Swagger, incluindo:

- Criação de pedidos com dados válidos.
- Validação de quantidade zero e negativa.
- Verificação de produtos indisponíveis ou não cadastrados.
- Verificação do cálculo automático do valor total.
- Consulta de produtos com identificadores inexistentes.
- Reteste após a correção de uma falha identificada durante os testes.

Os casos de teste, resultados e evidências de execução estão documentados no relatório acadêmico.

 6. Como executar o projeto

1. Instale o Python 3.11 ou uma versão compatível.
2. Abra a pasta do projeto no terminal.
3. Instale as dependências:

   `python -m pip install -r requirements.txt`

4. Inicie a API:

   `python -m uvicorn main:app --reload`

5. Acesse a documentação interativa:

   `http://127.0.0.1:8000/docs`

 7. Escopo e limitações

O projeto concentra-se em um módulo funcional do estudo de caso, com ênfase em QA. Não representa a implementação completa de todos os processos de uma rede de lanchonetes.

8. Relatório acadêmico

O relatório acadêmico apresenta a análise do projeto, a implementação realizada, o plano de testes, os resultados obtidos e as capturas de tela utilizadas como evidências.
