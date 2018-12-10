import sys, socket

target = sys.argv[1]
minport = int(sys.argv[2])
maxport = int(sys.argv[3]) 

def porttry(cur_target, port):
    try:
        s.connect((cur_target, port))   
        return True
    except:
        return None

for i in range(minport, maxport+1):
    s = socket.socket(2, 1) #socket.AF_INET, socket>SOCK_STREAM
    value = porttry(target, i)
    if value != None:
        print("port opened on %d" % i)
        