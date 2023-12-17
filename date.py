import datetime

def currenttime():
    return datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")