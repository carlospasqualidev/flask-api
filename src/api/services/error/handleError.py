
errors = []

def addError(error):
    errors.append(error)

def getErrors():
    clonedErrors = errors[:]
    errors.clear()
    return clonedErrors