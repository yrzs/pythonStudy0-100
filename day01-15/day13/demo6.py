import tkinter
import tkinter.messagebox
from time import sleep


def download():
    sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 月染指上(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    pannel = tkinter.Frame(top)
    button1 = tkinter.Button(pannel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(pannel, text='关于', command=show_about)
    button2.pack(side='right')
    pannel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
