# -*- coding:utf-8 -*-
#'eater.gif'是吃豆人的图像
#'demon.gif'是怪物的图像
# map1,map2,map3,map4,map5的txt文件中储存了要用的地图的墙的分割为小矩形的坐标
from Tkinter import *
from string import *
from random import random
from time import *

def rebackLevel1():   #第一关失败后重来的窗口
    askFail.destroy()
    paintCanvas1()

def rebackLevel2():   #第二关失败后重来的窗口
    askFail2.destroy()
    paintCanvas2()

def rebackLevel3():   #第三关失败后重来的窗口
    askFail3.destroy()
    paintCanvas3()

def rebackLevel4():   #第四关失败后重来的窗口
    askFail4.destroy()
    paintCanvas4()

def rebackLevel5():   #第五关失败后重来的窗口
    askFail5.destroy()
    paintCanvas5()

def continueLevel2():   #第一关成功后继续的窗口
    ask.destroy()
    paintCanvas2()

def continueLevel3():   #第二关成功后继续的窗口
    ask2.destroy()
    paintCanvas3()

def continueLevel4():   #第三关成功后继续的窗口
    ask3.destroy()
    paintCanvas4()

def continueLevel5():   #第四关成功后继续的窗口
    ask4.destroy()
    paintCanvas5()

def destroyI():
    askI.destroy()

def rebackI():
    askFailI.destroy()
    Invincible()

def Right(i,L,cv):   #在第L关中检验怪物向右移动一次是否撞墙
    walls=[9,16,16,13,26,9]   #每关中墙的块数+1
    xyb=list(cv.coords(i))   #返回i的坐标
    xyb_=list(cv.find_overlapping(xyb[0]-14+1,xyb[1]-14,xyb[0]+14+1,xyb[1]+14))
    if xyb_[0]<walls[L-1]:
        return False   #撞墙了
    return True   #没撞墙

def Left(i,L,cv):   #在第L关中检验怪物向左移动一次是否撞墙
    walls=[9,16,16,13,26,9]
    xyb=list(cv.coords(i))
    xyb_=list(cv.find_overlapping(xyb[0]-14-1,xyb[1]-14,xyb[0]+14-1,xyb[1]+14))
    if xyb_[0]<walls[L-1]:
        return False
    return True

def Up(i,L,cv):   #在第L关中检验怪物向上移动一次是否撞墙
    walls=[9,16,16,13,26,9]
    xyb=list(cv.coords(i))
    xyb_=list(cv.find_overlapping(xyb[0]-14,xyb[1]-14-1,xyb[0]+14,xyb[1]+14-1))
    if xyb_[0]<walls[L-1]:
        return False
    return True

def Down(i,L,cv):   #在第L关中检验怪物向下移动一次是否撞墙
    walls=[9,16,16,13,26,9]
    xyb=list(cv.coords(i))
    xyb_=list(cv.find_overlapping(xyb[0]-14,xyb[1]-14+1,xyb[0]+14,xyb[1]+14+1))
    if xyb_[0]<walls[L-1]:
        return False
    return True

def zhq(i,x,y,L,cv):   #在第L关中检验怪物是否撞墙并移动
    walls=[9,16,16,13,26,9]
    xyb = list(cv.coords(i))
    xyb_ = list(cv.find_overlapping(xyb[0] - 14 + x, xyb[1] - 14 + y, xyb[0] + 14 + x, xyb[1] + 14 + y))
    if xyb_[0] < walls[L-1]:
        cv.move(i, 0, 0)   #撞墙了，不移动
    else:
        cv.move(i, x, y)   #没有撞墙，移动


def zhqEater(x,y,i,L,cv):   #在第L关中检验吃豆人是否撞墙并移动
    walls=[9,16,16,13,26,9]
    xyc__=list(cv.coords(i))
    xyc___=list(cv.find_overlapping(xyc__[0]-8+x,xyc__[1]-8+y,xyc__[0]+8+x,xyc__[1]+8+y))
    if xyc___[0]<walls[L-1]:
        cv.move(i, 0, 0)   #撞墙了，不移动
    else:
        cv.move(i, x, y)   #没有撞墙，移动

def budongle(i,x,y,L,cv):   #解决怪物不动了的问题
    back=0
    if Down(i,L,cv)==False:
        back +=1
    if Up(i,L,cv)==False:
        back +=1
    if  Right(i,L,cv)==False:
        back += 1
    if  Left(i,L,cv)==False:
        back += 1
    if back == 3:
        return True

def zhuan(i,a,b,L,cv):   #使怪物随机运动
    if budongle(i,a,b,L,cv):
        return -a,-b
    else:
        if b == 0 :   #目前处于水平运动状态
            x=random()
            if Up(i,L,cv) and Down(i,L,cv):   #除了水平运动，上下都可以走
                if x > 0.75:
                    a,b = 0,-1   #向上走
                elif x > 0.5:
                    a,b = 0,1   #向下走
                elif x > 0.25:
                    a,b = -a,-b   #向反方向走
            elif Up(i,L,cv):   #除了水平运动，只有向上可以走
                if x > 0.66:
                    a,b = 0,-1   #向上走
                elif x > 0.33:
                    a,b = -a,-b   #向反方向走
                
            elif Down(i,L,cv):   #除了水平运动，只有向下可以走
                if x > 0.66:
                    a,b = 0,1   #向下走
                elif x > 0.33:
                    a,b = -a,-b   #向反方向走
                
        else:   #目前处于上下运动状态
            y=random()
            if Right(i,L,cv) and Left(i,L,cv):   #除了上下运动，左右都可以走
                if y > 0.75:
                    a,b = -1,0   #向左走
                elif y > 0.5:
                    a,b = 1,0   #向右走
                elif y > 0.25:
                    a,b = -a,-b   #向反方向走
            elif Right(i,L,cv):   #除了上下运动，只能向右走                        
                if y > 0.66:
                    a,b = 1,0   #向右走
                elif y > 0.33:
                    a,b = -a,-b   #向反方向走
            elif Left(i,L,cv):   #除了上下运动，只能向左走
                if y > 0.66:
                    a,b = -1,0   #向左走
                elif y > 0.33:
                    a,b = -a,-b   #向反方向走
    
    return a,b


def movetriangle(event):   #移动吃豆人
    global c
    global d
    if event.keysym == 'Up':
        c,d=0,-1        
    elif event.keysym == 'Down':
        c,d=0,1         
    elif event.keysym == 'Left':
        c,d = -1,0
    elif event.keysym == 'Right':
        c,d = 1,0


def deleteBeans(maps,cv,L):   #在第L关中的地图上除去与墙重叠的豆子
    itemsBesidesBeans=[13,20,20,17,30,13]   #每关中墙块、吃豆人和怪物的总数
    f = open(maps, "r")  #读入地图中的矩形的大致坐标
    r = f.readlines()  #全部读取
    list1 = []  #创建用来存储坐标的list1
    for i in r:
        a = i.split()  #将r拆分为坐标数值的列表
        for t in a:  #遍历列表
            t = int(t)  #将列表中的元素类别转化为数值
            s = (t + 5) / 10 * 10  #四舍五入精确坐标
            list1.append(s)  #添加到list1中

    listx1 = []  # 坐标分类
    # 因为此时list1中的坐标数值是以' x1,x2,y1,y2 ,x1,x2,y1,y2 …… '的形式存在的，
    # 所以在这里将其分类到专门存储x1,x2,y1,y2的四个列表中
    listy1 = []
    listx2 = []
    listy2 = []
    for i in range(0, len(list1), 4): #每四个为一组
        listx1.append(list1[i])  #将所有的x1,y1,x2,y2坐标分别放在listx1,listy1,listx2,listy2中
        listy1.append(list1[i + 1])
        listx2.append(list1[i + 2])
        listy2.append(list1[i + 3])

    for i in range(len(listx1)):  #遍历坐标列表，四个一组为一个地图的矩形坐标
        x1 = listx1[i]
        y1 = listy1[i]
        x2 = listx2[i]
        y2 = listy2[i]
        list3 = list(cv.find_overlapping(x1, y1, x2, y2))  # 找出与地图重叠的豆豆

        for t in list3:
            if t > itemsBesidesBeans[L-1]:   
                cv.delete(t)  # 删掉豆豆
                
