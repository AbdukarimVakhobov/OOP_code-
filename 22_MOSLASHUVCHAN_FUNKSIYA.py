
# def kopaytiruvchi(*son):
#     """sonlarni ko'paytmasini qaytaruvchi funksiya"""
#     if son:
#         kopaytma = 1 
#         for n in son:
#             kopaytma *= n
#     else:
#         kopaytma = None
#     return kopaytma

# print(kopaytiruvchi(1,9,5,7,4))
        
def malumot(name, surname, **qoshimcha):
    talaba_malumot = {}
    talaba_malumot['name'] =name
    talaba_malumot['surname'] =name
    
    for keys, value in qoshimcha.items():
        talaba_malumot[keys] = value
    return talaba_malumot
print(malumot("Karimjon", "Vakhobov", kurs = 4 ))

# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs

# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')
# print(talaba)