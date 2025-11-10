# My-Python-Learning-Journey
For anyone who are reading this description, you should notice that this is a project repository that use for my python HOMEWORK.
**对于任何正在阅读这条描述的各位，请注意这是一个为作业而创建的Github仓库，接下来的描述都是中文描述**

# 项目介绍
这是一个用来“评定等级”的项目。其实在比赛和各种评级中其实非常常见。简单来说，给定10个分数，这段代码会自动移除最小值和最大值，随后计算剩下值的平均分。根据单独每个值与平均值差值的绝对值，判断评定的等级是A、B还是C，随后放入一个列表，自动计数并打印三个等级出现的次数
只需要调整参数，或者简单的加几句代码，便可以转换为多种评级的模式。

## 原代码展示（.py格式）
```py

org_score=[10,7,8,9,6,7,9,9,8,9]

# 移除最大值和最小值并进行提示
print("已移除最大值"+str(max(org_score)))
print("已移除最小值"+str(min(org_score)))
org_score.remove(max(org_score))
org_score.remove(min(org_score))
score=org_score

# 计算平均分
mean_score=sum(score)/len(score)

# 进行等级评定并输入列表"final_result",然后打印三个等级出现的次数，并打印列表本身
final_result=[]
for i in score:
    if abs(i-mean_score)<1:
        final_result.append("A")
    elif abs(i-mean_score)<1.5:
        final_result.append("B")
    else:
        final_result.append("C")

print("等级A出现了"+str(final_result.count("A"))+"次")
print("等级B出现了"+str(final_result.count("B"))+"次")
print("等级C出现了"+str(final_result.count("C"))+"次")
print(final_result)

```

## 运行说明
直接将代码段内的代码复制进各种支持运行.py文件的编译器即可。可以随意修改以满足各种需要

## 代码说明
org_score是只能存储数字（无论什么类型，int，float什么都可以）的列表。存储数量不限。这是输入数据的地方。
对于以下代码：

```py

print("已移除最大值"+str(max(org_score)))
print("已移除最小值"+str(min(org_score)))
org_score.remove(max(org_score))
org_score.remove(min(org_score))
score=org_score

```
其实就是先输出最大值和最小值，然后利用list的.remove方法删除最大值和最小值，再创建清理后的列表score，以作区分。
最后在输出时，首先创建了一个空列表final_result。再使用for循环，根据以下条件进行ABC三个等级的判定：

1. 如果值与平均值之差的绝对值小于1，评定为等级A
2. 如果值与平均值之差的绝对值大于等于1小于1.5，评定为等级B
3. 如果值与平均值之差的绝对值大于等于1.5，评定为等级C

*其实这个判断条件随便改都行*
在判断出结果后，利用列表的.append方法直接添加到score列表末尾
最后简单利用print函数输出，就都结束了！

# 学习心得与规划
