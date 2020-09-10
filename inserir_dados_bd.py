import sqlite3
from generator import geradorPDF
import shutil

conectar = sqlite3.connect('clientes.db')
cursor = conectar.cursor()

#armazenando os dados que são pegos do banco
salvar = []

def exibir_cliente():
	cursor.execute("""SELECT nome_cliente,cpf_cliente FROM cliente """)
	for linha in cursor.fetchall():
		print(linha)

def inserir_dados(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x):
	cursor.execute(""" INSERT INTO cliente(nome_cliente,estado_civil_cliente,profissao_cliente,
		cpf_cliente,rg_cliente,rua_cliente, bairro_cliente, municipio_cliente,estado_cliente,cep_cliente,
		telefone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,
		rg_procurador,rua_procurador,bairro_procurador,municipio_procurador,estado_procurador,cep_procurador,
		telefone_procurador,solicitacao_procurador)
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
		(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x))
	conectar.commit()

def consulta_cpf(x):
	cursor.execute(""" SELECT nome_cliente,estado_civil_cliente,profissao_cliente,
		cpf_cliente,rg_cliente,rua_cliente, bairro_cliente, municipio_cliente,estado_cliente,cep_cliente,
		telefone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,
		rg_procurador,rua_procurador,bairro_procurador,municipio_procurador,estado_procurador,cep_procurador,
		telefone_procurador,solicitacao_procurador FROM cliente WHERE cpf_cliente = ?""",
		(x,))
	
	for linha in cursor.fetchall():
		salvar.append(linha)

	conectar.commit()

def gerar_pdf(s):
	geradorPDF(s[0][0],s[0][1],s[0][2],s[0][3],s[0][4],s[0][5],s[0][6],s[0][7],s[0][8],s[0][9],s[0][10],
		s[0][11],s[0][12],s[0][13],s[0][14],s[0][15],s[0][16],s[0][17],s[0][18],s[0][19],s[0][20],s[0][21],s[0][22])
	
	#move o arquivo para a area de trabalho
	shutil.move('{}.pdf'.format(s[0][0]),'/home/usuario/Área de Trabalho/')

	print("\n***Procuração gerado com sucesso***\n***O arquivo se encontra na sua area de trabalho***\n")

def deletar_bd(x):
	cursor.execute(""" DELETE FROM cliente WHERE cpf_cliente = ?""",
		(x,))
	print('\n***Dados do cliente deletados com sucesso***\n')
	conectar.commit()

cont = 'sim'
while cont =='sim' or cont == 's':

	per = input("\nDigite (ADD) para adicionar novo cliente ou (VER) para visualizar clientes cadastrados\nou (SAIR) "
		"para sair do sistema ou (DEL) para apagar dados do cliente\n*").lower()

	if per == 'ver':
		exibir_cliente()
		
		per1 = input("\nPara gerar uma procuracao digite(PDF), para deletar digite(DEL)\n*").lower()
		
		if per1 == 'pdf' or per1 == 'p':
			per2 = input('\nDigite o cpf do seu cliente\n*')
			consulta_cpf(per2)
			gerar_pdf(salvar)
			cont = input('\ndeseja algo mais? digite sim ou nao\n*').lower()
			if cont == 'nao' or cont == 'n':
				print("\n***Obrigadx!***\n")

		elif per1 == 'del' or per1 == 'd':
			per2 = input('\nDigite o cpf do seu cliente\n*')
			deletar_bd(per2)
			exibir_cliente()
			cont = input('\ndeseja algo mais? digite sim ou nao\n*').lower()
			if cont == 'nao' or cont == 'n':
				print("\n***Obrigadx!***\n")

	elif per == 'add':
		print("*****DADOS DO CLIENTE*****\n")
		nomeOr = input('\nDigite o nome do cliente\n*')
		estado_civilOr = input('\nDigite o estado civil do cliente\n*')
		profissaoOr = input('\nDigite a profissão do cliente\n*')
		cpfOr = input('\nDigite o cpf do cliente\n*')
		rgOr = input('\nDigite o rg do cliente\n*')
		ruaOr = input('\nDigite a rua onde reside o cliente\n*')
		bairroOr = input('\nDigite o bairro onde reside o cliente\n*')
		municipioOr = input('\nDigite o municipio onde reside o cliente\n*')
		estadorOr = input('\nDigite o estado onde reside o cliente\n*')
		cepdOr = input('\nDigite o cep da rua onde o cliente reside\n*')
		foneOr = input('\nDigite o numero de telefone do cliente\n*')

		print("\n*****DADOS DO PROCURADXR*****\n")
		nomePro = input('\nDigite o nome do Procurador\n*')
		estado_civilPro = input('\nDigite estado civil do procurador\n*')
		profissaoPro = input('\nDigite a profissao do Procurador\n*')
		cpfPro =input('\nDigite o cpf do Procurador\n*')
		rgPro = input('\nDigite o rg do Procurador\n*')
		ruaPro = input('\nDigite a rua onde reside o Procurador\n*')
		bairroPro = input('\nDigite o bairro onde reside o Procurador\n*')
		municipioPro = input('\nDigite o municipio onde reside o Procurador\n*')
		estadoPro = input('\nDigite o estado onde reside o Procurador\n*')
		cepPro = input('\nDigite o cep da rua onde reside o Procurador\n*')
		fonePro = input('\nDigite o numero de telefone do Procurador\n*')

		texto = input('\nDigite o motivo para criacao dessa procuracao\n*')

		inserir_dados(nomeOr,estado_civilOr,profissaoOr,cpfOr,rgOr,ruaOr,bairroOr,municipioOr,estadorOr,cepdOr,foneOr,
		nomePro,estado_civilPro,profissaoPro,cpfPro,rgPro,ruaPro,bairroPro,municipioPro,estadoPro,cepPro,fonePro,texto)

		print('\n***DADOS ADICIONADOS NO BANCO COM SUCESSO***\n')
		
		salvar.clear()
		consulta_cpf(cpfOr)
		gerar_pdf(salvar)

		cont = input('\nDeseja algo mais? digite sim ou nao\n*').lower()
		if cont == 'nao' or cont == 'n':
			print("\n***Obrigadx!***\n")
	elif per == 'sair' or per =='s':
		print("\n***Obrigadx!***\n")
		cont = 'nao'

	elif per == 'del' or per == 'd':
		exibir_cliente()
		per2 = input('\nDigite o cpf do seu cliente\n*')
		deletar_bd(per2)
		exibir_cliente()
		cont = input('\ndeseja algo mais? digite sim ou nao\n*').lower()
		if cont == 'nao' or cont == 'n':
			print("\n***Obrigadx!***\n")

conectar.close()