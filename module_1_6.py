# -*- coding: utf-8 -*-
number_of_completed_HW = 12
number_of_hours_spent = 1.5
course_title = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed_HW
print ('Курс: ',course_title,
       ', всего задач: ', number_of_completed_HW,
       ', затрачено часов: ', number_of_hours_spent,
       ', среднее время выполнения: ', time_for_one_task,
       sep='')