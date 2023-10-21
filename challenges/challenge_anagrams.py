def sort_string(string):
    if len(string) < 2:
        return string
    low, same, high = [], [], []

    pivot = string[len(string) // 2]
    for item in string:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            same.append(item)
    return ''.join(sort_string(low)) + ''.join(
        same
        ) + ''.join(sort_string(high))


def is_anagram(first_string, second_string):
    first_string = sort_string(first_string.lower())
    second_string = sort_string(second_string.lower())
    if not first_string or not second_string:
        resposta = (first_string, second_string, False)
        return resposta
    if first_string == second_string:
        resposta = (first_string, second_string, True)
        return resposta
    return (first_string, second_string, False)
