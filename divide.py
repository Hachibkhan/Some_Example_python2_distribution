def divide(a, b):

    try:

        result = a / b

    except ZeroDivisionError:

        print "You can't divide by zero"

    except TypeError:

        print "Data type not supported"

    else:

        return result

    finally:
        print "inside finally"

a = 10

b = 2

print divide(a, b)

a = 6

b = 0

print divide(a, b)

a = "3"

b = "4"

print divide(a, b)


