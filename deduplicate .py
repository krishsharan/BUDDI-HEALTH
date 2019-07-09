lines_read = set()  # holds lines already seen
outfile = open('orig.txt', "w")
infile = open('correct.txt', "r")
print "The file orig.txt is as follows"
for line in infile:
    print line
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print "The file correct.txt is as follows"
for line in open('correct.txt', "r"):
    print line
