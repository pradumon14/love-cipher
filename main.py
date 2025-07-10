# main.py
# 💌 LoveCipher — A Fun Caesar Cipher Tool for Love Letters
# Created by Pradumon 💖

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char  # emojis, punctuation, and symbols stay the same
    return result

def brute_force(text):
    print("\n💘 Trying all keys to decode your love letter:\n")
    for shift in range(1, 26):
        guess = caesar_cipher(text, shift, mode='decrypt')
        print(f"🔓 ROT-{shift:2}: {guess}")

def get_multiline_input(prompt):
    print(prompt + " (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("\n💌 Welcome to LoveCipher 💌")
    print("1. 💕 Write & Encrypt a Love Letter")
    print("2. 💖 Read & Decrypt a Love Letter")
    print("3. 💔 Forgot the Key? Brute-force it")
    print("")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        message = get_multiline_input("\n📝 Write your love letter below")
        shift = int(input("🔐 Choose a secret ROT key (1–25): "))
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print("\n📩 Encrypted Love Letter:\n")
        print(encrypted)

    elif choice == '2':
        cipher_text = get_multiline_input("\n🔐 Paste your encrypted love letter below")
        shift = int(input("🔑 Enter the ROT key (1–25): "))
        decrypted = caesar_cipher(cipher_text, shift, mode='decrypt')
        print("\n💖 Decrypted Love Letter:\n")
        print(decrypted)

    elif choice == '3':
        cipher_text = get_multiline_input("\n🔍 Paste the encrypted letter (no key needed)")
        brute_force(cipher_text)

    else:
        print("⚠️ Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
