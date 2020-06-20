#command input : python task4.py singlefile
#command input : python task4.py multifile
import os
import sys
from datetime import datetime

def query():
    date_format = "%Y/%m/%d"

    print("Enter mining Date ; Y/M/D-Y/M/D")
    print("eg. 2005/4/1-2005/4/30")
    period = input("Input: ")
    period=period.split("-")
    print("mining result(s)")
    for file in os.listdir(target):
        try:
            with open(os.path.join(target, file)) as f:
                for line in f:
                    extract=line.split(" ")
                    hms=extract[3][12:].split("/")
                    convtime=extract[3][1:-9].split("/")
                    month=datetime.strptime(convtime[1], "%b").month
                    t2=convtime[2]+"/"+str(month)+"/"+convtime[0]
                    if period[0] <= t2 <= period[1]:
                        print(line)
                    else:
                        pass
        except:
            pass
#Target directory is the directory where your logfile(s) exit
#Move your log file(s) to new directory if anything else than log file exit
#Edit variable "target" to desired path
dir = sys.argv[1]
target = os.getcwd()+"/"+dir
#target = "/var/log/httpd/"+dir

host = []
time = []
for file in os.listdir(target):
    try:
        with open(os.path.join(target, file)) as f:
            for line in f:
                extract=line.split(" ")
                hn = [i[0] for i in host]
                if extract[0] in hn:
                    loc=hn.index(extract[0])
                    host[loc][1]+=1
                else:
                    host.append([extract[0],1])
                hms=extract[3][12:].split("/")
                convtime=extract[3][1:-9].split("/")
                month=datetime.strptime(convtime[1], "%b").month
                t = convtime[0]+"/"+str(month)+"/"+convtime[2]+hms[0]
                st = [i[0] for i in time]
                if t in st:
                    loc=st.index(t)
                    time[loc][1]+=1
                else:
                    time.append([t,1])
    except:
        pass

host=sorted(host, reverse=True)
print("remotehost: access count")
for x in host:
    print(str(x[0])+": "+str(x[1]))
print("timstamp, access count")
for x in time:
    print(str(x[0])+": "+str(x[1]))
print("Mine Data By Date? Y/N")
ans= input()
if ans=="Y" or ans=="y":
    query()
elif ans=="N" or ans=="n":
    print("exit")
