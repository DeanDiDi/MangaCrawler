# http://effbot.org/tkinterbook/tkinter-index.htm - An Introduction To Tkinter
from tkinter import *
from functions import *
import os


def start_crawl(event):
    name = mangaNameEntry.get()
    url = urlEntry.get()
    chapters = get_chapters(url)      # a dictionary contains "title : url" pairs
    chapter_index = 1
    max_chapter = int(chaptersEntry.get())

    while chapter_index <= max_chapter and chapter_index <= len(chapters):
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
        print(title + " finished.")


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
crawlButton.grid(row=3, columnspan=2)
crawlButton.bind("<Button-1>", start_crawl)

root.mainloop()
