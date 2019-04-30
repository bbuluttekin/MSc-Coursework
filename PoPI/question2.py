def common_elements(list1, list2):
    '''implement the function'''
    set_1 = set(list1)
    set_2 = set(list2)
    intersection = set_1.intersection(set_2)
    intersection = sorted(intersection)
    return intersection
