# funksiya- OOp larsiz
# Bank dasturining birinchi versiyasi (chiziqli dastur)
# yagona accaunt


accaunt_name = 'Abdukarim'
accaunt_balans = 5000
accaunt_password = 'qwert'

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
        print("Balansni ko'rish")
        user_password = input("Parolingizni kiriting ")
        if user_password != accaunt_password:
            print("Parol XATO! ")
        else:
            print("Sizning balansingiz ", accaunt_balans)
    
    elif action == 'd': # Depozit
        print("Depozit : ")
        user_depozit_amount = input("Depozit miqdorini kiriting ")
        user_depozit_amount = int(user_depozit_amount) #Depozitni int qiymatga o'tkazib olish uchun kerak
        user_password = input("Parolingizni kiriting ")

        if user_depozit_amount < 0:
            print(" depozit manfiy bo'lishi mumkin emas")
        elif user_password != accaunt_password:
            print("Xato PAROL")
        else:
            accaunt_balans = accaunt_balans + user_depozit_amount
            print("Sizning hozzirgi balansingiz: ", accaunt_balans)
    elif action == 'w': # yechib olish
        print("Pul yechish")
        user_withdraw_amount = input("Yechib olmoqchi bo'lgan pul miqdorini kiriting")
        user_withdraw_amount =  int(user_withdraw_amount)
        user_password = input("Parolingizni kiriting")

        if user_withdraw_amount < 0:
            print("Yechib olmoqchi bo'lgan pul miqdorini manfiy kiritmang")
        elif user_password != accaunt_password:
            print("Parol XATO! ")
        elif user_withdraw_amount > accaunt_balans:
            print("Mablag' yetarli emas, kiritishungiz mumkin bo'lgan maximal miqdor :" , accaunt_balans)
        else:
            accaunt_balans = accaunt_balans - user_depozit_amount
            print("PUL MUOFIQQIYATLI YECHILDI")
            print("Sizning hozzirgi balansingiz: ", accaunt_balans)
    elif action == 's':
        print("Accaunt malumotlari")
        print("             Foydalanuvchi: ", accaunt_name)
        print("             Balans :       ", accaunt_balans)
        passwor_f= ''
        for n in accaunt_password: # Parolni yashirish uchun
            passwor_f += '*'
        print("              Parol :        ", passwor_f)
    elif action == 'q':
        break
        
            


