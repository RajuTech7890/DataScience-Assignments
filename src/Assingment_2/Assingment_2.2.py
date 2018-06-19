# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
rows = input("Enter the no of rows...\n")
rows = int(rows)+1
for number in range(1, rows):
    print(" ".join("*"*min(number, rows-number)))
