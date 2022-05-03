from tkinter import *
import random

gList = []
bList = []

for i in range(36):
    y = i + 1
    gList.append(str(y))
    bList.append(str(y))

def randomSort(L):
    result = []
    while L:
        cabin = []
        for i in range(4):
            x = random.choice(L)
            cabin.append(x)
            L.remove(x)
        result.append(cabin)
    return result

gCabins = randomSort(gList)
bCabins = randomSort(bList)

def compileCabins():    
    girl1.configure(text = gCabins[0][0])
    girl2.configure(text = gCabins[0][1])
    girl3.configure(text = gCabins[0][2])
    girl4.configure(text = gCabins[0][3])
    
    girl5.configure(text = gCabins[1][0])
    girl6.configure(text = gCabins[1][1])
    girl7.configure(text = gCabins[1][2])
    girl8.configure(text = gCabins[1][3])
    
    girl9.configure(text = gCabins[2][0])
    girl10.configure(text = gCabins[2][1])
    girl11.configure(text = gCabins[2][2])
    girl12.configure(text = gCabins[2][3])
    
    girl13.configure(text = gCabins[3][0])
    girl14.configure(text = gCabins[3][1])
    girl15.configure(text = gCabins[3][2])
    girl16.configure(text = gCabins[3][3])
    
    girl17.configure(text = gCabins[4][0])
    girl18.configure(text = gCabins[4][1])
    girl19.configure(text = gCabins[4][2])
    girl20.configure(text = gCabins[4][3])
    
    girl21.configure(text = gCabins[5][0])
    girl22.configure(text = gCabins[5][1])
    girl23.configure(text = gCabins[5][2])
    girl24.configure(text = gCabins[5][3])
    
    girl25.configure(text = gCabins[6][0])
    girl26.configure(text = gCabins[6][1])
    girl27.configure(text = gCabins[6][2])
    girl28.configure(text = gCabins[6][3])
    
    girl29.configure(text = gCabins[7][0])
    girl30.configure(text = gCabins[7][1])
    girl31.configure(text = gCabins[7][2])
    girl32.configure(text = gCabins[7][3])
    
    girl33.configure(text = gCabins[8][0])
    girl34.configure(text = gCabins[8][1])
    girl35.configure(text = gCabins[8][2])
    girl36.configure(text = gCabins[8][3])
    
    boy1.configure(text = bCabins[0][0])
    boy2.configure(text = bCabins[0][1])
    boy3.configure(text = bCabins[0][2])
    boy4.configure(text = bCabins[0][3])
    
    boy5.configure(text = bCabins[1][0])
    boy6.configure(text = bCabins[1][1])
    boy7.configure(text = bCabins[1][2])
    boy8.configure(text = bCabins[1][3])
    
    boy9.configure(text = bCabins[2][0])
    boy10.configure(text = bCabins[2][1])
    boy11.configure(text = bCabins[2][2])
    boy12.configure(text = bCabins[2][3])
    
    boy13.configure(text = bCabins[3][0])
    boy14.configure(text = bCabins[3][1])
    boy15.configure(text = bCabins[3][2])
    boy16.configure(text = bCabins[3][3])
    
    boy17.configure(text = bCabins[4][0])
    boy18.configure(text = bCabins[4][1])
    boy19.configure(text = bCabins[4][2])
    boy20.configure(text = bCabins[4][3])
    
    boy21.configure(text = bCabins[5][0])
    boy22.configure(text = bCabins[5][1])
    boy23.configure(text = bCabins[5][2])
    boy24.configure(text = bCabins[5][3])
    
    boy25.configure(text = bCabins[6][0])
    boy26.configure(text = bCabins[6][1])
    boy27.configure(text = bCabins[6][2])
    boy28.configure(text = bCabins[6][3])
    
    boy29.configure(text = bCabins[7][0])
    boy30.configure(text = bCabins[7][1])
    boy31.configure(text = bCabins[7][2])
    boy32.configure(text = bCabins[7][3])
    
    boy33.configure(text = bCabins[8][0])
    boy34.configure(text = bCabins[8][1])
    boy35.configure(text = bCabins[8][2])
    boy36.configure(text = bCabins[8][3])

