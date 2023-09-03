import string as s
import argparse

ALPHABET: str = s.ascii_letters + s.digits + s.punctuation

def encrypt(message: str, shift: int) -> str:
    """This function encrypts string by Caesar method.
    
        Arguments
        ---------
            message: str 
                The information which will be encrypted.
            shift: int
                The size of shift in Caesar encryption.

        Return
        ------
            str
                Encrypted message.
    """
    return''.join([ALPHABET[(ALPHABET.index(i) + shift)  % len(ALPHABET)] if i in ALPHABET else i for i in message])

def decrypt(message: str, shift: int) -> str:
    """This function decrypts string by Caesar method.
    
        Arguments
        ---------
            message: str 
                The information which will be decrypted.
            shift: int
                The size of shift in Caesar decryption.

        Return
        ------
            str
                Decrypted message.
    """
    return encrypt(message, -shift)

parser = argparse.ArgumentParser(prog="Caesar_Cypher_and_Decypher",
                                 usage="This software takes three parameters and returns message encrypted by Caesar cypher.",)

parser.add_argument("shift", type=int, help="Means the shift for encryption/decryption.")
parser.add_argument("message", type=str, nargs="+", help="Message to enctrypt or decrypt.")
parser.add_argument("--operation", dest='operation', const=decrypt, default=encrypt, action="store_const", help="Choose enctryption or decryption.")

args = parser.parse_args()
print(args.operation(" ".join(args.message), args.shift))
