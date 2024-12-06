# trying to answer without llm's.
# gosh, sucks to be in this timeline.
# made by arthur lorencini bergamaschi


def convert_line(line):
    "12345 67890\n"
    lines = line.replace("\n", "").split("   ")
    # ["12345","67890"]
    numbers = [int(number) for number in lines]
    # numbers = [12345, 67890]
    return numbers


def calculate_distance(l1, l2):
    distance = 0
    for i, j in zip(l1, l2):
        print(i, j)
        aux = abs(i - j)
        distance += aux

    print("A distância total entre l1 e l2 é:", distance)
    return distance


def calculate_similarity(l1, l2):
    similarity = 0
    for i in l1:
        indv_sim = 0
        for idx in range(len(l2)):
            if i == l2[idx]:
                indv_sim += 1
        similarity += indv_sim * i
    print("o valor final da similaridade é:", similarity)
    return similarity


def main():
    sum = 0
    # a maracutaia é que cada coluna é uma lista, e não cada linha.
    # essa era a minha confusão.
    elfs_lists = [[], []]
    # essa lista vai ser 10 listas contendo cada coluna.

    print("utilizando o arquivo")
    path = "day_01_input.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    lines = [convert_line(line) for line in lines]
    # lines = [
    # [12345, 67890],
    # [23456, 67877],
    # ...
    # ]
    for line in lines:
        for idx, number in enumerate(line):
            elfs_lists[idx].append(number)
    for l in elfs_lists:
        l.sort()
    calculate_distance(elfs_lists[0], elfs_lists[1])
    calculate_similarity(elfs_lists[0], elfs_lists[1])

    print("O valor final da soma é:", sum)


if __name__ == "__main__":
    main()
    print("end")
