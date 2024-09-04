def filter_by_state(list_dict, state):
    list_sort = []
    for i in list_dict:
        if i['state'] == state:
            list_sort.append(i)
    return list_sort


def sort_by_date():
    pass
