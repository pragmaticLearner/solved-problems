def grid_index(grids, indexes):
    flat_list = []
    for grid in grids:
        for item in grid:
            flat_list.append(item)

    my_str = ''.join(flat_list)

    l = []
    for i in indexes:
        l.append(my_str[i - 1])
    return ''.join(l)


print(grid_index([['m', 'y', 'e'],
                  ['x', 'a', 'm'],
                  ['p', 'l', 'e']],
                 [5, 6, 9]))