def eat(cv,i,L,beans,windows):
    global life,score
    positionOfEater=[97,97,97,68,97,97]   #吃豆人在每关中的初始位置和复活位置
    xPositionOfDemons=[355,415,355,275,215,355]   #怪物在每关中的复活位置
    itemsOfWallsAndEater=[9,16,16,13,26,9]   #每关中墙块和吃豆人的总数
    itemsBesidesBeans=[13,20,20,17,30,13]   #每关中墙块、吃豆人和怪物的总数
    xya1 = list(cv.coords(i))  # 报告吃豆人的中心坐标,存储形式：xya1=[x1,y1,x2,y2]
    xya = list(cv.find_overlapping(xya1[0] - 10, xya1[1] - 10, xya1[0] + 10, xya1[
            1] + 10))  # 吃豆人的大小是20*20，所以(xya1[0]-10,xya1[1]-10,xya1[0]+10,xya1[1]+10)得到的是吃豆人矩形 用find_overlapping找出与吃豆人矩形范围内重叠的其他图形（豆豆）的标识号，存到列表中
    for n in xya:  # 删掉xya中的图形项（豆豆），表示被吃掉了
        if n > itemsBesidesBeans[L-1]: 
            cv.delete(n)   #吃掉豆豆
            score+=10   #分数+10
            if n == beans[-1] or n == beans[-2]:   #吃掉大豆豆
                score += 50   #分数+50
                life += 1   #生命值+1

            Label(windows, text="Your scores: %d"%(score), fg='black', font="Times -15 bold",
                      bg='LightSkyBlue').place(x=300, y=0, anchor=N)
            #写有分数的标签
            Label(windows, text="Your lives: %d" % (life), fg='black', font="Times -15 bold",
                  bg='LightSkyBlue').place(x=300, y=600, anchor=S)
            #写有生命值的标签
        elif n > itemsOfWallsAndEater[L-1]:   #被怪物吃掉
            sleep(0.5)
            cv.move(i,positionOfEater[L-1]-xya1[0],positionOfEater[L-1]-xya1[1])
            #吃豆人回到初始位置
            xyn = list(cv.coords(n))
            cv.move(n,xPositionOfDemons[L-1]-xyn[0],300-xyn[1])
            #怪物回到复活位置
            life=life-1   #生命值-1
            Label(windows, text="Your lives: %d" % (life), fg='black', font="Times -15 bold",
              bg='LightSkyBlue').place(x=300, y=600, anchor=S)
            #写有生命值的标签

def paintCanvas1(): #LEVEL1
    global askFail
    global score,life
    life = 3
    score = 0
    win1 = Toplevel()
    win1.resizable(0,0)

    bg1 = Canvas(win1, width=600, height=600, bg="white")  # 画布
    bg1.pack()
    global a1

    p1 = (20, 20, 580, 20, 580, 580, 20, 580, 20, 20)  # 地图坐标
    pw1 = (20, 20, 580, 20, 580, 580, 20, 580, 20, 80, 80, 80, 80, 490, 490, 490, 490, 80, 20, 80)
    pw2 = (110, 110, 200, 110, 200, 230, 110, 230)
    pw3 = (230, 110, 340, 110, 340, 230, 230, 230)
    pw4 = (370, 110, 460, 110, 460, 230, 370, 230)
    pw5 = (110, 260, 340, 260, 340, 340, 110, 340)
    pw6 = (370, 260, 460, 260, 460, 340, 370, 340)
    pw7 = (110, 370, 340, 370, 340, 460, 110, 460)
    pw8 = (370, 370, 460, 370, 460, 460, 370, 460)

    w1_1 = bg1.create_polygon(pw1, outline="", fill="LightSkyBlue")  # 画地图
    w1_2 = bg1.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w1_3 = bg1.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w1_4 = bg1.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w1_5 = bg1.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w1_6 = bg1.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w1_7 = bg1.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w1_8 = bg1.create_polygon(pw8, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    a1 = bg1.create_image(97, 97, image=pic, anchor=CENTER)

    dem = PhotoImage(file="demon.gif")  # 怪物
    a10 = bg1.create_image(355,324, image=dem,anchor=CENTER)
    a11 = bg1.create_image(475,474, image=dem,anchor=CENTER)
    a12 = bg1.create_image(475,95, image=dem,anchor=CENTER)
    a13 = bg1.create_image(95,474, image=dem,anchor=CENTER)

    Label(win1, text="LEVEL 1", fg='black', font="Times -30 bold",
          bg='LightSkyBlue').place(x=500, y=50, anchor=CENTER)
    #表示关卡数的标签

    for i in range(14):  # 将地图铺满豆豆
        for j in range(14):
            bij = (90 + i * 29, 90 + j * 29, 100 + i * 29, 100 + j * 29)
            #豆豆的坐标（每隔29个像素，铺一个豆豆，铺满地图）
            bi_j = bg1.create_oval(bij, outline="pink", fill="pink")#豆豆的形状：圆形 以及 颜色

    bigbean1=bg1.create_oval(346,232,366,252,outline='GreenYellow',fill='GreenYellow') # 放置两个大豆子
    bigbean2=bg1.create_oval(230,467,250,487,outline='GreenYellow',fill='GreenYellow')

    bean=list(bg1.find_overlapping(0, 0, 600, 600))
    bean1=bean[0:len(bean)]   #生成大豆豆

    deleteBeans("map1.txt",bg1,1)   #删除与墙重叠的豆豆

    global c
    global d
    global a
    global b

    c,d=1,0
    x0,y0=-1,0
    x1,y1 = -1,0
    x2,y2 = -1,0
    x3,y3 = -1,0

    while True:
        bg1.bind_all('<KeyPress-Up>', movetriangle)   #绑定键盘与吃豆人移动的关系
        bg1.bind_all('<KeyPress-Down>', movetriangle)
        bg1.bind_all('<KeyPress-Left>', movetriangle)
        bg1.bind_all('<KeyPress-Right>', movetriangle)

        zhqEater(c, d,a1,1,bg1)   #在第L关中检验吃豆人是否撞墙并移动

        eat(bg1,a1,1,bean1,win1)   #游戏进行，吃豆子&碰怪物
        
        zhq(a10,x0,y0,1,bg1)   #四个怪物的随机移动
        x0,y0=zhuan(a10,x0,y0,1,bg1)
        zhq(a11,x1,y1,1,bg1)
        x1,y1=zhuan(a11,x1,y1,1,bg1)
        zhq(a12,x2,y2,1,bg1)
        x2,y2=zhuan(a12,x2,y2,1,bg1)
        zhq(a13,x3,y3,1,bg1)
        x3,y3=zhuan(a13,x3,y3,1,bg1)
        bg1.update()         
            
        sleep(0.001)

        if life == 0 :   #Game Over
            askFail = Toplevel(height=200, width=400)
            askFail.resizable(0,0)

            askCanvas = Canvas(askFail, width=198, height=171, bg="white")
            askCanvas.grid(row=9)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFail, text="   失败！", font="Times -24 bold", bg="white",
                      fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFail, text="重头开始？", font="Times -20 bold", bg="white",
                      fg="black").grid(row=10, rowspan=2, sticky=W + E)
            backButton = Button(askFail, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=rebackLevel1).grid(row=12)
            win1.destroy()


        global ask
        itemsBesidesBeans=[13,20,20,17,30]   #墙块、吃豆人和怪物的总数
        final=list(bg1.find_overlapping(0,0,600,600))
        if final[-1] == itemsBesidesBeans[0] :   #豆豆已经被吃完了
            ask = Toplevel(height=200, width=400)
            ask.resizable(0,0)
            askCanvas2 = Canvas(ask, width=178, height=179, bg="white")
            askCanvas2.grid(row=9)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(ask, text="   通关！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(ask, text="继续下一关？", font="Times -20 bold", bg="white",
                  fg="black").grid(row=10, rowspan=2, sticky=W + E)
            continueButton = Button(ask, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=continueLevel2).grid(row=12)
            win1.destroy()

