
from SepaUciGenerator import crear_nif, is_integer_num
def main():

    Nif=input("Introduzca NIF ")
    Sufijo= input("Introduzca Sufijo ")
    if len(Sufijo)>3 or is_integer_num(Sufijo)==False  :

        print("sufijo introducido es incorrecto")
        return False
    if len(Nif)>10 or len(Nif)<6:
        print("Nif introducido es incorrecto")
        return False

    else:
        
        crear_nif(Nif,Sufijo)
    
    





if __name__ == "__main__":
    main()
