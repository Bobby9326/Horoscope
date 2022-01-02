from tkinter import *
pro = Tk()
pro.title("Hello TK")
pro.iconbitmap("horoscope/crystal.ico")
pro.geometry("500x700+700+100")
pro.config(bg="#7b00c1")
pro.option_add("*Font", "charcoal 16")
bg = PhotoImage(file="horoscope/pro.png")
# label = Label(pro,image=bg)
# label.place(x=0, y=0)
Label(pro, image=bg, borderwidth=0,bg="#7b00c1").pack()
Button(pro,text = "OK",).pack(ipady=550)
textname = Entry(pro, width= 12).place(x = 70,y = 250)
textsname = Entry(pro, width= 12).place(x = 320,y = 250)
bloods = ["AB","A","B","O"]
clicked = StringVar()
clicked.set(bloods[0])
textblood = OptionMenu(pro,clicked,*bloods).place(x = 222,y = 530)
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
clicked1 = StringVar()
clicked1.set(days[0])
textday = OptionMenu(pro,clicked1,*days).place(x = 80,y = 380)    
months = ["January","February","March","April","May","June","July","August","September","October","November","December "]
clicked2 = StringVar()
clicked2.set(months[0])
textmonth = OptionMenu(pro,clicked2,*months).place(x = 210,y = 380)
years = [2020,2021,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1984,1983,1982,1981,1980,1979,1978,1977,1976,1975,1974,1973,1972,1971]
clicked3 = StringVar()
clicked3.set(years[21])
textyear = OptionMenu(pro,clicked3,*years).place(x = 380,y = 380)
Button(pro,text="Ok").place(x=200,y=550)
pro.mainloop()

