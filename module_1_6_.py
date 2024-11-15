#  Работа со словарями
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print ('Dict: ', my_dict) # Вывод на экран содержимое словаря my_dict
print ('Existing value: ', my_dict['Masha']) # Вывод на экран одно значение по существующему ключу словаря my_dict
print ('Not existing value: ', my_dict.get('Dima')) # Вывод на экран по отсутствующему из ключу словаря my_dict
my_dict.update({ 'Kamila': 1981, 'Artem': 1915}) # Добавление двух произвольных пар того же формата в словарь my_dict
del my_dict ['Egor'] # Удаление одной из пар по существующему ключу из словаря my_dict
print ('Modified dictionary: ', my_dict) # Вывод на экран словаря my_dict
print ()

# Работа с множествами
my_set = {1, 'Яблоко', 42.314, 'Яблоко', 'Яблоко', 1, 1, 1}
print ('Set: ', my_set) # Вывод на экран множество my_set
my_set.add (42.314) # Добавление 2 произвольных элемента в множество my_set, которых ещё нет
my_set.add ((5, 6, 1.6))
my_set.discard (1) # Удаление одного любого элемента из множества my_set
print ('Modified set: ', my_set) # Вывод на экран измененного множества my_set