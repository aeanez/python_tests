# two.py

import one
print('Top Level in two.py')

one.func()

if __name__ == '__main__':
    print('two.py se esta llamando directamente!')
else:
    print('two.py ha sido importado!')
