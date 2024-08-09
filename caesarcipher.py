def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')        
            if mode == 'encrypt':
                result += chr((ord(char) - start + shift) % 26 + start)
            elif mode == 'decrypt':
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result
def main():
    while True:
        mode = input("Select 'encrypt' or 'decrypt' for your message ").lower()
        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        processed_text = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed message is: {processed_text}")
        again = input("Would you like to run the program again? (yes/no): ").lower()
        if again != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
