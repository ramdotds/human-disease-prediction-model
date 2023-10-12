from flask import request

def input():
    inp_lst = []
    for i in range(0,131):
        inp = request.form["inp{}".format(i+1)]
        if inp=='yes':
            inp_lst.append(1)
        elif inp=='no':
            inp_lst.append(0)
        else:
            break
    
    return inp_lst