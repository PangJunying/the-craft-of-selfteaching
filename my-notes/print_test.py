import sys

print("Hello", 'world')
print('hello', 'wold!', sep=' ', end='\n',  file=sys.stdout, flush=False)
print('hello', 'world', sep='-', end='\t')
print('hello', 'world!', sep='~')
print('hello', 'world!', sep='\n')

print('-'*10)
print(print(1, flush=True))
