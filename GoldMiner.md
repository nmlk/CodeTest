# 动态规划--金矿模型

有一个国家，所有的国民都非常老实憨厚，某天他们在自己的国家发现了十座金矿，并且这十座金矿在地图上排成一条直线，国王知道这个消息后非常高兴，他希望能够把这些金子都挖出来造福国民，首先他把这些金矿按照在地图上的位置从西至东进行编号，依次为0、1、2、3、4、5、6、7、8、9，然后他命令他的手下去对每一座金矿进行勘测，以便知道挖取每一座金矿需要多少人力以及每座金矿能够挖出多少金子，然后动员国民都来挖金子。

链接：https://www.jianshu.com/p/0b5ba87ac486

链接：http://www.cnblogs.com/sdjl/articles/1274312.html

```python
people = [77,22,29,50,99]
gold   = [92,22,87,46,90]

m = 100
n = 5

fn = [[0 for i in xrange(n+1)] for j in xrange(m)]

for g in range(n):
    for p in range(m):
        if p < people[g]:
            fn[p][g+1]= fn[p][g]
        else:
            fn[p][g+1]= max(fn[p][g],gold[g]+fn[p-people[g]][g])

print fn[m-1][n]
```
$python main.py
133
