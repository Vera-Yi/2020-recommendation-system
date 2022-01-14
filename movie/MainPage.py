from tkinter import *
from GetPage import *  # 菜单栏对应的各个子页面

class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (400, 300))  # 设置窗口大小
        self.createUpper()

    def createUpper(self):
        self.MainPage = MainFrame(self.root)  # 创建不同Frame
        self.GetPage = GetFrame(self.root)
        self.MainPage.pack()  # 默认显示主页

        menubar = Menu(self.root)
        menubar.add_command(label='主页', command=self.gotoMain)
        menubar.add_command(label='获取电影推荐', command=self.gotoGet)
        self.root['menu'] = menubar  # 设置菜单栏

    def gotoMain(self):
        self.MainPage.pack()
        self.GetPage.pack_forget()

    def gotoGet(self):
        self.MainPage.pack_forget()
        self.GetPage.pack()

class MainFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self).pack()







