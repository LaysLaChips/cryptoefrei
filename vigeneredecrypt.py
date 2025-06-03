def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


# Fonction de déchiffrement Vigenère
def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)

    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i].upper()) + 26) % 26 +
                                 ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i].lower()) + 26) % 26 +
                                 ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)

    return "".join(decrypted_text)


# === Saisie utilisateur pour déchiffrement ===
texte = input("Entrez le texte chiffré : ")
cle = input("Entrez la clé : ")

texte_dechiffre = decrypt_vigenere(texte, cle)
print("Texte déchiffré :", texte_dechiffre)