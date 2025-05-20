# Juego de adivinar un numero aleatorio entre 1 y 20

print("---Adivina el numero aleatorio entre 1 y 20---")
import random
numero_secreto = random.randint(1,20)
intentos = 1

usuario = int(input("digite un número entre 1 y 20:"))

while usuario != numero_secreto:
    print(f"❌ {usuario} no es el número. Intenta de nuevo.")
    
    if usuario < numero_secreto:
        print("🔻 Pista: el número es mayor.")
    else:
        print("🔺 Pista: el número es menor.")
    
    usuario = int(input("➡️ Digita otro número: "))
    intentos += 1

print(f"🎉 ¡Correcto! El número secreto era {numero_secreto}.")
print(f"🔁 Lo lograste en {intentos} intento(s).")

