def read_file(f):
    with open(f, 'r') as _file:
        text = _file.read()
        return [int(number) for number in text.split(',')]

def median(l: list):
    if len(l) % 2 != 0:
        return l[int(len(l)/2)]
    else:
        return int((l[len(l)//2 - 1] + l[len(l)//2])/2)

f = read_file('input.txt')
f.sort()
median = median(f)
fuel_sum = 0
for num in f:
   fuel_sum += abs(num - median)

print(fuel_sum)
