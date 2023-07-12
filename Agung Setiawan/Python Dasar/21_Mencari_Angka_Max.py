numbers = [1,3,41,5,1,2,4]

sum_numbers = sum(numbers)
print(sum_numbers)
number_max = max(numbers)
print(number_max)

numbers.sort()
print(numbers[-1])

numbers = [1,3,41,5,1,2,4]

firs_number = numbers[0]
for number in numbers:
    if number > firs_number:
        firs_number = number

print(firs_number)

numbers = [1,3,41,5,1,2,4]

number_min = min(numbers)
print(number_min)
numbers.sort()
print(numbers[0])

numbers = [1,3,41,5,1,2,4]

last_number = numbers[4]
for number in numbers:
    if number < last_number:
        last_number = number

print(last_number)
