# Lab 11

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift_letter(letter, k):
    # Shif only letters
    if letter.isalpha():
        is_lower = letter.islower()
        oneletter = letter.upper()

        i = a.find(oneletter)
        if i == -1:
            return letter

        i = i + k
        i = i % 26
        r = a[i]

        return r.lower() if is_lower else r
    else:
        return letter

def caesar_with_key(text, k):
    result = ""
    for ch in text:
        result += shift_letter(ch, k)
    return result

def break_caesar(text):
    for k in range(26):
        decoded = caesar_with_key(text, k)
        print("Key", k, "-->", decoded)

def main():
    ciphertext = input("Enter the text to break (caesar cipher): ")
    print("\nAll Possible Shifts:")
    break_caesar(ciphertext)

if __name__ == "__main__":
    main()