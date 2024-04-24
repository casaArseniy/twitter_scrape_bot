import pandas as pd

def create_Table():
    column_names =['Page Source URL', 'Name Tag', 'Post Date', 'Message', 'Num. of Replies', 'Post URL']
    df = pd.DataFrame(columns=column_names)
    return df

def insert_post_into_Table(df, html, post):
    df.loc[len(df.index)] = [html, post.name_tag, post.post_date, post.message, post.num_replies, post.url]
    return df