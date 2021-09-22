def Decimaltobinary(dec):
    binary = ""
    while(dec):
        x = dec%2
        binary+=str(x)
        dec= dec//2
    binary = binary[::-1]
    return binary

def binarytoDecimal(binary):
    dec = 0
    m=1
    while(binary):
        x = binary%10
        dec = dec + x*m
        m*=2
        binary = binary//10
    return dec

def DecimaltoOctal(dec):
    octal = ""
    while(dec):
        x = dec%8
        octal+=str(x)
        dec=dec//8
    octal= octal[::-1]
    return octal
    
def OctaltoDecimal(octal):
    dec=0
    m=1
    while(octal):
        x = octal%10
        dec = dec+ m*x
        m*=8
        octal =octal//10
    return dec

def DecimaltoHexadecimal(dec):
    hexa = ""
    while(dec):
        x = dec%16
        if(x<=9):
            hexa+= str(x)
        else:
            hexa+= chr(65+x-10)
        dec = dec//16
    hexa = hexa[::-1]
    return hexa
    
def HexadecimaltoDecimal(hexa):
    m=1
    dec=0
    i= len(hexa)-1
    while(i >= 0):
        if(hexa[i]>='0' and hexa[i]<='9'):
            dec+= int(hexa[i]) * m
        else:
            dec+= (ord(hexa[i])-65+10) * m
        m*=16
        i=i-1
    return dec
    
flag = 1
while(flag):
    print("1.Decimal to binary\n2.binary to Decimal\n3.Decimal to octal\n4.Octal to decimal\n5.Decimal to hexadecimal\n6.hexadecimal to decimal\n7.Exit")
    n =int(input("Enter your choice : "))
    if(n == 1):
        dec = int(input("Enter decimal number : "))
        print("Decimal : ",dec," --> binary : ",Decimaltobinary(dec))
    elif(n == 2):
        binary = int(input("Enter binary number : "))
        print("binary : ",binary," --> Decimal : ",binarytoDecimal(binary))
    elif(n == 3):
        dec = int(input("Enter decimal number : "))
        print("Decimal : ",dec," --> Octal : ",DecimaltoOctal(dec))
    elif(n == 4):
        octal = int(input("Enter octal number : "))
        print("Octal : ",octal," --> Decimal : ",OctaltoDecimal(octal))
    elif(n == 5):
        dec = int(input("Enter decimal number : "))
        print("Decimal : ",dec," --> Hexadecimal : ",DecimaltoHexadecimal(dec))
    elif(n == 6):
        hexa = input("Enter hexadecimal number : ")
        print("Hexadecimal : ",hexa," --> Decimal : ",HexadecimaltoDecimal(hexa))
    elif(n == 7):
        flag=0
    else:
        print("Wrong choice")

print("Thank You!!!")