def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
seq=[1,2,3,4,2,3,5,6]
print(f7(seq))
