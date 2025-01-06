wheel_roulette = [0,
                  32, 15, 19, 4, 21, 2,
                  25, 17, 34, 6, 27, 13,
                  36, 11, 30, 8, 23, 10,
                  5, 24, 16, 33, 1, 20,
                  14, 31, 9, 22, 18, 29,
                  7, 28, 12, 35, 3, 26]


def neighbors(num):
    num = int(num)
    lst_answer = []
    num_index = wheel_roulette.index(num)
    lst_answer.append(wheel_roulette[num_index - 2])
    lst_answer.append((wheel_roulette[num_index - 1]))
    lst_answer.append(wheel_roulette[num_index])
    lst_answer.append(wheel_roulette[num_index + 1 if num_index < 36 else num_index + 1 - 37])
    lst_answer.append(wheel_roulette[num_index + 2 if num_index < 35 else num_index + 2 - 37])
    return lst_answer
