def line_Count(file):
    fhand = open(file, 'r')
    count = 0
    for line in fhand:
        count += 1
    print "line count", count
    fhand.close()

line_Count("BulkPayment.txt")
