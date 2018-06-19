
# Write a program which will find all 
# such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200(both included).
#  The numbers obtained should be printed in a comma-seperated sequence on a single line

l = ""
count = 0
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        if(count != 0):
            l = l + ','            
        l = l + str(i)
        count += 1

print(l)