from MainPage import *

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (400, 300))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page,height=3).pack()
        Button(self.page, text='开始', width=15,command=self.kaishi).pack()
        Label(self.page).pack()
        Button(self.page, text='退出', width=15, command=self.page.quit).pack()

    def kaishi(self):
        self.page.destroy()
        MainPage(self.root)




