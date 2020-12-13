letras=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")
palabra="El rio esta frio y con un pez"
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
                if indice+num >len(letras)-1:
                    indice=indice-len(letras)-1
                resultado= resultado + letras[indice+num]
        except:#Mayusculas
            indice=letras.index(palabra[i].lower())
            if indice+num >len(letras)-1:
                    indice=indice-len(letras)-1
            resultado= resultado + letras[indice+num].upper()
        
        i=i+1
    
    print(resultado)
   
incriptaCesar(palabra,20)