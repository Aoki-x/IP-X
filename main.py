import requests
import os
from termcolor import  colored
from time import sleep

#A função abaixo consulta o pais do usuário para traduzir os nomes(paises, continentes, etc) de acordo com o seu pais. 
def my_country(my_ip):
    req_country = requests.get(f"https://ipwho.is/{my_ip}")
    data = req_country.json()
    if data['country'] == 'Brazil':
        return "pt-BR"
    else:
        return "en"

def text_exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("\t\tVISITE O MEU PERFIL DO GITHUB: Aoki-x", "yellow"))
    sleep(2)

while True:

        
    os.system('cls' if os.name == 'nt' else 'clear')

    print(colored(f'''
                                        
    \t\t*@@@@*     *@@@***@@m         *@@@*   *@@* 
    \t\t  @@         @@   *@@m          @@@m  m@   
    \t\t  @@         @@   m@@            *@@m@*    
    \t\t  @@         @@@@@@@               @@@     
    \t\t  @!         @@         @@@@@    m@**@@m   
    \t\t  @!         @!                  @   *@@m  
    \t\t !!         @!                  !!   !!!  
    \t\t:!         !!                 !!    *!!! 
    \t\t :!: :      :!:!:              : : :    : ::
                                            
    \t\t\t----------------
    \t\t\t CONSULTA DE IP\t\t
    \t\t\t  POR: {colored("Aoki-x",  "yellow")}\t

    ''', "red"))

    try:
    #Aqui o sistema tentará pegar o seu ip externo.
        req_myip = requests.get("https://ipwho.is/")
        my_ip = req_myip.json()
        ip = my_ip['ip']
        print(f"\t(SEU IP: {ip}) | {my_country(ip)}")
    except:
        print(colored("\tHouve um erro ao tentar exibir o seu ip.", "red"))

    #Aqui daremos início a consulta a API do Whois
    ip = input("\n\tDigite o ip do alvo ou N para sair: ")
    if ip == 'N' or ip == 'n':
        text_exit()
        break
    else:
        req_api = requests.get(f"https://ipwho.is/{ip}?lang={my_country(ip)}")

    #Aqui verificaremos o status da API, se for 200 é porque não houve problemas.
    if req_api.status_code == 200:

        data = req_api.json()
        print(f'''
            SUCCESS: {colored(data['success'], "blue")}
            \n\t  -----------------\n
            IP: {colored(data['ip'], "yellow")}\n
            TIPO: {data['type']}\n
            CONTINENTE: {data['continent']}| {data['continent_code']}\n
            PAIS: {colored(data['country'], "green")}| {data['country_code']}\n
            CAPITAL: {colored(data['capital'], "green")}\n
            REGIÃO: {colored(data['region'], "green")}| {data['region_code']}\n
            CIDADE: {colored(data['city'], "green")}\n
            LATITUDE: {data['latitude']}\n
            LONGITUDE: {data['longitude']}\n
            CONEXÕES: \n
            \t |----->ORG: {colored(data['connection']['org'], "blue")}\n
            \t |----->FORNECEDOR: {colored(data['connection']['isp'], "blue")}\n
            \t |----->DOMÍNIO: {colored(data['connection']['domain'], "blue")}\n
            FUSO HORARIO: \n
            \t |----->ID: {data['timezone']['id']}\n
            \t |----->ABBR: {data['timezone']['abbr']}\n
            \t |----->HORARIO: {data['timezone']['current_time']}
            \n\t  -----------------\n
        ''')

        try:
        #Aqui tentaremos solicitar a segurança do alvo, funcionará apenas se você tiver a API premium.
            print(f'''
            SEGURANÇA: \n
            \t ANONIMO: {data['security']['anonymous']}\n
            \t PROXY: {data['security']['proxy']}\n
            \t VPN: {data['security']['vpn']}\n
            \t HOSTING: {data['security']['hosting']}\n
            ''')
        except:
            print(colored("\tNão foi possível consultar a segurança do alvo.", "red"))
        
        sleep(1)

        back = input(f"\n\tDeseja consultar novamente?\n\t1 - Sim(Yes)\n\t2 - Não(No)\n\t|-->")
        if back == '1':
            continue
        else:
            text_exit()
            break
    else:
        print("\t\tOcorreu um erro, verifique a sua Internet.")
