# http://effbot.org/tkinterbook/tkinter-index.htm - An Introduction To Tkinter
from tkinter import *
from tkinter import ttk
from functions import *
import os
import threading


def handle_click(event):
    def start_crawl():
        name = mangaNameEntry.get()
        url = urlEntry.get()
        chapters = get_chapters(url)      # a dictionary contains "title : url" pairs
        chapter_index = 1
        if int(chaptersEntry.get()) >= len(chapters):
            max_chapter = len(chapters)
        else:
            max_chapter = int(chaptersEntry.get())
        while chapter_index <= max_chapter:
            title, chapter_url = chapters.popitem()
            print("Crawling " + title + "   ...", end='    ')
            title = title.replace(':', '-')      # replace ':' to '-'
            path = name + "\\" + title
            os.makedirs(path)    # using title to make a directory
            image_urls = get_images(chapter_url)
            index = 1
            for image_url in image_urls:
                download_file(image_url, path + '\\' + str(index) + '.jpg')  # postfix jpg
                index += 1
            chapter_index += 1
            progress.step(100/max_chapter)
            print(title + " finished.")
    t = threading.Thread(target=start_crawl)
    t.start()


root = Tk(className=" Manga Crawler")

Label(root, text="Manga Name:").grid(row=0, column=0, sticky=E)
mangaNameEntry = Entry(root, width=50)
mangaNameEntry.grid(row=0, column=1, sticky=W)

Label(root, text="URL:").grid(row=1, column=0, sticky=E)
urlEntry = Entry(root, width=50)
urlEntry.grid(row=1, column=1, sticky=W)

Label(root, text="How Many Chapters:").grid(row=2, column=0, sticky=E)
chaptersEntry = Entry(root, width=50)
chaptersEntry.grid(row=2, column=1, sticky=W)

crawlButton = Button(root, text="Crawl")
crawlButton.grid(row=3, column=0, sticky=E)
crawlButton.bind("<Button-1>", handle_click)

progress = ttk.Progressbar(root, length=200, mode="determinate")
progress.grid(row=3, column=1)

root.mainloop()
