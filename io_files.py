# bad practice
# my_file = open('mbox-short.txt')
# my_file.read()
# my_file.seek(0)  # reset cursor to position 0 to read again
# my_file.read()

# my_file.seek(0)  # reset cursor to position 0 to read again
# print(my_file.readline(4))

# my_file.close()


# good practice

try:
    with open('aExcercises\docs\mbox-short.txt', mode='r') as my_file:
        # mode= w creates a file, mode=a appends a file
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist')
    # raise err
