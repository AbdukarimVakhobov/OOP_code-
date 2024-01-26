"""---------------------BIRINCHI TOPSHIRIQ-----------------------"""
# buxoriy = {
#     "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#     "tyil": 810,
#     "vyil": 870,
#     "tjoy": "Buxoro",
# }

# qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

# vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

# navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

# buxoriy['asarlari'] = ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
# qodiriy['asarlari'] = ["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
# vohidov['asarlari'] = ["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
# navoiy['asarlari'] = ["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']


# persons = [buxoriy, qodiriy, vohidov, navoiy]

# for person in persons:
#     print(f"{person['ism']} {person['tyil']}-yilda {person['tjoy']}da tug'ulgan",
#           f"{person['vyil']}-yilda {person['vyil']-person['tyil']} yoshida vafot etgan")
    
# for person_a in persons:
#     print(f"\n{person_a['ism']}ning mashxur asarlari: ")
#     for asar in person_a['asarlari']:
#         print(asar)

"""------------- IKKINCHI TOPSHIRIQ--------------"""


# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
# for person in kinolar:
#     print(f"\n{person.title()}ning yoqtirgan kinolari:")
#     for kino in kinolar[person]:
#         print(kino)



"""---------------UCHUNCHI TOPSHIRIQ--------------"""

# cauntries = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
# }       

# for state, information in cauntries.items():
#     print(f"\n{state.title()}ning poytaxti {information['poytaxt']}",
#           f"\nMaydoni-     {information['maydon']} metr kv",
#           f"\nAholisi-     {information['aholi']}",
#           f"\nPul birligi- {information['pul birligi']}")




"""---------------TO'RTINCHI TOPSHIRIQ--------------"""

cauntries = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
}       

state = input("Davlat nomini kiriting ")
state.lower()

if state in cauntries:
    information = cauntries[state]
    
    print(f"\n{state.title()}ning poytaxti {information['poytaxt']}",
          f"\nMaydoni-     {information['maydon']} metr kv",
          f"\nAholisi-     {information['aholi']}",
          f"\nPul birligi- {information['pul birligi']}")
else:
    print("Bizda bu davlat haqida malumot mavjud emas")
    
    
