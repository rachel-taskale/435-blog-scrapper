import pandas as pd
import smtplib
from datetime import date


# Function to check
def read_html():
    pd.set_option('display.max_colwidth', None)
    # Use pandas to read in the html file into a list of dataframe objects
    table = pd.read_html('https://seam.cs.umd.edu/purtilo/435/blog.html')
    # Put the data into a pandas table and remove the scoping of the list
    df = table[0]

    # Drop unnecessary table
    df.drop(df.index[0])

    # call the check_if_updated text file method
    blog_idx_to_send = check_if_updated(len(df))
    blog_updates_log = df.iloc[1:(blog_idx_to_send + 1)]

    return blog_updates_log


# function to check if the blog was updated through reading the file
# if blog is updated then will write new table length to the text file
def check_if_updated(length_of_blog_table):
    # get path of the text file
    path = "./tally.txt"
    # read it as an integer and get the current number of blog posts
    fil = open(path, "r")
    tally = int(fil.readline())
    fil.close()
    # if the number of blog posts when we check the website now is greater
    # than the tally we got from the text file then we update the file 
    if length_of_blog_table > tally:
        # open the file with writing priviledges
        fil = open(path, "w")
        # update the file
        fil.write(str(length_of_blog_table))
    # compute the difference in the number of blog posts in case there was more than
    # one update
    diff = length_of_blog_table - tally
    fil.close()
    return diff
