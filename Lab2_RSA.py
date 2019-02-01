#Alex Thayn
import sys

#Write and test the extended Euclid's algorithm
#Extended euclidean algorithm: ax + by = gcd(a,b)
def ExtendedEuclidean(a,b):
    #Base case
    if(a == 0):
        return b, 0, 1
    else:
        gcd, x, y = ExtendedEuclidean(b%a, a)
        return (gcd, y - (b//a)*x, x)
    

#Write and test the efficient power mod algorithm
def PowerMod(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b /=2
        if b == 0: 
            break
        a = a * a % n
    return r

#Write and test a function that finds the multiplicative inverse of a mod n
def MultiplicativeInverse(a,n):
    gcd, x, y = ExtendedEuclidean(a,n)
    #A multiplicative inverse only exists if a and n are relatively prime, so gcd must be 1
    if(gcd == 1):
        #Get rid of negative values
        if(x < 1): 
            return x % n
        return x
    return 0

#Write and test a function that converst a string to an array of integers to encrypt 
def StringToIntArr(message):
    messageList = list(message)
    intList = [int(ord(s)) for s in messageList]
    return intList

#Write and test a function that converts back from integer array to string
def IntArrToString(intArr):
    message = ''
    for i in intArr:
        message = message + chr(i)
    return message

#Write and test encryption and decryption

def EncryptRSA(message):
    #convert message to int array
    intArr = StringToIntArr(message)
    cipher = [0]*len(intArr)
    for i in range(len(intArr)):
        cipher[i] = PowerMod(intArr[i],e,n)
    return cipher

def DecryptRSA(intArr):
    m = (p-1)*(q-1)
    d = MultiplicativeInverse(e,m)
    messageArr = [0]*len(intArr)
    for i in range(len(intArr)):
        messageArr[i] = PowerMod(intArr[i], d, n)
    return IntArrToString(messageArr)

###################################################
###################### TESTS ######################
###################################################

def test_ExtendedEuclidean():
    assert ExtendedEuclidean(0,0) == (0,0,1)
    assert ExtendedEuclidean(1,1) == (1,1,0)
    assert ExtendedEuclidean(1,2) == (1,1,0)
    assert ExtendedEuclidean(2,1) == (1,0,1)
    assert ExtendedEuclidean(100,2) == (2,0,1)
    assert ExtendedEuclidean(100,50) == (50,0,1)
    assert ExtendedEuclidean(12,18) == (6,-1,1)
    assert ExtendedEuclidean(1024,20) == (4,1,-51)

def test_PowerMod():
    assert PowerMod(6,2,3) == 0
    assert PowerMod(1,8,2) == 1
    assert PowerMod(2,8,7) == 4
    assert PowerMod(8,3,49320) == 512
    assert PowerMod(100,918,2000403402) == 1194280768

def test_MultiplicativeInverse():
    assert MultiplicativeInverse(0,0) == 0
    assert MultiplicativeInverse(0,1) == 0
    assert MultiplicativeInverse(3,11) == 4
    assert MultiplicativeInverse(3,43) == 29
    assert MultiplicativeInverse(23,28) == 11
    assert MultiplicativeInverse(324,4123) == 2965

def test_StringToIntArr():
    assert StringToIntArr('') == []
    assert StringToIntArr('1a@#') == [49, 97, 64, 35]
    assert StringToIntArr('1,2,3,4') == [49, 44, 50, 44, 51, 44, 52]
    assert StringToIntArr('abcde') == [97,98,99,100,101]
    assert StringToIntArr('HELLO!') == [72,69,76,76,79,33]

def tets_IntArrToString():
    assert StringToIntArr([]) == ''
    assert StringToIntArr([49, 97, 64, 35]) == '1a@#'
    assert StringToIntArr([49, 44, 50, 44, 51, 44, 52]) == '1,2,3,4'
    assert StringToIntArr([97,98,99,100,101]) == 'abcde'
    assert StringToIntArr([72,69,76,76,79,33]) == 'HELLO!'

###################################################
#################### END TESTS ####################
###################################################

#Choose p, q, and e to be three large, random prime numbers in increasing order
p = 129485023332071707933738382916401449533641429854401982997094004590315877456171636358095039465240846827538029950571129593738792376890229674390327761144443983750216503536908345315421877704009030386457606021982880563161989106528276736547445291897101752828333504822305817794362568577622132836880295842256828790663
q = 153715834450489562463849837675877072003597968603772497851993838998671736216460867072809004851853984784500916582056424506818121582249876434026855099884649811135710709303203754995652355774351958175103715494697141939913847139824283438873455911864292614373543989722102037383089106515386884300815378110108716900969
e = 174936522803921418571387048546144057648483486437030569660913986547830736401921573836149603460433706344137498637531461621214146833189489981579451352331285554371733332543772088955179877027166430734220696794537447498152611353914320533702480407937301402657378278430173894544681733621258698183254290589113435098079
n = p*q

message = "Hello!!"
Ciphertext = EncryptRSA(message)
print("The original message was: " + message)
print("The encrypted message: ")
print(Ciphertext)

print("The decrypted cipher: ")
Message = DecryptRSA(Ciphertext)
print(Message)