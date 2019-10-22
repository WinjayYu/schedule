from tools import current_time

def writeFile(filepath, message):
    try:
        f = open(filepath, "a+")
        f.write(current_time() + ": " + message + "\n")
        f.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

def error(errorMessage):
    writeFile("./error.txt", errorMessage)

def log(message):
    writeFile("./logs.txt", message)

    
