from time import sleep
count = 1


def receive():
    try:
        global count
        f = open("file2.txt", 'r')
        data = f.read()
        #t = open("received-message.txt","a")
        # t.write(data+"\n")
        # t.close()
        print()
        print(f"{data}.............Received")
        # print(data+"................Received")
        f.close()
        sleep(2)
        v = open("channel2.txt", "w")
        data1 = "Ack"+str(count)+" Received"
        v.write(data1+"\n")
        v.close()

        print(f"Ack{count} Sent")

        count = count+1

    except:
        print("....Didnt Recieved")


while True:
    sleep(3)
    receive()
