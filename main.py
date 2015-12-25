import os
import requests, bs4

def getPosts(url):
    out_file= open("posts.html", "w")

    r= requests.get(url)
    print(r.text)
    out_file.write(r.text)

    #print(r.response_code)


def makeDayoneEntry():
    text= '''<p>akdjfaj adjfk klajdf alsjsf </p>'''
    outText= "echo '"+ text+ "' | dayone new"
    os.system(outText)


if __name__== "__main__":
    URL= "https://twitter.com/SnShines"
    #getPosts(URL)
    #parsePosts()
    #makeDayoneEntry()
