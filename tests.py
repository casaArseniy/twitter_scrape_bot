from gui import *
from bot_classes import *
from table import *

test_OP_Post_1 = Post("@OPname1", "April 1st", "Joking OP test1", 2, "http://OPtest1.com")
test_OP_Post_2 = Post("@OPname2", "April 2nd", "Joking OP test2", 3, "http://OPtest2.com")
test_COMMENTER_Post_1 = Post("@Cname1", "1hr", "OP 1 Commenter test 1", 0, "http://OP1COMtest1.com")
test_COMMENTER_Post_2 = Post("@Cname2", "March 1st", "OP 1 Commenter test 2", 1, "http://OP1COMtest2.com")
test_COMMENTER_Post_3 = Post("@Cname3", "2hr", "OP 2 Commenter test 1", 3, "http://OP2COMtest1.com")
test_COMMENTER_Post_4 = Post("@Cname4", "1min", "OP 2 Commenter test 2", 4, "http://OP2COMtest2.com")
test_COMMENTER_Post_5 = Post("@Cname5", "10min", "OP 2 Commenter test 3", 5, "http://OP2COMtest3.com")

OP_POSTS = [test_OP_Post_1, test_OP_Post_2]
COMMENTER_POSTS = [[test_COMMENTER_Post_1, test_COMMENTER_Post_2], [test_COMMENTER_Post_3, test_COMMENTER_Post_4, test_COMMENTER_Post_5]]

# print("*******************************************")
# print("**********all_OP posts print test**********")
# print("*******************************************")
# print_OP_posts(OP_POSTS)
# print("*******************************************")
# print("*******************************************")
# print("*******************************************")

# print()
# print("*******************************************")
# print("*********Commenter posts print test********")
# print("*******************************************")
# for i in range(len(OP_POSTS)):
#     print(OP_POSTS[i])
#     print("---------------------------------")
#     print_COMMENTER_posts(COMMENTER_POSTS[i])
#     print("---------------------------------")
# print("*******************************************")
# print("*******************************************")
# print("*******************************************")


# TABLE TEST
df_OP_Posts = create_Table()
df_COMMENT_Posts = create_Table()

df_OP_Posts = insert_post_into_Table(df_OP_Posts, "OP_post1.com",test_OP_Post_1)
df_OP_Posts = insert_post_into_Table(df_OP_Posts, "OP_post2.com",test_OP_Post_2)

df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_1.url,test_COMMENTER_Post_1)
df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_1.url,test_COMMENTER_Post_2)
df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_3)
df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_4)
df_COMMENT_Posts = insert_post_into_Table(df_COMMENT_Posts, test_OP_Post_2.url,test_COMMENTER_Post_5)

print(df_OP_Posts.head())
print(df_COMMENT_Posts.head())







