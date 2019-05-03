def fnc(x, li):

    print 'Type of x:', type(x)

    print 'Type of li:', type(li)

    x = 500

    li.append(4)

    return x

a = 10

my_li = [1, 2, 3]

print 'List befor function call:', my_li

y = fnc(a, my_li)

print 'value of y:', y

print 'value of a:', a

print 'List after function call:', my_li
