def recall_password(grille:tuple, password:tuple):
    #找出X的初始位置
    x_list = []
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 'X':
                x_list.append([i,j])

    #根据x_list中的下标从密码表中取值
    result = ""
    k = 0
    while k < 4:
        for x in sorted(x_list):
            result += password[x[0]][x[1]]

        #X位置顺时针旋转90度
        for m in x_list:
            tmp1 = m[0]
            m[0] = m[1]
            m[1] = 3 - tmp1

        k += 1

    return result

print(recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi'))) #'icantforgetiddqd'
print(recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr'))) #'rxqrwsfzxqxzhczy'