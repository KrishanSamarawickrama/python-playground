def commaCode(list):
    output = ''
    if len(list) == 1:
        return list[0]
    if len(list) > 1:
        for i in range(len(list)):
            if i < len(list) - 1 and i > 0:
                output += ', '
            elif i == len(list) - 1:
                output += ' and '
            output += list[i]            
    return output

print(commaCode([]))
print(commaCode(['spam']))
print(commaCode(['apples', 'bananas', 'tofu', 'cats']))