# _*_ code:utf-8 _*_
#!/usr/local/bin/python

scores = []
while 1:
    score = input("请输入成绩，输入q结束输入：")
    if score == 'q':
        break
    scores.append(int(score))

def quicksort(left, right):
    if left>right:
        return
    temp = scores[left]
    i, j = left, right
    while i!=j:
        while scores[j]>=temp and i<j:
            j-=1
        while scores[i]<=temp and i<j:
            i+=1
        
        if i<j:
            scores[i], scores[j] = scores[j], scores[i]
    
    scores[left] = scores[i]
    scores[i] = temp
    print(scores)
    quicksort(left,i-1)
    quicksort(i+1,right)

quicksort(0, len(scores)-1)
print(scores)
