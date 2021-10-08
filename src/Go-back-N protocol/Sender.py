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
        sleep(1)
        # print(messg+"......................Sent")
    except:
        print("Cant send")


a = "True Friendship cannot be forged overnight"
count1=0
index = 0
end = 4
while(count1 < len(a)):
    count = 0
    m = a[index:end]
    index = index+4
    end = end+4
    count1 = count1+4
    print(m+"......................Sent")
    while(count < len(m)):
        sleep(3)
        send(m[count])
        count = count+1
    sleep(5)
