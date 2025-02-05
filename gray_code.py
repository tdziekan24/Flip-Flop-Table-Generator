def create_list(n):
    new_list = ['']
    for _ in range(n):
        new_list = [*new_list, *reversed(new_list)]
        for index, _ in enumerate(new_list):
            if index >= len(new_list) // 2:
                new_list[index] = "1" + new_list[index]
            else:
                new_list[index] = "0" + new_list[index]

    return new_list
