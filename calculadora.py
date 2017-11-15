class Soma:
    def __init__(self):
        print("################################")
        print("#############SOMAR##############")
        print("-------------------------------")
        num1 = input("Digite o 1 numero : ")
        try:
            num1 == int(num1)
        except:
            print("você deve digitar um numero ! ")

        else:
            num2 = input("Digite o 2 numero : ")

            try:
                num2 == int(num2)

            except:
                print("você deve digitar um numero ! ")

            else:
                print("   ", int(num1), "\n", " +", int(num2), "\n",
                      "  ----------", "\n", "  ", int(num1) + int(num2))


class Div:
    def __init__(self):

        print("################################")
        print("###########DIVIDIR##############")
        print("-------------------------------")
        num1 = input("Digite o 1 numero : ")
        try:
            num1 == int(num1)
        except:
            print("você deve digitar um numero ! ")

        else:
            num2 = input("Digite o 2 numero : ")

            try:
                num2 == int(num2)

            except:
                print("você deve digitar um numero ! ")

            else:
                print("   ", int(num1), "\n", " /", int(num2), "\n",
                      "  ----------", "\n", "  ", int(num1) / int(num2))


class Mult:
    def __init__(self):
        print("################################")
        print("##########multiplicaçã##########")
        print("-------------------------------")
        num1 = input("Digite o 1 numero : ")
        try:
            num1 == int(num1)
        except:
            print("você deve digitar um numero ! ")

        else:
            num2 = input("Digite o 2 numero : ")

            try:
                num2 == int(num2)

            except:
                print("você deve digitar um numero ! ")

            else:
                print("   ", int(num1), "\n", " *", int(num2), "\n",
                      "  ----------", "\n", "  ", int(num1) * int(num2))


class Sub:
    def __init__(self):

        print("################################")
        print("##########SUBTRAIR##############")
        print("-------------------------------")
        num1 = input("Digite o 1 numero : ")
        try:
            num1 == int(num1)
        except:
            print("você deve digitar um numero ! ")

        else:
            num2 = input("Digite o 2 numero : ")

            try:
                num2 == int(num2)

            except:
                print("você deve digitar um numero ! ")

            else:
                print("   ", int(num1), "\n", " /", int(num2), "\n",
                      "  ----------", "\n", "  ", int(num1) / int(num2))


print("###########################")
print("########CALCULADORA########")

perg = input("soma = 1 \nsub = 2\ndiv = 3\nmult = 4\n"
             "OU ESCREVA A OPERAÇÃO IGUAL DESCRITO ACIMA \n-- > ")


try:
    perg == int(perg)
except:
    def Dicionario_opcao(operador):
        return {
            'soma': lambda: Soma(),
            'sub': lambda: Sub(),
            'div': lambda: Div(),
            'mult': lambda: Mult()
        }.get(operador, lambda: None)()

    Dicionario_opcao(perg)

else:
    def Dicionario_opcao(operador):
        return {
            1: lambda: Soma(),
            2: lambda: Sub(),
            3: lambda: Div(),
            4: lambda: Mult(),
        }.get(operador, lambda: None)()

    Dicionario_opcao(int(perg))

