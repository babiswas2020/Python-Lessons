import re

string="""The regex Bat(wo)+man will not match the string ‘The Adventures of Batman’ because at least one wo is required by the plus sign.\n
If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.\n
This article is contributed by Shubham Machal. If you like GeeksforGeeks and would like to contribute, you can also write an article using contribute.geeksforgeeks.org or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.\n
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above"""


#^ is begining of the string
#$ is the end of the string

print(re.search('^Please Write\s',string)





