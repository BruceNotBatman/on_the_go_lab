import sys

line = input()
split = line.split()

if len(split) !=3:
    print("Operation Error")
    sys.exit()

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == "-":
    val = left - right
elif op == "*":
    val = left * right
elif op == "/":
    if right == 0:
        print("Error 0 Division")
        sys.exit()
    else:
        val = left/right
else:
    print("Unknown operator: {operator}".format(operator = op))
    sys.exit()

print("{operation} = {answer:.2f}".format(operation = line, answer = val))