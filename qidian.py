#起点中文网————以诡秘之主为例
#罗皓 2021年12月22日11:13:50
import re
import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Cookie':'_gid=GA1.2.2056225732.1640136282; newstatisticUUID=1640136282_2091080035; _csrfToken=GZy012teFEsnPWXSry1waBv14tjaXOdr27iC6QWi; e2=; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%2C%22l1%22%3A3%7D; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; showSectionCommentGuide=1; lrbc=1030870265%7C689267528%7C1; rcr=1030870265; bc=1030870265; _ga_FZMMH98S83=GS1.1.1640136280.1.1.1640136877.0; _ga_PFYW0QLV3P=GS1.1.1640136280.1.1.1640136877.0; _ga=GA1.2.1681453437.1640136281; _gat_gtag_UA_199934072_2=1'
}
#获取单章内容
def get_content(url,index):
    f=open('诡秘之主\\诡秘之主第'+str(index)+'章.txt','w',encoding='utf-8')
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'lxml')

    #标题等信息
    #select返回list
    title=soup.select('.content-wrap')[0].string
    info=str(soup.select('.info')[0])
    book=re.findall('<em class="iconfont"></em>(.*?)</a>',info)[0]
    author=re.findall('<em class="iconfont"></em>(.*?)</a>',info)[0]
    words=re.findall('<span class="j_chapterWordCut">(.*?)</span>字</i>',info)[0]+'字'
    time=re.findall('</em><span class="j_updateTime">(.*?)</span></i>',info)[0]

    f.write(title+'\n')
    f.write('作品： '+book+' ')
    f.write('作者： '+author+' ')
    f.write('字数： '+words+' ')
    f.write('发表时间： '+time+'\n')

    #内容
    article=soup.select('.j_readContent.read-content')[0]
    #<class 'bs4.element.Tag'>可以当list来用
    for i in range(len(article)-2):
        paragraph=article.select('p')[i].text
        f.write(paragraph+'\n')
        
    f.close()

#获取章节url
r=requests.get('https://book.qidian.com/info/1010868264/#Catalog',headers=headers)
soup=BeautifulSoup(r.text,'lxml')
base_url='https:'
#只获取免费能看的129章内容
for i in range(129):#29
    print(i)
    section_url=re.findall('data-cid="(.*?)" data-eid=',str(soup.select('.book_name')[i])) [0]      
    get_content(base_url+section_url,i+1)
    
