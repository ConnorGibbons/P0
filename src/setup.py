import sys
import gzip

if __name__ == '__main__':
    # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "../P0-sample.txt.gz"
    openedFile = gzip.open(inputFile,'rb')
    print(openedFile.read())
    outputFile = sys.argv[2] if argv_len >= 3 else "../P0-sampleout.txt"
    k = int(sys.argv[3]) if argv_len >= 4 else 7


def tokenize(text,k):
    return 'h'
    