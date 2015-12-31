#!/bin/bash

import os, sys
import requests
from bs4 import BeautifulSoup
import time, datetime

'''
1. Set the USER_NAME to your twitter handle
'''

#need to change this
USER_NAME= "SnShines"


URL= "https://twitter.com/"+ USER_NAME



def getPosts(url):
    print("Fetching tweets from twitter handle: @"+ USER_NAME)
    r= requests.get(url)

    #print(r.text)
    return r.text



def parsePosts(html_page, interest_date):
    print("Parsing fetched html page to find today's tweets...")
    posts_data= html_page

    entries= []
    flag= True


    find_string= '<a href="/'+ USER_NAME+ '/status'
    while flag and find_string in posts_data:
        entry_text= ""

        posts_data= posts_data[posts_data.index(find_string):]
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
    print("Making DayOne entry...")
    entries= entries[::-1]
    #print(entries)

    entry_text= "".join(entries)
    entry_text= "Today's tweets\n"+ entry_text

    print("goint to try block............")
    try:
        print("1")
        outText= 'echo "%s" | dayone new' % entry_text
        #abc= "dfadfaf"
        #outText= 'echo "%s" | dayone new' % abc
        #outText= 'echo "asdfasdf" | dayone new'
        print("2")
        #print(outText)
        print("3")
        os.system(outText)
        print("wrote the entry")
    except:
        print(sys.exc_info())




if __name__== "__main__":
    # get current date to cross-check with parsed tweets
    interest_date= (time.strftime("%Y-%m-%d"))

    # Fetch tweets from provided twitter handle
    html_page= getPosts(URL)

    # Parse fetched html page
    entries= parsePosts(html_page, interest_date)

    # make dayOne entry if there are enough entries
    if len(entries)>0:
        print("Found %d tweets tweeted on %s (today)" %(len(entries), interest_date))
        # make one DayOne entry with all the parsed html tweets
        makeDayoneEntry(entries)
    else:
        print("You haven't tweeted yet!")

    print("Opening DayOne app as a reminder to make a manual entry...")
    os.system("open -a 'Day One'")
