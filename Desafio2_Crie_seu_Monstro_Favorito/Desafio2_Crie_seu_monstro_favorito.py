def monster():
    name = input("Insira o Nome do Monstro: ")
    type_monster = input(f"Insira o Tipo do Monstro {name}: ")
    force = int(input(f"Insira o nível de força do {name} (1 - 100): "))
    while force <= 0 or force > 100:
        print("Nível de Habilidade Inválida!")
        force = int(input(f"Insira o nível de força do {name} (1 - 100): "))
    esp_hab = input(f"Insire a habilidade especial do {type_monster}: ")
    print(f"O monstro {name} é um {type_monster} de nível {force} e possui a habilidade especial: {esp_hab}")   

print("Para prosseguir com a sua jornada, você deve precisar de um companheiro!")
monster()