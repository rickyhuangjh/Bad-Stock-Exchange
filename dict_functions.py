def insertSortedList(sorted_list, x):
    for i in range(len(sorted_list)):
        if x < sorted_list[i]:
            sorted_list.insert(i, x)
            return sorted_list
    sorted_list.append(x)
    return sorted_list

def removeEmptyFirst(sorted_dict):
    if dictFirstKey(sorted_dict) <= 0:
        print(dictFirstKey(sorted_dict))
        sorted_dict.pop(dictFirstKey(sorted_dict))
    return sorted_dict

def removeEmptyLast(sorted_dict):
    if dictLastKey(sorted_dict) <= 0:
        sorted_dict.pop(-1)
    return sorted_dict

def insertSortedDict(sorted_dict, updateKey, value=1):
    if updateKey in sorted_dict.keys():
        sorted_dict[updateKey] += value
        return sorted_dict
    else:
        pairList = []
        for pair in sorted_dict.items():
            pairList.append(pair)
        insertAt = 0
        for key in sorted_dict.keys():
            if updateKey < key:
                break
            insertAt += 1
            if insertAt == len(sorted_dict) +1:
                break
        temp_dict = {}
        keyIndex = 0
        while keyIndex < insertAt:
            temp_dict.update({pairList[keyIndex][0]: pairList[keyIndex][1]})
            keyIndex += 1
        temp_dict.update({updateKey: value})
        temp_dict.update(sorted_dict)
        return temp_dict

def dictFirstKey(dict):
    key_list = []
    for x in dict.keys():
        key_list.append(x)
        break
    if key_list == []:
        return None
    return key_list[0]

def dictLastKey(dict):
    key_list = []
    for x in dict.keys():
        key_list.append(x)
    if key_list == []:
        return None
    return key_list[-1]

def returnUpdatedDict(dict, key, new_value):
    return dict.update({key, new_value}).copy()