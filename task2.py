def input_nums(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicates(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = input_nums(3)

if check_predicate(statement) == True:
    print(f"Утверждение верно")
else:
    print(f"Утверждение ложно")
#end