def paintCanvas2():#LEVEL2   #注释同第一关
    global askFail2
    global score,life
    life = 3
    score = 0
    win2 = Toplevel()
    win2.resizable(0,0)

    bg2 = Canvas(win2, width=600, height=600, bg="white")  # 画布
    bg2.pack()
    global a2


    p2 = (20, 0, 20, 20, 580, 20, 580, 0)
    pw1 = (20, 20, 50, 20, 50, 550, 550, 550, 550, 20, 580, 20, 580, 580, 20, 580)
    pw2 = (80, 50, 430, 50, 430, 80, 80, 80)
    pw3 = (460, 50, 520, 50, 520, 310, 490, 310, 490, 80, 460, 80)
    pw4 = (490, 340, 520, 340, 520, 520, 430, 520, 430, 490, 490, 490)
    pw5 = (80, 490, 400, 490, 400, 520, 80, 520)
    pw6 = (80, 230, 110, 230, 110, 460, 80, 460)
    pw7 = (80, 110, 310, 110, 310, 140, 110, 140, 110, 200, 80, 200)
    pw8 = (340, 110, 460, 110, 460, 230, 430, 230, 430, 140, 340, 140)
    pw9 = (430, 260, 460, 260, 460, 460, 340, 460, 340, 430, 430, 430)
    pw10 = (140, 290, 170, 290, 170, 430, 310, 430, 310, 460, 140, 460)
    pw11 = (140, 170, 400, 170, 400, 400, 370, 400, 370, 200, 170, 200, 170, 260, 140, 260)
    pw12 = (200, 230, 340, 230, 340, 260, 200, 260)
    pw13 = (260, 290, 340, 290, 340, 340, 260, 340)
    pw14 = (200, 290, 230, 290, 230, 370, 340, 370, 340, 400, 200, 400)

    ol2 = bg2.create_polygon(p2, outline='', fill="LightSkyBlue")
    w2_1 = bg2.create_polygon(pw1, outline="", fill="LightSkyBlue")
    w2_2 = bg2.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w2_3 = bg2.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w2_4 = bg2.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w2_5 = bg2.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w2_6 = bg2.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w2_7 = bg2.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w2_8 = bg2.create_polygon(pw8, outline="", fill="LightSkyBlue")
    w2_9 = bg2.create_polygon(pw9, outline="", fill="LightSkyBlue")
    w2_10 = bg2.create_polygon(pw10, outline="", fill="LightSkyBlue")
    w2_11 = bg2.create_polygon(pw11, outline="", fill="LightSkyBlue")
    w2_12 = bg2.create_polygon(pw12, outline="", fill="LightSkyBlue")
    w2_13 = bg2.create_polygon(pw13, outline="", fill="LightSkyBlue")
    w2_14 = bg2.create_polygon(pw14, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    a2 = bg2.create_image(97, 97, image=pic, anchor=CENTER)

    dem = PhotoImage(file="demon.gif")  # 怪物
    a20 = bg2.create_image(415,300, image=dem,anchor=CENTER)
    a21 = bg2.create_image(95,535 ,image=dem,anchor=CENTER)
    a22 = bg2.create_image(535,534, image=dem,anchor=CENTER)
    a23 = bg2.create_image(535,95, image=dem,anchor=CENTER)

    Label(win2, text="LEVEL 2", fg='black', font="Times -20 bold",
          bg='LightSkyBlue').place(x=130, y=65, anchor=CENTER)

    for i in range(18):   #将地图铺满豆豆
        for j in range(18):
            bij = (32 + i * 29, 32 + j * 29, 42 + i * 29, 42 + j * 29)
            bi_j = bg2.create_oval(bij, outline="pink", fill="pink")

    bigbean1=bg2.create_oval(346,232,366,252,outline='GreenYellow',fill='GreenYellow') # 放置两个大豆子
    bigbean2=bg2.create_oval(230,467,250,487,outline='GreenYellow',fill='GreenYellow')

    bean=list(bg2.find_overlapping(0, 0, 600, 600))
    bean2=bean[0:len(bean)]


    deleteBeans("map2.txt",bg2,2)

    global c
    global d

    x0_,y0_=-1,0
    c,d=1,0
    x1_,y1_ = -1,0
    x2_,y2_ = -1,0
    x3_,y3_ = -1,0

    while True:
        bg2.bind_all('<KeyPress-Up>',movetriangle)
        bg2.bind_all('<KeyPress-Down>',movetriangle)
        bg2.bind_all('<KeyPress-Left>',movetriangle)
        bg2.bind_all('<KeyPress-Right>',movetriangle)

        zhqEater(c,d,a2,2,bg2)

        eat(bg2,a2,2,bean2,win2)

        zhq(a20,x0_,y0_,2,bg2)
        x0_,y0_=zhuan(a20,x0_,y0_,2,bg2)
        zhq(a21,x1_,y1_,2,bg2)
        x1_,y1_=zhuan(a21,x1_,y1_,2,bg2)
        zhq(a22,x2_,y2_,2,bg2)
        x2_,y2_=zhuan(a22,x2_,y2_,2,bg2)
        zhq(a23,x3_,y3_,2,bg2)
        x3_,y3_=zhuan(a23,x3_,y3_,2,bg2)
        bg2.update()         
            
        sleep(0.001)

        if life == 0 :   #Game Over
            askFail2 = Toplevel(height=200, width=400)
            askFail2.resizable(0,0)
            askCanvas = Canvas(askFail2, width=198, height=171, bg="white")
            askCanvas.grid(row=9)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFail2, text="   失败！", font="Times -24 bold", bg="white",
                      fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFail2, text="重头开始？", font="Times -20 bold", bg="white",
                      fg="black").grid(row=10, rowspan=2, sticky=W + E)
            backButton = Button(askFail2, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=rebackLevel2).grid(row=12)
            win2.destroy()

        global ask2
        itemsBesidesBeans=[13,20,20,17,30]
        final=list(bg2.find_overlapping(0,0,600,600))
        if final[-1] == itemsBesidesBeans[1] :
            ask2 = Toplevel(height=200, width=400)
            ask2.resizable(0,0)
            askCanvas2 = Canvas(ask2, width=178, height=179, bg="white")
            askCanvas2.grid(row=9)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(ask2, text="   通关！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(ask2, text="继续下一关？", font="Times -20 bold", bg="white",
                  fg="black").grid(row=10, rowspan=2, sticky=W + E)
            continueButton = Button(ask2, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=continueLevel3).grid(row=12)
            win2.destroy()

