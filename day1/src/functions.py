def solution(data):
    highest_total = 0
    total = 0
    total_list = []
    for index, value in enumerate(data):
        if value == "" or index == len(data) - 1:
            total_list.append(total)
            total = 0
        else:
            total += int(value)
            if total > highest_total:
                highest_total = total
    highest_total_3 = sum(sorted(total_list, reverse=True)[:3])
    return highest_total, highest_total_3