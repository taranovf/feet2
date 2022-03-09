import cryptocode
import random as rnd
from time import sleep

seed_encrypt = ("feet.protocol:2/")

print("███████╗███████╗███████╗████████╗  ██████╗░")
print("██╔════╝██╔════╝██╔════╝╚══██╔══╝  ╚════██╗")
print("█████╗░░█████╗░░█████╗░░░░░██║░░░  ░░███╔═╝")
print("██╔══╝░░██╔══╝░░██╔══╝░░░░░██║░░░  ██╔══╝░░")
print("██║░░░░░███████╗███████╗░░░██║░░░  ███████╗")
print("╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░  ╚══════╝\n")

while True:
  yn = input("Шифровка - (e), Дешифровка - (d): ")
  if yn != "e" and yn != "d":
    continue
  
  if yn == "e":
    message = input("Введите сообщение для шифровки: ")
    seed = input("Введите сид шифровки: ")
    shifr = cryptocode.encrypt(message, seed)
    shifr2 = cryptocode.encrypt(shifr, "12a")

    print("------------------------------------")
    print("Шифровка в процессе... \n")
    sleep(rnd.randint(1,3))
    print(f"Ваш шифр ({seed}): {seed_encrypt}{shifr2}\n")
    print("------------------------------------")
    continue
    
  elif yn == "d":
    decrypt_seed = input("Введите сид шифровки: ")
    decrypt_message = input("Введите сообщение для дешифровки: ")

    decrypt_start = decrypt_message.replace(seed_encrypt, "")
    decrypt = cryptocode.decrypt(decrypt_start, "12a")
    decrypt_2 = cryptocode.decrypt(decrypt, decrypt_seed)
    
    print("------------------------------------") 
    print("Дешифровка в процессе... \n")
    sleep(rnd.randint(1,3))   
    print(f"Сообщение ({decrypt_seed}): {decrypt_2}\n")
    print("------------------------------------")
    continue