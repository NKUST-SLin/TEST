# import tkinter
import tkinter as tk


class Timer:

    def __init__(self, parent):
        # variable storing time
        self.Ssec=0
        self.Smin=0
        self.Shour=0
        self.time_go = 0  #0 is stop 1 is go
        self.seconds = 00
        self.minute = 00
        self.hour = 9123123123
        # label displaying time
        self.label = tk.Label(parent, text="09:00:00 ", font="Arial 30", width=10)
        self.label.pack()
        # start the timer
        self.label.after(1000, self.refresh_label)

    def start(self):
        self.time_go = 1
        self.label.after(1000, self.refresh_label)
        print("1\n")
    def stop(self):
        self.time_go = 0
        print("0\n")

    def StopIn(self,Ssec,Smin,Shour):
        self.Ssec=Ssec
        self.Smin=Smin
        self.Shour=Shour

    def StopCheck(self):
        if self.Ssec == self.seconds:
            if self.Smin == self.minute:
                if self.Shour == self.hour:
                    self.time_go = 0

    def SetTime(self,seconds,minute,hour):
        self.seconds = self.seconds
        self.minute = self.minute
        self.hour = self.hour
        self.label.configure(text="%02i:%02i:%02i" % (self.hour ,self.minute ,self.seconds))

    def refresh_label(self):
        """ refresh the content of the label every second """
        if self.time_go == 0:
            self.time_go=0
        # increment the time
        if self.time_go == 1:
            self.seconds += 1
        # display the new time
            if self.seconds==60:
                self.minute+=1
                self.seconds = 00
            if self.minute==60:
                self.hour+= 1
                self.minute= 00
           # print("Time going...") ForTest
            self.label.configure(text="%02i:%02i:%02i" % (self.hour ,self.minute ,self.seconds))
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        
            self.label.after(500, self.refresh_label)


if __name__ == "__main__":
    rot = tk.Tk()
    timer = Timer(rot)
   # timer.start()
    if timer.seconds == 3:
        timer.stop()
        print("%02i\n" % timer.seconds)
    rot.mainloop()