def paintCanvas3():#LEVEL3   #注释同第一关
    global askFail3
    global win3
    global bg3
    global score,life
    life = 3
    score = 0
    win3 = Toplevel()
    win3.resizable(0,0)

    bg3 = Canvas(win3, width=600, height=600, bg="white")  # 画布
    bg3.pack()
    global a3

    p31 = (0, 0, 0, 600, 600, 600, 600, 0, 580, 0, 580, 580, 20, 580, 20, 0)
    p32 = (20, 0, 20, 20, 580, 20, 580, 0)
    pw1 = (50, 50, 370, 50, 370, 80, 310, 80, 310, 140, 230, 140, 230, 80, 50, 80)
    pw2 = (400, 50, 550, 50, 550, 80, 430, 80, 430, 140, 340, 140, 340, 110, 400, 110)
    pw3 = (20, 110, 200, 110, 200, 140, 20, 140)
    pw4 = (460, 110, 550, 110, 550, 200, 290, 200, 290, 170, 460, 170)
    pw5 = (50, 170, 260, 170, 260, 260, 50, 260)
    pw6 = (290, 230, 490, 230, 490, 310, 400, 310, 400, 370, 370, 370, 370, 260, 290, 260)
    pw7 = (520, 230, 580, 230, 580, 490, 520, 490, 520, 430, 490, 430, 490, 400, 520, 400)
    pw8 = (20, 290, 340, 290, 340, 370, 260, 370, 260, 430, 170, 430, 170, 400, 230, 400, 230, 310, 20, 310)
    pw9 = (50, 340, 200, 340, 200, 370, 140, 370, 140, 430, 50, 430)
    pw10 = (430, 340, 490, 340, 490, 370, 460, 370, 460, 460, 490, 460, 490, 520, 550, 520,
            550, 550, 400, 550, 400, 490, 370, 490, 370, 400, 430, 400)
    pw11 = (290, 400, 340, 400, 340, 490, 310, 490, 310, 550, 230, 550, 230, 460, 290, 460)
    pw12 = (50, 460, 200, 460, 200, 550, 50, 550)
    pw13 = (340, 520, 370, 520, 370, 580, 340, 580)

    w3_14 = bg3.create_polygon(p31, fill="LightSkyBlue")
    w3_15 = bg3.create_polygon(p32, fill="LightSkyBlue")
    w3_1 = bg3.create_polygon(pw1, outline="", fill="LightSkyBlue")
    w3_2 = bg3.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w3_3 = bg3.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w3_4 = bg3.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w3_5 = bg3.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w3_6 = bg3.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w3_7 = bg3.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w3_8 = bg3.create_polygon(pw8, outline="", fill="LightSkyBlue")
    w3_9 = bg3.create_polygon(pw9, outline="", fill="LightSkyBlue")
    w3_10 = bg3.create_polygon(pw10, outline="", fill="LightSkyBlue")
    w3_11 = bg3.create_polygon(pw11, outline="", fill="LightSkyBlue")
    w3_12 = bg3.create_polygon(pw12, outline="", fill="LightSkyBlue")
    w3_13 = bg3.create_polygon(pw13, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    a3 = bg3.create_image(97, 97, image=pic, anchor=CENTER)

    dem = PhotoImage(file="demon.gif")  # 怪物
    a30 = bg3.create_image(355,300, image=dem,anchor=CENTER)
    a31 = bg3.create_image(95,565, image=dem,anchor=CENTER)
    a32 = bg3.create_image(565,565, image=dem,anchor=CENTER)
    a33 = bg3.create_image(565,95, image=dem,anchor=CENTER)

    Label(win3, text="LEVEL 3", fg='black', font="Times -30 bold",
          bg='LightSkyBlue').place(x=152, y=212, anchor=CENTER)

    for i in range(19):
        for j in range(19):
            bij = (32 + i * 29, 32 + j * 29, 42 + i * 29, 42 + j * 29)
            bi_j = bg3.create_oval(bij, outline="pink", fill="pink")
            
    bigbean1=bg3.create_oval(205,435,225,455,outline='GreenYellow',fill='GreenYellow') # 放置两个大豆子
    bigbean2=bg3.create_oval(490,205,510,225,outline='GreenYellow',fill='GreenYellow')

    bean=list(bg3.find_overlapping(0, 0, 600, 600))
    bean3=bean[0:len(bean)]

    deleteBeans("map3.txt",bg3,3)

    global c
    global d

    x0__,y0__=-1,0
    c,d=1,0
    x1__,y1__= -1,0
    x2__,y2__= -1,0
    x3__,y3__ = -1,0

    while True:
        bg3.bind_all('<KeyPress-Up>', movetriangle)
        bg3.bind_all('<KeyPress-Down>', movetriangle)
        bg3.bind_all('<KeyPress-Left>', movetriangle)
        bg3.bind_all('<KeyPress-Right>', movetriangle)

        zhqEater(c,d,a3,3,bg3)

        eat(bg3,a3,3,bean3,win3)

        zhq(a30,x0__,y0__,3,bg3)
        x0__,y0__=zhuan(a30,x0__,y0__,3,bg3)
        zhq(a31,x1__,y1__,3,bg3)
        x1__,y1__=zhuan(a31,x1__,y1__,3,bg3)
        zhq(a32,x2__,y2__,3,bg3)
        x2__,y2__=zhuan(a32,x2__,y2__,3,bg3)
        zhq(a33,x3__,y3__,3,bg3)
        x3__,y3__=zhuan(a33,x3__,y3__,3,bg3)
        bg3.update()         
            
        sleep(0.001)

        if life == 0 :   #Game Over
            askFail3 = Toplevel(height=200, width=400)
            askFail3.resizable(0,0)
            askCanvas = Canvas(askFail3, width=198, height=171, bg="white")
            askCanvas.grid(row=9)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFail3, text="   失败！", font="Times -24 bold", bg="white",
                      fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFail3, text="重头开始？", font="Times -20 bold", bg="white",
                      fg="black").grid(row=10, rowspan=2, sticky=W + E)
            backButton = Button(askFail3, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=rebackLevel3).grid(row=12)
            win3.destroy()

        global ask3
        itemsBesidesBeans=[13,20,20,17,30]
        final=list(bg3.find_overlapping(0,0,600,600))
        if final[-1] == itemsBesidesBeans[2] :
            ask3 = Toplevel(height=200, width=400)
            ask3.resizable(0,0)
            askCanvas2 = Canvas(ask3, width=178, height=179, bg="white")
            askCanvas2.grid(row=9)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(ask3, text="   通关！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(ask3, text="继续下一关？", font="Times -20 bold", bg="white",
                  fg="black").grid(row=10, rowspan=2, sticky=W + E)
            continueButton = Button(ask3, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=continueLevel4).grid(row=12)
            win3.destroy()
    
