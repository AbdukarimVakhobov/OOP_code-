# print('BIRINCHI TOPSHIRIQ')

# dictionary = { 'boolean': 'mantiqiy qiymat', 'Float': "o'nlik son", "for":"biror amalni qayta bajarish sikli",
#               'if': "biror shartni tekshirish operatori", 'integer': "butun son"
#               }

# for key  in sorted(dictionary):
#     print(f" {key} - {dictionary[key]}")

# print('IKKINCHI TOPSHIRIQ')

# cauntries = {"AQSH": "Washinton", "Italiya":'Rim', "Rossiya":"Maskva", "O'zbekiston":"Toshkent"}

# print('Davlatlar     Poytaxti')
# for state, capital in sorted(cauntries.items()):
#     print(state, capital)

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }


print("Uchta taom buyirtma bering")
order = []
for n in range(1,4):
    food = input(f" {n}- taomni kriting ")
    food.lower()
    order.append(food)

for f in order:
    if f in menu:
        print(f"{f.title()} narxi {menu[f] } so'm")
    else:
        print(f"Kechirasiz bizda {f.title()} yo'q")
