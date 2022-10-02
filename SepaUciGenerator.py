def crear_nif(nif, sufijo, pais="ES"):
    



    

    def convertir(posicion, nif_list):
        for claves in letra_num.keys():
            
                try:
                    if (nif_list[posicion] == claves):
                        nif_list[posicion] = str(letra_num[claves])
                    else:
                        pass
                    
                except:
                    
                    return False

    letra_num = {
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":18,
        "J":19,
        "K":20,
        "L":21,
        "M":22,
        "N":23,
        "O":24,
        "P":25,
        "Q":26,
        "R":27,
        "S":28,
        "T":29,
        "U":30,
        "V":31,
        "W":32,
        "X":33,
        "Y":34,
        "Z":35,
        "a":10,
        "b":11,
        "c":12,
        "d":13,
        "e":14,
        "f":15,
        "g":16,
        "h":17,
        "i":18,
        "j":19,
        "k":20,
        "l":21,
        "m":22,
        "n":23,
        "o":24,
        "p":25,
        "q":26,
        "r":27,
        "s":28,
        "t":29,
        "u":30,
        "v":31,
        "w":32,
        "x":33,
        "y":34,
        "z":35,
    }
#B12345678ES    #12345678BES
    
    try:
    
        nif_list = list(nif + pais)
        
        
        
        convertir(0, nif_list)
        convertir(8,nif_list)
        convertir(9, nif_list)
        convertir(10, nif_list)
        nif_list.append('0')
        nif_list.append('0')
        nif2 = "".join(nif_list)
        nif3 = 98-(int(nif2) % 97)
        nif_full = pais + str(nif3) + sufijo + nif        
        print (nif_full)

        return nif_full
    except:
        print("No se ha podido concatenar el NIF con Sufijo y con Código país")
        return False



def is_integer_num(n):
    try:
        int(n)
        return True
    except:
        return False