#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


a = 0
def b():
 global a
 a = c(a)
def c(a):
 return a + 2


# In[2]:


b()
b()
b()
a


# Here, we start with a number called a, which is 0.
# 
# Then, we have a function called b() that adds 2 to a.
# 
# We use b() three times in a row.
# 
# Now, if we look at a, it's become 6 because each time we used b(), it added 2 to a.

# # Question 2

# In[3]:


def fileLength(filename):
    try:
        infile = open(filename)
        content = infile.read()
        infile.close()
        return len(content)
    except FileNotFoundError:
        print(f"Oops! The file '{filename}' seems to be missing. Please check the file name and try again.")


# In[4]:


fileLength('Filelength.txt')


# In[5]:


fileLength('idterm.py')


# # Question 3

# SUB QUESTION 1

# In[6]:


class Marsupial:
    def __init__(self):
        self.pouch = []
    
    def carry(self, item):
        self.pouch.append(item)
    
    def contents(self):
        return self.pouch


# In[7]:


k = Marsupial()
k.carry('doll')
k.carry('firetruck')
k.carry('kitten')


# In[8]:


print(k.contents())


# SUB QUESTION 2

# In[9]:


class Marsupial:
    def __init__(self):
        self.pouch = []
    
    def carry(self, item):
        self.pouch.append(item)
    
    def contents(self):
        return self.pouch

class Kangaroo(Marsupial):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
    
    def jump(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


# In[10]:


k = Kangaroo()
k.carry('doll')
k.carry('firetruck')
k.carry('kitten')


# In[11]:


print(k.contents())


# In[12]:


k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)


# In[13]:


print(k)


# # Question 4

# In[14]:


def collatz(x):
    print(x, end=' ')
    if x == 1:
        return
    elif x % 2 == 0:
        collatz(x // 2)
    else:
        collatz(3 * x + 1)


# In[15]:


collatz(1)


# In[16]:


collatz(10)


# # Question 5 

# In[17]:


def binary(n):
    if n == 0:
        print(0, end='')
    elif n == 1:
        print(1, end='')
    else:
        binary(n // 2)
        print(n % 2, end='')


# In[18]:


binary(0)
print()
binary(1)
print()
binary(3)
print()
binary(9)


# # Question 6

# In[19]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.indentation = 0
        self.in_heading = False
    
    def handle_starttag(self, tag, attrs):
        if tag.startswith('h') and tag[1:].isdigit():
            self.indentation = int(tag[1:]) - 1
            self.in_heading = True
    
    def handle_endtag(self, tag):
        if tag.startswith('h'):
            self.indentation = 0
            self.in_heading = False
    
    def handle_data(self, data):
        if self.in_heading:
            print(' ' * self.indentation + data.strip())


# In[20]:


infile = open('w3c.html')
content = infile.read()
infile.close()


# In[21]:


hp = HeadingParser()
hp.feed(content)


# # Question 7

# In[22]:


import requests
from bs4 import BeautifulSoup

def webdir(url, depth, indent=0):
    if depth < 0:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(' ' * indent + url)

    if depth == 0:
        return

    links = soup.find_all('a', href=True)
    for link in links:
        next_url = link['href']
        if next_url.startswith('http'):  # Ensure it's an absolute URL
            webdir(next_url, depth - 1, indent + 1)


# In[23]:


webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)


# # Question 8

# In[24]:


import pandas as pd
import sqlite3


# In[25]:


get_ipython().system('pip install ipython-sql')


# In[26]:


df= pd.DataFrame({'City': ['Mumbai', 'Mumbai','Mumbai','Mumbai','London','London','London','London','Cairo','Cairo','Cairo','Cairo'],
                  'Country': ['India','India','India','India', 'United Kingdom','United Kingdom','United Kingdom','United Kingdom','Egypt','Egypt','Egypt','Egypt'],
                  'Season': ['Winter','Sprng','Summer','Fall','Winter','Spring','Summer','Fall','Winter','Spring','Summer','Fall'],
                  'Temperature(C)': [24.8,28.4,27.9,27.6,4.2,8.3,15.7,10.4,13.6,20.7,27.7,22.2],
                 'Rainfall(mm)': [5.9,16.2,1549.4,346.0,207.7,169.6,157.0,218.5,16.5,6.5,0.1,4.5]})


# In[27]:


df


# In[47]:


cnn = sqlite3.connect('jupyter_sql_tutorial.db')



# In[48]:


df.to_sql('people', cnn)
get_ipython().run_line_magic('load_ext', 'sql')


# In[49]:


get_ipython().run_line_magic('sql', 'sqlite:///jupyter_sql_tutorial.db')


# In[50]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM people\n')


# a)  All the temperature data:

# In[67]:


get_ipython().run_cell_magic('sql', '', '\nSELECT "Temperature(C)"\nFROM people;\n')


# b) All the cities, but without repetition:

# In[60]:


get_ipython().run_cell_magic('sql', '', '\nSELECT DISTINCT City\nFROM people;\n')


# c) All the records for India:

# In[61]:


get_ipython().run_cell_magic('sql', '', "SELECT *\nFROM people\nWHERE Country = 'India';\n")


# d) All the Fall records:

# In[62]:


get_ipython().run_cell_magic('sql', '', "SELECT *\nFROM people\nWHERE Season = 'Fall';\n")


# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters:

# In[63]:


get_ipython().run_cell_magic('sql', '', 'SELECT City, Country, Season\nFROM people\nGROUP BY City, Country, Season\nHAVING AVG("Rainfall(mm)") BETWEEN 200 AND 400;\n')


# f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order:

# In[64]:


get_ipython().run_cell_magic('sql', '', 'SELECT City, Country\nFROM people\nWHERE Season = \'Fall\'\nGROUP BY City, Country\nHAVING AVG("Temperature(C)") > 20\nORDER BY AVG("Temperature(C)") ASC;\n')


# g) The total annual rainfall for Cairo:
# 
# 

# In[65]:


get_ipython().run_cell_magic('sql', '', 'SELECT SUM("Rainfall(mm)")\nFROM people\nWHERE City = \'Cairo\';\n')


# h) The total rainfall for each season:
# 
# 

# In[66]:


get_ipython().run_cell_magic('sql', '', 'SELECT Season, SUM("Rainfall(mm)") AS Total_Rainfall\nFROM people\nGROUP BY Season;\n')


# # Question 9 

# In[77]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over',
'the', 'lazy', 'dog']


# a) Convert all words to uppercase:

# In[78]:


upper_words = [word.upper() for word in words]
upper_words


# b) Leave all words as lowercase:
# 
# 

# In[79]:


lower_words = [word.lower() for word in words]
lower_words


# c) Get the lengths of all words:
# 
# 

# In[80]:


word_lengths = [len(word) for word in words]
word_lengths


# d) Generate a list of lists containing each word in uppercase, lowercase, and its length:
# 
# 

# In[81]:


word_info = [[word.upper(), word.lower(), len(word)] for word in words]
word_info


# e) Filter words with 4 or more characters:
# 
# 

# In[82]:


long_words = [word for word in words if len(word) >= 4]
long_words

