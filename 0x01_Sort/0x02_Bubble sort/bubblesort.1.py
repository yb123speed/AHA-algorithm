# _*_ code:utf-8 _*_
#!/usr/local/bin/python

scores = []
while 1:
    score = input("请输入成绩，输入q结束输入：")
    if score == 'q':
        break
    name = input("请输入名字：")
    scores.append((name, int(score)))

for i in range(len(scores)-1):
    for j in range(len(scores)-1):
        if scores[j][1]<scores[j+1][1]:
            scores[j+1],scores[j] = scores[j], scores[j+1]

for idx in range(len(scores)):
    print(scores[idx])
