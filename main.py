import os
import subprocess
import sys
import getpass
import pwd
import logging
import datetime
from time import sleep

LOG_FILENAME = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")+".log"
logging.basicConfig(
    filename=LOG_FILENAME,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
  
def get_file():
    try:
        return open('usuarios.csv', 'r')
    except:
        logging.error('Archivo no encontrado')
        logging.info('Programa terminado')
        sys.exit(1)

def add_user(username, password):
    logging.info(f'Agregando usuario {username}')
    try:
        subprocess.run(['useradd', '-p', password, username ]) 
        logging.info(f'Usuario {username} registrado')
    except:
        logging.error(f'No se ha logrado registrar al usuario {username}')
        
def user_exist(usuario):
    try:
        username = usuario['username']
        password = usuario['password']
        pwd.getpwnam(username)
        logging.info('Usuario {} ya existe'.format(username))
        logging.info('Actualizando contraseña')
        proc=subprocess.Popen(['passwd', username],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout,stderr = proc.communicate(input="{}\n{}".format(password,password).encode('utf-8'))
        logging.info(stdout)
        logging.error(stderr)
        return True
    except KeyError:
        logging.info('Usuario {} no existe'.format(username))
        return False


if __name__=='__main__':
    logging.info('Iniciando registro masivo de usuario')
    logging.info('Verificando si existe el archivo en el directorio predeterminado')
    file_lines = get_file().readlines()

    print('Procesado archivo csv')
    for i, line in enumerate(file_lines):
        line = line.strip()
        line = line.split(',')
        usuario = {'username':line[3],'password':line[4]}
        if not user_exist(usuario):
            add_user(line[3],line[4])
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[{:{}}] {:.1f}%".format("="*i, len(file_lines)-1, (100/(len(file_lines)-1)*i)))
        sys.stdout.flush()
        sleep(0.25)
    print("\nTerminado")