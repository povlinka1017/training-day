from __future__ import annotations

import string


def square_sum(numbers: list) -> int:
    res: list[int] = []
    for num in numbers:
        x = num**2
        res.append(x)
    return sum(res)


def titled(string: str) -> str:
    l: list = []
    for char in string.split(' '):
        l.append(char.capitalize())
    res: str = ' '.join(l)
    return res


def find_short(s: str) -> int:
    return min(len(x) for x in s.split(' '))


def dna(dna: str) -> str:
    compl_dna = list(dna)
    res: list = []
    for char in compl_dna:
        if char == 'A':
            res.append('T')
        elif char == 'T':
            res.append('A')
        elif char == 'C':
            res.append('G')
        elif char == 'G':
            res.append('C')
    return ''.join(res)


def get_sum(a: int, b: int):
    if a > b:
        return sum(range(b, a + 1)) if a != b else a
    else:
        return sum(range(a, b + 1)) if a != b else a


def open_or_senior(data: list):
    output: list = []
    for [age, hc] in data:
        if age >= 55:
            if hc in range(7, 27):
                output.append('Senior')
            else:
                output.append('Open')
        else:
            output.append('Open')
    return output


# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

# print(string.ascii_lowercase)


def is_pangram(sentence: str):
    s: str = (
        sentence.lower()
        .replace(string.whitespace, '')
        .replace('.', '')
        .replace(',', '')
    )
    char_list = list(s)

    for char in list(string.ascii_lowercase):
        if char not in char_list:
            return False
    return True


# print(is_pangram('abcdefghijklm opqrstuvwxyz'))


def find_even_index(arr: list):
    '''
    if len(arr) == 1:
        return 0
    x = 0
    if 2 <= len(arr) < 1000:
        for i in arr:
            left_side = arr[:x]
            right_side = arr[x+1:]
            if sum(left_side) == sum(right_side):
                return i
            x += 1
    return -1
    '''

    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1 :]):
            return i
    return -1


# print(find_even_index([1,100,50,-51,1,1]))


def delete_nth(order: list, max_e: int):
    res: list = []
    count = 0
    for i in order:
        if count <= max_e:
            res.append(i)

    return res


# print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))


def solution(s: str) -> str:
    s_list: list[str] = list(s)
    l: list = []
    for item in s_list:
        if item.isupper():
            l.append(' ')
        l.append(item)

    res: str = ''.join(map(str, l))
    return res


# print(solution("camelCase"))
# print(solution("breakCamelCase"))


def pig_it(text: str) -> str:
    text_array: list[str] = text.split(' ')
    # print(f'Text array - {text_array}')
    out: list = []
    for word in text_array:
        # print(f'Iter of word - {word}')
        if word in string.punctuation:
            out.append(word)
        else:
            out.append(word[1:] + word[0] + 'ay')

    return ' '.join(map(str, out))


print(pig_it('12345 456789 !'))
print(pig_it('Pig latin is cool'))  #
print(pig_it('This is my string'))
