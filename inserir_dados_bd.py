import sqlite3

conectar = sqlite3.connect('clientes.db')
cursor = conectar.cursor()

def tabela():
	cursor.execute("""
		CREATE TABLE cliente(
		id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
		nome_cliente VARCHAR(100) NOT NULL,
		estado_civil_cliente VARCHAR(20) NOT NULL,
		profissao_cliente VARCHAR(70) NOT NULL,
		cpf_cliente VARCHAR(14) NOT NULL,
		rg_cliente VARCHAR(9) NOT NULL,
		rua_cliente VARCHAR(100) NOT NULL,
		bairro_cliente VARCHAR(100) NOT NULL,
		municipio_cliente VARCHAR(100) NOT NULL,
		estado_cliente VARCHAR(50) NOT NULL,
		cep_cliente VARCHAR(9) NOT NULL,
		telefone_cliente VARCHAR(15),

		nome_procurador VARCHAR(100) NOT NULL,
		estado_civil_procurador VARCHAR(20) NOT NULL,
		profissao_procurador VARCHAR(70) NOT NULL,
		cpf_procurador VARCHAR(14) NOT NULL,
		rg_procurador VARCHAR(9) NOT NULL,
		rua_procurador VARCHAR(100) NOT NULL,
		bairro_procurador VARCHAR(100) NOT NULL,
		municipio_procurador VARCHAR(100) NOT NULL,
		estado_procurador VARCHAR(50) NOT NULL,
		cep_procurador VARCHAR(9) NOT NULL,
		telefone_procurador VARCHAR(15)

		solicitacao_procurador TEXT NOT NULL

		);
		""")