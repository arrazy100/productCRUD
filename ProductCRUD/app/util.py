import random

def generateCode(num_of_digits):
    code = ''

    for i in range(num_of_digits):
        if (i == 0):
            rand = random.randint(1, 9)
        else:
            rand = random.randint(0, 9)
        
        code += str(rand)

    return code