#Importa o modulo datetime para trabalhar com datas e descobrir a data atual
import datetime

#Definindo as constantes necessarias
def simular_anos_trabalhados(nome, dia_de_nascimento, mes_de_nascimento, ano_de_nascimento):
    
    #Definindo as variaveis
    data_de_nascimento = datetime.date(ano_de_nascimento, mes_de_nascimento, dia_de_nascimento)
    hoje = datetime.date.today()
    idade = hoje.year - data_de_nascimento.year - ((hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day))
    maioridade = (data_de_nascimento.year + 18)
    aposentadoria = (maioridade + 47)
    ano_inicial = ano_de_nascimento + 18
    
    #Informando a idade atual do usuario
    print(f"Minha idade atual é: {idade} anos.")
    
    #Caso seja aniversario do usuario ele ganha um parabens
    if hoje.month == data_de_nascimento.month and hoje.day == data_de_nascimento.day:
        print(f"- Inclusive, feliz aniversário {nome}! -")

    #Informando o ano em que o usuario completou 18 anos
    print(f"No ano de {maioridade}, completei 18 anos, isso quer dizer que em: ")
    
    #Apartir do ano de maioridade ate o ano de aposentadoria, imprime ano a ano, com uma mensagem diferente caso o ano seja par ou impar 
    while ano_inicial <= aposentadoria:
        print(f"{ano_inicial}: Eu, {nome}, {'trabalhei' if ano_inicial % 2 == 0 else 'não trabalhei'} esse ano.")
        ano_inicial += 1
        
    #Informa o fim da simulacao
    print("Simulação encerrada aos 65 anos.")

#Entrada de dados do usuario
nome = input("Digite seu nome (Exemplo: Max): ")
dia_de_nascimento = int(input("Digite o dia de seu nascimento(Exemplo: 17): "))
mes_de_nascimento = int(input("Digite o mês de seu nascimento (Exemplo: 8): "))
ano_de_nascimento = int(input("Digite o ano de seu nascimento (Exemplo: 1997): "))

#Inicio da simulacao
simular_anos_trabalhados(nome, dia_de_nascimento, mes_de_nascimento, ano_de_nascimento)
