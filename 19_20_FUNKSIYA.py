# def info(ism, t_yil, joriy_yil = 2024):
#     """Ismingizni hamda tug'ulgan yilingizni kiriting  info(ismingiz, tug'ulgan yilingiz)"""
#     print(f" {ism.title()} sizning yoshingiz {joriy_yil-t_yil} da")

# info('Abdukarim', 2001 , )

# def darajaga_kotaruvchi(son):
#     """Siz kiritgan sonni 1 dan 10 darajaga kotarib beradi va listga joylaydi"""
    
#     son_darajasi = []
#     for n in range(1,11):
#         son_darajasi.append(son**n)
#         print(f"{son} ning {n}-darajasi {son**n}")

# darajaga_kotaruvchi(2)

# def chek_juft_toq(son):
#     """sonni juf yoki toqligini aniqlovchi funksiya"""
#     if son % 2 == 0:
#         print(f" {son} juft son")
#     else:
#         print(f"{son} toq son")

# chek_juft_toq(5)

# def chek_katta_kichik(son1,son2):
#     """Ikki sonni taqqoslovchi funksiya"""
#     if son1 > son2:
#         print(f"{son1} {son2}dan katta")
#     elif son2 > son1:
#         print(f"{son2} {son1}dan katta")
#     else:
#         print("ikkala sonlar teng")
# chek_katta_kichik(12,12)

# def daraja(son, daraja = 2):
#     """Sonni darajaga ko'taruvchi funksiya"""
#     natija = son ** daraja
#     print(natija)
# daraja(2,4)

# def bolish_hossai(son):
#     """Argumentdagi sonni 2 dan 10 gacha qoldiqsiz bo'linishini tekshiradi"""
#     for n in range(2,11):
#         if son % n == 0:
#             print(f"{son} ni {n} ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{son} ni {n} ga qoliqli bo'linadi")
# bolish_hossai(88)




# def info_you(name, surname, b_year, tel_num = None, email = None):
#     """Foydalanuvchini to'liq malumotlarini saqlavchi funksiya\n info_you(ismi, familiyasi, telefon raqami, elektron pochtasi)"""
#     info_general = {'name': name, 'surname': surname, 'b_year':b_year, 'tel_nam': tel_num, 'email': email}

#     return info_general

# print(info_you('Abdukarim', 'Vakhobov', 2001, None, 'aseswweew'))
# persons = []
# while True:
#     ism = input("Ismingizni kirting ")
#     familiya = input("Familiyangizni kiriting ")
#     t_yil = input("Tug'ulgan yilingizni kiriting ")
#     tel_num = input("Telefon raqamingizni kiriting ")
#     email = input("Elektron pochta manzilingizni kiriting ")
#     print("\nMalumotlaringiz qabul qilindi  ")
#     sikl = input("davom etishni istaysizmi (ha / yoq) ")
#     sikl.lower()
#     print(info_you(ism, familiya, t_yil, tel_num, email))
#     persons.append(info_you(ism, familiya, t_yil, tel_num, email))
#     if sikl != 'ha':
#         break

# print(persons)




# def max_nam(son1, son2, son3):
#     """Uchta son kiritasiz va funksiya eng katta qiymatni topib beradi"""
#     numbers = [son1, son2, son3]
#     result = max(numbers)
#     return result
# print(max_nam(123, 124, 222))





# import math
# def aylana(radus):
#     """Aylananing radusini kiritasiz va funksiya sizga aylananing diametri, aylana uzunligini, yuzasini topib lug'atga joylaydi"""
#     diametr = 2*radus
#     uzunligi = 2*radus*math.pi
#     yuza = 2*math.pi*radus**2
#     aylana_parametr = {"radus":radus, "diametr": diametr, 'yoy_uzunligi': uzunligi, "yuza":yuza}
    
#     return aylana_parametr
# print(aylana(3))


# def tub_son(min, max):
#     """siz kiritgan oraliqda tub sonlarini listga joylab qiymat qaytaradi"""
#     tub_sonlar = []
#     for n in range(min,max+1):
#         result = True
#         for m in range(2,n):
#             if n % m == 0:
#                 result = False
#         if result:
#             tub_sonlar.append(n)
#     return tub_sonlar
# print(tub_son(1,100))



# def oraliq(min, max=None, qadam = 1):
#     """Minumum va Maxsimum kiritilgan sonlarni qadam va qadam listga joylatdi \n Agar qadam kiritilmasa qadamni 1 deb oladi"""
#     if max == None:
#         """ bu agar minumum qiymtni kiritmasdan max qiymat kiritilganda """
#         max = min
#         min = 1

#     sonlar = []
#     while min < max:
        
#         sonlar.append(min)
#         min = min +qadam
#     return sonlar
# print(oraliq(5))



"""Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
Bunda boshlang’ish had ko’pincha 1 deb olinadi.
  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,..."""



