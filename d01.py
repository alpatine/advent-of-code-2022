def get_group_sums(inputFile: str) -> list[int]:
    with open(inputFile) as file:
        lines = file.read().splitlines()
        sums = []
        group_sum = 0
        for line in lines:
            if line != '':
                group_sum += int(line)
            else:
                sums.append(group_sum)
                group_sum = 0
        sums.append(group_sum)
        return sums


if __name__ == '__main__':
    group_sums = get_group_sums('d01-input.txt')
    group_sums.sort(reverse=True)
    print(group_sums[0])
    print(sum(group_sums[0:3]))
    