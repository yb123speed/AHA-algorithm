# _*_ coding:utf-8 _*_
#!/usr/local/bin/python

encrypted = [6,3,1,7,5,8,9,2,4]

def decrypt(encryptedTxt):
    head = 0
    tail = len(encryptedTxt)-1
    decrypted = []

    while len(encryptedTxt)>0:
        decrypted.append(encryptedTxt[0])
        del encryptedTxt[0]
        print(encryptedTxt)
        if(len(encryptedTxt)<=0):
            break
        encryptedTxt.append(encryptedTxt[0])
        del encryptedTxt[0]
        print(encryptedTxt)
    
    return decrypted

if __name__ == "__main__":
    decrypted = decrypt(encrypted)
    print(decrypted)


