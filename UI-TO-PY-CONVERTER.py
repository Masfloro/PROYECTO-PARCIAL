## import Pyuic5
import os
import subprocess

class Convertidor:
    def __init__(self):
        super().__init__()

    def capturarDirectorio(self):
        nombreDirectorioOrigen = os.getcwd()
        return nombreDirectorioOrigen
    
    def convertirInterfaz(self,directorio):
        nombre_origen = input("Escribe el nomnbre del archivo .UI : ")
        nombre_destino  = input("Escribe el nombre de destino del archivo .PY")
        comando = "pyuic5 -x " + str(nombre_origen) + ".ui -o " + str(nombre_destino) + ".py"
        resultado = subprocess.run(comando, cwd=directorio, shell=True, capture_output=True, text=True)
        print(resultado.stdout)



if __name__ == '__main__':
    convertidor = Convertidor()
    directorio = convertidor.capturarDirectorio()
    convertidor.convertirInterfaz(directorio)


##pyuic5 -x  -o (NombreArchivo.py)

