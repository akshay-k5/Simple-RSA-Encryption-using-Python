#SIMPLE RSA  ASYMMETRIC ENCRYPTION DEMO

# ---------- Extended Euclidean Algorithm & RSA helpers ----------

def egcd(a: int, b: int):
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b)
    """
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return old_r, old_x, old_y  # gcd, x, y

def modinv(a: int, m: int) -> int:
    """
    Multiplicative inverse of a modulo m, i.e., a*d ≡ 1 (mod m).
    Raises ValueError if inverse doesn't exist (gcd(a, m) != 1).
    """
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse: gcd({a}, {m}) = {g} ≠ 1")
    return x % m

#_KEY_GENERATION_INITIALISATION_AND_VALIDATION

from math import gcd

def checkprime(p : int):
    flag=0
    for i in range(2,p):
        if(p%i==0):
            flag=1
    if(flag==0):
        return True
    return False

def userkeygen():
    p,q=map(int,input(f'Enter P Q FOR USER :').split())
    if p == q:
        print("P and Q can't be Equal !!")
        userkeygen()
    if(checkprime(p) and checkprime(q)):
        phi = (p - 1) * (q - 1)
        e=int(input(f"Enter value for e (1<e<{phi}):"))
        if not (1 < e < phi) or gcd(e, phi) != 1:
            print(f"e must be in (1, phi) and coprime to phi. Given e={e}, phi={phi}\n")
            userkeygen()
        d = modinv(e, phi)
        n=p*q
        return n, e, d
    else:
        print("Enter Prime numbers!!!")
        userkeygen()

#Message Enter code
def message_ascii(msg):
    ASCIIlist=[ord(i) for i in msg]
    print('ASCII: ',ASCIIlist)
    return ASCIIlist


def message_char(ASCIIlist):
    msg=''
    for i in  ASCIIlist:
        msg+=chr(i)
    return msg

#Message Encryption block
def encrypt(asciilist,e,n):
    encrypted=[]
    for c in asciilist:
        val=c**e % n
        encrypted.append(val)
    return encrypted

#Message Decryption block

def decrypt(encrypted,d,n):
    decrypted=[]
    for m in encrypted:
        val=m**d % n
        decrypted.append(val)
    return decrypted

### MAIN PROGRAM

import sys
N1,E1,D1= userkeygen()
while(1):
    print("\n------MENU------")
    print("-> Enter 1 to Send a message   : ")
    print("-> Enter 2 to Decrypt message  : ")
    print("-> Enter 3 to exit")
    print()
    res=int(input("Enter response:"))
    if(res==1):
        public,N2=map(int,input("Enter the Public Key and Modulus of Receiver :").split())
        msg=list(input("Enter the text message:"))
        asciilist=message_ascii(msg)                   #ASCII VALUE LIST
        encryptmsg=encrypt(asciilist,public,N2)         #ENCRYPTED ASCII VALUE LIST
        print("Encrypted Message:",message_char(encryptmsg))


    elif(res==2):
        print("--Public Key :",E1)
        print("--Modulus    :",D1)
        N2=int(input("Enter Sender Modulus :"))
        msg=list(input("Enter the Cipher text message:"))
        asciilist=message_ascii(msg)                   #ASCII VALUE LIST

        print(f">>>Private Key  is {D1}")
        Decryptmsg=decrypt(asciilist,D1,N2)        #DECRYPTED ASCII VALUE LIST
        print(f"ASCII decrypted by user1 using Private key of user1 :{Decryptmsg}")
        print()
        print(f"Decrypted message :{message_char(Decryptmsg)}")
        print()

    elif(res==3):
        sys.exit(0)
    else:
        print("Invalid Input......\n")
