import requests
from bs4 import BeautifulSoup
AllUniv=[]#二维列表，用来储存所有大学信息
def GetSoup():#获取网页文档
    try:
        r = requests.get("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html",timeout=30)
        r.raise_for_status()#若连接网页错误则抛出异常
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'html.parser')
        return soup
    except:
        print("获取错误!")
        return ''
def GetRanking(soup):
    tr=soup.find_all('tr')
    for i in tr:#遍历所有tr标记
        td=i.find_all('td')
        if len(td)==0:
            continue
        Univ=[]#一维列表，用来储存单个大学的信息
        for n in td:#遍历tr标记中的td标记
            Univ.append(str(n.string))
        AllUniv.append(Univ)
def PrintAllUniv(num):
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".\
          format(chr(12288),"排名","学校名称","省市","总分","生源质量600"))
    for i in range(num):
        Univ=AllUniv[i]
        print("{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8.1f}{5:{0}^10}".\
              format(chr(12288),Univ[0],Univ[1],Univ[2],eval(Univ[3]),Univ[4]))
def SaveCSV(num):
    fw = open("123.csv", 'w')
    Str = "排名", "学校名称", "省市", "总分", "生源质量","毕业生就业率","社会声誉","论文数量",\
          "论文质量","被引论文","被引学者","企业科研经费","技术转让收入","留学生比例"
    fw.write(','.join(Str) + '\n')
    for i in range(num):
        fw.write(",".join(AllUniv[i]) + '\n')#用“，”分割数据，每行以“\n”结束
    fw.close()
def main():
    soup=GetSoup()
    GetRanking(soup)
    num=eval(input("请输入要查询的排名范围(1~600)："))
    if num<1 or num >600:
        print("输入错误！")
        return
    PrintAllUniv(num)
    SaveCSV(num)
    end=input("回车关闭")
main()