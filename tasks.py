def move_zeros(lst: list):
    """
    Write an algorithm that:
    - takes an array
    - moves all of the zeros to the end, preserving the order of the other elements.
    :param lst:
    :return: list
    """
    non_zero: list = [i for i in lst if i != 0]
    nulls: list = [i for i in lst if i == 0]
    return non_zero + nulls

#print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def expanded_form(num: int):
    num_list = [int(i) for i in str(num)]
    lst = []

    for index, digit in enumerate(num_list):
        print(index, digit)
        if digit != 0:
            place_value = digit * 10 ** (len(num_list) - index - 1)
            lst.append(str(place_value))
    return ' + '.join(map(str, lst))

print(expanded_form(10020062))
