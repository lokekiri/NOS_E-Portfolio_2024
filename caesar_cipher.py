def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift_amount) % 26) + 97)
            result += new_char
        else:
            result += char
    return result

# Example usage
message = "HELLO"
shift_key = 3
print("Encrypted:", caesar_cipher(message, shift_key))
print("Decrypted:", caesar_cipher(caesar_cipher(message, shift_key), shift_key, mode="decrypt"))
