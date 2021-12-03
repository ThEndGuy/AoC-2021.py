#!/usr/bin/env python
DATA2 = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]
def cal_common(col: list, ep: str ='', gam: str ='') -> tuple:
    if col.count('1') >= col.count('0'):
        ep += '0'
        gam += '1'
    else:
        ep += '1'
        gam += '0'
    return ep, gam

def parse_file(filename: str) -> list:
    with open(filename, "r") as f:
        return [word.strip("\n") for word in f.readlines()]

def calc_ep_gam(numlist: list) -> tuple:
    ep = ''
    gam = ''
    dig_dict = {i : [] for i in range(len(numlist[0]))}
    for num in numlist:
        for i, digit in enumerate(num):
            dig_dict[i].append(digit)
    val_list = list(dig_dict.values())
    for col in val_list:
       ep, gam = cal_common(col, ep, gam)
    return ep, gam

data = parse_file("input.txt")
ep, gam = calc_ep_gam(data)
print(ep, gam)
# UNCOMMENT FOR RESULT
# print(int(ep, 2), int(gam, 2))

# PART 2



def cal_lsr(numlist: list):
    less_com, most_com = calc_ep_gam(numlist)
    numl1, numl2 = numlist.copy(), numlist.copy()
    print(most_com)
    print(numl1)
    for i in range(len(most_com)):
        col = [num[i] for num in numl1]
        _, gam = cal_common(col)
        for j, number in enumerate(numl1):
            if number[i] != gam:
                numl1[j] = False
        numl1 = [num for num in numl1 if num is not False]
        print(numl1)
        if len(numl1) == 1:
            o2r = numl1[0]
            break

    for i in range(len(less_com)):
        col = [num[i] for num in numl2]
        ep, _ = cal_common(col)
        for j, number in enumerate(numl2):
            if number[i] != ep:
                numl2[j] = False
        numl2 = [num for num in numl2 if num is not False]
        if len(numl2) == 1:
            co2r = numl2[0]
            break
    return o2r, co2r

o2r, co2r = cal_lsr(data)
print(int(o2r, 2), int(co2r, 2))
