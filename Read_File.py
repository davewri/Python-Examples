def read_File(file):
    fhand =  open(file, 'r').read()
    print fhand
    fhand.close()

read_File("BulkPayment.txt")
