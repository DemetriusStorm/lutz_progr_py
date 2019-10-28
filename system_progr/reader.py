import sys

print('Got this: {}'.format(input()))
data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data) * 2)
