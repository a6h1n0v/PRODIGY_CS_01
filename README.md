# Caesar Cipher 

This project implements a simple Caesar Cipher in Python. The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted by a certain number of places down or up the alphabet. This implementation allows the user to both encrypt and decrypt messages using a specified shift value.

## Features

- **Encryption**: Shift the letters of your message forward by a specified number of places.
- **Decryption**: Shift the letters of your message backward by the same number of places to restore the original text.
- **Looped Interface**: The program runs continuously, allowing multiple encryptions and decryptions until the user chooses to exit.

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/caesar-cipher.git
    cd caesar-cipher
    ```

2. **Run the Program**:
    To run the Caesar Cipher program, execute the following command:
    ```bash
    python3 caesar_cipher.py
    ```

3. **User Input**:
    - The program will prompt you to choose whether to encrypt or decrypt a message.
    - Enter the message you wish to process.
    - Enter the shift value (an integer) that will be used for the cipher.

4. **Example**:
    ```text
    Select 'encrypt' or 'decrypt' for your message: encrypt
    Enter your message: Hello World
    Enter the shift value: 3
    The encrypted message is: Khoor Zruog
    Would you like to run the program again? (yes/no): yes
    ```

5. **Exit**:
    - To exit the program, type `no` when prompted with the "Would you like to run the program again?" message.

## Requirements

- Python 3.x

## Customization

You can easily modify the code to adjust the range of characters the cipher processes or to implement other variations of the Caesar Cipher.

## Author

- **Abhinav T** - 


