import sys, getopt
import time

def main(ifile, targetdir):
    MAXL = 100
    OUTFILENAME = "stream"
    
    ifile = "movie_metadata.csv"
    destdir = "C:\\Dev\\python-projects\\modifsrt\\target\\"
    with open(ifile, encoding='utf-8') as fin:
        line = fin.readline()
        fcnt = 0
        while line:
            cnt = 0
            fcnt += 1
            fout = open("{}out_{}.txt".format(targetdir,fcnt), "w") 
            while line and cnt<MAXL:
                cnt += 1
                fout.write(line)
                line = fin.readline()
            fout.close
            time.sleep(1)

if __name__== "__main__":
    if len(sys.argv) == 1:
        print ('Command syntax:')
        print ('run.py -h -i <inputfile> -d <targetdir>' )
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:d:")
    except getopt.GetoptError:
        print ('run.py -i <inputfile> -d <targetdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('run.py -i <inputfile> -d <targetdir>')
            sys.exit()
        if opt == '-i':
            ifile = (arg)
        if opt == '-d':
            targetdir = (arg)
 
    main(ifile, targetdir)
