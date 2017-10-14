def snail(array):
    if array == [[]]:
        return []
    i_range = [i for i in range(len(array))]
    j_range = [i for i in range(len(array))]
    component_list = []
    i = j = 0
    while i_range and j_range:
        for j in j_range:
            component_list.append(array[i][j])
        i_range.pop(0)
        for i in i_range:
           component_list.append(array[i][j])
        j_range.pop()
        i_range.reverse()
        j_range.reverse()        
    return component_list
