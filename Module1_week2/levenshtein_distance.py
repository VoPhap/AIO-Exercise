
def levenshtein_distance(source, target):
    distance = []
    for idx in range(len(source)+1):
        row = [0] * (len(target)+1)
        distance.append(row)

    for idx in range(len(source)+1):
        distance[idx][0] = idx
    for idx in range(len(target)+1):
        distance[0][idx] = idx

    del_cost = 0
    ins_cost = 0
    sub_cost = 0

    for idx in range(1, len(source)+1):
        for jdx in range(1, len(target)+1):
            if source[idx-1] == target[jdx-1]:
                distance[idx][jdx] = distance[idx-1][jdx-1]
            else:
                del_cost = distance[idx-1][jdx] + 1
                ins_cost = distance[idx][jdx-1] + 1
                sub_cost = distance[idx-1][jdx-1] + 1
                distance[idx][jdx] = min(del_cost, ins_cost, sub_cost)

    result = distance[-1][-1]
    print(distance)
    return print(result)


s = 'hola'
t = 'hello'
levenshtein_distance(s, t)
