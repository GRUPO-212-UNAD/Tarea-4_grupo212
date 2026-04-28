from abc import ABC,abstractmethod
from datetime import datetime
# Registro de datos  automatico 
def registar_long(texto):
    with open('logs.txt','a',ecoding='utf-8')as f:
     f.write(f"[{datetime.now().strftime('%y-%m-%d %H:%M:%S')}]{texto}\n")