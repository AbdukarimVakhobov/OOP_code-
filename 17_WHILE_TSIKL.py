"""-----------------------------------BIRINCHI TOPSHIRIQ-----------------------------------------------------"""
# print("yoqtirgan kitoblarizni kiriting\n So'rovnomani toxtatish uchun STOP kalit so'zini kiriting")
# books = []
# while True:
#     book = input()
    
#     if book.lower() == 'stop':
#         break
#     books.append(book)

# print(books)

"""-----------------------------------IKKINCHI TOPSHIRIQ------------------------------------------------------"""

# print("Yoshingizga mos chipta narxini bilish uchun dastur",
#       "\n Dasturni tugatish uchun QUIT yoki EXIT kalit so'zni kiriting ")
# while True:
#     age = input("\nYoshingizni kiriting ")
#     if age.isdigit():
        
#         if int(age) <= 7:
#             print("siz uchun chipta narxi 2000 so'm")
#             #narxni iteger tipida foydalanish kerak bolganda foydalanish uchun qoldirdim
#             narx = 2000
#         elif int(age) <= 18 and int(age) > 7:
#             print("siz uchun chipta narxi 3000 so'm")
#             #narxni iteger tipida foydalanish kerak bolganda foydalanish uchun qoldirdim
#             narx = 3000
#         elif int(age) < 65 and int(age) > 18:
#             print("siz uchun chipta narxi 10000 so'm")
#             #narxni iteger tipida foydalanish kerak bolganda foydalanish uchun qoldirdim
#             narx = 10000
#         elif int(age) >= 65:
#             print("siz uchun chipta bepul")
#             #narxni iteger tipida foydalanish kerak bolganda foydalanish uchun qoldirdim
#             narx = 0

#     elif age.lower() == 'exit' or age.lower() == 'quit':
#         print('dastur mofiqiyatli yakunlandi')
#         break

#     else:

#         print("Yoshizni raqam shaklida yoki dasturni tugatuvchi kalit so'z kiriting")



"""----------------------------------UCHINCHI TOPSHIRIQ------------------------------------------------"""



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.lower()=='exit':
        break
    elif int(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")