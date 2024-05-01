# from ..gui import *
# from scrapper_classes.post import Post
# from table import *
# from soup import *
# from credentials import ID, PASSWORD
# from scrapper_classes.scrapper import Scrapper 

import sys
sys.path.append(".")
from resources import  *

import unittest

# to test soup.py extensively need to create a test html page 

class TestScrapper(unittest.TestCase):
    def test_Soup_functionality(self):
        posts_OP = get_OP_soup()
        post_COMMENTER = get_COMMENTER_soup()
        self.assertTrue(posts_OP) 
        self.assertTrue(post_COMMENTER) 
    
    def test_Table_functionality(self):
        test_OP_Post_1 = Post("@OPname1", "April 1st", "Joking OP test1", 2, "http://OPtest1.com")
        test_OP_Post_2 = Post("@OPname2", "April 2nd", "Joking OP test2", 3, "http://OPtest2.com")

        test_COMMENTER_Post_1 = Post("@Cname1", "1hr", "OP 1 Commenter test 1", 0, "http://OP1COMtest1.com")
        test_COMMENTER_Post_2 = Post("@Cname2", "March 1st", "OP 1 Commenter test 2", 1, "http://OP1COMtest2.com")
        test_COMMENTER_Post_3 = Post("@Cname3", "2hr", "OP 2 Commenter test 1", 3, "http://OP2COMtest1.com")
        test_COMMENTER_Post_4 = Post("@Cname4", "1min", "OP 2 Commenter test 2", 4, "http://OP2COMtest2.com")
        test_COMMENTER_Post_5 = Post("@Cname5", "10min", "OP 2 Commenter test 3", 5, "http://OP2COMtest3.com")

        s = Scrapper()

        s.df_OP = insert_post_into_Table(s.df_OP, "OP_post1.com",test_OP_Post_1)
        s.df_OP = insert_post_into_Table(s.df_OP, "OP_post2.com",test_OP_Post_2)

        s.df_COMM = insert_post_into_Table(s.df_COMM, test_OP_Post_1.url,test_COMMENTER_Post_1)
        s.df_COMM = insert_post_into_Table(s.df_COMM, test_OP_Post_1.url,test_COMMENTER_Post_2)
        s.df_COMM = insert_post_into_Table(s.df_COMM, test_OP_Post_2.url,test_COMMENTER_Post_3)
        s.df_COMM = insert_post_into_Table(s.df_COMM, test_OP_Post_2.url,test_COMMENTER_Post_4)
        s.df_COMM = insert_post_into_Table(s.df_COMM, test_OP_Post_2.url,test_COMMENTER_Post_5)

        self.assertFalse(s.df_OP.empty) 
        self.assertFalse(s.df_COMM.empty)

        s.clear_data() 

if __name__ == '__main__':
    unittest.main()



















# Workable Unit Case
# test_OP_Post_1 = Post("@OPname1", "April 1st", "Joking OP test1", 2, "http://OPtest1.com")
# test_OP_Post_2 = Post("@OPname2", "April 2nd", "Joking OP test2", 3, "http://OPtest2.com")

# test_COMMENTER_Post_1 = Post("@Cname1", "1hr", "OP 1 Commenter test 1", 0, "http://OP1COMtest1.com")
# test_COMMENTER_Post_2 = Post("@Cname2", "March 1st", "OP 1 Commenter test 2", 1, "http://OP1COMtest2.com")
# test_COMMENTER_Post_3 = Post("@Cname3", "2hr", "OP 2 Commenter test 1", 3, "http://OP2COMtest1.com")
# test_COMMENTER_Post_4 = Post("@Cname4", "1min", "OP 2 Commenter test 2", 4, "http://OP2COMtest2.com")
# test_COMMENTER_Post_5 = Post("@Cname5", "10min", "OP 2 Commenter test 3", 5, "http://OP2COMtest3.com")

# OP_POSTS = [test_OP_Post_1, test_OP_Post_2]
# COMMENTER_POSTS = [[test_COMMENTER_Post_1, test_COMMENTER_Post_2], [test_COMMENTER_Post_3, test_COMMENTER_Post_4, test_COMMENTER_Post_5]]


# # Table Test
# df_OP_Posts = create_Table()
# df_COMMENT_Posts = create_Table()

# df_OP_Posts = insert_post_into_Table(df_OP_Posts, "OP_post1.com",test_OP_Post_1)
# df_OP_Posts = insert_post_into_Table(df_OP_Posts, "OP_post2.com",test_OP_Post_2)

# df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_1.url,test_COMMENTER_Post_1)
# df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_1.url,test_COMMENTER_Post_2)
# df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_3)
# df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_4)
# df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_5)

# print(df_OP_Posts.head())
# print(df_COMMENT_Posts.head())

# Scrape test  #<<<<<<<<<<<<----- waiting time test
# HTML scrape test
# GUI test







