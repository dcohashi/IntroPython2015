#draw a grid
def print_grid(n):
    size = (n-3)//2
    cross_line = '+' + size*' -' + ' +' + size*' -' + ' +' + '\n'
    in_between = '|' + (n-2)*' ' + '|' + (n-2)*' ' + '|' +'\n'
    print (cross_line + size*in_between + cross_line + size*in_between + cross_line)

print_grid(11)
print_grid(5)
print_grid(15)
