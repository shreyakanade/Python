global f
f=0
def t_movie():
    f=f+1
    print("Which movie do you want")
    print("1, movie 1")
    print("2, movie 2")
    print("3, movie 3")
    print("4, movie 4")
    print("5, movie 5")
    print("4, back")
    movie= int (input("Choose your movie:"))
    if movie == 4:
        center()
        theater()
        return 0
    if f == 1:
        theater()
        # this theater function used to select screen 
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    
    a = int(input("Choose your Screen: "))
    ticket = int(input("Number of ticket do you want?: "))
    timing(a)
 
# this timing function used to select timing for movie 
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "3.00-6.00",
        "3": "8.00-11.00",
        "4": "12.00-3.00"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.30-4.30",
        "3": "4.45-7.45",
        "4": "7.55-10.55"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.45-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successful!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successful!, enjoy movie at "+x)
    return 0
 
# movie Theater function 
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
 
# center of movie  function
def center():
    print("Which theater do you wish to see movie? ")
    print("1,Inox")
    print("2,Icon")
    print("3,MVP")
    print("4,RRR")
    a = int(input("Choose your option: "))
    movie(a)
    return 0
 
# this function is used to select city 
def city():
    print("Hi welcome to movie ticket booking: ")
    print("Where you want to watch movie?:")
    print("1,city 1")
    print("2,city 2 ")
    print("3,city 3 ")
    print("4,city 4 ")
    place = int(input("Choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    elif place == 4:
      center() 
    else:
      print("wrong choice")
 
 
city() # it calls the function city 
