#in this programs we will use nested loops to make patterns
#lets make a program to generate multiplication tables from 1 to 10
print('Multiplication table from 1 to 10 is as follows ')
for i in range(1,11,1):
    for j in range(1,11,1):
        print(format(i * j, "4d"), end=" ")
    print() # for the sake of new line


