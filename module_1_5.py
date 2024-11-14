immutable_var = (1, 2, 'a', 'b')
# immutable_var [0] = 3 - TypeError: 'tuple' object does not support item assignment
print(immutable_var)


mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified') # Изменение элементов списка mutable_list
mutable_list.remove('Modified')
mutable_list.extend(['Modified'])
print(mutable_list)
