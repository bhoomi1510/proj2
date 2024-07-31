def Encryption(string,step):
    encrypttext=[]
    capletter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B']
    lowletter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','q','r','s','t','u','v','w','x','y','z','a','b']
    for i in string:
        if i in capletter:
            index=capletter.index(i)
            encrypt=index+step
            newletter=capletter[encrypt]
            encrypttext.append(newletter)
        elif i in lowletter:
            index=lowletter.index(i)
            encrypt=index+step
            newletter=lowletter[encrypt]
            encrypttext.append(newletter)
    return encrypttext

def Decryption(string,step):
    encrypttext=[]
    capletter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowletter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','q','r','s','t','u','v','w','x','y','z']
    for i in string:
        if i in capletter:
            index=capletter.index(i)
            encrypt=index-step
            newletter=capletter[encrypt]
            encrypttext.append(newletter)
        elif i in lowletter:
            index=lowletter.index(i)
            encrypt=index-step
            newletter=lowletter[encrypt]
            encrypttext.append(newletter)
    return encrypttext

userinput=input("for encryption enter 1 and for decryption enter 2>").lower()

if userinput=="1":
    string=input("enter text>")
    print(''.join(Encryption(string,2)))
elif userinput=="2":
    string=input("enter text>")
    print(''.join(Decryption(string,2)))
else:
    print("invalid input")