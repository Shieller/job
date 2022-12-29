a = [['0']*5, ['0']*5, ['0']*5, ['0']*5 ]

for i in range(4):
    print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])

for g in range(6):
    print('ХОДИТ ИГРОК *') 
    x = int(input('Введите х'))
    y = int(input('Введите y'))
    a[x][y] = '*'
    for i in range(4):
        print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])
    print('ХОДИТ ИГРОК $')
    x = int(input('Введите х'))
    y = int(input('Введите y'))
    a[x][y] = '$'
    for i in range(4):
        print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])
    print('ХОДИТ ИГРОК #')
    x = int(input('Введите х'))
    y = int(input('Введите y'))
    a[x][y] = '#'
    for i in range(4):
        print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])
        
print('ХОДИТ ИГРОК *')
x = int(input('Введите х'))
y = int(input('Введите y'))
a[x][y] = '*'
for i in range(4):
    print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])
print('ХОДИТ ИГРОК $')
x = int(input('Введите х'))
y = int(input('Введите y'))
a[x][y] = '$'
for i in range(4):
    print(a[i][0]+a[i][1]+a[i][2]+a[i][3]+a[i][4])


    
score = {'*': 0, '%': 0,}
for i in range(4):
    for g in range(3):
        if a[i][g] == a[i][g+1] and a[i][g] != '0':
            score[a[i][g]]+=1
        if a[i][g] == a[i+1][g] and a[i][g] != '0':
            score[a[i][g]]+=1
        if a[i][g] == a[i+1][g+1] and a[i][g] != '0':
            score[a[i][g]]+=1
        if a[i][g] == a[i+1][g-1] and g != 0 and a[i][g] != '0':
            score[a[i][g]]+=1
print(score)
print(max(score))