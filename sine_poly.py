from decimal import Decimal

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
    
    table = [[], [1]]

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
print a polynomial w given degree taken mod
if no mod is provided, then it just prints the polynomial out
'''
def print_poly(deg, mod = None):
    global table_created
    global table

    if not table_created:
        create_table()

    for i in range(deg, -1, -1):
        if mod is None:
            print(table[deg + 1][i], end = 'x^%d + ' % i if i > 0 else '') 
        else:
            print(table[deg + 1][i] % mod, end = 'x^%d + ' % i if i > 0 else '') 
    print()

'''
prints out the value of the expression evaluated at for a specific polynomial
n = degree of polynomial
val = val to evaluate (x = val in polynomial)
use the decimal module for best accuracy
'''
def eval(n, val):
    global table_created
    global table

    if not table_created:
        create_table()

    if not isinstance(val, Decimal):
        print('warning: using the built-in decimal module gives better accuracy')

    ans = 0
    for i in range(n, -1, -1):
        ans *= val
        ans += table[n][i]

    return ans
