pessoas = []

for total in range(15):
 altura = float(input("Digite sua altura: "))
 genero = input("digite seu genero(F/M): ")
 pessoas.append((altura, genero))

homens = [altura for altura, genero in pessoas if genero == "M"]
mulheres = [altura for altura, genero in pessoas if genero == "F"]
maior = max(altura for altura, genero in pessoas)
menor = min(altura for altura, genero in pessoas)

print(f"A maior altura é {maior}")
print(f"A maior altura é {menor}")

if homens:
    mediah = (sum(homens)/len(homens))
    print(f"A media de altura entre os homens é {mediah}m")

if mulheres:
    print("O total de mulheres:", len(mulheres))

