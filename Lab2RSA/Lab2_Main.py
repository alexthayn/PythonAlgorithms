#Driver for RSA Lab
import Lab2_RSA

def main():
    m = input("Enter a message to be encrypted: ")
    message = str(m)
    Ciphertext = Lab2_RSA.EncryptRSA(message)
    print("The original message was: " + message)
    print("The encrypted message is: ")

    print(Ciphertext)

    print("The decrypted cipher: ")
    Message = Lab2_RSA.DecryptRSA(Ciphertext)
    print(Message)

main()
