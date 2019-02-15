num_words = 0
 
with open('Book1.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")

num_words1 = 0
 
with open('Book2.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

num_words2 = 0
 
with open('Book3.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)


print(num_words+num_words1+num_words2)


