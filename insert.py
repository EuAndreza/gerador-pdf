from generator import geradorPDF
import sqlite3
import shutil

conectar = sqlite3.connect('clientes.db')
cursor = conectar.cursor()

salvar = []

def adicionar(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x):
	cursor.execute(""" INSERT INTO cliente(nome_cliente,estado_civil_cliente,profissao_cliente,
		cpf_cliente,rg_cliente,rua_cliente, bairro_cliente, municipio_cliente,estado_cliente,cep_cliente,
		telefone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,
		rg_procurador,rua_procurador,bairro_procurador,municipio_procurador,estado_procurador,cep_procurador,
		telefone_procurador,solicitacao_procurador)
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
		(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x))
	conectar.commit()

def exibir():
	cursor.execute("""SELECT nome_cliente,cpf_cliente FROM cliente """)
	for linha in cursor.fetchall():
		print(linha)

def gerar_pdf(s):
	geradorPDF(s[0][0],s[0][1],s[0][2],s[0][3],s[0][4],s[0][5],s[0][6],s[0][7],s[0][8],s[0][9],s[0][10],
		s[0][11],s[0][12],s[0][13],s[0][14],s[0][15],s[0][16],s[0][17],s[0][18],s[0][19],s[0][20],s[0][21],s[0][22])
	shutil.move('{}.pdf'.format(s[0][0]),'/home/usuario/Área de Trabalho/')
	salvar.clear()

def consultar_cpf(x):
	cursor.execute(""" SELECT nome_cliente,estado_civil_cliente,profissao_cliente,
		cpf_cliente,rg_cliente,rua_cliente, bairro_cliente, municipio_cliente,estado_cliente,cep_cliente,
		telefone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,
		rg_procurador,rua_procurador,bairro_procurador,municipio_procurador,estado_procurador,cep_procurador,
		telefone_procurador,solicitacao_procurador FROM cliente WHERE cpf_cliente = ?""",
		(x,))

def deletar_dados(x):
	cursor.execute(""" DELETE FROM cliente WHERE cpf_cliente = ?""",
		(x,))
	print('\n***Dados do cliente deletados com sucesso***\n')
	conectar.commit()
	
	for linha in cursor.fetchall():
		salvar.append(linha)

	conectar.commit()

cont = 'sim'

print("*** BEM VINDX AO GENERATOR ***")

while cont == 'sim' or cont == 's':
	
	pergunta = input("\nDigite (ADD) para adicionar novo cliente,(VER) para visualizar clientes cadastrados\n(SAIR) "
			"para sair do sistema (DEL) para apagar dados do cliente\n*").lower()

	if pergunta == 'add' or pergunta == 'ad':

		print('\n*** DADOS DO CLIENTE ***\n')

		nomeOr = input('\nDigite o nome\n\n*')
		estado_civilOr = input('\nDigite o estado civil\n\n*')
		profissaoOr = input('\nDigite a profissão\n\n*')
		cpfOr = input('\nDigite o cpf\n\n*')
		rgOr = input('\nDigite o rg\n\n*')
		ruaOr = input('\nDigite o nome da rua\n\n*')
		bairroOr = input('\nDigite o nome do bairro\n\n*')
		municipioOr = input('\nDigite o nome do municipio\n\n*')
		estadorOr = input('\nDigite o nome do estado\n\n*')
		cepdOr = input('\nDigite o cep\n\n*')
		foneOr = input('\nDigite o numero de telefone\n\n*')

		print('\n*** DADOS DO PROCURADOR ***\n')

		nomePro = input('\nDigite o nome do Procurador\n\n*')
		estado_civilPro = input('\nDigite estado civil do procurador\n\n*')
		profissaoPro = input('\nDigite a profissao do Procurador\n\n*')
		cpfPro =input('\nDigite o cpf do Procurador\n\n*')
		rgPro = input('\nDigite o rg do Procurador\n\n*')
		ruaPro = input('\nDigite a rua do Procurador\n\n*')
		bairroPro = input('\nDigite o bairro do Procurador\n\n*')
		municipioPro = input('\nDigite o municipio do Procurador\n\n*')
		estadoPro = input('\nDigite o estado do Procurador\n\n*')
		cepPro = input('\nDigite o cep do Procurador\n\n*')
		fonePro = input('\nDigite o telefone do Procurador\n\n*')

		texto = input('\nDigite o o motivo para pedido da procuracao\n\n*')

		adicionar(nomeOr,estado_civilOr,profissaoOr,cpfOr,rgOr,ruaOr,bairroOr,municipioOr,estadorOr,cepdOr,foneOr,
			nomePro,estado_civilPro,profissaoPro,cpfPro,rgPro,ruaPro,bairroPro,municipioPro,estadoPro,cepPro,fonePro,texto)

	elif pergunta == 'ver' or pergunta == 'v':
		exibir()
		pergunta1 = input("\nPara gerar uma procuracao digite(PDF), para deletar digite(DEL),(SAIR) para sair do sistema\n*").lower()
		if pergunta1 == 'pdf' or pergunta1 == 'p':
			cpf = input('\nDigite o numero do pdf que deseja gerar a procuracao\n\n*')
			consultar_cpf(cpf)
			gerar_pdf(salvar)
		elif pergunta1 == 'del' or pergunta1 == 'd':
			cpf = input('\nDigite o numero do pdf que deseja excluir\n\n*')
			deletar_dados(cpf)
			exibir()
	elif pergunta == 'del' or pergunta == 'd':
		cpf = input('\nDigite o numero do pdf que deseja excluir\n\n*')
		deletar_dados(cpf)
		exibir()
	elif pergunta == 'sair' or pergunta == 's':
		cont = 'nao'
	print('\nOBRIGADO')

conectar.close()