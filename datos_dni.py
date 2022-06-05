#from email.quoprimime import body_check
import os
#from telnetlib import PRAGMA_HEARTBEAT
import time
from bs4 import BeautifulSoup
#from matplotlib.pyplot import title
from mechanize import Browser
from colorama import Back, Fore, init
import requests
from requests.structures import CaseInsensitiveDict

#colores
init()
verde = Fore.GREEN
lverde = Fore.LIGHTGREEN_EX
rojo = Fore.RED
lrojo = Fore.LIGHTRED_EX
amarillo = Fore.YELLOW
blanco = Fore.WHITE
cyan = Fore.CYAN
violeta = Fore.MAGENTA
azul = Fore.BLUE
lazul = Fore.LIGHTBLUE_EX
fblanco = Back.WHITE
fin = Back.RESET
negro= Fore.BLACK

#FUNCIONES
def consultar_DNI():
    dni = input(f"{azul}Ingresa el numero de DNI: ")
    url = "https://www.dayangels.xyz/api/reniec/reniec-dni"
    API_TOKEN= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4NCwiY29ycmVvIjoibGlsanVtZXg3NDFAZ21haWwuY29tIiwiaWF0IjoxNjU0MjI2NDQxfQ.cwgCEOPkXNZVEeY2uNp260W--qhh7cQ_X-WlCvTswzA"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    res = requests.post(url, headers=headers, json={"dni": dni})
    data = res.json()
    mensaje = data["message"]
    if data["success"] == False:
        print(f"{amarillo}DNI no encontrado, {rojo} {mensaje}")
    else:
        print(f"{amarillo}DNI encontrado, con {verde} {mensaje}")
        print(f"{negro} {fblanco}NOMBRES: ", data["result"]["nombres"],f"{fin}","\n",f"{fblanco}APELLIDO PATERNO: ", data["result"]["paterno"],f"{fin}","\n",f"{fblanco}APELLIDO MATERNO: ", data["result"]["materno"],f"{fin}","\n",f"{fblanco}SEXO:", data["result"]["sexo"],f"{fin}")
        print(f"{rojo}-----------------------------------------------------")

def consultar_NOMBRE():
    print(f"{amarillo}Escribe los nombres y apellidos de forma correcta")
    nombre = input(str(f"{azul}Ingresa el nombre: "))
    apellidop = input(str(f"{azul}Ingresa el apellido paterno: "))
    apellidom = input(str(f"{azul}Ingresa el apellido materno: "))

    url1 = "https://www.dayangels.xyz/api/reniec/reniec-nombres"
    API_TOKEN= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4NCwiY29ycmVvIjoibGlsanVtZXg3NDFAZ21haWwuY29tIiwiaWF0IjoxNjU0MjI2NDQxfQ.cwgCEOPkXNZVEeY2uNp260W--qhh7cQ_X-WlCvTswzA"
    headers1 = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    res1 = requests.post(url1, headers=headers1, json={ "paterno": apellidop, "materno": apellidom, "nombres": nombre })
    data1 = res1.json()
    mensaje1 = data1["message"]
    if data1["success"] == False:
        print(f"{amarillo}Datos no encontrados, {rojo} {mensaje1}")
    else:
        print(f"{amarillo}Datos encontrados, con {verde} {mensaje1}")
        #print(data1["result"])
        for x in data1["result"]:
            print(x["dni"], x["paterno"], x["materno"], x["nombres"])
        print(f"{rojo}-----------------------------------------------------")  
