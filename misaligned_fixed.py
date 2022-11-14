
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    list = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            interval = i * 5 + j
            list.append(interval)
            #assert list[0] == 0
            #print(f'{interval} | {major} | {minor}')
            #print("{:<7}|".format(interval), "{:<7}|".format(major), "{:<7}|".format(minor) )
            #text = f'{interval} | {major} | {minor}'
            #print(format(text, '=^20'))
            s = 6
            text = '| {:^6} | {:^6} | {:^6} |'.format(interval, major, minor)
            print(text)
            
         
    #return len(major_colors) * len(minor_colors)
    return list

    
    
result = print_color_map()
assert result[0] == 1 , "Index is not started at 1"
print("All is well (maybe!)\n")