# twitter_scrape_bot

## Overview

This Python application is designed to scrape posts from X (Twitter) without using the official API. The project was done in response to a client's need to have a repository of comment tweets that instigated a single reply or a conversation from the original poster (e.g.: @Bob posts a tweet. @John posts a comment. @Bob replies to the comment). It provides a simple interface to target specific accounts. Target posts and people's replies are scrapped, labeled, and saved. The scraped data can be used for various purposes such as sentiment analysis, trend analysis, or data visualization.

## Prerequisites
- Python 3.10.12
- See requirements.txt

## Installation
- Clone repository
- Install requirements
```
    pip install -r requirements.txt
```
- Create resources/credentials.py file with variables:
```python
ID = "Your Twitter ID"
PASSWORD = "Your Twitter Password"
```
## Screenshots
- Main Menu
  
![main_menu screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/main_menu.png)

- You can either target all targets (using the checkmark) on the list or select a single target from the list.

  
![add_target screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/add_target.png)

- Adding a target, saves the target to target_data.csv file. Add a name for the target and a valid HTML link to their profile. Input error checks are not implemented so you'll have to be careful when inputting links to not break the program.
    
![start screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/start_v2.png)

- Select the date until which you want to scrape data from the target.

## Data
- Tweet data is saved in the **data** folder.
- **TARGET_NAME_posts.csv** : contains target tweets (e.g.: @Bob posts a tweet).
- **TARGET_NAME_comments.csv** : contains comments to target tweets by others (e.g.: @John posts a comment).
- Files contain the following rows: ['Page Source URL', 'Name Tag', 'Post Date', 'Message', 'Num. of Replies', 'Post URL', 'Extraction Date', 'Label']
  
#### Labels: 
- -1: N/A or no replies
- 0: No replies from target to comment
- 1: Single reply from target to comment
- 2: Multiple replies from target to comment (conversation).

## Docker (Under Development)

```
sudo docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd)/app:/app --rm difficult_x_scrapper
```

## Testing
With unittest.

