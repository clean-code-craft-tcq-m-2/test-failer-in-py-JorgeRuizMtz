
def size(cms):
        if cms <= 38:
             return 'S'
        elif cms > 38 and cms < 42:
            return 'M'
        else:
         return 'L'

assert size(37) == 'S'
assert size(40) == 'M'
assert size(43) == 'L'


assert size(38) == 'S', " You should try your shirt, you can use an S or an M"
assert size(42) == 'L', " You should try your shirt, you can use an M or an L"
print("All is well (maybe!)\n")



