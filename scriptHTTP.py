# Que hace el script: Generar un .htaccess

# Indicar el directorio
# Indicar el fichero index por defecto
# Usuario y contraseña en ese directorio
# Bloquee el listado del contenido del directorio

# Argumentos: ./scriptHTTP.py /htdocs/asir /index-asir.php asir 123456 S

import sys
import hashlib

# Funcion para generar el hash de la contraseña
# https://blog.tiraquelibras.com/?p=1041
pwd = sys.argv[4]
pwdCifrado = pwd.encode('utf-8')
md5 = hashlib.md5(pwdCifrado).hexdigest()
print(md5)

#args = sys.argv

if len(sys.argv) != 6:
    print("Error. Debe introducir 6 argumentos")
    sys.exit(1)
else:
    #print(sys.argv[0])

    file = open(sys.argv[1]+"\.htpasswd", "w")
    file.write(f"{sys.argv[3]}:{md5}")

    f = open(sys.argv[1] + "\.htaccess", "w") #a para añadir, w para escribir, r para leer
    f.write("DirectoryIndex " + sys.argv[2])
    f.write("\n#Protect directory\nAuthName 'Dialog prompt'\nAuthType Basic\nAuthUserFile " + sys.argv[1] + "\.htpasswd\nRequire valid-user")

    if sys.argv[5] == "S":
        f.write("\nOptions -Indexes")
    
    #else:
    #    f.write("\nOptions +Indexes")
    #f.close()


