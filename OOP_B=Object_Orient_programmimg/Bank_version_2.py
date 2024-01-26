# OOP siz funksiyalar bilan
# yagona account bilan

accaunt_name = ''
accaunt_balanse = 0
accaunt_password = ''

def new_accaunt(name, balanse, password):
    """Yangi account yaratuvchi funksiya"""
    global accaunt_name, accaunt_balanse, accaunt_password
    accaunt_name = name
    accaunt_balanse = balanse
    accaunt_password = password

def show_accaunt():
    """accaunt malumotlarini qaytaradi"""
    global accaunt_name, accaunt_balanse, accaunt_password
    if accaunt_name == '':
        print("Accaunt mavjud emas")
    else:
        print("Accaunt malumotlari")
        print("             Foydalanuvchi: ", accaunt_name)
        print("             Balans :       ", accaunt_balanse)
        passwor_f= ''
        for n in accaunt_password: # Parolni yashirish uchun
            passwor_f += '*'
        print("              Parol :        ", passwor_f)

def get_balanse(password):
    """accaunt balansini qaytaradi"""
    global accaunt_name, accaunt_balanse, accaunt_password
    if password != accaunt_password:
        print("Parol XATO ! ")
        return None
    return accaunt_balanse

def depozit(user_depozit_amount, user_password):
    """accaunt balansiga depozit qo'shadi"""
    global accaunt_name, accaunt_balanse, accaunt_password
    if user_depozit_amount < 0:
        print(" depozit manfiy bo'lishi mumkin emas")
        return None
    if user_password != accaunt_password:
        print("Xato PAROL")
        return None
    
    accaunt_balanse = accaunt_balanse + user_depozit_amount
    print("Sizning hozzirgi balansingiz: ", accaunt_balanse)

def withdraw(user_withdraw_amount, user_password):
    """accauntdan pul yechadi"""
    global accaunt_name, accaunt_balanse, accaunt_password
    if user_withdraw_amount < 0:
        print("Yechib olmoqchi bo'lgan pul miqdorini manfiy kiritmang")
        return None
    if user_password != accaunt_password:
        print("Parol XATO! ")
        return None
    if user_withdraw_amount > accaunt_balanse:
        print("Mablag' yetarli emas, kiritishungiz mumkin bo'lgan maximal miqdor :" , accaunt_balans)
        return None
    accaunt_balanse = accaunt_balanse - user_withdraw_amount
    return accaunt_balanse


    
new_accaunt('abdukarim', 2000, 'qwert')


while True:
    print()
    print("Balansingizni ko'rish uchun  b  ni bosing")
    print("depozit qo'yish uchun  d  ni bosing")
    print("Yechib olish uchun  w  ni bosing ")
    print("Xisobni ko'rsatish uchun s  ni bosing")
    print("chiqish uchun  q ni bosing")
    print()

    action = input("Nima qilmoqchisiz ")
    action = action.lower()  # javobni kichik harfga o'zgartirish uchun
    action = action[0] # kiritilgan javobni birinchi harfni olish uchun
    print()

    if action == 'b':
        print("Get Balanse")
        user_password = input("Parolingizni kiiting ")
        the_balanse = get_balanse(user_password)
        if the_balanse != None:
            print("sizning balansingiz : ", the_balanse)
    
    elif action == 'd':
        print("Depozit")
        depozit_N = input("Qo'ymoqchi bo'lgan depozit miqdorini kiriting: ")
        depozit_N = int(depozit_N)
        password = input("Parolingizni kiriting")

        new_balanse = depozit(depozit_N, password)
        if new_balanse is not None:
            print("Sizning hozzirgi balansingiz : ", new_balanse)
    
    elif action == 'w':
        print("pul yechish")
        withdraw_n = input("Yechib olmoqchi bo'lgan mablag'ni kiriting: ")
        withdraw_n = int(withdraw_n)
        password = input("Parolingizni kiriting")
        
        new_balanse = withdraw(withdraw, password)

        if new_balanse is not None:
            print("Pul muofiqiyatli yechildi. Sizning hozzirgi balansingiz : ", new_balanse)
        
    elif action == 's':
        show_accaunt()
    
    elif action == 'q':
        break
print("Dastur tugatildi")


