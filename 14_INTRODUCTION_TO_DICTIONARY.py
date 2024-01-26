# print("BIRINCHI TOPSHIRIQ")
# my_father = {'name': 'Mardon', 'surname': 'Abdullayev', 'ege': 57}
# my_mather = {'name': 'Gavhar', 'surname': 'Abdullayeva', 'ege': 52}

# print(f"Otam {my_father['name']} {my_father['surname']} {2023-my_father['ege']}-yilda tug'ulgan")

# print(f"Otam {my_mather['name']} {my_mather['surname']} {2023-my_mather['ege']}-yilda tug'ulgan")

# print("IKKINCHI TOPSHIRIQ")

# foods = { 'my_mather': 'mastava', 'my_father': 'polov', 'my_brother': 'somsa', 'my_sister': 'shirinlik', }

# for people, food in foods.items():
#     print(f"{people.title()}s like {food}    ")

 # print("UCHUNCHI  TOPSHIRIQ")

# annotated_dictionary = {'integer': ' butun sonlar turidagi ozgaruvchi', 'float': 'onli sonlar turidagi ozgaruvchi',
#                         'string': "text ko'rinishidagi ozgaruvchi", 'if': 'shart operatori (agar)', 
#                         'else': 'shart operatori(aks xolda)'
#                         }


# operator = str(input('pythondagi kaltit sozlarni kirirting  '))

# print(f" {operator} - {annotated_dictionary.get(operator, "biz yaratgan lug'atda siz kiritgan kalit so'z yo'q")}")


print("To'rtinchi  TOPSHIRIQ")

annotated_dictionary = {'integer': ' butun sonlar turidagi ozgaruvchi', 'float': 'onli sonlar turidagi ozgaruvchi',
                        'string': "text ko'rinishidagi ozgaruvchi", 'if': 'shart operatori (agar)', 
                        'else': 'shart operatori(aks xolda)'
                        }


operator = str(input('pythondagi kaltit sozlarni kirirting  '))

if operator.lower() in annotated_dictionary:
    print(f"{operator}- {annotated_dictionary[operator]}")
else:
    print("bunday so'z lug'atimizda yo'q")
    