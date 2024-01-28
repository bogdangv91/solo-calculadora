# Instrucciones para ejecutar el programa:
# Antes que nada debe ejecutar con play el programa,esta opción esta situada en la esquina superior derecha.
#Paso 1: el programa le mostrara en pantalla el siguente mensaje: Inserte el nombre de la criptomoneda que desea convertir:(debera insertar el nombre que desea).
#Paso 2: el programa le mostrará en pantalla el siguiente mensaje: Seleccione la moneda a la que desea convertir: EUR/USD
#Paso 3: el programa le mostrara en pantalla el siguiente mensaje: Inserte la cantidad de criptomonedas que desea convertir:(deberá insertar la cantidad de monedas que deseea convertir).
#Paso 4: finalmente el programa le devolverá la cantidad ya convertida a euros de la criptomoneda que le haya marcado en el paso 2.
#En el caso de que cometa algun error siga las instruciones/mensajes que el programa le indica. Ejemplo : si no ingresa ninguna criptomoneda le saldra un mensaje de error en el cual dira:(Debe insertar el nombre de la criptomoneda que desea convertir para seguir ejecutando el programa).
import requests #He importado la biblioteca requests
import sys #He importado el sys para poder cerrar el programa en caso de que no se cumplan las condiciones que le he marcado.

def obtener_cambio(criptomoneda, moneda_a_convertir):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={criptomoneda}&vs_currencies={moneda_a_convertir}' #La f nos indica que se trata de una cadena de formato(f-string). 
           #&vs_currencies=eur es un parametro que indica que  queremos obtener el precio en euros. El & se utiliza para concatenar este parametro a la URL.
    respuesta = requests.get(url) #Aqui se utiliza el get  en la variable respuesta de la biblioteca request para hacer una solicitud HTTP a la URL
    
    if respuesta.status_code == 200: #Si la respuesta es 200 indica que ha ido todo bien. status_code es un atributo de respuesta que contiene el codigo de estado HTTP 
        cifra = respuesta.json() #Aqui estamos convirtiendo la respuesta en formato json.
        tasa_cambio = cifra[criptomoneda][moneda_a_convertir]
        return tasa_cambio
    else:
        print(f"Error al  calcular el cambio de la criptomoneda {criptomoneda} {moneda_a_convertir}") #Este mensaje nos saldra en caso de que la tasa no sea correcta.
        

def convertir_a_euros(criptomoneda, cantidad, moneda_a_convertir):
    tasa_cambio = obtener_cambio(criptomoneda, moneda_a_convertir)
    
    if tasa_cambio:
        euros = cantidad * tasa_cambio
        return euros #Aqui nos esta retornando la cantidad de la criptomoneda en euros.
    else:
        return None

if __name__ == "__main__":
    criptomoneda = input("Inserte el nombre de la criptomoneda que desea convertir: ")

    if criptomoneda:
        print("Sigamos con el paso 2")
    else:
        print("Debe insertar el nombre de la criptomoneda que desea convertir para seguir ejecutando el programa")
        sys.exit() #Nos  para el programa porque no se cumple la condición del if por lo tanto nos mostrara un mensaje de error.
    print("Seleccione la moneda a la que desea convertir:")
    print("(EUR)")
    print("(USD)")
    
    opcion = input("Inserte la oppción  en la que desea  recibir la conversión  : ")
    
    if opcion == "EUR":
        moneda_a_convertir = "eur"
    elif opcion == "USD":
        moneda_a_convertir = "usd"
    else:
        print("No ha seleccionado ninguna de las opciones (EUR/USD,)")
        sys.exit()

       

    
    cantidad = float(input("Inserte la cantidad de criptomonedas que desea convertir: ")) #El float lo ponemos para que pueda facilitarnos numeros decimales.
  
     
    
    resultado = convertir_a_euros(criptomoneda, cantidad,moneda_a_convertir)
    
    if resultado is not None:
        print(f"{cantidad} {criptomoneda} es aproximadamente {resultado:.2f}{moneda_a_convertir.upper()}.") # :. Indica el inicio.    2 indica que debe mostrar 2 digitos decimales despues del punto.     f indica que el numero debe ser formateado como un numero flotante.
