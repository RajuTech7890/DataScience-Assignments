# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list.
outputList = []
inputString = input("Enter the numbers separated by comma: ").split(',')
for items in inputString:
    outputList.append(int(items))
print(outputList)
