def eh_bissexto(ano:int) -> bool:
    """
    Retorna True se o ano for bissexto e False caso não seja.
    
    Regras para que o ano seja bissexto:

    - Divisível por 400 = bissexto
    - Divisível por 100 = não é bissexto
    - Divisível por 4 = bissexto
    """
    
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    ano = int(input("Digite um ano: "))
    
    if eh_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")