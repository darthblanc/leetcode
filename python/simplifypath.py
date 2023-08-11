import re


def simplifyPath(path):
    path = re.sub("/{2}", "/", path)

    path_stack = path.split("/")
    refinery_stack = []
    path_stack = list(filter(lambda x: x != '', path_stack))

    for i, p in enumerate(path_stack):
        if p == ".":
            continue
        if p == "..":
            if len(refinery_stack) > 0:
                # print(refinery_stack, i)
                refinery_stack.pop()
                # print(refinery_stack, i)
        else:
            refinery_stack.append(p)

    # refinery_stack = list(filter(lambda x: x != '', refinery_stack))
    simp_path = "/".join(refinery_stack)

    if len(simp_path) == 0 or simp_path[0] != '/':
        simp_path = '/' + simp_path

    return f"path: {simp_path}"


print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/bruv/yo/.."))
print(simplifyPath("/a//b////c/d//././/.."))
print(simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))
