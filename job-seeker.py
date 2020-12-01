from socket import *
from scapy.all import *
class jobSeeker:
    active = True
    def __init__(self, ip):
        self.serverName = ip
        self.serverPort = 12000
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        print(self.clientSocket.connect((self.serverName, self.serverPort)))

    def getJobs(self):
        while(self.active):
            ##print(self.active)
            message = self.clientSocket.recv(1024)
            lines = message.decode().split(":")
            self.method = lines[0].split(" ")[0]
            self.nums = lines[0].split(" ")[1:]
            print(lines[0])
            print(lines[1])
            decision = input("""What would you like to do?
1. Complete Task
2. Reject Task and disconnect""")
            if(decision == "1"):
                if(self.method == "LEAVE"):
                    self.clientSocket.send(self.message("","close","").encode())
                    self.clientSocket.close()
                    break;
                elif(self.method == "ADD"):
                    answer = 0
                    flag = True
                    for i in range (len(self.nums)):
                        if(self.nums[i].isnumeric()):
                            answer += int(self.nums[i])
                        else:
                            self.clientSocket.send(self.message("200 INVALID REQUEST","open","").encode())
                            flag = False
                            break;
                    if(flag):
                        self.clientSocket.send(self.message("100 OK","open",answer).encode())
                elif(self.method == "PINGIP"):
                    self.clientSocket.send(self.message("100 OK","open",pingIP(self.nums)).encode())
            else:
                self.reject()

    def message(self, status, connect, data):
        self.status = status
        self.connect = connect
        self.data = data
        return "Status "+self.status+":Connection "+self.connect+":"+str(self.data)
    
    def reject(self):
        self.clientSocket.send(self.message("300 REJECTED","close","").encode())
        self.clientSocket.close()
        self.active = False

    def pingIP(self, data):
        cmp = IP(dst=data)/ICMP()
        response = sr1(cmp, timeout=5)
        if response == None:
            return "This host is down"
        else:
            return "This host is up"

    def pingHost(self, data):
        cmp = socket.gethostbyname(data)
        response = sr1(cmp, timeout=5)
        if response == None:
            return "This host is down"
        else:
            return "This host is up"


js = jobSeeker("192.168.1.17"); ##enter ip address here
js.getJobs()
