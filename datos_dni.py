import os
import time
import requests

import importlib
import subprocess

paquetes_necesarios = ['requests', 'colorama', 'mechanize', 'beautifulsoup4', 'python-dotenv', 'halo']
def verificar_paquetes():
    paquetes_faltantes = [paquete for paquete in paquetes_necesarios if not importlib.util.find_spec(paquete)]
    return paquetes_faltantes

def instalar_paquetes(paquetes):
    for paquete in paquetes:
        subprocess.run(['pip', 'install', paquete])

paquetes_faltantes = verificar_paquetes()

if paquetes_faltantes:
    print("Faltan paquetes necesarios para el funcionamiento del script:")
    for paquete in paquetes_faltantes:
        print(f"- {paquete}")
    respuesta = input("¿Desea instalar los paquetes faltantes? (y/n): ").lower()
    if respuesta == 'y':
        instalar_paquetes(paquetes_faltantes)
    else:
        print("No se han instalado los paquetes. El script puede no funcionar correctamente.")
else:
    pass

from bs4 import BeautifulSoup
from mechanize import Browser
from colorama import Back, Fore, init
from halo import Halo
from dotenv import load_dotenv


#colores
init()
VERDE = Fore.GREEN
LVERDE = Fore.LIGHTGREEN_EX
ROJO = Fore.RED
LROJO = Fore.LIGHTRED_EX
AMARILLO = Fore.YELLOW
BLANCO = Fore.WHITE
CYAN = Fore.CYAN
VIOLETA = Fore.MAGENTA
AZUL = Fore.BLUE
LAZUL = Fore.LIGHTBLUE_EX
FBLANCO = Back.WHITE
FIN = Back.RESET
NEGRO= Fore.BLACK

load_dotenv()

spinner = Halo(text="Iniciando script... 🔥", text_color= 'cyan', color='green', spinner='dots' )
spinner.start()
time.sleep(3)
spinner.succeed('Listo para funcionar!🔥')
spinner.text = 'Buscando... 🔎'
#spinner = Halo(text="Buscando...", spinner={ "interval": 400, "frames": ["⏳", "⌛", ""]})
#FUNCIONES    
def consultar_DNI():
    url = os.getenv("API1_URL")
    print(f"{AMARILLO}Porfavor ingrese el DNI de forma correcta (8 digitos) 🪪")
    dni = input(f"{AZUL}Ingresa el numero de DNI: ")
    
    if not dni.isnumeric() or len(dni) != 8:
       return print(f"{ROJO}El numero de DNI que ingresaste no es correcto ⚠️")
        
    formData = {
        "txtDocumento": dni,
        "codigoDocumento": "01"
    }
        
    try:
        spinner.start()
        time.sleep(1)
        res = requests.post(url, data=formData)
        data = res.json()
        response = data["dataJson"]["persona"]
        spinner.stop()
        if response["coRpta"] != 'OK':
            print(f"{AMARILLO} DNI no encontrado ⚠️")
        else:
            
            print(f"{LVERDE}DNI {dni} encontrado ⚡")
            print(
                f"{NEGRO} {FBLANCO}NOMBRES: ", response["preNombres"],
                f"{FIN}","\n",
                f"{FBLANCO}APELLIDO PATERNO: ", response["apPaterno"],
                f"{FIN}","\n",
                f"{FBLANCO}APELLIDO MATERNO: ", response["apMaterno"],
                f"{FIN}","\n",
                f"{FBLANCO}GENERO: ", response["coGenero"],
                f"{FIN}","\n",
                f"{FBLANCO}FECHA DE NACIMIENTO: ", response["feNac"],
                f"{FIN}","\n",
                f"{FBLANCO}COD. UBIGEO: ", response["coUbigeo"],
                f"{FIN}","\n",
                f"{FBLANCO}DIRECCION: ", response["deDireccion"],
                f"{FIN}","\n",
                f"{FBLANCO}UBIGEO: ", response["deUbigeoDep"],"/",response["deUbigeoPro"],"/",response["deUbigeoDis"],
                f"{FIN}"
            )
            
    except requests.exceptions.Timeout:
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")
    




def consultar_DNI2():
    url = os.getenv("API2_URL")
    print(f"{AMARILLO}------------------------------------------------------")
    print(f"{AMARILLO}Porfavor ingrese el DNI de forma correcta (8 digitos) 🪪")
    dni = input(f"{AZUL}Ingresa el numero de DNI: ")
    
    if not dni.isnumeric() or len(dni) != 8:
        return print(f"{ROJO}El numero de DNI que ingresaste no es correcto ⚠️")
    
    formData = {
        "dni": dni,
    }
    try:
        spinner.start()
        time.sleep(1)
        res = requests.post(url, data=formData)
        response = res.json()
        spinner.stop()
        if response["cod_error"] != '0000':
            print(f"{AMARILLO} DNI no encontrado ⚠️")
        else:
            print(f"{LVERDE}DNI {dni} encontrado ⚡")
            print(
                f"{NEGRO} {FBLANCO}NOMBRES: ", response["nombres"],
                f"{FIN}","\n",
                f"{FBLANCO}APELLIDO PATERNO: ", response["ap_paterno"],
                f"{FIN}","\n",
                f"{FBLANCO}APELLIDO MATERNO: ", response["ap_materno"],
                f"{FIN}","\n",
                f"{FBLANCO}GENERO: ", response["sexo"],
                f"{FIN}","\n",
                f"{FBLANCO}FECHA DE NACIMIENTO: ", response["fec_nacimiento"],
                f"{FIN}","\n",
                f"{FBLANCO}EDAD: ", response["edad"],
                f"{FIN}","\n",
                f"{FBLANCO}DIRECCION: ", response["direccion"],
                f"{FIN}","\n",
                f"{FBLANCO}UBIGEO: ", response["departamento"],"/",response["provincia"],"/",response["distrito"],
                f"{FIN}"
            )
    except requests.exceptions.Timeout:
        spinner.stop()
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")

