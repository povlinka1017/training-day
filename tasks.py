import datetime


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

# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def make_readable(seconds: int):
    """
    Write a function, which takes a non-negative integer (seconds) as input
    and returns the time in a human-readable format (HH:MM:SS)
    :param seconds:
    :return: time in a human-readable format (HH:MM:SS)
    """

#    return datetime.time(hour=seconds/3600, minute=(seconds/60), second=)
    pass

# print(make_readable(3600))

x = 86400

t = int(x)

day = t//86400
hour = (t-(day*86400))//3600
min = (t - ((day*86400) + (hour*3600)))//60
seconds = t - ((day*86400) + (hour*3600) + (min*60))

hello= datetime.time(hour=hour, minute=min, second=seconds)
print(hello)
