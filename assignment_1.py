## 1. List Questions

#  Create a list of 5 fruits and print it.
Fruits = ["Apple", "Banana", "Pineapple", "Grapes", "Watermelon"]
print(Fruits) #['Apple', 'Banana', 'Pineapple', 'Grapes', 'Watermelon']

# Add "Mango" to the end of the list.
Fruits.append("Mango")
print(Fruits) #['Apple', 'Banana', 'Pineapple', 'Grapes', 'Watermelon', 'Mango']

# Insert "Orange" at index 2 in a list.
Fruits.insert(2, "Orange")
print(Fruits) #['Apple', 'Banana', 'Orange', 'Pineapple', 'Grapes', 'Watermelon', 'Mango']

# Remove an element from a list using remove().
Fruits.remove("Pineapple")
print(Fruits) #['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon', 'Mango']

# Print the first and last element of a list.
print(Fruits[0]) #Apple
print(Fruits[-1]) #Mango

# Find the length of a list.
print(len(Fruits)) #6

# Sort a list of numbers in ascending order.
Num = [1, 2, 10, 5, 3, 10, 5, 10]
print(Num)
Num.sort()
print(Num) #[1, 2, 3, 5, 5, 10, 10, 10]

# Reverse a list.
    #By using Slicing
print(Num[::-1]) #[10, 5, 10, 3, 5, 10, 2, 1]

    #By using reverse()
Num.reverse()
print(Num) #[10, 5, 10, 3, 5, 10, 2, 1]

# Count how many times 10 appears in a list.
print(Num.count(10)) #3

# Take 5 numbers from the user and store them in a list.
list1 =[]
for i in range(5):
    num = int(input("Enter The Number: "))
    list1.append(num)

print("Your list is: ",list) #Your list is:  [2, 3, 4, 3, 3]

# Find smallest number in list
a = [5, 2, 8, 1]
print(min(a)) #1

# Count even numbers in list
a = [5, 2, 8, 1]
print(a) #[5, 2, 8, 1]
count = 0
for i in a:
    if i % 2 == 0:
        print(i) # 2, 8
        count = count + 1
print("count of even number:", count) #count of even number: 2

# Create a list of squares from 1 to 10
squares = []
for i in range(1,11):
    num = i * i
    squares.append(num)