def consultar_NOMBRE():
    print(f"{AMARILLO}En constriccion... ⚠️")

def consultar_NOMBRE2():
    print(f"{AMARILLO}Escribe los nombres y apellidos de forma correcta")
    nombre1 = input(str(f"{AZUL}Ingresa el nombre: "))
    apellidop1 = input(str(f"{AZUL}Ingresa el apellido paterno: "))
    apellidom1 = input(str(f"{AZUL}Ingresa el apellido materno: "))
    try:
        spinner.start()
        time.sleep(1)
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
        soup = BeautifulSoup(data, "html.parser")
        titulo = soup.find("h4", {"class": "text-center"})
        t = titulo.get_text()
        
        spinner.stop()
        print(f"\n {AMARILLO} {t} \n", sep="")
        body = soup.find_all('tr')
        for x in body:
            print(f"{CYAN}",x.get_text("  |  ", strip=True))
        print(f"{ROJO}-----------------------------------------------------")
    except requests.exceptions.Timeout:
        spinner.stop()
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")
    

def consultar_OPERADOR():
    numero = input(f"{AZUL}Ingrese el número de celular: ")
    url = f"http://apilayer.net/api/validate?access_key=fa98ed6dafaad5258279886948185705&number={numero}&country_code=PE&format=1" 
    try:
        spinner.start()
        time.sleep(1)
        data3 = requests.get(url)
        response = data3.json()
        spinner.stop()
        
        if response['valid'] == False:
            print(f"{ROJO}Número no válido o no existe")
        else:        
            print(f"{VIOLETA} Número válido: {VERDE}{response['valid']}\n {VIOLETA}Numero de celular: {BLANCO}{response['international_format']}\n {VIOLETA}Pais: {BLANCO}{response['country_name']} \n {VIOLETA}Operador:{BLANCO} {response['carrier']} ")
        print(f"{ROJO}-----------------------------------------------------")
    except requests.exceptions.Timeout:
        spinner.stop()
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")
        
def inicio():
    print(f'''{ROJO}
    ┌──┐░░░░┌┐░┌───┐░
    │┌┐│░░░┌┘└┐│┌─┐│░
    │└┘└┬──┼┐┌┘│└─┘│░
    │┌─┐│┌┐│││░│┌┐┌┘░
    │└─┘│└┘││└┐│││└┬┐
    └───┴──┘└─┘└┘└─┴┘ {VIOLETA}Version. 1.2
    {VERDE}DESARROLLADO POR ROKE
    {AZUL}https://github.com/roke741
    ''')
    print(f'''{ROJO}Importante⚠️  :
        La información provista en esta aplicación es de dominio público y se ofrece con el propósito de compartir conocimientos.
        No garantizamos la integridad de la información.
        Los usuarios deben evaluar y utilizarla bajo su propio riesgo.
        Nos reservamos el derecho de realizar cambios sin previo aviso.
        Al usar la aplicación, aceptas este descargo de responsabilidad.''')
    time.sleep(0.5)

def opcion():
    print(f'''{VERDE}
    --------------------------------------------
    {LROJO}OPCIONES DISPONIBLES:
    {LVERDE}[1] Buscar DNI
    {LVERDE}[2] Buscar DNI (metodo 2)
    {ROJO}[3] Buscar DNI por nombres - NO DISPONIBLE
    {LVERDE}[4] Buscar DNI por nombres (metodo 2)
    {LVERDE}[5] Consultar operadora
    --------------------------------------------
    {ROJO}[6] Salir

    {AZUL}...Elige una opción🔥 :''')
    op = input(f"{VIOLETA}>> ")
    if op == "1":
        consultar_DNI()
        opcion()
    elif op == "2":
        consultar_DNI2()
        opcion()
    elif op == "3":
        consultar_NOMBRE()
        opcion()
    elif op == "4":
        consultar_NOMBRE2()
        opcion()
    elif op == "5":
        consultar_OPERADOR()
        opcion()
    elif op == "6":
        print(f"{FBLANCO}{AMARILLO}bye :3{FIN} ")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print(f"{ROJO}ERROR :,c opción incorrecta")
        opcion()

if __name__ == "__main__":
    inicio()
    opcion()