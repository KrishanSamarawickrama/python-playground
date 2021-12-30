def announce(f):
    def wrapper():
        print('About to run the function')
        f()
        print('End of running fuction')
    return wrapper

@announce
def hello():
    print(f'Hello !! form the function')

    
hello()