#2
my_list = ['apple', 'coconut', 'mango', 'banana', 'dragonfruit']
print("Список: " + str(my_list))
print("Первый и последний элементы списка: " + my_list[0] + ", " + my_list[-1])
print("Третий-пятый элементы списка: " + str(my_list[2:]))
my_list[2] = 'абрикос'
print("Измененный список: " + str(my_list))

#3
my_dict = {
    'I': 'Я',
    'You': 'Ты',
    'We': 'Мы',
    'He': 'Он',
    'She': 'Она',
    'His': 'Его',
    'Her': 'Её',
}
print()
print("Словарь: " + str(my_dict))
print("Значение для ключа I: " + str(my_dict['I']))
my_dict['I'] = 'ЯЯяя'
print("Измененный словарь: " + str(my_dict))