a = [0]*10
print(a)

book = [0]*10
sum = 0
total = 0
for a[1] in range(1,10):
    for a[2] in range(1,10):
        for a[3] in range(1,10):
            for a[4] in range(1,10):
                for a[5] in range(1,10):
                    for a[6] in range(1,10):
                        for a[7] in range(1,10):
                            for a[8] in range(1,10):
                                for a[9] in range(1,10):
                                    for i in range(1,10):
                                        book[i] = 0
                                    for i in range(1,10):# 如果某数出现过就标记一下
                                        book[a[i]] = 1
                                    # 统计共出现了多少个不同的数
                                    sum = 0
                                    for i in range(1,10):
                                        sum += book[i]
                                    if(sum==9 and\
                                     a[1]*100 + a[2]*10 + a[3] +\
                                     a[4]*100 + a[5]*10 + a[6] ==\
                                     a[7]*100 + a[8]*10 + a[9]):
                                        total+=1
                                        print('%d%d%d+%d%d%d=%d%d%d' % (a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
print('total=%d' % total)