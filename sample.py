#this a project from https://www.youtube.com/watch?v=NI9LXzo0UY0
#this project makes a youtube link downloader and has a bit of ui


import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()  # <-- FIXED

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()

        finishLabel.configure(text="Download complete!")
    except Exception as e:  # <-- Print the actual error message
        finishLabel.configure(text="Download failed")
        print(f"Error: {e}")  # <-- Debugging output


def on_progress(stream, chunk, bytes_remaining):
    total_size= stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded/ total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    progressBar.set(float(percentage_of_completion)/100)

    
#System Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=10, pady=10)

#input Link 
url_var= tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var)
link.pack()

#finish label
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()

#progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

#progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download button 
download = customtkinter.CTkButton(app, text = "Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run the app
app.mainloop()







