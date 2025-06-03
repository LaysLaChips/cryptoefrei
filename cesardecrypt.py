def decrypt(text, s):
    result = ""

    # Parcourir chaque caractère du texte
    for i in range(len(text)):
        char = text[i]

        # Déchiffrer les majuscules
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Déchiffrer les minuscules
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)

        # Conserver les autres caractères tels quels
        else:
            result += char

    return result

# Entrées utilisateur
text = input("Entrez le texte chiffré : ")
s = int(input("Entrez le décalage (shift) utilisé : "))

# Résultat
print("Texte chiffré :", text)
print("Décalage :", s)
print("Texte déchiffré :", decrypt(text, s))