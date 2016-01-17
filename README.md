# Twitter-to-DayOne

* Script to fetch all your tweets and make a DayOne entry.
* One entry will be created with all the tweets of the day you are running the script.

![Alt text](/preview_2.png?raw=true)

## Usage

* Change the username in `src/main.py` to your username
* Run the script to make a DayOne entry with your tweets on that day
* If you want to run this script daily, modify (if you know what you are doing) and add `src/com.mine.twitter-to-dayone.scheduler.plist` to `~/Library/LaunchAgents`
* My plist runs daily at 23:55 to fetch my tweets and make a DayOne entry and opend DayOne app as a reminder to write it.
