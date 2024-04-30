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
