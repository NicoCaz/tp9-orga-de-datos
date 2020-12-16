
letras=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
palabra="el rio esta frio y con un pez"


def control(indice,largo):
    if indice >len(largo)-1:
        return indice-len(largo)-1
    else:
        return indice


def incriptaCesar(palabra,num):
    i=0
    resultado=""
    while i< len(palabra):
        if palabra[i]==" ":
            resultado =resultado + " "
        else:    
            try: #Letras minusculas y espacios
                indice=letras.index(palabra[i])
                indice= control(indice+num,letras)
                resultado= resultado + letras[indice]
            except:#Mayusculas
                indice=letras.index(palabra[i].lower())
                if indice+num >len(letras)-1:
                    indice=indice-len(letras)-1
                resultado= resultado + letras[indice+num].upper()
                letras[indice+num].lower()
        
    i=i+1
    
    print(resultado)
   
#incriptaCesar(palabra,20)


clave="secreto"

def incriptacionvigenere(palabra,clave):
    resultado=""
    i=0
    j=0
    indice=0
    caracter=""
    while i< len(palabra):
        if palabra[i]==" ":
            resultado=resultado+" "
            caracter=" "
        else:
            indice=letras.index(palabra[i])       
            try:  
                indice = control((indice+letras.index(clave[j])),letras)
                caracter=letras[indice]
                resultado = resultado + caracter
            except:
                indice=letras.index(palabra[i].lower())
                indice= control((indice+letras.index(clave[j])),letras)
                caracter= letras[indice].upper()
                resultado= resultado + caracter
                letras[indice].lower()        
        i=i+1
        if j>len(clave)-2:
            j=0
        else:
            if indice<len(letras)-2 and caracter!=" ":
                j=j+1
            
    print(resultado)


incriptacionvigenere(palabra,clave)


#letras.index(clave[control(j,clave)])

#wp tzs xgle himh m usp lr isr