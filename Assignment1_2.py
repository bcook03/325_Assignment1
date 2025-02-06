import time

def getTime(func):
    def wrapper(*args):
        print("The time is: ", time.time())


@getTime
def ctime():
    ctime()



