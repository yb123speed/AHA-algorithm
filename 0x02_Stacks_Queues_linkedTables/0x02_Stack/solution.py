# _*_ code:utf-8 _*_
#!/usr/local/bin/python

txt = input('请输入字符串：')
# method 1
print(txt == txt[::-1])

# method 2
for i in range(int(len(txt)/2)):
    if txt[i] != txt[-1-i]:
        print(False) 
print(True)

# method 3
txt1 = ""
for i in txt:
    txt1 = i + txt1
print(txt1 == txt)