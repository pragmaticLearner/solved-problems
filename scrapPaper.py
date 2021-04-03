def parts_sums(ls):
    t = sum(ls)
    new_ls = [t]

    if not ls:
        return new_ls
    else:
        return new_ls + parts_sums(ls[1:])


print(parts_sums([0, 1, 3, 6, 10]))


def _sum_of_parts(ls):

    new_ls = []
    t = 0

    while ls:
        t = sum(ls)
        new_ls.append(t)
        ls.remove(ls[0])
    return new_ls + [0]

print(_sum_of_parts([0, 1, 3, 6, 10]))
