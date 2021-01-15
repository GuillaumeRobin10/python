def encore ():
    continuer_str_array = input ("voulez vous continuer ? ")
    continuer_str_array = continuer_str_array.lower()
    continuer_str_array = continuer_str_array.split()
    if continuer_str_array[0] == "continuer" or continuer_str_array[0] == "oui":
        return True
    else :
        return False
    return False

def calcul (nb1,ope,nb2) :

    try :
        if ope == "+" :
            print (f"le resultat de {nb1} + {nb2} est {nb1 + nb2}")
            return 0
        elif ope == "-" :
            
            print (f"le resultat de {nb1} - {nb2} est {nb1 - nb2}")
            return 0
        elif ope == "*" :
            
            print (f"le resultat de {nb1} * {nb2} est {nb1 * nb2}")
            return 0
        elif ope == "/" :
            print (f"le resultat de {nb1} / {nb2} est {nb1 / nb2}")
            return 0
        else :
            return 9999.0
    except :
        return 9998.0


def Operation ():
    operation_str = input (" entrez une opération : ")
    operation_str = operation_str.strip()
    operation_str = operation_str.split()
    longeur = len(operation_str)
    if longeur == 3 :
        try :
            nombre1 = int(operation_str [0])
            operation = operation_str [1]
            nombre2 = int(operation_str [2])
            if operation == "+" or operation == "-" or operation == "*" or operation == "/" :
                return calcul (nombre1,operation,nombre2) 
                print ("ok")
            else :
                return 9997.0
        except :
            return 9996.0
    else :
        return 9995.0


continuer = True
resultat = 0.0
while continuer :
    resultat = Operation()
    if resultat == 9999.0 :
        print("une erreur d'opérateur est survenur")
    elif resultat == 9998.0 :
        print ("impossible de diviser par 0")
    elif resultat == 9997.0 :
        print ("erreur opérateur")
    elif resultat == 9996.0 :
        print ("merci de renseigner des chiffres")
    elif resultat == 9995.0 :
        print ("merci de renseigne un calcule a 2 nombre et 1 seul opérateur")
    else :
        print("")

    continuer = encore()

print("Bien on arrêt la, à bientôt")

