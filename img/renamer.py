import os

if __name__ == '__main__':
    fname = input('Enter Filename Prefix: ')
    fformat = input('Enter File Format: ')
    count = 0
    for f in os.listdir('.'):
        if not f.startswith('.') and not f.endswith('.py'):
            count += 1
            os.rename(f, '{} - {:03d}.{}'.format(fname, count, fformat))
