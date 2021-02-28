f = open('input.txt', 'r')
b = open('new.txt', 'w')
i = 1
for line in f.readlines():
    if i % 2 == 1:
        pass
    else:
        print(line)
        b.write(line)
    i += 1

# the paragraph starts with 1 based numbering instead
# comp sci 0 based numbering