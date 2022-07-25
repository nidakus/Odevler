# ****************************

# Salary Hike 

# salary tam sayı veri tipinde maaşınızı temsil eden değerdir. 
# hike tam sayı veri tipinde maaşınıza yapılacak olan yüzdelik % bazında zam miktarıdır. (bu değerleri kullanıcıdan alınız.)
# Zammın uygulanması sonucu yeni maaşı ekrana yazdırınız.


# ****************************

# ****************************

# Is Prime?

# `num`  bir pozitif tam sayıdır (integer). 
# `num` sayısı eğer bir asal sayı ise `true` döndürün, değilse `false` döndürün.  (num değerini kullanıcıdan alınız)

# 1 ve kendisinden başka pozitif böleni olmayan 1 den büyük doğal sayılara **asal sayı** denir.
#  2, 3, 5, 7, 11, 13, 17, 19, 23… sayıları birer asal sayıdır.


# ****************************
salary = int(input("Maaşınızı giriniz:"))
hike = int(input("Zam yüzdenizi giriniz:"))
newSalary = salary + (salary*(hike/100))

print(f"Yeni maaşınız:{newSalary}")

# ******************************

num = int(input("Sayı giriniz: "))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num," Asal sayı değildir.")
            break
        else:
            print(num," Asal sayıdır.")
else:
    print(num," Geçersiz sayı girdiniz.")
