from random import *

def password_generator(length):
    symbols =("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:><")
    password =''.join(choice(symbols) for _ in range(length))
    return password

length =int(input("kaç harfli bir şifre istersin: "))
password =password_generator(length)

print(f"şifreniz: {password}")


#import random
#karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#sifre_uzunlugu = int(input("istediğiniz şifre uzunluğunu girin : "))

#sifre =""

#for i in range(sifre_uzunlugu):
#    sifre += random.choice(karakterler)
    
#print(sifre)