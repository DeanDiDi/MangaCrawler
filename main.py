from functions import *
import os

if __name__ == "__main__":
    name = input("Please enter the name of the manga: ")
    manga_url = input("Please enter the url: ")
    print("Loading...")
    chapters = get_chapters(manga_url)      # a dictionary contains "title : url" pairs
    chapter_index = 1
    max_chapter = 0
    while max_chapter == 0:
        try:
            max_chapter = int(input("Please enter how many chapters would you like to crawl: "))
        except ValueError:
            print("Please enter valid number!")

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

