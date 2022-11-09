# API de Agenda de Contatos

# Sobre o Projeto

O projeto é referente a uma agenda de contatos. Esse projeto foi proposto na matéria de Sistemas Distribuidos do Curso de Análise e Desenvolvimento de sistema da UNA.

# Índice/Sumário

* [Sobre](#sobre-o-projeto)
* [Sumário](#índice/sumário)
* [Requisitos Funcionais](#requisitos-funcionais)
* [Tecnologias Usadas](#tecnologias-usadas)
* [Autora](#autora)

# Requisitos Funcionais 

- [x] Criar a base de dados agenda.db em SQLite
- [x] Criar a tabela contatos (id, nome, empresa, telefone, email)
- [x] Implementar CRUD completo:
	- [x] Criar contato (Método POST -> INSERT no database)
	- [x] Recuperar contato (Método GET -> SELECT no database)
	- [x] Atualizar contato (Método PUT -> UPDATE no database)
	- [x] Deletar contato (Método DELETE -> DELETE no database)
- [x] Implementar consultas:
	- [x] por nome
	- [x] por empresa
	- [x] por e-mail
	OBS: As consultas devem ser feitas de forma que seja possível consultar por coincidência exata ou parcial
- [x] Criar segundo endpoint filtrando os contatos por empresa e use o protocolo http (404) em caso de falha.
- [x] Criar terceiro endpoint inserindo um novo registro e usar o protocolo http.
- [x] Criar quarto endpoint deletando um novo registro e usar o protocolo http.
- [x] Utilize a conexão com o banco de dados para fazer as operações CRUD

# Tecnologias Usadas

- [Python]()
- [Flask]()
- [SQLite]()


# Autora

<table>
  <tbody>
    <tr>
    <td align="center">
	  	<a href="https://github.com/annekarolinefc">
			<img src="imagens/ft_Anne.jpg" width="100px;" alt="Anne Karoline"/>
			<br />
			<sub><b>Anne K. F. Carmo</b></sub>
		</a>
		<br />
		<a href="https://github.com/annekarolinefc" title="Code">💻</a>
	</td>
    </tr>
	</tbody>
<table>
