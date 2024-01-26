
# # BYURTMA QABUL QILUVCHI DASTUR

# orders = []

# while True:
#     order = input("\nbuyurtmangizni kiriting ")
#     orders.append(order)
#     sikl = input("\nYana byurtma berasizmi( ha / yoq)")
#     if sikl.lower() == 'yoq':
#         break
# print(orders)

"""---------------------------IKKINCHI TOPSHIRIQ--------------------------------------------"""

# # e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# # Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang

# products = {}
# while True:
#     print("e-bozor da sotmoqchi bolgan maxsulot nomi narxini kiriting")
#     product_name = input("Maxsulot nomi ")
#     product_price = input("Maxsulot  ")
#     int(product_price)
#     products[product_name] = product_price

#     sikl = input("maxsulot kiritmoqchimisiz? (ha/yoq)")
#     if sikl.lower() == 'yoq':
#         break 
# print(products)


"""---------------------------UCHINCHI TOPSHIRIQ--------------------------------------------"""

""" Yuqoridagi ikki dasturni jamlaymiz. 
    Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
    (tayyor ro'yxat ishlatishingiz mumkin).
    Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, 
    aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating. """


products = {}
while True:
    print("e-bozor da sotmoqchi bolgan maxsulot nomi narxini kiriting")
    product_name = input("Maxsulot nomi ")
    product_price = input("Maxsulot  ")
    int(product_price)
    products[product_name] = product_price

    sikl = input("maxsulot kiritmoqchimisiz? (ha/yoq)")
    if sikl.lower() == 'yoq':
        break 
print(products)

orders = []

while True:
    order = input("\nbuyurtmangizni kiriting ")
    orders.append(order)
    sikl = input("\nYana byurtma berasizmi( ha / yoq)")
    if sikl.lower() == 'yoq':
        break
print(orders)

for order_product in orders:
    if order_product in products.keys():
        print(f"Bizda siz buyurtma qilgan {order_product} bor narxi- {products[order_product]}")
    else:
        print(f"\nBizda  {order_product} afsuski yoq ")