print("Square of 1 to 10 numbers:", squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Reverse list without using reverse()
print(a) #[5, 2, 8, 1]
print(a[::-1]) #[1, 8, 2, 5]

# Find second largest number
print(a) # #[5, 2, 8, 1]
a.sort()
print(a) #[1, 2, 5, 8]
print(a[-2]) #5

# Remove all duplicate values from list
a1 = [1,4,1,5,2,1]
print(a1) #[1, 4, 1, 5, 2, 1]
print(list(set(a1))) #[1, 2, 4, 5]

# Merge two lists
    # by using concatenation
a1 = [1,4,1,5,2,1]
a2 = [6,7,4]
merge = a1 + a2
print(merge) #[1, 4, 1, 5, 2, 1, 6, 7, 4]

    #By using extend()
a1 = [1,4,1,5,2,1]
a2 = [6,7,4]
a1.extend(a2)
print(a1) #[1, 4, 1, 5, 2, 1, 6, 7, 4]
 
# Convert string into list of characters
# "python"
a = "python"
print(list(a)) #['p', 'y', 't', 'h', 'o', 'n']

## 2.Tuple Questions

# Create a tuple with 5 integer values.
Tuple = (10, 30, 5, 8, 9)
print(Tuple) #(10, 30, 5, 8, 9)

# Print the second element of a tuple.
print(Tuple[1]) #30

# Find the length of a tuple.
print(len(Tuple)) #5

# Create a tuple with one element.
Tuple2 = (70,)
print(type(Tuple2)) #<class 'tuple'>
print(Tuple2) #(70,)

# Convert a tuple into a list.
print(Tuple) #(10, 30, 5, 8, 9)
print(list(Tuple)) #[10, 30, 5, 8, 9]

# Check whether a value exists in a tuple.
print(9 in Tuple) #True
print(90 in Tuple) #False

# Concatenate two tuples.
num = Tuple + Tuple2
print(num) #(10, 30, 5, 8, 9, 70)

# Find the index of an element in a tuple.
print(Tuple.index(5)) #2

# Count how many times a value appears in a tuple.
print(Tuple.count(10)) #1

# Create a nested tuple and access inner values.
Tuple3 =(1, ("Kavita", "Mansee"),( 15, "apple", 3.14), "Banana")
print(Tuple3) #(1, ('Kavita', 'Mansee'), (15, 'apple', 3.14), 'Banana')
print(Tuple3[0]) #1

print(Tuple3[1]) #('Kavita', 'Mansee')
print(Tuple3[1][0]) #Kavita
print(Tuple3[1][1]) #Mansee

print(Tuple3[2][0]) #15
print(Tuple3[2][1]) #apple
print(Tuple3[2][2]) #3.14

print(Tuple3[3]) #Banana


## 3. Dictionary Questions

# Create a dictionary with keys: name, age, city.
Dict = {"Name":"Kavita", "Age":23, "City":"Bhadgaon"}
print(Dict) #{'Name': 'Kavita', 'Age': 23, 'City': 'Bhadgaon'}

# Print the value of the name key.
print(Dict["Name"]) #Kavita

# Add a new key salary to a dictionary.
Dict["salary"] = 20000
print(Dict) #{'Name': 'Kavita', 'Age': 23, 'City': 'Bhadgaon', 'salary': 20000}

# Update the value of an existing key.
Dict["Age"] = 22
print(Dict) #{'Name': 'Kavita', 'Age': 22, 'City': 'Bhadgaon', 'salary': 20000}

# Remove a key from a dictionary using pop().
Dict2 = Dict.pop("Name")
print(Dict2) #Kavita
print(Dict) #{'Age': 22, 'City': 'Bhadgaon', 'salary': 20000}

# Print all keys of a dictionary.
print(Dict.keys()) #dict_keys(['Age', 'City', 'salary'])

# Print all values of a dictionary.
print(Dict.values()) #dict_values([22, 'Bhadgaon', 20000])

# Check whether a key exists in a dictionary.
print("Name" in Dict) #False
print("Age" in Dict) #True

# Loop through a dictionary and print keys and values.
Dict3 = {"Name":"Kavita", "Age":23, "City":"Bhadgaon"}
for k, v in Dict3.items():
    print(k, ":", v)

# Create a dictionary for a student with marks in 3 subjects.
Dict4 = {"Name": "Kavita", "Marks":{"math": 50, "science":60, "English": 70}}
print(type(Dict4)) #<class 'dict'>
print(Dict4) #{'Name': 'Kavita', 'Marks': {'math': 50, 'science': 60, 'English': 70}}


## 4. Set Questions

# Create a set with 5 numbers.
my_set = {25, 64, 23, 89, 45}
print(type(my_set)) #<class 'set'>
print(my_set) #{64, 23, 89, 45, 25}

# Add an element to a set.
my_set.add(32)
print(my_set) #{64, 32, 23, 89, 45, 25}

# Remove an element from a set.
my_set.remove(64)
print(my_set) #{32, 23, 89, 45, 25}

# Find the length of a set.
print(len(my_set)) #5

# Check whether an element exists in a set.
print(89 in my_set) #True
print(90 in my_set) #False

# Create two sets and find their union.
set1 = {2.2, "Apple", 55, True, "Banana"}
set2 = {"Banana", "Kavita", 44.7, False, 55}
print(set1.union(set2)) #{False, True, 2.2, 'Banana', 'Apple', 44.7, 'Kavita', 55}

# Create two sets and find their intersection.
print(set1.intersection(set2)) #{'Banana', 55}

# Create two sets and find their difference.
print(set1.difference(set2)) #{True, 2.2, 'Apple'}

# Convert a list into a set.
my_list = ["Kavita", 34, 7.5, True]
print(type(my_list )) #<class 'list'>
set1 = set(my_list )
print(set1) #{True, 'Kavita', 34, 7.5}
print(type(set1)) #<class 'set'>

# Remove duplicate values from a list using a set.
my_list = [10, "Kavita", 2.2, 10, 2.2]
print(my_list) #[10, 'Kavita', 2.2, 10, 2.2]
set1 = list(set(my_list))
print(set1) #[10, 2.2, 'Kavita']
