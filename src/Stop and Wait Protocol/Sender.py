from time import sleep


def send(messg):
    t = open("channel2.txt", "r")
    data = t.read()
    print(data)
    t.close()
    sleep(1)

    f = open("file2.txt", "w")
    try:
        f.write(messg)
        f.close()
        print(messg+"......................Sent")
    except:
        print("Cant send")


while True:
    a = "True Friendship cannot be forged overnight"
    count = 0
    while(count < len(a)):
        sleep(5)
        send(a[count])
        count = count+1
