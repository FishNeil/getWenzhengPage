import urllib.request
import re

urls=["http://zs.sdwz.cn/2017/1107/c124a23333/page.htm", #2017
      # "http://zs.sdwz.cn/2016/0716/c124a10356/page.psp", #2016 文正网页出错
      # "http://zs.sdwz.cn/2016/0613/c124a10355/page.psp", #2015 文正网页出错
      # "http://zs.sdwz.cn/2015/0610/c124a10351/page.psp",#2014 文正网页出错
      "http://zs.sdwz.cn/2013/1226/c124a10346/page.htm", #2013 江苏
      "http://zs.sdwz.cn/2013/1226/c124a10345/page.htm", #2013外省
      # "http://zs.sdwz.cn/2012/1221/c124a10342/page.psp", #2012 江苏文正网页出错
      # "http://zs.sdwz.cn/2012/1221/c124a10341/page.psp",#2012 外省文正网页出错
      # "http://zs.sdwz.cn/2012/0519/c124a10340/page.psp", #2011 江苏文正网页出错
      # "http://zs.sdwz.cn/2012/0519/c124a10339/page.psp",#2011 外省文正网页出错
     "http://zs.sdwz.cn/2011/0506/c124a10338/page.htm", #2010 江苏
      "http://zs.sdwz.cn/2010/0513/c124a10337/page.htm"#2010 外省
]



def getUrlsPagesInfo(urls,path):
    for url in urls:
        index=url.rfind("/")
        if index==-1: continue
        filename=url[:index]
        index=filename.rfind("/")
        filename=filename[index+1:]+".htm" #用最后两个  /  之间的字符串作为文件名
        fp = open(path + filename, "w", encoding="utf-8")
        raw = urllib.request.urlopen(url).read()
        text = raw.decode('utf-8')
        fp.write(text)
        fp.close()

def main():
    getUrlsPagesInfo(urls,"f:\\html\\") #这个第二个参数路径你可以自己修改

main()