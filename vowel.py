a=input("enter a statement")
vowels=['a','e','i','o','u']
list=[]
for x in a:
    if (x in vowels and x not in list):
        list.append(x)
print(list)