def paintCanvas4(): #LEVEL4   #注释同第一关
    global askFail4
    global win4
    global bg4
    global score,life
    life = 3
    score = 0
    win4 = Toplevel()
    win4.resizable(0,0)

    bg4 = Canvas(win4, width=600, height=600, bg="white")  # 画布
    bg4.pack()
    global a4

    p41 = (0, 0, 0, 600, 600, 600, 600, 0, 580, 0, 580, 580, 20, 580, 20, 0)
    p42 = (20, 0, 20, 20, 580, 20, 580, 0)
    pw1 = (20, 20, 580, 20, 580, 310, 550, 310, 550, 430, 520, 430, 520, 230, 430, 230,
           430, 310, 370, 310, 370, 200, 340, 200, 340, 170, 310, 170, 310, 230, 340, 230,
           340, 310, 290, 310, 290, 140, 400, 140, 400, 200, 520, 200, 520, 50, 50, 50, 50, 460,
           110, 460, 110, 550, 370, 550, 370, 580, 20, 580)
    pw2 = (80, 80, 170, 80, 170, 110, 110, 110, 110, 140, 200, 140, 200, 80, 260, 80, 260, 310,
           200, 310, 200, 170, 80, 170)
    pw3 = (290, 80, 490, 80, 490, 170, 430, 170, 430, 110, 290, 110)
    pw4 = (80, 200, 170, 200, 170, 310, 80, 310)
    pw5 = (460, 260, 490, 260, 490, 430, 290, 430, 290, 340, 460, 340)
    pw6 = (80, 340, 170, 340, 170, 460, 370, 460, 370, 520, 140, 520, 140, 430, 80, 430)
    pw7 = (200, 340, 260, 340, 260, 430, 200, 430)
    pw8 = (400, 460, 460, 460, 460, 490, 430, 490, 430, 520, 460, 520, 460, 550, 400, 550)
    pw9 = (490, 460, 550, 460, 550, 520, 490, 520)
    pw10 = (490, 550, 580, 550, 580, 580, 490, 580)

    o41 = bg4.create_polygon(p41, fill="LightSkyBlue")
    o42 = bg4.create_polygon(p42, fill="LightSkyBlue")
    w4_1 = bg4.create_polygon(pw1, outline="", fill="LightSkyBlue")
    w4_2 = bg4.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w4_3 = bg4.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w4_4 = bg4.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w4_5 = bg4.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w4_6 = bg4.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w4_7 = bg4.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w4_8 = bg4.create_polygon(pw8, outline="", fill="LightSkyBlue")
    w4_9 = bg4.create_polygon(pw9, outline="", fill="LightSkyBlue")
    w4_10 = bg4.create_polygon(pw10, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    a4 = bg4.create_image(68, 68, image=pic, anchor=CENTER)

    dem = PhotoImage(file="demon.gif")  # 怪物
    a40 = bg4.create_image(275,300,image=dem,anchor=CENTER)
    a41 = bg4.create_image(565,534, image=dem,anchor=CENTER)
    a42 = bg4.create_image(505,100, image=dem,anchor=CENTER)
    a43 = bg4.create_image(130,535, image=dem,anchor=CENTER)

    Label(win4, text="LEVEL 4", fg='black', font="Times -30 bold",
          bg='LightSkyBlue').place(x=120, y=27, anchor=CENTER)

    for i in range(19):
        for j in range(19):
            bij = (32 + i * 29, 32 + j * 29, 42 + i * 29, 42 + j * 29)
            bi_j = bg4.create_oval(bij, outline="pink", fill="pink")

    bigbean1=bg4.create_oval(465,520,485,540,outline='GreenYellow',fill='GreenYellow') # 放置两个大豆子
    bigbean2=bg4.create_oval(345,205,365,225,outline='GreenYellow',fill='GreenYellow')

    bean=list(bg4.find_overlapping(0, 0, 600, 600))
    bean4=bean[0:len(bean)]

    deleteBeans("map4.txt",bg4,4)

    global c
    global d

    x0___,y0___=-1,0
    c,d=1,0
    x1___,y1___= -1,0
    x2___,y2___= -1,0
    x3___,y3___= -1,0

    while True:
        bg4.bind_all('<KeyPress-Up>', movetriangle)
        bg4.bind_all('<KeyPress-Down>', movetriangle)
        bg4.bind_all('<KeyPress-Left>', movetriangle)
        bg4.bind_all('<KeyPress-Right>', movetriangle)

        zhqEater(c, d,a4,4,bg4)

        eat(bg4,a4,4,bean4,win4)
        
        zhq(a40,x0___,y0___,4,bg4)
        x0___,y0___=zhuan(a40,x0___,y0___,4,bg4)
        zhq(a41,x1___,y1___,4,bg4)
        x1___,y1___=zhuan(a41,x1___,y1___,4,bg4)
        zhq(a42,x2___,y2___,4,bg4)
        x2___,y2___=zhuan(a42,x2___,y2___,4,bg4)
        zhq(a43,x3___,y3___,4,bg4)
        x3___,y3___=zhuan(a43,x3___,y3___,4,bg4)
        bg4.update()         
            
        sleep(0.001)

        if life == 0 :   #Game Over
            askFail4 = Toplevel(height=200, width=400)
            askFail4.resizable(0,0)
            askCanvas = Canvas(askFail4, width=198, height=171, bg="white")
            askCanvas.grid(row=9)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFail4, text="   失败！", font="Times -24 bold", bg="white",
                      fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFail4, text="重头开始？", font="Times -20 bold", bg="white",
                      fg="black").grid(row=10, rowspan=2, sticky=W + E)
            backButton = Button(askFail4, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=rebackLevel4).grid(row=12)
            win4.destroy()

        global ask4
        itemsBesidesBeans=[13,20,20,17,30]
        final=list(bg4.find_overlapping(0,0,600,600))
        if final[-1] == itemsBesidesBeans[3] :
            ask4 = Toplevel(height=200, width=400)
            ask4.resizable(0,0)
            askCanvas2 = Canvas(ask4, width=178, height=179, bg="white")
            askCanvas2.grid(row=9)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(ask4, text="   通关！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(ask4, text="继续下一关？", font="Times -20 bold", bg="white",
                  fg="black").grid(row=10, rowspan=2, sticky=W + E)
            continueButton = Button(ask4, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=continueLevel5).grid(row=12)
            win4.destroy()
    
