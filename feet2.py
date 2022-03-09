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
  yn = input("Шифровка - (e)\nДешифровка - (d)\nВыход - (l)\nВаш выбор: ")
  if yn != "e" and yn != "d" and yn != "l":
    continue
  
  if yn == "e":
    message = input("Введите сообщение для шифровки: ")
    seed = input("Введите сид шифровки: ")
    seed_edit = seed.replace(" ", "")
    shifr = cryptocode.encrypt(message, seed_edit)
    shifr2 = cryptocode.encrypt(shifr, seed_encrypt)
    
    print("------------------------------------")
    print("Шифровка в процессе... \n")
    sleep(rnd.randint(1,3))
    print(f"Ваш шифр ({seed_edit}): {seed_encrypt}{shifr2}\n")
    print("------------------------------------")
    continue
    
  elif yn == "d":
    decrypt_seed = input("Введите сид шифровки: ")
    decrypt_message = input("Введите сообщение для дешифровки: ")
    decrypt_seed_edit = decrypt_seed.replace(" ", "")
    decrypt_start = decrypt_message.replace(seed_encrypt, "")
    decrypt = cryptocode.decrypt(decrypt_start, seed_encrypt)
    decrypt_2 = cryptocode.decrypt(decrypt, decrypt_seed_edit)
    
    print("------------------------------------") 
    print("Дешифровка в процессе... \n")
    sleep(rnd.randint(1,3))   
    print(f"Сообщение ({decrypt_seed_edit}): {decrypt_2}\n")
    print("------------------------------------")
    continue
  elif yn == "l":
    print("Удачи! :)")
    break