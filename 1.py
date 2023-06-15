stih = 'пара-па-рам рам-пам-папам па-ра-па-да'

stih = stih.split()

glasnye = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']

def counter(stih):
    new = []
    for i in stih:
        count = 0
        for j in i:
            if j in glasnye:
                count += 1
        new.append(count)
    return new

new = counter(stih)

if all(new):
    print('Парам пам-пам')
else:
    print('Пам парам')

