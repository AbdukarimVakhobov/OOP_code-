

class Avto:
    """Avto nomli class """

    def __init__(self, model, rangi, karobka, narxi, xolat):
        self.model = model
        self.rangi = rangi
        self.karobka = karobka,
        self.narxi = narxi
        self.xolat = xolat
        self.probek = 0

    def get_info(self):
        """Avtomabil haqida malumotlarni text ko'rinishida qaytaradi"""
        text = f"Avtomabil modeli {self.model.upper()}\n"
        text += f"Rangi {self.rangi}\nUzatma mexanizimi: {self.karobka} \nNarxi: {self.narxi}"
        return text
    def avto_dict(self):
        """Avtomabil malumotlarini dict ko'rinishda qaytaradi"""
        avto_dict = {'modeli': self.model, 'rangi': self.rangi, 'narx' : self.narxi, 'xolat': self.xolat, 'probek': self.probek}
        return avto_dict


    def get_model(self):
        """Avtimabil modelini qaytaridi"""
        return self.model
    def get_color(self):
        """Avtimabil rangini qaytaridi"""
        return self.rangi
    def get_karobka(self):
        """Avtimabil karobkasi turini qaytaridi"""
        return self.karobka
    def get_price(self):
        """Avtimabil narxini qaytaridi"""
        return int(self.narxi)
    def get_probek(self):
        """Avtomabil probekini qaytaradi"""
        int(self.probek)
        return self.probek
    
    def update_probek(self, probek):
        """Avtomabil probekini kiritiladi. Kiritilgan son manfiy bo'lishi kerak"""
        if probek > 0 :
            self.probek += int(probek) 
            return self.probek
        else:
            return self.probek

class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avto_soni = 0
        self.avtolar = []
    
    def avtosalon_info(self):
        """Avtosalon malumotlarini text ko'rinishini qaytaradi"""
        text = f"Avtosalon nomi : {self.nomi}  Manzili : {self.manzili}"
    
    def get_avto_son(self):
        """Avtosalondagi avtolaer sonini integer ko'rinishida qaytaradi"""
        return self.avto_soni
    
    def get_avtolar_list(self):
        """Avtolar malumotlari joylashgan listni qaytaradi"""
        return [avto.avto_dict() for avto in self.avtolar]
    
    def add_avto(self, avto):
        """Avtosalonga avto qo'shadi"""
        self.avtolar.append(avto)
        self.avto_soni += 1

    


    
    

avto1 = Avto('malibu', 'oq', 'avtomat', 30000, 'yangi')

avtosalon1 = Avtosalon('GM', 'Toshkent')
print(avtosalon1.get_avto_son(), avtosalon1.get_avtolar_list())
avtosalon1.add_avto(avto1)
print(avtosalon1.get_avto_son(), avtosalon1.get_avtolar_list())


