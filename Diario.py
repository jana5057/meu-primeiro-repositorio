with open("diario.txt", "w", encoding = "utf-8") as arquivo:
          arquivo.write("hoje é segunda feira. \n")
          arquivo.write("Amanhã será terça.\n")
          arquivo.write("Será que vai chover na quarta?\n")
with open("diario.txt", "a", encoding="utf-8") as arquivo:
          arquivo.write("Hoje aprendi a usar arquivos em Python.\n")
          arquivo.write("Estou começando a entender o GitHub.\n")
with open("diario.txt", "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
                print(numero, linha.strip())
                
                
          
