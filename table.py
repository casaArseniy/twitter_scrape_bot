import pandas as pd
from datetime import datetime


def create_Table():
    column_names =['Page Source URL', 'Name Tag', 'Post Date', 'Message', 'Num. of Replies', 'Post URL', 'Extraction Date']
    df = pd.DataFrame(columns=column_names)
    return df

def insert_post_into_Table(df, html, post):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    df.loc[len(df.index)] = [html, post.name_tag, post.post_date, post.message, post.num_replies, post.url, dt_string]
    return df