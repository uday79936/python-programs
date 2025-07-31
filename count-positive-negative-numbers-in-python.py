data = [10,-2,-3,2,5]
positive_number = 0
negative_number = 0

for i in data:
    if i > 0:
        positive_number += 1
    else:
        negative_number += 1
print(positive_number, negative_number)