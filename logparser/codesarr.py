x2 = ['200']
x4 = ['400', '403', '404']
x5 = ['500']

def codes(num):

    for i in x2:
        if num == i:
            return x2
    for i in x4:
        if num == i:
            return x4
    for i in x5:
        if num == i:
            return x5
