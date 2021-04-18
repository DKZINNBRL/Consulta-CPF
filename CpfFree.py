import requests, json, re
from os import system
from time import sleep
from subprocess import run

# Tabela de cores:

Red = "\033[1;31m"
Verde = "\033[1;32m"
Azul = "\033[1;34m"
Branco = "\033[1;97m"

# Inicio do script:
	
print(f"{Azul}Verificando por atualizações...{Azul}")
sleep(1)
print(f"{Azul}1...{Azul}")
sleep(1)
print(f"{Azul}2...{Azul}")
sleep(1)
print(f"{Azul}3...{Azul}")
sleep(1)
print(f"{Azul}4...{Azul}")
sleep(1)
print(f"{Azul}5...{Azul}")
sleep(1)
print(f"\n{Azul}Entrando no sistema...{Azul}")
sleep(2)

system("clear")

print(f"{Verde}Me apoie com um pix de R$ 2?\nChave: d03a31f7-a5c9-4821-8371-c1c91be8a095\n\nTelegram: @DKZINNBR{Verde}")

def pergunta():
		pergunta = input(f"\n{Verde}Digite o CPF: {Verde}")
		cpf = re.sub('[^0-9]+', '', pergunta)
		consulta(cpf)

def consulta(cpf):
    try:
        r = requests.get('http://poisonbr.sytes.net:12344/ConsultaCPF/' + cpf).text
        result1 = r.replace("{", "")
        result2 = result1.replace("}", "")
        result3 = result2.replace(",", "")
        result4 = result3.replace("[", "")
        result5 = result4.replace("]", "")
        result = result5.replace('"', "")
        print(f"\n{Branco}{result}{Branco}")
        nova = input(f'{Verde}Realizar outra consulta? [ s/n ]: {Verde}').lower()

        if nova == 's' or nova == 'sim':
            pergunta()

        else:
            print(f'\n{Red}Me acompanhe no telegram\n@DKZINNBR{Red}')
            exit()

    except Exception:
        print(f'resul')
        pergunta()


if __name__ == '__main__':
    try:
        pergunta()

    except Exception as e:
        print(f'erro')