# Python code​​​​​​‌‌​​​​​​​‌​‌​​‌​​‌​‌​​‌‌‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num) - num

for i in range(1, 100):
    print(f'The square of {i} is {square(i)}')
