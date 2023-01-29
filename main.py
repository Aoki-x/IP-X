import requests
import os
from termcolor import  colored

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

    #A função abaixo consulta o pais do usuário para traduzir os nomes(paises, continentes, etc) de acordo com o seu pais. 
    def my_country(my_ip):
        req_country = requests.get(f"https://ipwho.is/{my_ip}")
        data = req_country.json()
        if data['country'] == 'Brazil':
            return "pt-BR"
        else:
            return "en"


    try:
    #Aqui o sistema tentará pegar o seu ip externo.
        req_myip = requests.get("http://checkip.dyndns.org")
        my_ip = req_myip.text.split(" ")[-1].strip().split("<")[0].strip()
        print(f"\t(SEU IP: {my_ip}) | {my_country(my_ip)}")
    except:
        print(" Houve um erro ao tentar exibir o seu ip.")

    #Aqui daremos início a consulta a API do Whois
    ip = input("\n\tDigite o ip do alvo ou aperte ENTER-> ")
    req_api = requests.get(f"https://ipwho.is/{ip}?lang={my_country(my_ip)}")

    #Aqui verificaremos o status da API, se for 200 é porque não houve problemas.
    if req_api.status_code == 200:

    #Aqui na variável data puxaremos o Json. Caso queira ver, logo abaixo da variável coloque - > print(data)
        data = req_api.json()
        print(f'''
            SUCCESS: {data['success']}
            \n\t  -----------------\n
            IP: {data['ip']}\n
            TIPO: {data['type']}\n
            CONTINENTE: {data['continent']}| {data['continent_code']}\n
            PAIS: {data['country']}| {data['country_code']}\n
            CAPITAL: {data['capital']}\n
            REGIÃO: {data['region']}| {data['region_code']}\n
            CIDADE: {data['city']}\n
            LATITUDE: {data['latitude']}\n
            LONGITUDE: {data['longitude']}\n
            CONEXÕES: \n
            \t |----->ORG: {data['connection']['org']}\n
            \t |----->FORNECEDOR: {data['connection']['isp']}\n
            \t |----->DOMÍNIO: {data['connection']['domain']}\n
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
            print("\t\033[0;31;41mNão foi possível consultar a segurança do alvo.\033[0m")
        
        try:
            back = int(input("\tDeseja consultar novamente?\n\t1 - Sim(Yes)\n\t2 - Não(No)\n\t|-->"))
        except ValueError as error:
            print(colored(error, "red"))
            back = int(input("\tDeseja consultar novamente?\n\t1 - Sim(Yes)\n\t2 - Não(No)\n\t|-->"))
        if back == 1:
            continue
        else:
            break
    else:
        print("Ocorreu um erro, verifique a sua Internet.")