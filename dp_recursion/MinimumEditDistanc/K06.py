# 单词最短编辑距离问题（递归解法）

def dpWordEdit(original, target, oplist):
    def dp(i, j):
        ops=[]
        if i == -1:
            return oplist["insert"]*(j+1)
        elif j == -1:
            return oplist["delete"]*(i+1)
        elif original[i]==target[j]:
            ops.append(dp(i-1, j-1) + oplist["copy"])
        else:
            ops.append(dp(i-1, j) + oplist["delete"]),
            ops.append(dp(i, j-1) + oplist["insert"])
        return min(ops) # 在上面的步骤中，我们模拟的"copy""delete""insert"
                        # 等步骤并没有真正在单词中进行，而只是在编号中"-1"，
                        # 模拟步骤的发生

    score = dp(len(original)-1, len(target)-1)

    return score


# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = [
    "cane", "sheep", "algorithm", "debug", "difficult", "directory",
    "wonderful"
]
targetWords = [
    "new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"
]
for i in range(len(originalWords)):
    score= dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
