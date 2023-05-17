T = int(input())

p = []
t = []

for i in range(T):
    p = []
    n = int(input())
    for j in range(n):
        case = input().split()
        name = case[0].replace(":", " ")
        name_classes = case[1].split("-")
        class_def = ""
        p.append(name)
        for name_class in name_classes:
            if name_class == "upper":
                class_def += "a"
            if name_class == "middle":
                class_def += "b"
            if name_class == "lower":
                class_def += "c"
        class_def = (((10 - len(class_def)) * "b") + class_def)
        t.append(class_def[::-1])
    d = {}
    for k in range(len(p)):
        d[p[k]] = t[k]

    sorted_d = sorted(d.items(), key=lambda x: x[1])
    for x in sorted_d:
        print(x[0])
    print("=" * 30)
