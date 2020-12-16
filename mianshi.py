import re

a = "not 404 50.56 found 张三 99 深圳"
list = a.split(" ")
res = re.findall('\d+\.?\d*|[a-zA-Z]+]', a)
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res)
print(new_str)
