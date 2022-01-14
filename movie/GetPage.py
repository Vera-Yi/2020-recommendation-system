from tkinter import *
import requests
import os
import pandas
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class GetFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        self.t = StringVar()
        self.t.set("例:Avatar?")

        f1 = Frame(self)
        f1.pack()

        Label(f1, text='请输入电影：').pack(side='left')
        Entry(f1, textvariable=self.t, width=15).pack(side='left')
        Label(f1, width=1).pack(side='left')
        Button(f1, text='开始寻找推荐的电影', command=self.confirm).pack(side='left')

        self.sh1 = StringVar()
        show1 = Label(self, text='=========', textvariable=self.sh1,fg='#00CCFF')
        show1.pack()



    def confirm(self):
        self.sh1.set("请输入正确的电影名称")
        aid = self.t.get()

        movies = pandas.io.parsers.read_csv('F:/推荐系统/movie_metadata.csv', escapechar='\\', encoding='ISO-8859-1')
        movies.head()  #查看movies的数据
        movies['genres'].head()  #查看label为“genres"的数据

        tfidf = TfidfVectorizer(stop_words='english')  #创建TfidfVectorizer对象
        movies['genres'] = movies['genres'].fillna('')  #用空值来填充缺失数据
        tfidf_matrix = tfidf.fit_transform(movies['genres']) #对genres进行向量化表示，得到TF-IDF权重矩阵，
        tfidf_matrix.shape
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) #用余弦距离来计算两个电影之间的相关性。
        indices = pandas.Series(movies.index, index=movies['movie_title']).drop_duplicates()#创建一个序列索引，序列是电影名字，去掉重复项

        def storageToLocalFiles(storagePath, data):
            fhandle = open(storagePath, "wb")
            fhandle.write(data)
            fhandle.close()

        def get_recommendation(title, consine_sim=cosine_sim):
            idx = indices[title]
            sim_scores = list(enumerate(cosine_sim[idx]))  #计算余弦相似度，将电影类别的矩阵组合为一个索引序列，为他们添加索引值，即所在行号值+2（第一行是列，名，且索引从0开始）
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) #，key=lambda 变量: x[维数]，按照第二维排序，降序
            sim_scores = sim_scores[1:11] #选取前十名
            movie_indices = [i[0] for i in sim_scores] #把遍历的的结果存进list i[0]
            result=movies['movie_title'].iloc[movie_indices] #按照第n行输出
            return print(result)
            # 调用文件数据保存方法
            storagePath = "C:/Users/Lenovo/Desktop/result.txt"
            storageToLocalFiles(storagePath, result)

        def storageToLocalFiles(storagePath, data):
            fhandle = open(storagePath, "wb")
            fhandle.write(data)
            fhandle.close()

        s = aid
        # 例如：41551729/177974677
        get_recommendation(s)

        if (os.path.exists('C:/Users/Lenovo/Desktop/result.txt') == True):
            self.sh1.set("推荐结果生成成功，文件已保存到桌面")
        else:
            self.sh1.set("生成失败，请您重试")
    def back(self):
        self.page.destroy()







