from generator import geradorPDF

nomeOr = input('digite o nome')
estado_civilOr = input('digite o estado civil')
profissaoOr = input('digite a profissão')
cpfOr = input('digite o cpf')
rgOr = input('digite o rg')
ruaOr = input('digite a rua')
bairroOr = input('digite o bairro')
municipioOr = input('digite o municipio')
estadorOr = input('digite o estado')
cepdOr = input('digite o cep')
foneOr = input('digite o telefone')


nomePro = input('digite o nome do Procurador')
estado_civilPro = input('digite estado civil do procurador')
profissaoPro = input('digite a profissao do Procurador')
cpfPro =input('digite o cpf do Procurador')
rgPro = input('digite o rg do Procurador')
ruaPro = input('digite a rua do Procurador')
bairroPro = input('digite o bairro do Procurador')
municipioPro = input('digite o municipio do Procurador')
estadoPro = input('digite o estado do Procurador')
cepPro = input('digite o cep do Procurador')
fonePro = input('digite o telefone do Procurador')

texto = input('digite o texto')

geradorPDF(nomeOr,estado_civilOr,profissaoOr,cpfOr,rgOr,ruaOr,bairroOr,municipioOr,estadorOr,cepdOr,foneOr,
	nomePro,estado_civilPro,profissaoPro,cpfPro,rgPro,ruaPro,bairroPro,municipioPro,estadoPro,cepPro,fonePro,texto)