import os
import time
import requests
import subprocess

print('Comprobando paquetes necesarios...')
paquetes_necesarios = ["requests", "colorama", "mechanize", "beautifulsoup4", "python-dotenv", "halo"]
def verificar_paquetes():
    paquetes_faltantes = []

    for paquete in paquetes_necesarios:
        try:
            subprocess.run(['pip', 'show', paquete], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            paquetes_faltantes.append(paquete)

    return paquetes_faltantes
    #paquetes_faltantes = [paquete for paquete in paquetes_necesarios if not importlib.util.find_spec(paquete)]
    #return paquetes_faltantes

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
    paquetes_faltantes = verificar_paquetes()

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
NEGRO = Fore.BLACK
FBLANCO = Back.WHITE
FIN = Back.RESET

load_dotenv()

spinner = Halo(text="🔥 Iniciando script...", text_color= 'cyan', color='green', spinner='dots' )
spinner.start()
time.sleep(3)
spinner.succeed('🔥 Listo para funcionar!')
spinner.text = '🔎 Buscando...'

#FUNCIONES
def consultar_DNI():
    url = os.getenv("API1_URL")
    print(f"\n{AMARILLO}⚠️ Porfavor ingrese el DNI de forma correcta (8 digitos) ")
    dni = input(f"{FBLANCO}{NEGRO}🪪 Ingresa el numero de DNI:{FIN}{BLANCO} ")
    
    if not dni.isnumeric() or len(dni) != 8:
       return print(f"{ROJO}⚠️ El numero de DNI que ingresaste no es correcto ")
        
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
            print(f"{AMARILLO}⚠️ DNI no encontrado ")
        else:
            print(f'''{LVERDE}
    ************** ⚡ DNI {dni} encontrado **************
    - NOMBRES: {LAZUL}{response["preNombres"]}{LVERDE}
    - APELLIDO PATERNO: {LAZUL}{response["apPaterno"]}{LVERDE}
    - APELLIDO MATERNO: {LAZUL}{response["apMaterno"]}{LVERDE}
    - GENERO: {LAZUL}{response["coGenero"]}{LVERDE}
    - FECHA DE NACIMIENTO: {LAZUL}{response["feNac"]}{LVERDE}
    - COD. UBIGEO: {LAZUL}{response["coUbigeo"]}{LVERDE}
    - DIRECCION: {LAZUL}{response["deDireccion"]}{LVERDE}
    - UBIGEO: {LAZUL}{response["deUbigeoDep"]}/{response["deUbigeoPro"]}/{response["deUbigeoDis"]}{LVERDE}
    ********************************************************
            ''')
    except requests.exceptions.Timeout:
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")

def consultar_DNI2():
    url = os.getenv("API2_URL")
    print(f"\n{AMARILLO}⚠️ Porfavor ingrese el DNI de forma correcta (8 digitos) ")
    dni = input(f"{FBLANCO}{NEGRO}🪪 Ingresa el numero de DNI:{FIN}{BLANCO} ")
    
    if not dni.isnumeric() or len(dni) != 8:
        return print(f"{ROJO}⚠️ El numero de DNI que ingresaste no es correcto ")
    
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
            print(f"{AMARILLO}⚠️ DNI no encontrado")
        else:
            print(f'''{LVERDE}
    ************** ⚡ DNI {dni} encontrado **************
    - NOMBRES: {LAZUL}{response["nombres"]}{LVERDE}
    - APELLIDO PATERNO: {LAZUL}{response["ap_paterno"]}{LVERDE}
    - APELLIDO MATERNO: {LAZUL}{response["ap_materno"]}{LVERDE}
    - GENERO: {LAZUL}{response["sexo"]}{LVERDE}
    - FECHA DE NACIMIENTO: {LAZUL}{response["nombres"]}{LVERDE}
    - EDAD: {LAZUL}{response["edad"]}{LVERDE}
    - DIRECCION: {LAZUL}{response["direccion"]}{LVERDE}
    - UBIGEO: {LAZUL}{response["departamento"]}/{response["provincia"]}/{response["distrito"]}{LVERDE}
    ********************************************************
            ''')
    except requests.exceptions.Timeout:
        spinner.stop()
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")

def consultar_NOMBRE():
    print(f'''{AMARILLO}
    *****************************
    *  ⚠️ EN CONSTRUCCION...    *
    *   Utiliza el metodo 2     *
    *****************************
    ''')

def consultar_NOMBRE2():
    print(f"\n{AMARILLO}⚠️ Escribe los nombres y apellidos de forma correcta")
    nombre1 = input(str(f"{FBLANCO}{NEGRO}🚹 Ingresa el nombre:{FIN}{BLANCO} "))
    apellidop1 = input(str(f"{FBLANCO}{NEGRO}🚹 Ingresa el apellido paterno:{FIN}{BLANCO} "))
    apellidom1 = input(str(f"{FBLANCO}{NEGRO}🚹 Ingresa el apellido materno:{FIN}{BLANCO} "))
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
        print(f"{ROJO}---------------------------------------------------------------")
    except requests.exceptions.Timeout:
        spinner.stop()
        print("La solicitud ha excedido el tiempo de espera ⌛")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")
    

def consultar_OPERADOR():
    print(f"\n{AMARILLO}⚠️ Porfavor ingrese el número de celular de forma correcta (9 digitos)")
    numero = input(f"{FBLANCO}{NEGRO}📞 Ingrese el número de celular:{FIN}{BLANCO} ")
   
    url = f"http://apilayer.net/api/validate?access_key=fa98ed6dafaad5258279886948185705&number={numero}&country_code=PE&format=1" 
    try:
        if not numero.isnumeric() or len(numero) != 9:
            return print(f"{ROJO}⚠️ El numero de celular que ingresaste no es correcto")
        
        spinner.start()
        time.sleep(1)
        data3 = requests.get(url)
        response = data3.json()
        spinner.stop()
        
        if response['valid'] == False:
            print(f"{ROJO}⚠️ Número no válido o no existe")
        else:
            print(f'''{LVERDE}
    ************* ⚡ Número encontrado *************
    - Número válido: {LVERDE}{response['valid']}"
    - Numero de celular: {LAZUL}{response['international_format']}{LVERDE}
    - Pais: {LAZUL}{response['country_name']}{LVERDE}
    - Operador: {LAZUL}{response['carrier']}{LVERDE}
    ************************************************
            ''')

    except requests.exceptions.Timeout:
        spinner.stop()
        print("⌛ La solicitud ha excedido el tiempo de espera")
    except Exception as e:
        spinner.stop()
        print(f"{ROJO}OCURRIO UN ERROR INESPERARDO ❗")
        print(f"Type: {type(e)}, Args: {e.args}")
        
def inicio():
    print(f'''{LROJO}
    ┌──┐░░░░┌┐░┌───┐░
    │┌┐│░░░┌┘└┐│┌─┐│░
    │└┘└┬──┼┐┌┘│└─┘│░
    │┌─┐│┌┐│││░│┌┐┌┘░
    │└─┘│└┘││└┐│││└┬┐
    └───┴──┘└─┘└┘└─┴┘ {LVERDE}Version. 1.2
    {VIOLETA}DESARROLLADO POR ROKE
    {VIOLETA}https://github.com/roke741
    ''')
    print(f'''{AMARILLO}Importante ⚠️  :{ROJO}
    La información provista en esta aplicación 
    es de dominio público y se ofrece con el propósito 
    de compartir conocimientos.
    No garantizamos la integridad de la información.
    Los usuarios deben evaluar y 
    utilizarla bajo su propio riesgo.
    Nos reservamos el derecho de realizar 
    cambios sin previo aviso.
    AL USAR LA APLICACION, ACEPTAS ESTE DESCARGO
    DE RESPONSABILIDAD.''')
    time.sleep(0.5)

def opcion():
    print(f'''{CYAN}
    ---------{CYAN}OPCIONES DISPONIBLES:{CYAN}--------------
    {LVERDE}[1] Buscar DNI
    {LVERDE}[2] Buscar DNI (metodo 2)
    {LROJO}[3] Buscar DNI por nombres - NO DISPONIBLE
    {LVERDE}[4] Buscar DNI por nombres (metodo 2)
    {LVERDE}[5] Consultar operadora{CYAN}
    --------------------------------------------
    {LROJO}[6] Salir

    {CYAN}...Elige una opción 🔥 :''')
    op = input(f"{CYAN}>>>{BLANCO} ")
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