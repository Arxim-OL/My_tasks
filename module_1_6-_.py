# Задание "Средний балл"

# На вход даны следующие данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list (students) # Создание списка из множества students
students_list.sort() # Сортировка списка students_list
s = 0 # Переменная для цикла
average_score = {} # Создание пустого словаря,  где ключом будет имя ученика, а значением - его средний балл

while s < len(students_list): # Выполнение итераций по количеству студентов
    av_s = round (sum (grades [s]) / len (grades [s]), 2) # определение средней оценки и округление до двух знаков после запятой
    average_score [students_list[s]] = av_s # Заполнение словаря
    s += 1

print (average_score) # Вывод решения в консоль


