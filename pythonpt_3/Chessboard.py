import sys

def chessboard(numberOfBoxes):
    black = "#"
    white = "_"
    string = ""
    for i in range(1, numberOfBoxes + 8):
        if(i % 9 == 0):
            string += "\n" 
        elif(i % 2 == 0):
            string += white
        else:
            string += black
    print(string)
    return string

chessboard(int(sys.argv[1]))