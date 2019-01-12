# _*_ code:utf-8 _*_
#!/usr/local/bin/python

buckets = [0 for i in range(11)]
print (buckets)

for i in range(5):
    score = int(input("请输入成绩:"))
    buckets[score] +=1

for i in range(10,-1,-1):
    if buckets[i]>0:
        for j in range(buckets[i]):
            print(i)
        
