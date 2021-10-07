from time import sleep


def receive():
    try:
        f = open("file2.txt", 'r')
        data = f.read()
        #t = open("received-message.txt","a")
        # t.write(data+"\n")
        # t.close()
        print()
        print(f"{data}.............Received")
        # print(data+"................Received")
        f.close()
        v = open("channel2.txt", "w")
        data1 = "AckReceived"
        v.write(data1+"\n")
        v.close()
        sleep(1)
        print("Ack Sent")
    except:
        print("....Didnt Recieved")


while True:
    sleep(5)
    receive()
