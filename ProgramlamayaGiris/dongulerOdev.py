# kişi vize ve final girecek,
# vize %40 , final %60
# o dersin ortalamasını hesaplayıp geçip kalma durumuna göre işlem yapacaksınız
# program sonunda girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır.

girilecekNotSayisi = int(input("Kaç adet not gireceksiniz? "))
vizeler = []
finaller = []
ortalamalar = []

for notlar in range(girilecekNotSayisi):
    vize = int(input(f"{notlar + 1}. vize notunu giriniz: "))
    final = int(input(f"{notlar + 1}. final notunu giriniz: "))

    vizeler.append(vize)
    finaller.append(final)

    ortalama = vize * 0.4 + final * 0.6
    if ortalama < 50:
        print(f"{notlar + 1}. dersin ortalaması: {ortalama} Kaldınız :(")
    else:
        print(f"{notlar + 1}. dersin ortalaması: {ortalama} Geçtiniz :)")
    print("***********************************")

    ortalamalar.append(ortalama)
    
for i in range(girilecekNotSayisi):
    print(f"{i+1}. Vize, Final, Ortalama : {vizeler[i]}, {finaller[i]}, {ortalamalar[i]}")
    