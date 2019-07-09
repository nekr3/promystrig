'''
don't run this file, just use the functions
running the file is just for testing
'''

table = []
table_created = False

'''
creates smth 
size = max degree polynomial
'''
def create_table(size = 1000):
    global table_created
    global table
    if table_created:
        raise Exception('Table Already Created') 
    
    table = [[1], [0, 1]]

    for i in range(2, size + 1):
        prev_one = table[i - 1]
        prev_two = table[i - 2] 

        cur = [0] * (len(prev_one) + 1)
        
        for i in range(len(prev_one)):
            cur[i + 1] = prev_one[i] * 2

        for i in range(len(prev_two)):
            cur[i] -= prev_two[i]

        table.append(cur)

    table_created = True

'''
print a polynomial w given degree
'''
def print_poly(deg):
    global table_created
    global table

    if not table_created:
        create_table()

    for i in range(deg, -1, -1):
        print(table[deg][i], end = 'x^%d + ' % i if i > 0 else '') 
    print()

'''
print a polynomial w given degree taken mod
'''
def print_poly(deg, mod):
    global table_created
    global table

    if not table_created:
        create_table()

    for i in range(deg, -1, -1):
        print(table[deg][i] % mod, end = 'x^%d + ' % i if i > 0 else '') 
    print()

for i in range(20):
    print_poly(i, 5)