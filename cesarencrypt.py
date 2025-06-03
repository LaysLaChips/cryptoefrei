def encrypt(text, s):
    result = ""

    # parcourir le texte caractère par caractère
    for i in range(len(text)):
        char = text[i]

        # Chiffre les majuscules
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Chiffre les minuscules
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        # Laissez les autres caractères (par exemple, l'espace, la ponctuation) inchangés
        else:
            result += char

    return result


# Get user input
text = input("Entrez le texte à chiffrer : ")
s = int(input("Entrez le décalage (shift) : "))

# Display the result
print("Texte  :", text)
print("Décalage :", s)
print("Texte chiffré :", encrypt(text, s))