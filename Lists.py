#create a list 
list1= ["apple","banana","cherry","tomato","guava","pear","mango"]

#Accessing elements from the list
print(list1[0])
print(list1[1])
print(list1[2]) 

#Negative Indexing
print(list1[-1])
print(list1[-2])
print(list1[-3])

# slicing
print(list1[2:4])

#2D Lists
matrix= [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0, len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end= "")
    print("\n")

    #Take an input for a matrix and print the elements
rows= int(input("Enter the number of rows:- "))
columns= int(input("Enter the number of columns:- "))

matrix=[]

for i in range (rows):
    temp= []
    for j in range(columns):
        x= int(input("enter your element-" ))
        temp.append(x)
    matrix.append(temp)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end= "")
    print("\n")

#Take the square-matrix as input and print the diagonalelements
n= int(input("Enter the dimensions of the matrix"))
for i in range(n):
    temp=[]
    for j in range(n):
        x = int(input("enter the element"))
        temp.append(x)
    matrix.append(x)

for i in range(n): 
    print(matrix[i][i])   
    
    


