# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] == True:
            result = fn(*args, **kwargs)
            return result
        else:
            return "not valid"
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)


# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1}')
#     return result
#   return wrapper
