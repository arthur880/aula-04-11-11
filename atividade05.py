def bom (num) :
    if num > 5 and num < 12 :
        return "bom dia"
    elif num > 2 and num < 18:
        return "boa tarde"
    elif num >18 and num < 0:
        return "boa noite"
    elif num >0 and num < 5:
        return "boa madrugada"
    else:
        print("vocẽ digitou errado tente novamente !!!")

hora = int(input("digite o numeti"))
print(bom(hora))
