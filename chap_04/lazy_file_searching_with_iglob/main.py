"""
This type of statement would find all the JSON files in the 06 directory
inside the 2015 directory inside the directory where we’re storing all our blog posts.
"""


from glob import iglob

blog_posts = iglob("path/to/blog/posts/2015/06/*.json")
