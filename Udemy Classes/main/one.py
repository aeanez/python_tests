# one.py


def func():
    print("FUNC() IN one.py")


print("Top Level in one.py")

if __name__ == '__main__':
    print('one.py se esta llamando directamente!')
else:
    print('one.py ha sido importado!')
