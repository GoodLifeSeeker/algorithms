# We have two strings imaged as a list of letters. We need to find how many letters are equal one after another
# Other words we need to find the longest sequence

word_a = ['h', 'i', 's', 'h']
word_b = ['f', 'i', 's', 'h']

table = [[0 for i in range(len(word_a))] for j in range(len(word_b))]
max_num = 0
for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:
            table[i][j] = table[i-1][j-1] + 1
            if table[i][j] > max_num:
                max_num = table[i][j]

print(max_num)


                                            


# We have two strings imaged as a list of letters. We need to find how many letters are equal at all


word_a = ['f', 'o', 's', 'h']
word_b = ['f', 'i', 's', 'h']

table = [[0 for i in range(len(word_a))] for j in range(len(word_b))]
max_num = 0
for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:
            table[i][j] = table[i-1][j-1] + 1
            if table[i][j] > max_num:
                max_num = table[i][j]
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])


print(max_num)