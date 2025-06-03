def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# Fonction de chiffrement Vigenère
def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)

    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i].upper()) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i].lower()) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return "".join(encrypted_text)

# Saisie utilisateur pour chiffrement
texte = input("Entrez le texte à chiffrer : ")
cle = input("Entrez la clé : ")

texte_chiffre = encrypt_vigenere(texte, cle)
print("Texte chiffré :", texte_chiffre)