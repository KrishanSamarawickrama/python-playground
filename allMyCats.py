catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames))
          + ' (or enter nothin to quit):')
    name = input()
    if name == '':
        break
    if name not in catNames:
        catNames = catNames + [name]
    else:
        print('Name already exist.')
print('The cat names are:')
for name in catNames:
    print(' ' + name)
