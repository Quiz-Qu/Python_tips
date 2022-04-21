def dpWordEdit(original, target, oplist):
    score = 0
    operation = []

    m = {(i, j): [0, None] for i in range(len(original)+1)
         for j in range(len(target)+1)}

    original, target = "-"+original, "-"+target

    # 生成第一行第一列
    for j in range(1, len(target)):
        m[0, j] = [oplist["insert"]*j, "insert"+target[j]]

    for i in range(1, len(original)):
        m[i, 0] = [oplist["delete"]*i, "delete"+original[i]]

    for i in range(1, len(original)):
        for j in range(1, len(target)):
            ops = []  # 可以的操作方式
            if original[i] == target[j]:
                ops.append([m[i-1, j-1][0]+oplist["copy"],
                            "copy"+original[i]])
            ops.append([m[i, j-1][0]+oplist["insert"],
                       "insert"+target[j]])
            ops.append([m[i-1, j][0]+oplist["delete"],
                       "delete"+original[i]])
            m[i, j] = min(ops, key=lambda x: x[0])
    score = m[i, j][0]
    while i > 0 or j > 0:
        op = m[i, j][1]
        operation.insert(0, op)  # 倒序输出操作序列
        if "copy" in op:
            i -= 1
            j -= 1
        elif "delete" in op:
            i -= i
        elif "insert" in op:
            j -= 1
    return score, operation

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
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)
