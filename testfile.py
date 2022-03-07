nofv = 5
num = []
sum = 0
for i in range(nofv):
    value = eval(input("Enter the value : "))
    num.append(value)
    sum += value
avg = sum / nofv

count = 0
for i in range(nofv):
    if num[i] > avg:
        count += 1


print("Average is: ", avg)
print("Number of values above average is: ", count)