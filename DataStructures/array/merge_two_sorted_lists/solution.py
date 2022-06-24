
def merge_lists(lst1, lst2):
    i = 0
    j = 0

    while (i < len(lst1)) and (j < len(lst2)):
        if lst1[i] > lst2[j]:
            lst1.insert(i, lst2[j])
            i += 1
            j += 1
        else:
            i += 1

    if j < len(lst2):
        lst1.extend(lst2[j:])
    
    return lst1

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9, 10]
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]
result = merge_lists(lst1, lst2)
print(result)