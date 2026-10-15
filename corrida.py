import threading
import time

saldo = 1000

def sacar(valor):
    global saldo

    saldo atual = saldo
    time.sleep(0.01)
    saldo = saldo atual - valor

    threads = []

    for i in range(10):
        t = threading.Thread(target=sacar, args=50,)
        threads.append(t)
        t.start()

        for t in threads:
            t.join()

            print("Saldo esperado: 500")
            print("Saldo obtido:", saldo)

RESULTADO:

PS C:\Users\Matias\Desktop\FACULDADE\SISTEMAS DISTRIBUIDOS\AULA 5> & C:\Users\Matias\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/Matias/Desktop/FACULDADE/SISTEMAS DISTRIBUIDOS/AULA 5/corrida.py"
  File "c:\Users\Matias\Desktop\FACULDADE\SISTEMAS DISTRIBUIDOS\AULA 5\corrida.py", line 9
    saldo atual = saldo
