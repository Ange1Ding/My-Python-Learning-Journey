# My-Python-Learning-Journey
For anyone who are reading this description, you should notice that this is a project repository that use for my python HOMEWORK. All the descriptions below will be written in **SIMPLIFIED CHINESE**.

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
## 管理个人项目
一个复杂的项目（比如上千段代码的项目）基本上离不开一个大“仓库”。

这个仓库里拥有众多的“类别”，将不同的代码分门别类，这样什么代码负责什么功能，大家一眼便懂。哪里出了问题也好寻找（毕竟debug确实不是容易事）

不能觉得把所有代码放进一个文件能多大程度上体现出自己的能力，会整理也是一种能力。当然，对于个人项目，如果这个项目比较简约，简单的写注释就行了。这也是一种“分类”。

## 展示个人技能
Github确实是一个适合展示个人技能的地方。代码质量只要够好，深耕一个领域，便有机会获得极大的关注。

比如数不清的Star。

将自己的代码放在Github公之于众，不仅仅是互联网最原始的“分享精神”的体现，更是一种向别人展示“我可以做到”的公开证明——你能做到这样而别人做不到（或者暂时不想做）的代码，这就是一种技能展示。

谁不喜欢分享那种令人感到“WOW”的代码思路呢？

当然了，个人技能也会反向获得提升。毕竟公开代码也意味着别人能随时发掘代码里面的bug，并随时提出指正意见。一个优秀的coding还包括*修改那些莫名其妙的bug，尽管大部分时候你不知道它们为何会出现*。

## 未来计划？
如果在未来学习的过程中有一些*能让我感到轻哼的代码*以及思路出现了，或许放在这个仓库是一个合适的地方。

可以将学习的新代码的功能、心得、体会，以及一些*邪门用法*丢在这个仓库里。也可以将自己的其他作业都放在这个仓库里，编码就好

甚至可以把之前学习的内容也都放到这个仓库里，这样整个学习体系就连接起来了。

当然，作为学习心理学的学生，或许在未来的某一天我会用到python进行心理学的实验编程。那个时候将一些简易的实验变成模板放到仓库里，甚至是某些经典实验范式丢到仓库里，都不是不行。

*Well希望未来真的会更新这个仓库*。
