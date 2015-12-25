import os
import requests
from bs4 import BeautifulSoup
import time, datetime

'''
Change the URL
'''

#need to change this
URL= "https://twitter.com/SnShines"

def getPosts(url):
    out_file= open("posts.html", "w")

    r= requests.get(url)
    #print(r.text)
    out_file.write(r.text)
    out_file.close()



def parsePosts(file_name, interest_date):
    posts_file= open(file_name, "r")
    posts_data= posts_file.read()
    posts_file.close()

    entries= []
    flag= True

    #need to use this from URL
    while flag and '<a href="/SnShines/status' in posts_data:
        entry_text= ""
        # need to use this from URL
        posts_data= posts_data[posts_data.index('<a href="/SnShines/status'):]
        soup= BeautifulSoup(posts_data, "html.parser")

        unix_time= (soup.a.span["data-time"])
        post_date= str(datetime.datetime.fromtimestamp(int(unix_time)))

        #print(post_date[:10], interest_date)

        if (post_date[:10])== interest_date:
            entry_text+= post_date[11:]
            entry_text+= " - https://twitter.com"+ soup.a["href"]
            entry_text+= "\n\n"
            entry_text+= str(soup.p)
            entry_text+= "\n<hr>\n"

            entries.append(entry_text)
        else:
            flag= False

        # print(soup.a)
        # print(soup.p)
        # print("\n")


        posts_data= posts_data[1:]

    return entries



def makeDayoneEntry(entries):
    entries= entries[::-1]
    #print(entries)

    entry_text= "".join(entries)
    entry_text= "Today's tweets\n"+ entry_text

    entry_file= open("entries.txt", "w")
    entry_file.write(entry_text)
    entry_file.close()

    outText= "dayone new<entries.txt"
    os.system(outText)



if __name__== "__main__":
    interest_date= (time.strftime("%Y-%m-%d"))

    getPosts(URL)

    entries= parsePosts("posts.html", interest_date)

    makeDayoneEntry(entries)

