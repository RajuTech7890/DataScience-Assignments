# numberSeq = input("Please enter a sequence of coma-separated numbers: \n")
# if numberSeq.count(",") != 0:
#     numberList = numberSeq.split(",")
#     numberList = list(map(lambda x: float(x), numberList))
# else:
#     print("Please enter coma-separated numbers")
# print(numberList)

inputString = "Test"
p = "Test"
output1 = []
# for x in p:
#     print(x)
# print(output1)

# output = [x for x in inputString]
# print(output)

inputString2 = "xyz"
outputArray2 = [(a*b) for a in inputString2 for b in range(1, 5)]
print(outputArray2)

for a in inputString2:
    for b in range(1, 5):
        print([a*b])
