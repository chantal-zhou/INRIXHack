import json 

def write_to_file(dictionary, name):
    with open(name + ".txt", 'w') as f:  
        for key, value in dictionary.items():  
            f.write('%s:%s\n' % (key, value))
