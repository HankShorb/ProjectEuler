global collatz_collection
collatz_collection = {1:1,2:2}
def collatz(n):
    if n==1:
        return 1
    elif n not in collatz_collection:
        if n%2 == 0:
            collatz_collection[n] = collatz(n/2) + 1
        else:
            collatz_collection[n] = collatz(3*n + 1) + 1

    return collatz_collection[n]



def max_collatz_in(x,y):
    for i in range(x,y+1):
        collatz(i)

    maximum = collatz_collection[2]
    max_index = 2

    for i in collatz_collection:
        if  i>=x and i<=y and collatz_collection[i] > maximum:
            maximum = collatz_collection[i]
            max_index = i

    print "The max collatz sequence in", x, "to", y, "is", collatz_collection[max_index], "for", max_index



find = True
while find:
    start = int(raw_input("Start number: "))
    end = int(raw_input("End number: "))
    print ""
    max_collatz_in(start,end)
    print ""
    cont = raw_input("Would you like to find another maximum collatz sequence? (y/n): ")
    if cont == "n":
        find = False
