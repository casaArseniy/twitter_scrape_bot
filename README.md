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
- Create credentials.py file with variables:
```python
ID = "Twitter ID"
PASSWORD = "Twitter Password"
```
## Screenshots
- Main Menu
  
![main_menu screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/main_menu.png)

- Adding a target, saves the target to target_data.csv file. Add a name for the target and a valid HTML link to their profile. Input error checks are not implemented so you'll have to be careful when inputting links to not break the program.

  
![add_target screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/add_target.png)

- You can either target all targets (using the checkmark) on the list or select a single target from the list.
  
![start screenshot](https://github.com/casaArseniy/twitter_scrape_bot/blob/main/readme_images/start.png)

## Testing
TBD

