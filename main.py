import math


def verifica_numeros(num):
    if "," in num:
        return num.replace(",", ".")
    else:
        return num
    
def verificar_variaveis(num):
    lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "."]
    for i in num:
        if i not in lista:
            return False
        else:
            return True
        
        
def valor_intrinseco():
    print("VALOR INTRINSECO")
    inicio = True
    i = 0
    while True:
        if inicio == False:
            break
        if inicio:
            i+=1
            constante_PL = input("Digite a media do P/L da acao: ")
            contante_PVP = input("Digite a media P/VP da acao: ")

            verificacao = verificar_variaveis(constante_PL)
            verificacao2 = verificar_variaveis(contante_PVP)

            if verificacao and verificacao2:

                pl = verifica_numeros(constante_PL)
                pvp = verifica_numeros(contante_PVP)

                resultado_PL = float(pl)
                resultado_PVP = float(pvp)
                print(f"Valor do preço liquido {resultado_PL}")
                print(f"Valor do preço sobre o valor patrimonial {resultado_PVP}") 
                soma = float(resultado_PL * resultado_PVP)
                soma_round = round(soma, 2)
                print(f"Esse é o resultado da constante para ser usada na formula {soma_round}")
                print()

                while True:
                    valor_cota = input("Digite o valor atual da acao: ")
                    verificacao3 = verificar_variaveis(valor_cota)
                    if verificacao3:
                        break
                    print("Não pode ter letras ou caracteres especiais")

                convt = verifica_numeros(valor_cota)
                vlc = float(convt)

                print()

                while True: 
                    vpa = input("Digite o valor da VPA: ")
                    verificacao4 = verificar_variaveis(vpa)
                    if verificacao4:
                        break
                    print("Não pode ter letras ou caracteres especiais")
                convt_vpa = verifica_numeros(vpa)
                vpa_float = float(convt_vpa)

                print()

                while True:
                    lpa = input("Digite o valor da LPA: ")
                    verificacao5 = verificar_variaveis(lpa)
                    if verificacao5:
                        break
                    print("Não pode ter letras ou caracteres especiais")
                convt_lpa = verifica_numeros(lpa)
                lpa_float = float(convt_lpa)

                print()
                print(f"Valor da cota é: {vlc}")
                print(f"Valor do Valor Patrimonial por Acao é: {vpa_float}")
                print(f"Valor do Lucro por Ação é: {lpa_float}")
                print()

                soma_indices = math.sqrt(soma_round * vpa_float * lpa_float)
                soma_round2 = round(soma_indices, 2)
                margem_de_seguranca = (soma_round2 - vlc) / vlc
                porcentagem = margem_de_seguranca * 100
                saida = "{:.0f}%".format(porcentagem)
                print(f"Essa é a margem de Segurança da acao: {saida}")
                print(f"Esse é o valor intrinseco da acao: {soma_round2}")
                print(i)
                while True:
                    continua = input("Deseja continuar ? [SIM/NAO] ").lower()
                    if continua == "SIM" or continua == "sim":
                        inicio = True
                        break
                    elif continua == "NAO" or continua == "nao":
                        inicio = False
                        break
                    else:
                        print("Apenas SIM ou NÂO")
                        continue
            else:
                print("Não pode ter letras ou caracteres especiais")
                continue
        else:
            print("Error")

valor_intrinseco()