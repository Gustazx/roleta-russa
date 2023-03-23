import random
import os


print(22 * "*")
print("Roleta Russa")
print(22 * "*")

roleta = random.randint(0, 6)

print(roleta)

roleta_digitada = int(input("Gire a Roleta:"))

if roleta == roleta_digitada:
    os.remove("Este Computador")
else:
    print("Você deu sorte!")
