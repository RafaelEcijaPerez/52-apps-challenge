'''
Generador de contraseña seguras Librerias
'''
import random
import string

''' longitud de la contraseña '''
length = 12
'''Contraseña'''
password = ''

def set_length(value):
    ''' Establecer la longitud de la contraseña '''
    global length
    length = value
    return length

def get_length():
    ''' Obtener la longitud de la contraseña '''
    return length

def generate_password():
    #bucle para generar contraseñas validas
    global password
    ok = False

    #mientras no se cumpla la condicion
    while not ok:
        #generar una contraseña aleatoria
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        #comprobar que la longitud de la contrasela es igual a la estabecida
        if len(password) ==length:
            #se cumple la condicion
            #Comprobar que la contraseña tiene al menos una mayuscula, minuscula, numero y simbolo
            if(any(c.islower() for c in password) and
               any(c.isupper() for c in password) and
               any(c.isdigit() for c in password) and
               any(c in string.punctuation for c in password)):
                ok = True
       
    #Guardar la contraseña en el historial
    with open('password_history.txt', 'a') as f:
        f.write(password + '\n')
    return password
#ver la contraseña generada
def get_password():
    ''' Obtener la contraseña generada '''
    return password

#ver el historial de contraseñas creadas
def get_history():
    #Obtener el historial de contraseñas creadas '''
    try:
        with open('password_history.txt', 'r') as f:
            history = f.readlines()
            return [line.strip() for line in history]
    except FileNotFoundError:
        return []

