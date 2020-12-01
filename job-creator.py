from socket import*
class jobCreator:
    active = True
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
        
    def sendJob(self, method, data, connect):
        task = self.message(method,data,connect)
        self.connectionSocket.send(task.encode())
        response = self.connectionSocket.recv(1024).decode()
        print(response.split(":")[0])
        print(response.split(":")[1])
        print(response.split(":")[2])
        if(response.split(":")[0].split(" ")[1] == "300"):
            self.connectionSocket.close()
            self.active = False
    def message(self, method, data, connect):
        return method+" "+data+":"+"Connection "+connect


jc = jobCreator()
while jc.active:
    print(jc.active)
    print("""1. jc.sendJob("ADD","a 1","open")
2. jc.sendJob("ADD","1 1 1 1","open")
3. jc.sendJob("LEAVE"," ","close")
4. jc.sendJob("PINGIP","192.168.1.10","open")
5. jc.sendJob("PORTSTATUS","192.168.1.17 1200","open")
6. jc.sendJob("TCPFLOOD","192.168.1.17 2300 20","open")
7. jc.sendJob("UDPFLOOD","192.168.1.17 12000 20","open")""")
    num = input("which case would you like to test\n")
    if(num == "1"):
        jc.sendJob("ADD","a 1","open")
    elif(num == "2"):
        jc.sendJob("ADD","1 1 1 1","open")
    elif(num == "3"):
        jc.sendJob("LEAVE"," ","close")
        break;
    elif(num == "4"):
        jc.sendJob("PINGIP","192.168.1.10","open")
    elif(num == "5"):
        jc.sendJob("PORTSTATUS","192.168.1.17 1200","open")
    elif(num == "6"):
        jc.sendJob("TCPFLOOD","192.168.1.17 12000 20","open")
    elif(num == "7"):
        jc.sendJob("UDPFLOOD","192.168.1.17 12000 20","open")
