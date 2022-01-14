import pandas
from tkinter import *
from LoginPage import *
import requests
from os import *
from time import *
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

root = Tk()
root.title('基于内容推荐的电影推荐系统')
LoginPage(root)
root.mainloop()