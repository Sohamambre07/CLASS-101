import time

seconds = input("enter the time in number or seconds")

def countdowntimer(seconds):
    while seconds>0:
        min=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{min} : {secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("time up")    
    
countdowntimer(int(seconds))    