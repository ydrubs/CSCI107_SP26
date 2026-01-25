"""
SP26
Example algorithms from class
"""
# n = 676773687365874356
# sum = 0
#
# for digit in str(n):
#     # print(digit)
#     sum += int(digit)
#
# print(sum)

# ---------------------------
n = 6776576453443432
prime = False

for i in range(2, int(n**0.5)):
    if n % i == 0:
        break
    else:
        prime = True

print(f'Prime Status of {n}: {prime}')

