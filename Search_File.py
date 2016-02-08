import pprint

select_List = []

def search(select_List):
    fhand= open("BulkPayment.txt")
    for line in fhand:
        # line = line.rstrip()
        if "SELECT" in line:
            line = line.rstrip()
            select_List.append(line)
    return select_List

def select_SQL():
    for entry in search(select_List):
        print "found:", entry
    pprint.pprint(select_List)

select_SQL()

