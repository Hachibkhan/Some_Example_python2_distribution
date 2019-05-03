def list (x, y, z = None):

    x = x * x

    y = y * y

    if z is None:

        z = []

    return x, y, z

x, y, z = list(10, 20)

print x

print y

print z




