# 3 adet sayısal değişken tanımlayınız.
# Bu sayılardan en büyük ve en küçük olanı ekrana ayrı ayrı yazdırınız.

a = 145
b = 141
c = 35

if(a < b and a < c):
    print(f"En küçük sayı: {a}")
    if(b < c):
        print(f"En büyük sayı: {c}")
    elif(c < b):
        print(f"En büyük sayı: {b}")

elif(b < a and b < c):
    print(f"En küçük sayı: {b}")
    if(a < c):
        print(f"En büyük sayı: {c}")
    elif(c < a):
        print(f"En büyük sayı: {a}")

else:
    print(f"En küçük sayı: {c}")  
    if(b < a):
        print(f"En büyük sayı: {a}") 
    if(a < b):
        print(f"En büyük sayı: {b}")
