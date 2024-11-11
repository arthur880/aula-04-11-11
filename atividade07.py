def soma(num1,num2): return num1+num2
def subtracao(num1,num2): return num1-num2
def multiplicacao(num1,num2): return num1*num2
def divisao(num1,num2): 
    if num2 == 0:
        return num1/num2

def menu(num):
    match num:
        case 1: soma
        case 2: subtracao
        case 3: multiplicacao
        case 4: divisao
        case 5: "sair"
        case 6: "ERR0"
while True:
    menu = int(input(f"Óla,slecione uma opçao
            \n 1-soma
            \n2-subtraçao
            \n3-multipicaçao
            \4-divisao"))
    funcao = input("digite o numero da operaçao que vc quer")

    try:
        num1 = float(input("digite o seu primeiro algarismo"))
        num2 = float(input("digite o seu segundo algarismo"))
    except ValueError:
        print("err0! digite numeros validos")

    if funcao == "1":
        print(f"{num1}+{num2} = {adicionar(num1,num2)}")
    elif operacao == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif operacao == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("opercao falhou! tente novamente.")