def master():
    global girl1
    global girl2
    global girl3
    global girl4
    global girl5
    global girl6
    global girl7
    global girl8
    global girl9
    global girl10
    global girl11
    global girl12
    global girl13
    global girl14
    global girl15
    global girl16
    global girl17
    global girl18
    global girl19
    global girl20
    global girl21
    global girl22
    global girl23
    global girl24
    global girl25
    global girl26
    global girl27
    global girl28
    global girl29
    global girl30
    global girl31
    global girl32
    global girl33
    global girl34
    global girl35
    global girl36
    global boy1
    global boy2
    global boy3
    global boy4
    global boy5
    global boy6
    global boy7
    global boy8
    global boy9
    global boy10
    global boy11
    global boy12
    global boy13
    global boy14
    global boy15
    global boy16
    global boy17
    global boy18
    global boy19
    global boy20
    global boy21
    global boy22
    global boy23
    global boy24
    global boy25
    global boy26
    global boy27
    global boy28
    global boy29
    global boy30
    global boy31
    global boy32
    global boy33
    global boy34
    global boy35
    global boy36
    
    root = Tk()
    root.title('Sort Campers')
    
    heading = Button(root, text = "Randomly Sort Campers", font = ("Verdana", 20), padx = 20, pady = 30, command = compileCabins)
    heading.pack()
    
    girls = LabelFrame(root, text = "Girls", padx = 5, pady = 5)
    girls.pack(side = LEFT, padx = 10, pady = 10)
    
    boys = LabelFrame(root, text = "Boys", padx = 5, pady = 5)
    boys.pack(side = LEFT, padx = 10, pady = 10)
    
    #Girls Frame Inputs
    Cabin1 = LabelFrame(girls, text = "Cabin 1")
    girl1 = Label(Cabin1, text = "", font = "Verdana")
    girl2 = Label(Cabin1, text = "", font = "Verdana")
    girl3 = Label(Cabin1, text = "", font = "Verdana")
    girl4 = Label(Cabin1, text = "", font = "Verdana")
    
    Cabin2 = LabelFrame(girls, text = "Cabin 2")
    girl5 = Label(Cabin2, text = "", font = "Verdana")
    girl6 = Label(Cabin2, text = "", font = "Verdana")
    girl7 = Label(Cabin2, text = "", font = "Verdana")
    girl8 = Label(Cabin2, text = "", font = "Verdana")
    
    Cabin3 = LabelFrame(girls, text = "Cabin 3")
    girl9 = Label(Cabin3, text = "", font = "Verdana")
    girl10 = Label(Cabin3, text = "", font = "Verdana")
    girl11 = Label(Cabin3, text = "", font = "Verdana")
    girl12 = Label(Cabin3, text = "", font = "Verdana")
    
    Cabin4 = LabelFrame(girls, text = "Cabin 4")
    girl13 = Label(Cabin4, text = "", font = "Verdana")
    girl14 = Label(Cabin4, text = "", font = "Verdana")
    girl15 = Label(Cabin4, text = "", font = "Verdana")
    girl16 = Label(Cabin4, text = "", font = "Verdana")
    
    Cabin5 = LabelFrame(girls, text = "Cabin 5")
    girl17 = Label(Cabin5, text = "", font = "Verdana")
    girl18 = Label(Cabin5, text = "", font = "Verdana")
    girl19 = Label(Cabin5, text = "", font = "Verdana")
    girl20 = Label(Cabin5, text = "", font = "Verdana")
    
    Cabin6 = LabelFrame(girls, text = "Cabin 6")
    girl21 = Label(Cabin6, text = "", font = "Verdana")
    girl22 = Label(Cabin6, text = "", font = "Verdana")
    girl23 = Label(Cabin6, text = "", font = "Verdana")
    girl24 = Label(Cabin6, text = "", font = "Verdana")
    
    Cabin7 = LabelFrame(girls, text = "Cabin 7")
    girl25 = Label(Cabin7, text = "", font = "Verdana")
    girl26 = Label(Cabin7, text = "", font = "Verdana")
    girl27 = Label(Cabin7, text = "", font = "Verdana")
    girl28 = Label(Cabin7, text = "", font = "Verdana")
    
    Cabin8 = LabelFrame(girls, text = "Cabin 8")
    girl29 = Label(Cabin8, text = "", font = "Verdana")
    girl30 = Label(Cabin8, text = "", font = "Verdana")
    girl31 = Label(Cabin8, text = "", font = "Verdana")
    girl32 = Label(Cabin8, text = "", font = "Verdana")
    
    Cabin9 = LabelFrame(girls, text = "Cabin 9")
    girl33 = Label(Cabin9, text = "", font = "Verdana")
    girl34 = Label(Cabin9, text = "", font = "Verdana")
    girl35 = Label(Cabin9, text = "", font = "Verdana")
    girl36 = Label(Cabin9, text = "", font = "Verdana")
    
    #Boys Frame Inputs 
    Cabin10 = LabelFrame(boys, text = "Cabin 10")
    boy1 = Label(Cabin10, text = "", font = "Verdana")
    boy2 = Label(Cabin10, text = "", font = "Verdana")
    boy3 = Label(Cabin10, text = "", font = "Verdana")
    boy4 = Label(Cabin10, text = "", font = "Verdana")
    
    Cabin11 = LabelFrame(boys, text = "Cabin 11")
    boy5 = Label(Cabin11, text = "", font = "Verdana")
    boy6 = Label(Cabin11, text = "", font = "Verdana")
    boy7 = Label(Cabin11, text = "", font = "Verdana")
    boy8 = Label(Cabin11, text = "", font = "Verdana")
    
    Cabin12 = LabelFrame(boys, text = "Cabin 12")
    boy9 = Label(Cabin12, text = "", font = "Verdana")
    boy10 = Label(Cabin12, text = "", font = "Verdana")
    boy11 = Label(Cabin12, text = "", font = "Verdana")
    boy12 = Label(Cabin12, text = "", font = "Verdana")
    
    Cabin13 = LabelFrame(boys, text = "Cabin 13")
    boy13 = Label(Cabin13, text = "", font = "Verdana")
    boy14 = Label(Cabin13, text = "", font = "Verdana")
    boy15 = Label(Cabin13, text = "", font = "Verdana")
    boy16 = Label(Cabin13, text = "", font = "Verdana")
    
    Cabin14 = LabelFrame(boys, text = "Cabin 14")
    boy17 = Label(Cabin14, text = "", font = "Verdana")
    boy18 = Label(Cabin14, text = "", font = "Verdana")
    boy19 = Label(Cabin14, text = "", font = "Verdana")
    boy20 = Label(Cabin14, text = "", font = "Verdana")
    
    Cabin15 = LabelFrame(boys, text = "Cabin 15")
    boy21 = Label(Cabin15, text = "", font = "Verdana")
    boy22 = Label(Cabin15, text = "", font = "Verdana")
    boy23 = Label(Cabin15, text = "", font = "Verdana")
    boy24 = Label(Cabin15, text = "", font = "Verdana")
    
    Cabin16 = LabelFrame(boys, text = "Cabin 16")
    boy25 = Label(Cabin16, text = "", font = "Verdana")
    boy26 = Label(Cabin16, text = "", font = "Verdana")
    boy27 = Label(Cabin16, text = "", font = "Verdana")
    boy28 = Label(Cabin16, text = "", font = "Verdana")
    
    Cabin17 = LabelFrame(boys, text = "Cabin 17")
    boy29 = Label(Cabin17, text = "", font = "Verdana")
    boy30 = Label(Cabin17, text = "", font = "Verdana")
    boy31 = Label(Cabin17, text = "", font = "Verdana")
    boy32 = Label(Cabin17, text = "", font = "Verdana")
    
    Cabin18 = LabelFrame(boys, text = "Cabin 18")
    boy33 = Label(Cabin18, text = "", font = "Verdana")
    boy34 = Label(Cabin18, text = "", font = "Verdana")
    boy35 = Label(Cabin18, text = "", font = "Verdana")
    boy36 = Label(Cabin18, text = "", font = "Verdana")
    
    
    #Display all info
    Cabin1.grid(row = 0, column = 0)
    girl1.pack()
    girl2.pack()
    girl3.pack()
    girl4.pack()
    
    Cabin2.grid(row = 1, column = 0)
    girl5.pack()
    girl6.pack()
    girl7.pack()
    girl8.pack()
    
    Cabin3.grid(row = 2, column = 0)
    girl9.pack()
    girl10.pack()
    girl11.pack()
    girl12.pack()
    
    Cabin4.grid(row = 0, column = 1)
    girl13.pack()
    girl14.pack()
    girl15.pack()
    girl16.pack()
    
    Cabin5.grid(row = 1, column = 1)
    girl17.pack()
    girl18.pack()
    girl19.pack()
    girl20.pack()
    
    Cabin6.grid(row = 2, column = 1)
    girl21.pack()
    girl22.pack()
    girl23.pack()
    girl24.pack()
    
    Cabin7.grid(row = 0, column = 2)
    girl25.pack()
    girl26.pack()
    girl27.pack()
    girl28.pack()
    
    Cabin8.grid(row = 1, column = 2)
    girl29.pack()
    girl30.pack()
    girl31.pack()
    girl32.pack()
    
    Cabin9.grid(row = 2, column = 2)
    girl33.pack()
    girl34.pack()
    girl35.pack()
    girl36.pack()
    
    Cabin10.grid(row = 0, column = 0)
    boy1.pack()
    boy2.pack()
    boy3.pack()
    boy4.pack()
    
    Cabin11.grid(row = 1, column = 0)
    boy5.pack()
    boy6.pack()
    boy7.pack()
    boy8.pack()
    
    Cabin12.grid(row = 2, column = 0)
    boy9.pack()
    boy10.pack()
    boy11.pack()
    boy12.pack()
    
    Cabin13.grid(row = 0, column = 1)
    boy13.pack()
    boy14.pack()
    boy15.pack()
    boy16.pack()
    
    Cabin14.grid(row = 1, column = 1)
    boy17.pack()
    boy18.pack()
    boy19.pack()
    boy20.pack()
    
    Cabin15.grid(row = 2, column = 1)
    boy21.pack()
    boy22.pack()
    boy23.pack()
    boy24.pack()
    
    Cabin16.grid(row = 0, column = 2)
    boy25.pack()
    boy26.pack()
    boy27.pack()
    boy28.pack()
    
    Cabin17.grid(row = 1, column = 2)
    boy29.pack()
    boy30.pack()
    boy31.pack()
    boy32.pack()
    
    Cabin18.grid(row = 2, column = 2)
    boy33.pack()
    boy34.pack()
    boy35.pack()
    boy36.pack() 

    root.mainloop()
    
master()

    
    
    