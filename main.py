letras=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

palabra="el rio esta frio y con un pez"
num=3
#print(letras.index("a"))

def incriptaCesar(palabra,num):
    i=0
    palabra.lower()
    resultado=""
    while i< len(palabra):
        try:
            indice=letras.index(palabra[i])
            if indice+num >len(letras):
                indice=indice-len(letras)
            resultado= resultado + letras[indice+num]
        except:
            resultado =resultado + " "
        i=i+1
    
    print(resultado)
   

incriptaCesar(palabra,20)