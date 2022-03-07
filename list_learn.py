no = 5
num = []
sum = 0
for i in range(no):
    value = eval(input("Enter the value : "))
    num.append(value)
    sum += value
avg = sum / no

count = 0
for i in range(no):
    if num[i] > avg:
        count += 1


print("Average is: ", avg)
print("Number of values above average is: ", count)