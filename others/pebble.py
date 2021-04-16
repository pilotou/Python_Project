import random

def pebble():
    box = []
    #生成 20 个元素的数组，只包括0和1
    for i in range(20):
        box.append(random.randint(0,1))
    #box中light pebble的个数
    light = box.count(0)
    #box中black pebble的个数
    black = box.count(1)
    # print("the total pebbles is {}".format(len(box)))
    print("the box have {} light pebble".format(light))
    print("the box have {} black pebble".format(black))

    i = 0
    # print("--------------------")
    # take 2 pebble form box
    while (len(box) >2):
        i = i+1
        # print("the {} times draw the pebble from box ".format(i))
        # print("number of pebbles remain: " + str(len(box)))
        # print("the drawing outcome is ")

        #取两个pebble：
        #在指定范围内产生两个不同的随机数，下标就是所取的pebble
        [a,b] = random.sample(range(0,len(box)-1),2)

        #match, discard both, add black
        if (box[a] == box[b]):
            # if box[a]==1:
            #     print("\t 2 black pebbles")
            # else:
            #     print("\t 2 light pebbles")
            # print("match, discard both and add a black pebble")

            # 删除box列表中指定下标的数
            # 将要删除的元素改为3， 然后删除list中值为3的元素。
            box[a] = 3
            box[b] = 3
            while 3 in box:
                box.remove(3)

            #向box中随机插入一个元素，值为1
            box.insert(random.randint(0,len(box)-1),1)
            # print("the box remain {} light pebble".format(box.count(0)))
            # print("and  {} black pebble".format(box.count(1)))
            # print("-----------------------")
        # not match, discard black, return light
        else:

            # print("\t 1 light pebble and 1 black pebble")
            # print("not match, discard black pebble and return light pebble")
            #找到black pebble的下标，并删除它
            if (box[a]== 1):
                black_index = a
            else:
                black_index = b
            box[black_index] =3
            box.remove(3)
            # print("the box remain {} light pebble".format(box.count(0)))
            # print("and  {} black pebble".format(box.count(1)))
            # print("-----------------------")

    if (box[1]==box[0]):
        print("the last pebble is black")
    else:
        print("the last pebble is light")

if __name__ == '__main__':
    ia = 0
    while (ia < 10):
        ia= ia + 1
        pebble()