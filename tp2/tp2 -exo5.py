a=int(input("Entrez un nombre entier:"))
if a<0:
    if a%2 == 0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")

if a>0 :
    if a%2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
if a==0:
    print("Le nombre est 0 et pair")
