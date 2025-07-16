def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Cæsar Chiffer ===")
    choice = input("Vil du (E)nkrtypere eller (D)ekryptere? ").upper()
    text = input("Skriv inn tekst: ")
    shift = int(input("Hvor mange plasser skal forskyves? (eks: 3): "))

    if choice == "E":
        encrypted = caesar_encrypt(text, shift)
        print("Kryptert tekst:", encrypted)
    elif choice == "D":
        decrypted = caesar_decrypt(text, shift)
        print("Dekryptert tekst:", decrypted)
    else:
        print("Ugyldig valg!")

if __name__ == "__main__":
    main()
