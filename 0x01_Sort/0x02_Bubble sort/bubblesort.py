# _*_ code:utf-8 _*_
#!/usr/local/bin/python

scores = []
while 1:
    isQ = input("请输入成绩，输入q结束输入：")
    if isQ == 'q':
        break
    scores.append(int(isQ))

for i in range(len(scores)-1):
    for j in range(len(scores)-1):
        if scores[j]<scores[j+1]:
            scores[j+1],scores[j] = scores[j], scores[j+1]

for idx in range(len(scores)):
    print(scores[idx])
