list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# sublist
list2 = ['h', 'i', 'j']
list1[2][1][2].extend(list2)
print(list1)
