lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."] 

input1 = input("Digite um Numero: ")

for i in input1:
    if i not in lista:
        print("Não esta na lista")    
        continue
    else:
        print("Esta na lista")
        break
  
