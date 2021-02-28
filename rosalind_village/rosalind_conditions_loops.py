def rosalind(a, b):
    total = 0
    for i in range(a, b):
        if i % 2 == 1:
            total = total + i
            print(total)
        else:
            pass
    return total

print(rosalind(4888, 9624))