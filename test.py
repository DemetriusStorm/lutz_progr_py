from typing import List, Dict


def solution(dna: str):
    return dna.translate(str.maketrans("GCTA", "CGAU"))


print(solution('UGCACCAGAAUU'))


def solution2(str: str):
    new = ''
    for i in str:
        if i not in new and not i.isdigit():
            new += i
    if len(new) != 26:
        return False
    return True


print(solution2('0123456789abcdefghijklmnop'))

