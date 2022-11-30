
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    list = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors, 1):
            interval = i * 5 + j
            list.append(interval)
            #assert list[0] == 0
            #print(f'{interval} | {major} | {minor}')
            #print("{:<7}|".format(interval), "{:<7}|".format(major), "{:<7}|".format(minor) )
            #text = f'{interval} | {major} | {minor}'
            #print(format(text, '=^20'))
            space = 6
            assert space >= 6, "Format not aligned"
            #text = '| {:^6} | {:^6} | {:^6} |'.format(interval, major, minor)
            #text = (f'{interval} | {major} | {minor}')
            #print(text)
            print('|',f'{interval}'.center(space),'|',f'{major}'.center(space),'|',f'{minor}'.center(space),'|')
            
         
    #return len(major_colors) * len(minor_colors)
    return list

    
    
result = print_color_map()
assert result[0] == 1 , "Index is not started at 1"
print("All is well (maybe!)\n")