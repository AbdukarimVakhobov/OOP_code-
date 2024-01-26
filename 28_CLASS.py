
class User:
    """Web sahifa uchun user"""
    def __init__(self, user_name, name, surname, password, tel_num, email):
        self.name = name
        self.surname = surname
        self.tel_num = tel_num
        self.email = email
        self.user_name = user_name
        self.password = password

    def info_user(self, year = 2024):
        """User foydalanuvchini malumotlarini qaytaruvchi funksiya"""
        text = f"{self.user_name} foydalanuvchi {self.name.title()} {self.surname.title()}\n"
        
        text += f"telefon raqami {self.tel_num} \n"
        
        password = ''
        for n in self.password:
            password += '*'
            
        text += f" parol: {password}"
        return text
    
    def info_email(self):
        password = input("email ni ko'rish uchun parolizni kiriting")
        n = 0
        if password != self.password:
            while n < 2:
            
                password2 = input("Parol xato! Qayta kiritng.  chiqish uchun (exit)")
                if password2.lower() == 'exit':
                    break
                else:
                    n += 1
            email = None            
        if password == self.password:
            email = self.email
        return email
    
    
    def get_name(self):
        """gehrjhrs"""
        return self.name.title()


user1 = User('mr_karimjon', 'karimjon', 'vakhobov', 'salomlar11', +998933573433, 'vakhobovkarimjon@gmail.com',)

print(user1.info_user())  
print(user1.info_email())  




