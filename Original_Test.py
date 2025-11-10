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