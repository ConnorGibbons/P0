import sys
import gzip


def tokenize(text,k):
    lines = text.splitlines()
    extractedTokens = []
    for line in lines:
        #line = line.lower() Doesn't need to be lowered, leaving for later
        #line = line.replace(":","").replace(",","").replace(".","").replace("\"","").replace("!","").replace("?","") -- Turns out we don't need to remove punctuation, but I'm leaving this here for later.
        tokens = line.split()
        if(len(tokens) >= k):
            extractedTokens.append(tokens[k-1])
        else:
            extractedTokens.append("Too Short")

    min = ""
    for token in extractedTokens:
        if(min == ""):
            min = token
        elif((token < min) and (token != "Too Short")):
            min = token

    max = ""
    for token in extractedTokens:
        if(max == ""):
            max = token
        elif((token > max) and (token != "Too Short")):
            max = token

    extractedTokens.append(f"{len(lines)} {min} {max}")
    return extractedTokens
    

if __name__ == '__main__':
    # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "../P0-sample.txt.gz"
    openedFile = gzip.open(inputFile,'rb')
    outputFile = sys.argv[2] if argv_len >= 3 else "../P0-sampleout.txt"
    k = int(sys.argv[3]) if argv_len >= 4 else 7
    tokenizedFile = tokenize(openedFile.read().decode('utf-8'),k)
    outputFileOpened = open(outputFile,'w+')
    for token in tokenizedFile:
        outputFileOpened.write(str(token) + "\n")
    outputFileOpened.close()



    