def paintCanvas5(): #LEVEL5   #注释同第一关
    global askFail5
    global win5
    global bg5
    global score,life
    life = 3
    score = 0
    win5 = Toplevel()
    win5.resizable(0,0)

    bg5 = Canvas(win5, width=600, height=600, bg="white")  # 画布
    bg5.pack()
    global a5

    p51 = (0, 0, 0, 600, 600, 600, 600, 0, 580, 0, 580, 580, 20, 580, 20, 0)
    p52 = (20, 0, 20, 20, 580, 20, 580, 0)
    pw1 = (230, 20, 260, 20, 260, 80, 200, 80, 200, 110, 260, 110, 260, 170, 230, 170,
           230, 140, 170, 140, 170, 50, 230, 50)
    pw2 = (400, 20, 460, 20, 460, 50, 430, 50, 430, 140, 340, 140, 340, 110, 400, 110)
    pw3 = (490, 20, 580, 20, 580, 50, 490, 50)
    pw4 = (50, 50, 140, 50, 140, 140, 110, 140, 110, 80, 50, 80)
    pw5 = (290, 50, 370, 50, 370, 80, 310, 80, 310, 260, 290, 260, 290, 230, 260, 230,
           260, 260, 230, 260, 230, 200, 290, 200)
    pw6 = (460, 80, 490, 80, 490, 140, 460, 140)
    pw7 = (520, 80, 550, 80, 550, 200, 340, 200, 340, 170, 520, 170)
    pw8 = (20, 110, 80, 110, 80, 140, 20, 140)
    pw9 = (50, 170, 80, 170, 80, 230, 200, 230, 200, 340, 260, 340, 260, 370, 170, 370,
           170, 260, 140, 260, 140, 370, 50, 370, 50, 340, 110, 340, 110, 260, 50, 260)
    pw10 = (110, 170, 200, 170, 200, 200, 110, 200)
    pw11 = (520, 230, 580, 230, 580, 260, 520, 260)
    pw12 = (340, 230, 490, 230, 490, 260, 400, 260, 400, 370, 310, 370, 310, 430, 140, 430,
            140, 550, 110, 550, 110, 400, 290, 400, 290, 340, 370, 340, 370, 260, 340, 260)
    pw13 = (20, 290, 80, 290, 80, 310, 20, 310)
    pw14 = (230, 290, 340, 290, 340, 310, 230, 310)
    pw15 = (430, 290, 550, 290, 550, 370, 520, 370, 520, 310, 430, 310)
    pw16 = (430, 340, 490, 340, 490, 370, 460, 370, 460, 430, 370, 430, 370, 460, 430, 460,
            430, 550, 400, 550, 400, 490, 310, 490, 310, 550, 290, 550, 290, 460, 340, 460,
            340, 400, 430, 400)
    pw17 = (20, 400, 80, 400, 80, 430, 20, 430)
    pw18 = (490, 400, 550, 400, 550, 490, 520, 490, 520, 430, 490, 430)
    pw19 = (50, 460, 80, 460, 80, 550, 50, 550)
    pw20 = (170, 460, 200, 460, 200, 580, 170, 580)
    pw21 = (230, 460, 260, 460, 260, 550, 230, 550)
    pw22 = (460, 460, 490, 460, 490, 520, 550, 520, 550, 550, 460, 550)
    pw23 = (340, 520, 370, 520, 370, 580, 340, 580)

    w5_24 = bg5.create_polygon(p51, fill="LightSkyBlue")
    w5_25 = bg5.create_polygon(p52, fill="LightSkyBlue")
    w5_1 = bg5.create_polygon(pw1, outline="", fill="LightSkyBlue")
    w5_2 = bg5.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w5_3 = bg5.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w5_4 = bg5.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w5_5 = bg5.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w5_6 = bg5.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w5_7 = bg5.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w5_8 = bg5.create_polygon(pw8, outline="", fill="LightSkyBlue")
    w5_9 = bg5.create_polygon(pw9, outline="", fill="LightSkyBlue")
    w5_10 = bg5.create_polygon(pw10, outline="", fill="LightSkyBlue")
    w5_11 = bg5.create_polygon(pw11, outline="", fill="LightSkyBlue")
    w5_12 = bg5.create_polygon(pw12, outline="", fill="LightSkyBlue")
    w5_13 = bg5.create_polygon(pw13, outline="", fill="LightSkyBlue")
    w5_14 = bg5.create_polygon(pw14, outline="", fill="LightSkyBlue")
    w5_15 = bg5.create_polygon(pw15, outline="", fill="LightSkyBlue")
    w5_16 = bg5.create_polygon(pw16, outline="", fill="LightSkyBlue")
    w5_17 = bg5.create_polygon(pw17, outline="", fill="LightSkyBlue")
    w5_18 = bg5.create_polygon(pw18, outline="", fill="LightSkyBlue")
    w5_19 = bg5.create_polygon(pw19, outline="", fill="LightSkyBlue")
    w5_20 = bg5.create_polygon(pw20, outline="", fill="LightSkyBlue")
    w5_21 = bg5.create_polygon(pw21, outline="", fill="LightSkyBlue")
    w5_22 = bg5.create_polygon(pw22, outline="", fill="LightSkyBlue")
    w5_23 = bg5.create_polygon(pw23, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    a5 = bg5.create_image(97, 97, image=pic, anchor=CENTER)

    dem = PhotoImage(file="demon.gif")  # 怪物
    a50 = bg5.create_image(215,300, image=dem,anchor=CENTER)
    a51 = bg5.create_image(95,565, image=dem,anchor=CENTER)
    a52 = bg5.create_image(565,565, image=dem,anchor=CENTER)
    a53 = bg5.create_image(565,100, image=dem,anchor=CENTER)

    Label(win5, text="LEVEL 5", fg='black', font="Times -20 bold",
          bg='LightSkyBlue').place(x=95, y=65, anchor=CENTER)

    for i in range(19):  # 铺豆豆
        for j in range(19):
            bij = (32 + i * 29, 32 + j * 29, 42 + i * 29, 42 + j * 29)
            bi_j = bg5.create_oval(bij, outline="pink", fill="pink")

    bigbean1=bg5.create_oval(145,290,165,310,outline='GreenYellow',fill='GreenYellow') # 放置两个大豆子
    bigbean2=bg5.create_oval(405,290,425,310,outline='GreenYellow',fill='GreenYellow')

    bean=list(bg5.find_overlapping(0, 0, 600, 600))
    bean5=bean[0:len(bean)]

    deleteBeans("map5.txt",bg5,5)

    global c
    global d

    x0____,y0____=-1,0
    c,d=1,0
    x1____,y1____ = -1,0
    x2____,y2____ = -1,0
    x3____,y3____ = -1,0

    while True:
        bg5.bind_all('<KeyPress-Up>', movetriangle)
        bg5.bind_all('<KeyPress-Down>', movetriangle)
        bg5.bind_all('<KeyPress-Left>', movetriangle)
        bg5.bind_all('<KeyPress-Right>', movetriangle)

        zhqEater(c, d,a5,5,bg5)

        eat(bg5,a5,5,bean5,win5)

        zhq(a50,x0____,y0____,5,bg5)
        x0____,y0____=zhuan(a50,x0____,y0____,5,bg5)
        zhq(a51,x1____,y1____,5,bg5)
        x1____,y1____=zhuan(a51,x1____,y1____,5,bg5)
        zhq(a52,x2____,y2____,5,bg5)
        x2____,y2____=zhuan(a52,x2____,y2____,5,bg5)
        zhq(a53,x3____,y3____,5,bg5)
        x3____,y3____=zhuan(a53,x3____,y3____,5,bg5)
        bg5.update()         
            
        sleep(0.001)

        if life == 0 :   #Game Over
            askFail5 = Toplevel(height=200, width=400)
            askFail5.resizable(0,0)
            askCanvas = Canvas(askFail5, width=198, height=171, bg="white")
            askCanvas.grid(row=9)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFail5, text="   失败！", font="Times -24 bold", bg="white",
                      fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFail5, text="重头开始？", font="Times -20 bold", bg="white",
                      fg="black").grid(row=10, rowspan=2, sticky=W + E)
            backButton = Button(askFail5, text="ok", font="Times -20 bold", bg="black",
                                    fg="white", command=rebackLevel5).grid(row=12)
            win5.destroy()

        global ask5
        itemsBesidesBeans=[13,20,20,17,30]
        final=list(bg5.find_overlapping(0,0,600,600))
        if final[-1] == itemsBesidesBeans[4] :
            ask5 = Toplevel(height=200, width=400)
            ask5.resizable(0,0)
            askCanvas2 = Canvas(ask5, width=178, height=179, bg="white")
            askCanvas2.grid(row=9)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(ask5, text="恭喜通关了本游戏！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W+E)
            Label(ask5, text="豆豆吃的好饱啊……", font="Times -20 bold", bg="white",
                  fg="black").grid(row=10, rowspan=2, sticky=W+E)
            quitButton5 = Button(ask5, text="byebye", font="Times -20 bold", bg="black",
                                 fg="white", command=rootwin.quit).grid(row=12)
            win5.destroy()

def Level_1(): #第一关
    global select
    select.destroy()
    paintCanvas1()

def Level_2(): #第二关
    global select
    select.destroy()
    paintCanvas2()

def Level_3(): #第三关
    global select
    select.destroy()
    paintCanvas3()

def Level_4(): #第四关
    global select
    select.destroy()
    paintCanvas4()

def Level_5(): #第五关
    global select
    select.destroy()
    paintCanvas5()

def start(): #由此函数进入第一关
    paintCanvas1()

def Invincible():  # 第一关无敌版   #注释同第一关
    winI = Toplevel()
    winI.resizable(0,0)
    global cvI

    cvI = Canvas(winI, width=600, height=600, bg="white")  # 创建画布
    cvI.pack()

    global aI
    
    global askI
    global askFailI

    p1 = (20, 20, 580, 20, 580, 580, 20, 580, 20, 20)  # 地图坐标
    pw1 = (20, 20, 580, 20, 580, 580, 20, 580, 20, 80, 80, 80, 80, 490, 490, 490, 490, 80, 20, 80)
    pw2 = (110, 110, 200, 110, 200, 230, 110, 230)
    pw3 = (230, 110, 340, 110, 340, 230, 230, 230)
    pw4 = (370, 110, 460, 110, 460, 230, 370, 230)
    pw5 = (110, 260, 340, 260, 340, 340, 110, 340)
    pw6 = (370, 260, 460, 260, 460, 340, 370, 340)
    pw7 = (110, 370, 340, 370, 340, 460, 110, 460)
    pw8 = (370, 370, 460, 370, 460, 460, 370, 460)

    w1_1 = cvI.create_polygon(pw1, outline="", fill="LightSkyBlue")  # 画地图，墙
    w1_2 = cvI.create_polygon(pw2, outline="", fill="LightSkyBlue")
    w1_3 = cvI.create_polygon(pw3, outline="", fill="LightSkyBlue")
    w1_4 = cvI.create_polygon(pw4, outline="", fill="LightSkyBlue")
    w1_5 = cvI.create_polygon(pw5, outline="", fill="LightSkyBlue")
    w1_6 = cvI.create_polygon(pw6, outline="", fill="LightSkyBlue")
    w1_7 = cvI.create_polygon(pw7, outline="", fill="LightSkyBlue")
    w1_8 = cvI.create_polygon(pw8, outline="", fill="LightSkyBlue")

    pic = PhotoImage(file="eater.gif")  # 吃豆人
    aI = cvI.create_image(97, 97, image=pic, anchor=CENTER)  # 引入吃豆人的初始坐标

    dem1 = PhotoImage(file="demon.gif")  # 引入怪物的图片
    a20 = cvI.create_image(355, 324, image=dem1, anchor=CENTER)  # 放置怪物的初始位置
    a21 = cvI.create_image(475, 474, image=dem1, anchor=CENTER)  # 放置怪物的初始位置
    a22 = cvI.create_image(475, 95, image=dem1, anchor=CENTER)  # 放置怪物的初始位置
    a23 = cvI.create_image(95, 474, image=dem1, anchor=CENTER)  # 放置怪物的初始位置

    Label(winI, text="无敌挑战版！！", fg='black', font="Times -30 bold",
          bg='LightSkyBlue').place(x=450, y=50, anchor=CENTER)

    for i in range(14):  # 将地图铺满豆豆
        for j in range(14):
            bij = (90 + i * 29, 90 + j * 29, 100 + i * 29, 100 + j * 29)  # 豆豆的坐标（每隔29个像素，铺一个豆豆，铺满地图）
            bi_j = cvI.create_oval(bij, outline="pink", fill="pink")  # 豆豆的形状：圆形 以及 颜色

    deleteBeans("map1.txt",cvI,6)

    global c
    global d
    global aII
    global bI

    x0, y0 = -1, 0
    c, d = 1, 0
    x1, y1 = -1, 0
    x2, y2 = -1, 0
    x3, y3 = -1, 0

    score = 1500000   #倒计
    Label(winI, text="Your lives: +∞", fg='black', font="Times -15 bold",
          bg='LightSkyBlue').place(x=300, y=600, anchor=S)
    
    while True:
        cvI.bind_all('<KeyPress-Up>', movetriangle)  # 绑定键盘的上下左右键
        cvI.bind_all('<KeyPress-Down>', movetriangle)
        cvI.bind_all('<KeyPress-Left>', movetriangle)
        cvI.bind_all('<KeyPress-Right>', movetriangle)

        zhqEater(c,d,aI,6,cvI)
        cvI.update()
        xya1 = list(cvI.coords(aI))  # 报告吃豆人的中心坐标,存储形式：xya1=[x1,y1,x2,y2]
        xya = list(cvI.find_overlapping(xya1[0] - 10, xya1[1] - 10, xya1[0] + 10, xya1[
            1] + 10))  # 吃豆人的大小是20*20，所以(xya1[0]-10,xya1[1]-10,xya1[0]+10,xya1[1]+10)得到的是吃豆人矩形 用find_overlapping找出与吃豆人矩形范围内重叠的其他图形（豆豆）的标识号，存到列表中

        for n in xya:  # 删掉xya中的图形项（豆豆），表示被吃掉了
            if n > 13:
                cvI.delete(n)
            elif n > 9:
                sleep(0.5)
                cvI.move(aI, 97 - xya1[0], 97 - xya1[1])
                xyn = list(cvI.coords(n))
                cvI.move(n, 475 - xyn[0], 474 - xyn[1])
                score -= 20000

        sleep(0.0002)
        score -= 1

        zhq(a20, x0, y0,6,cvI)
        x0, y0 = zhuan(a20, x0, y0,6,cvI)
        zhq(a21, x1, y1,6,cvI)
        x1, y1 = zhuan(a21, x1, y1,6,cvI)
        zhq(a22, x2, y2,6,cvI)
        x2, y2 = zhuan(a22, x2, y2,6,cvI)
        zhq(a23, x3, y3,6,cvI)
        x3, y3 = zhuan(a23, x3, y3,6,cvI)
        cvI.update()

        final = list(cvI.find_overlapping(0, 0, 600, 600))
        if final[-1] == 13:
            askI = Toplevel(height=200, width=400)
            askI.resizable(0,0)
            askCanvas2 = Canvas(askI, width=178, height=179, bg="white")
            askCanvas2.grid(row=12)
            winwin = PhotoImage(file="winwinwin.gif")
            winPicture = askCanvas2.create_image(89, 89, image=winwin, anchor=CENTER)
            Label(askI, text="Your HP: %d" % (score), fg="black", font="Times -20 bold",
                  bg="white").grid(row=3, rowspan=2, sticky=W + E)
            Label(askI, text="恭喜通关了无敌（鬼畜）版！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            secret = "嗯……\n通关了无敌版的你应该发现了：\n这个无敌版是有限制的！\n" \
                     "在最开始你有1,500,000HP的，\n但是随着时间增加，它是慢慢减少的；\n" \
                     "并且如果怪物吃了你，\n你的HP会减少20,000！\n\n" \
                     "……所以如果你输过了的话，\n你应该知道你是怎么输的了吧\n"
            Label(askI, text=secret, font="Times -20 bold", bg="white",
                  fg="black").grid(row=13, sticky=W + E)
            Label(askI, text="hhh,游戏愉快！", font="Times -20 bold", bg="white",
                  fg="black").grid(row=21, rowspan=2, sticky=W + E)
            quitButtonI = Button(askI, text="byebye", font="Times -20 bold", bg="black",
                                 fg="white", command=destroyI).grid(row=23)
            winI.destroy()

        if score <= 0:
            askFailI = Toplevel(height=200, width=400)
            askFailI.resizable(0,0)
            askCanvas = Canvas(askFailI, width=198, height=171, bg="white")
            askCanvas.grid(row=12)
            fail = PhotoImage(file="hahaha.gif")
            failing = askCanvas.create_image(99, 85, image=fail, anchor=CENTER)
            Label(askFailI, text="Your HP: %d" % (score), fg="black", font="Times -20 bold",
                  bg="white").grid(row=3, rowspan=2, sticky=W + E)
            Label(askFailI, text="   失败！", font="Times -24 bold", bg="white",
                  fg="black").grid(row=1, rowspan=2, sticky=W + E)
            Label(askFailI, text="重头开始？", font="Times -20 bold", bg="white",
                  fg="black").grid(row=13, rowspan=2, sticky=W + E)
            backButton = Button(askFailI, text="ok", font="Times -20 bold", bg="black",
                                fg="white", command=rebackI).grid(row=15)
            winI.destroy()

def SelectLevel(): #选择关卡，有对应关卡的按钮
    global select
    select = Toplevel()
    select.resizable(0,0)
    bgr3 = Canvas(select, width=600, height=800, bg="white")
    bgr3.pack()

    pe1 = (40, 36, 114, 110)
    pee1 = (75, 57, 79, 61)
    eater1 = bgr3.create_arc(pe1, start=45, extent=270, fill="black")
    eatereye1 = bgr3.create_oval(pee1, fill="white")

    pe2 = (600 - 114, 800 - 110, 600 - 40, 800 - 36)
    pee2 = (600 - 79, 800 - 61, 600 - 75, 800 - 57)
    eater2 = bgr3.create_arc(pe2, start=225, extent=270, fill="black")
    eatereye2 = bgr3.create_oval(pee2, fill="white")

    adornment1 = bgr3.create_rectangle(40, 110, 50, 720, outline="", fill="black")
    adornment2 = bgr3.create_rectangle(80, 754, 464, 764, outline="", fill="black")
    adornment3 = bgr3.create_rectangle(600 - 50, 800 - 720, 600 - 40,
                                     800 - 110, outline="", fill="black")
    adornment4 = bgr3.create_rectangle(600 - 464, 800 - 764, 600 - 80,
                                     800 - 754, outline="", fill="black")
    adornment5 = bgr3.create_oval(600 - 51, 800 - 764, 600 - 40,
                                800 - 753, outline="", fill="black")
    adornment6 = bgr3.create_oval(40, 753, 51, 764, outline="", fill="black")

    selecttitle = Label(select, text="关卡选择", font="Times -25 bold",
                        bg="black", fg="white").place(x=170, y=110, anchor=CENTER)
    Button_1 = Button(select, text="关卡1", font="Times -20 bold", bg="black",
                      fg="white", command=Level_1).place(x=170, y=240, anchor=CENTER)
    Button_2 = Button(select, text="关卡2", font="Times -20 bold", bg="black",
                      fg="white", command=Level_2).place(x=170, y=340, anchor=CENTER)
    Button_3 = Button(select, text="关卡3", font="Times -20 bold", bg="black",
                      fg="white", command=Level_3).place(x=170, y=440, anchor=CENTER)
    Button_4 = Button(select, text="关卡4", font="Times -20 bold", bg="black",
                      fg="white", command=Level_4).place(x=170, y=540, anchor=CENTER)
    Button_5 = Button(select, text="关卡5", font="Times -20 bold", bg="black",
                      fg="white", command=Level_5).place(x=170, y=640, anchor=CENTER)
    Button_I = Button(select, text="无敌版", font="Times -20 bold", bg="black",
                      fg="white", command=Invincible).place(x=430, y=240, anchor=CENTER)

def Destroy1():#用于退出帮助界面的命令函数
    global rootwin1
    rootwin1.destroy()

def Help(): #帮助界面
    global rootwin1
    rootwin1 = Toplevel()
    rootwin1.resizable(0,0)
    bgr1 = Canvas(rootwin1, width=600, height=800, bg="white")
    bgr1.pack()

    pe1 = (40, 36, 114, 110)
    pee1 = (75, 57, 79, 61)
    eater1 = bgr1.create_arc(pe1, start=45, extent=270, fill="black")
    eatereye1 = bgr1.create_oval(pee1, fill="white")

    pe2 = (600 - 114, 800 - 110, 600 - 40, 800 - 36)
    pee2 = (600 - 79, 800 - 61, 600 - 75, 800 - 57)
    eater2 = bgr1.create_arc(pe2, start=225, extent=270, fill="black")
    eatereye2 = bgr1.create_oval(pee2, fill="white")

    adornment1 = bgr1.create_rectangle(40, 110, 50, 720, outline="", fill="black")
    adornment2 = bgr1.create_rectangle(80, 754, 464, 764, outline="", fill="black")
    adornment3 = bgr1.create_rectangle(600 - 50, 800 - 720, 600 - 40,
                                     800 - 110, outline="", fill="black")
    adornment4 = bgr1.create_rectangle(600 - 464, 800 - 764, 600 - 80,
                                     800 - 754, outline="", fill="black")
    adornment5 = bgr1.create_oval(600 - 51, 800 - 764, 600 - 40,
                                800 - 753, outline="", fill="black")
    adornment6 = bgr1.create_oval(40, 753, 51, 764, outline="", fill="black")

    title_H = "游戏帮助"
    helpstitle = Label(rootwin1, text=title_H, font="Times -25 bold",
                    bg="black", fg="white").place(x=170, y=110, anchor=CENTER)
    helptext = "利用键盘方向键控制吃豆人的移动方向，避开怪物，把地图上的所有豆豆吃掉过关！\n\n" \
               "普通豆豆（小豆子）：吃掉一颗分数增加10点\n奖励豆豆（大豆子）：吃掉一颗分数增加50点，" \
               "并且增加一条生命\n怪物：怪物会随机运动，一旦碰到怪物会失去一条生命" \
               "\n\n游戏共有5关，在每一关你有初始的三条生命，" \
               "生命全部失去后会GAME OVER\n\n\n\n" \
               "Ps: 其实有一个无敌版，操作方法是没有变化的，但是……" \
               "具体是什么情况呢请慢慢探索(◍ ´꒳` ◍)"
    helps = Message(rootwin1,text=helptext,font="Times -20 bold",
                    bg="white",fg="black",width=460).place(x=300,y=400,anchor=CENTER)
    ExitButton1 = Button(rootwin1, text="exit", font="Times -20 bold", bg="black",
                        fg="white", command=Destroy1).place(x=437, y=700, anchor=CENTER)

def Destroy2():#用于退出制作人员界面的命令函数
    global rootwin2
    rootwin2.destroy()

def Staff(): #制作人员界面
    global rootwin2
    rootwin2 = Toplevel()
    rootwin2.resizable(0,0)
    bgr2 = Canvas(rootwin2, width=600, height=800, bg="white")
    bgr2.pack()

    pe1 = (40, 36, 114, 110)
    pee1 = (75, 57, 79, 61)
    eater1 = bgr2.create_arc(pe1, start=45, extent=270, fill="black")
    eatereye1 = bgr2.create_oval(pee1, fill="white")

    pe2 = (600 - 114, 800 - 110, 600 - 40, 800 - 36)
    pee2 = (600 - 79, 800 - 61, 600 - 75, 800 - 57)
    eater2 = bgr2.create_arc(pe2, start=225, extent=270, fill="black")
    eatereye2 = bgr2.create_oval(pee2, fill="white")

    adornment1 = bgr2.create_rectangle(40, 110, 50, 720, outline="", fill="black")
    adornment2 = bgr2.create_rectangle(80, 754, 464, 764, outline="", fill="black")
    adornment3 = bgr2.create_rectangle(600 - 50, 800 - 720, 600 - 40,
                                      800 - 110, outline="", fill="black")
    adornment4 = bgr2.create_rectangle(600 - 464, 800 - 764, 600 - 80,
                                      800 - 754, outline="", fill="black")
    adornment5 = bgr2.create_oval(600 - 51, 800 - 764, 600 - 40,
                                 800 - 753, outline="", fill="black")
    adornment6 = bgr2.create_oval(40, 753, 51, 764, outline="", fill="black")

    title_S = "制作人员"
    StaffTitle = Label(rootwin2, text=title_S, font="Times -25 bold",
                        bg="black", fg="white").place(x=170, y=110, anchor=CENTER)
    stafflist = "组长:\n\n方焯\n\n\n组员:\n\n乔蕴昭\n\n王梦瑶\n\n李    珊"
    Stafflist = Message(rootwin2, text=stafflist, font="Times -20 bold",
                        bg="white", fg="black",width=460).place(x=170,y=300,anchor=CENTER)
    ExitButton2 = Button(rootwin2, text="exit", font="Times -20 bold", bg="black",
                        fg="white", command=Destroy2).place(x=437, y=700, anchor=CENTER)

#以下为菜单界面及对应按钮
rootwin = Tk()
rootwin.resizable(0,0)
rootwin.title("PAC-MAN")
rootwin.geometry("600x800")

bg = Canvas(rootwin,width=600,height=800,bg="white")
bg.pack()

pe1 = (40, 36, 114, 110)
pee1 = (75, 57, 79, 61)
eater1 = bg.create_arc(pe1, start=45, extent=270, fill="black")
eatereye1 = bg.create_oval(pee1, fill="white")

pe2 = (600 - 114, 800 - 110, 600 - 40, 800 - 36)
pee2 = (600 - 79, 800 - 61, 600 - 75, 800 - 57)
eater2 = bg.create_arc(pe2, start=225, extent=270, fill="black")
eatereye2 = bg.create_oval(pee2, fill="white")

adornment1 = bg.create_rectangle(40, 110, 50, 720, outline="", fill="black")
adornment2 = bg.create_rectangle(80, 754, 464, 764, outline="", fill="black")
adornment3 = bg.create_rectangle(600-50, 800-720, 600-40, 800-110, outline="", fill="black")
adornment4 = bg.create_rectangle(600-464, 800-764, 600-80, 800-754, outline="", fill="black")
adornment5 = bg.create_rectangle(365, 240, 479, 245, outline="", fill="black")
adornment6 = bg.create_rectangle(365, 240+17, 479, 245+17, outline="", fill="black")
adornment7 = bg.create_oval(600-51, 800-764, 600-40, 800-753, outline="", fill="black")
adornment8 = bg.create_oval(40, 753, 51, 764, outline="", fill="black")

#上述部分是界面装饰部分

#下面三行是主标题
TitleFrame = Frame(rootwin,width=320,height=80)
TitleFrame.place(x=300,y=175,anchor=CENTER)
Title = Label(TitleFrame,text="Pac - Man", font="Times -80 bold", bg="black",
              fg="white").grid(sticky=E+W+N+S)

#接下来是按钮
ButtonFrame = Frame(rootwin,width=320,height=410)
ButtonFrame.place(x=300,y=510,anchor=CENTER)
#开始按钮，对应函数start()
StartButton = Button(ButtonFrame,text="Start New Game",font="Times -30 bold",bg="black",
                     fg="white",command=start).grid(row=0,rowspan=2,sticky=W+E)
#跳关按钮，对应函数SelectLevel()
SelectButton = Button(ButtonFrame,text="Select Level",font="Times -30 bold",bg="black",
                      fg="white",command=SelectLevel).grid(row=4,rowspan=2,sticky=W+E)
#帮助按钮，对应函数Help()
HelpButton = Button(ButtonFrame,text="Game Help",font="Times -30 bold",bg="black",
                    fg="white",command=Help).grid(row=8,rowspan=2,sticky=W+E)
#制作组按钮，对应函数Staff()
StaffButton = Button(ButtonFrame,text="Staff List",font="Times -30 bold",bg="black",
                     fg="white",command=Staff).grid(row=12,rowspan=2,sticky=W+E)
#退出按钮，根窗口主循环退出
ExitButton = Button(rootwin,text="exit",font="Times -20 bold",bg="black",
                    fg="white",command=rootwin.quit).place(x=437,y=700,anchor=CENTER)

rootwin.mainloop() #进入主循环