def consultar_NOMBRE2():
    nombre1 = input(str(f"{azul}Ingresa el nombre: "))
    apellidop1 = input(str(f"{azul}Ingresa el apellido paterno: "))
    apellidom1 = input(str(f"{azul}Ingresa el apellido materno: "))

    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')] 

    br.open("https://www.eldni.com/pe/buscar-por-nombres")
    br.select_form(nr=0)

    br["nombres"] = nombre1
    br["apellido_p"] = apellidop1
    br["apellido_m"] = apellidom1

    response = br.submit()
    data = response.read()
    #soup = BeautifulSoup(data, "lxml")
    soup = BeautifulSoup(data, "html.parser")
    #numero de datos encontrados
    titulo = soup.find("h4", {"class": "text-center"})
    t = titulo.get_text()
    print(f"\n {amarillo} {t} \n", sep="")
    #imprimir cabecera de la tabla
    #print(f"{violeta}{fblanco}  DNI  | NOMBRES    |APELLIDO PATERNO|APELLIDO MATERNO")
    #imprimir datos de la tabla
    #print(soup.find_all('tr') & soup.find_all('th'))
    body = soup.find_all('tr')
    for x in body:
        print(f"{cyan}",x.get_text("  |  ", strip=True))
    print(f"{rojo}-----------------------------------------------------")
    #h, [_, *d] = [i.text for i in soup.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('th')]
    #result = [dict(zip(h, i)) for i in d]
    #print(result)
    #for x in result:
    #    print(x)
    #try: 
    #    response = requests.get(url2, headers = headers2 ,timeout=3) 
    #    response.raise_for_status()                 # Raise error in case of failure 
    #except requests.exceptions.HTTPError as httpErr: 
    #    print ("Http Error:",httpErr) 
    #except requests.exceptions.ConnectionError as connErr: 
    #    print ("Error Connecting:",connErr) 
    #except requests.exceptions.Timeout as timeOutErr: 
    #    print ("Timeout Error:",timeOutErr) 
    #except requests.exceptions.RequestException as reqErr: 
    #    print ("Something Else:",reqErr)
    #text = res2.text
    #print(text)
    #soup = BeautifulSoup(text, "lxml")
    #text2 = soup.get_text()
    #print(text2)
    #new_b = text2[131:]
    #characters = "ver"
    #string = ''.join( x for x in new_b if x not in characters)
    #print(string)

def consultar_OPERADOR():
    numero = input(f"{azul}Ingrese el número de celular: ")
    url3 = f"https://phonevalidation.abstractapi.com/v1/?api_key=49f4fe982a1b4f5cacdde03608161cdd&phone=51{numero}"
    data3 = requests.get(f"{url3}")
    dataJson1 = data3.json()
    operador= dataJson1["carrier"]
    valido= dataJson1["valid"]
    numeroPass=dataJson1["format"]["local"]
    #validar datos
    if dataJson1["valid"] == False:
        print(f"{rojo}Número no válido o no existe")
        consultar_OPERADOR()
    else:
        print(f"{azul} Número válido: {verde}{valido}\n {azul}Numero de celular: {blanco}+51 {numeroPass}\n {azul}Operador:{blanco} {operador} ")
    print(f"{rojo}-----------------------------------------------------")

def inicio():
    print(f'''{rojo}
    ┌──┐░░░░┌┐░┌───┐░
    │┌┐│░░░┌┘└┐│┌─┐│░
    │└┘└┬──┼┐┌┘│└─┘│░
    │┌─┐│┌┐│││░│┌┐┌┘░
    │└─┘│└┘││└┐│││└┬┐
    └───┴──┘└─┘└┘└─┴┘ {violeta}Version. 1.0
    {verde}DESARROLLADO POR ROKE
    {azul}https://github.com/roke741
    ''')
    time.sleep(0.5)

def opcion():
    print(f'''
    {lrojo}OPCIONES DISPONIBLES:
    {verde}[1] Buscar DNI
    {verde}[2] Buscar DNI por nombres
    {verde}[3] Buscar DNI por nombres(metodo2)
    {verde}[4] Consultar operadora
    -------------------------------------------
    {rojo}[5] Salir

    {lazul}...elige una opción: ''')
    op = input(f"{violeta}>> ")
    if op == "1":
        consultar_DNI()
        opcion()
    elif op == "2":
        consultar_NOMBRE()
        opcion()
    elif op == "3":
        consultar_NOMBRE2()
        opcion()
    elif op == "4":
        consultar_OPERADOR()
        opcion()
    elif op == "5":
        print(f"{fblanco}{amarillo}bye :3{fin} ")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print(f"{rojo}ERROR :,c opción incorrecta")
        opcion()


if __name__ == "__main__":
    inicio()
    opcion()