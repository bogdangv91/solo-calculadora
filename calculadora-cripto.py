import requests #He importado la biblioteca requests

def obtener_cambio(criptomoneda):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={criptomoneda}&vs_currencies=eur' #La f nos indica que se trata de una cadena de formato(f-string). 
           #&vs_currencies=eur es un parametro que indica que  queremos obtener el precio en euros. El & se utiliza para concatenar este parametro a la URL.
    respuesta = requests.get(url) #Aqui se utiliza el get  en la variable respuesta de la biblioteca request para hacer una solicitud HTTP a la URL
    
    if respuesta.status_code == 200: #Si la respuesta es 200 indica que ha ido todo bien. status_code es un atributo de respuesta que contiene el codigo de estado HTTP 
        cifra = respuesta.json() #Aqui estamos convirtiendo la respuesta en formato json.
        tasa_cambio = cifra[criptomoneda]['eur']
        return tasa_cambio
    else:
        print(f"Error al  calcular el cambio de la criptomoneda {criptomoneda}") #Este mensaje nos saldra en caso de que la tasa no sea correcta.
        

def convertir_a_euros(criptomoneda, cantidad):
    tasa_cambio = obtener_cambio(criptomoneda)
    
    if tasa_cambio:
        euros = cantidad * tasa_cambio
        return euros #Aqui nos esta retornando la cantidad de la criptomoneda en euros.
    else:
        return None

if __name__ == "__main__": #Estamos verificando si esta ejecutado directamente y no importado.
    criptomoneda = input("Inserte el nombre de la criptomoneda que desea que desea convertir: ")
    cantidad = float(input("Inserte la cantidad de criptomonedas que desea convertir: ")) #El float lo ponemos para que pueda facilitarnos numeros decimales.
    
    resultado = convertir_a_euros(criptomoneda, cantidad)
    
    if resultado is not None:
        print(f"{cantidad} {criptomoneda} es aproximadamente {resultado:.2f} euros.") # :. Indica el inicio.    2 indica que debe mostrar 2 digitos decimales despues del punto.     f indica que el numero debe ser formateado como un numero flotante.
