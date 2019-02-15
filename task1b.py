with open('Book1.txt', 'r') as f:
    count = {}
    lines = f.read()
    lines = lines.split()
    for i in lines:
        count[i] = lines.count(i)
    print(count)
