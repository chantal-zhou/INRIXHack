def write_to_file(dictionary, name):
    with open(name + ".txt", 'w') as f:  
        for key, value in dictionary.items():  
            f.write('%s:%s\n' % (key, value))

def sort_by_highest(dictionary):
    return dict(reversed(sorted(dictionary.items(), key=lambda item: item[1])))

def sort_by_lowest(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))
