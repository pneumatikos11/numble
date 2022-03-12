'''

Pseudocode

You would guess a number based on some clues


'''


from random import randint
right_answer = randint(100, 999)
print(right_answer)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
answer_list = []
x = right_answer

while x > 0:
    answer_list.append(x % 10)
    x //= 10
answer_list.reverse()
wrong_list = [i for i in number_list if i not in answer_list]


def one_correct_well_placed():
    clue_list = [1, 2, 3]
    right_number = randint(0, 2)
    for i in range(3):
        if i == right_number:
            clue_list[i] = answer_list[right_number]
        else:
            clue_list[i] = wrong_list[randint(0, 6)]
    print("One number is correct and well placed \n" + f"{clue_list[0]}{clue_list[1]}{clue_list[2]}")


def none_is_correct():
    clue_list = [wrong_list[randint(0, 6)] for i in range(3)]
    print("Nothing is correct \n" + f"{clue_list[0]}{clue_list[1]}{clue_list[2]}")


def one_number_correct_wrong_place():
    clue_list = [1, 2, 3]
    right_number = randint(0, 2)
    x = randint(0, 2)
    if x == right_number:
        x = randint(0, 2)
    random_index = x
    for i in range(3):
        if i == right_number:
            clue_list[i] = answer_list[right_number]
        else:
            clue_list[i] = wrong_list[randint(0, 6)]
    print("One number is correct and well placed \n" + f"{clue_list[0]}{clue_list[1]}{clue_list[2]}")


one_correct_well_placed()
none_is_correct()
