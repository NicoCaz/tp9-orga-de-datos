
letras=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")
palabra="el rio esta frio y con un pez"


def control(indice):
    if indice >len(letras)-1:
        return indice-len(letras)-1
    else:
        return indice




def incriptaCesar(palabra,num):
    i=0
    palabra.lower()
    resultado=""
    while i< len(palabra):
        
        try: #Letras minusculas y espacios
            indice=letras.index(palabra[i])
            if indice==len(letras)-1:
                resultado =resultado + " "
            else:    
                indice= control(indice)
                resultado= resultado + letras[indice+num]
        except:#Mayusculas
            indice=letras.index(palabra[i].lower())
            if indice+num >len(letras)-1:
                    indice=indice-len(letras)-1
            resultado= resultado + letras[indice+num].upper()
            letras[indice+num].lower()
        
        i=i+1
    
    print(resultado)
   
incriptaCesar(palabra,20)


def incriptaCesarModificado(palabra,num):
    

    i=0
    cant=0
    while i<len(palabra):
        letrasMod[num+i]=palabra[i]
        i=i+1
    indice=len(palabra)+num
    i=0
    while cant<len(letras):
        indice=control(indice)
        caracter=letras[i]
        try:
            palabra[caracter]           
        except:
            letrasMod[indice:caracter]

        i=i+1
        cant=cant+1

    print(letrasMod)   
        

#incriptaCesarModificado("murcielago",5)



def incriptacionvigenere(palabra):
    pass
