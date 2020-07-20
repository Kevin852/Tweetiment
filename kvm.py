from tkinter import *
from tkinter import Label
import tkinter
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import sentiment_mod as s
import graphh as g
import barr as b
from PIL import Image, ImageTk

# Here, we are creating our class, Window, and inheriting from the Frame

class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)
        load = Image.open("pic.png")
        load=load.resize((1100,600),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.master = master
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
    

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("TWEETIMENT")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        T=Text(height=2, width=15)
        T.place(x=720,y=100)
        

        def callback():

            def hi():
                print("Byee")
                exit(0)
            win = tk.Toplevel()
            #win.configure(bg='#036CB5')
            lod = Image.open("second.jpg")
            lod=lod.resize((1400,1000),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(lod)
            imag = Label(win, image=render)
            imag.image = render
            imag.place(x=0, y=0)

            menubar = Menu(win)
            menubar.add_command(label="Exit",font = ('Courier', 14), command=hi)
            menubar.add_command(label="Compare",font = ('Courier', 14), command=b.comp)
            menubar.add_command(label="Graph",font = ('Courier', 14), command=g.am)
                
            win.config(menu=menubar)
            
            def tr():

                s = tk.Scrollbar(win)
                T1 = tkinter.Text(win, height=150, width=100, font=("Courier", 14))
                T1.focus_set()
                s.pack(side=tk.RIGHT, fill=tk.Y)
                T1.pack(fill=tk.Y)
                s.config(command=T1.yview)
                T1.config(yscrollcommand=s.set)
                file = open("tweeti.txt")
                data = file.read()
                file.close()
                T1.insert(tk.END,data)
                T1.config(state=DISABLED)
                
                
            ip=T.get("1.0","end-1c") 
            B1 = tkinter.Button(win, text ="Submit", command=tr)
            B1.place(x = 5, y = 5, height=20, width=80)
            ltext = Label(win, text=ip)
            #tkinter.Tk() - TO CREATE NEW WINDOW
            ckey="42at9XEBHtZED548WGDuLymLx"
            csecret="cFkCeXVpxAAnJKtgca8ZnQCBLwZQKQlAmVV0ejvD9ECs9wauKs"
            atoken="725996785559293952-FYFy8coPR9D2oJcLXN3vYz9gRp5sDcy"
            asecret="p9A2fUJVFmIfUTTmku4Otn117agDrJvHK6s6cHywuRLUQ"
            try:
                class listener(StreamListener):
                    def on_data(self, data):
                        all_data = json.loads(data)
                        tweet = all_data["text"]
                        char_list = [tweet[j] for j in range(len(tweet)) if ord(tweet[j]) in range(65536)]
                        tweet=''
                        for j in char_list:
                            tweet=tweet+j
                        sentiment_value, confidence = s.sentiment(tweet)
                       
                        if confidence*100 >= 80:
                            output = open("tweeti.txt","a")
                            op = open("value.txt","a")
                            op.write(sentiment_value)
                            op.write('\n')
        
                            output.write(sentiment_value)
                            output.write('\n')
                            output.write(tweet)
                            output.write('\n\n')
                            output.close()
                            op.close()
                        return(True)
                    def on_error(self, status):
                        print(status)
                auth = OAuthHandler(ckey, csecret)
                auth.set_access_token(atoken, asecret)
                twitterStream = Stream(auth, listener())
                twitterStream.filter(track=[ip])
                
            except:
                return(True)
                
            

        B = tkinter.Button(text ="Submit",command=callback, bg='#66d9ff')
        B.place(x = 850, y = 100, height=40, width=60)

        menu = Menu(self.master)
        self.master.config(menu=menu)




root = Tk()

root.geometry("1100x580")


#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()
