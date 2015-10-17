#draw a grid
def print_grid(n):
    size = (n-3)//2
    cross_line = '+' + size*' -' + ' +' + size*' -' + ' +' + '\n'
    in_between = '|' + (n-2)*' ' + '|' + (n-2)*' ' + '|' +'\n'
    print (cross_line + size*in_between + cross_line + size*in_between + cross_line)

print_grid(11)
print_grid(5)
print_grid(15)

def print_grid_with_size(n,rows,cols):
    size = (n-3)//2
    cross_line = '+' + cols*(size*' -'+ ' +')  + '\n'
    in_between = '|' + (cols-2)*' ' + '|' + (cols-2)*' ' + '|' +'\n'
    print (rows*(cross_line + size*in_between) + cross_line)

print_grid_with_size(15,2,2)
print_grid_with_size(5,3,2)
print_grid_with_size(5,3,4)




