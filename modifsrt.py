#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import sys, getopt

def longtfm2sec(timestr):
    t = timestr.split(":")
    sec = int(t[0])*3600 + int(t[1])*60 + float(t[2].replace(',','.'))
    return (sec)

def sec2longtfm(sec):
    dm = divmod(sec,3600) 
    jam = str(round(dm[0])).zfill(2)
    dm = divmod(dm[1],60) 
    mnt = str(round(dm[0])).zfill(2)
    dtk = str('%.3f' % dm[1]).zfill(6).replace('.',',')
    return ("%s:%s:%s" % (jam, mnt, dtk))


# In[2]:


def main(srtfile, shift, starton="00:00:00,000", endon="99:99:99,999"):
      
    starttime = longtfm2sec(starton)
    endon = longtfm2sec(endon)
    # namafile = 'Outlander S01E09.srt'
    try:
        f= open(srtfile,"r")
        if f.mode == "r":
            fout= open(srtfile.replace('.srt','_new.srt'), "w")
            f1 = f.readlines()
            reg = re.compile('\d\d\:\d\d:\d\d\,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d')
            for i in f1:
                m = reg.match(i)
                if m:
                    t = i.split(" --> ")
                    if longtfm2sec(t[0])>=starttime and longtfm2sec(t[1])<=endon:
                        t1 = longtfm2sec(t[0]) + shift
                        t2 = longtfm2sec(t[1]) + shift
                        fout.write(sec2longtfm(t1) + ' --> ' + sec2longtfm(t2) + '\n')
                    else:
                        fout.write(i)
                else:
                    fout.write(i)
            fout.close()
        f.close()
        print ('Output file: ' + srtfile.replace('.srt','_new.srt'))
    except FileNotFoundError:
        print('Error read file',srtfile)

if __name__== "__main__":
    if len(sys.argv) == 1:
        print ('Command syntax:')
        print ('run.py -h -i <inputfile> -s <sec shifted>' [-b <begin time> -e <end time>])
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:s:b:e:")
    except getopt.GetoptError:
        print ('run.py -h -i <inputfile> -s <sec shifted>' [-b <begin time> -e <end time>])
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
			print ('run.py -h -i <inputfile> -s <sec shifted>' [-b <begin time> -e <end time>])
            sys.exit()
        if opt == '-i':
            ifile = (arg)
        if opt == '-s':
            shift = int(arg)
        if opt == '-b':
            btime = (arg)
        if opt == '-e':
            etime = (arg)
 
    main(ifile, shift, btime, etime)
