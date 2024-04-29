class Post:

    comments = []

    def __init__(self, name_tag, post_date, message, num_replies, url):
        self.name_tag = name_tag
        self.post_date = post_date
        self.message = message
        self.num_replies = num_replies
        self.url = url
        self.label = -1
    
    # def store_comment(self, post)
    #     self.comments.append(post)

    def __str__(self):
        return f"{self.name_tag}, date: {self.post_date} \nmessage: {self.message}\nurl:{self.url}\nreplies: {self.num_replies}\n"