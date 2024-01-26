ismlar = ['ali', 'vali', 'hasan', 'husan']

def katta_harf(list):
    copy_list = list[:]
    """list turidagi ro'yxatni elementlarini har birini katta harfga o'girib beradi"""
    
    new_list = []
    while copy_list:
        new_list.append(copy_list.pop().title())
        new_list.reverse()
    return new_list
print(katta_harf(ismlar))
print(ismlar)


def katta_harf2(list):
    new_list = []
    for n in range(len(list)):
        new_list.append(list[n].title())
    return new_list
print(katta_harf(ismlar))
print(ismlar)
