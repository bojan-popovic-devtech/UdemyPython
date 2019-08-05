ip = input("Please enter IP address: ")
numberOfSegments = 0
segmentLength = 0
number=""
for number in ip:
    if number != ".":
        segmentLength += 1
    elif number == ".":
        numberOfSegments += 1
        print("{}. Segment had {} length".format(numberOfSegments,segmentLength))
        segmentLength = 0
if number != ".":
    numberOfSegments += 1
    print( "{}. Segment had {} length".format( numberOfSegments, segmentLength ) )

print("There were {} segments".format(numberOfSegments))



