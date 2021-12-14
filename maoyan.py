#written by 罗皓 
#这个文件爬取了猫眼影片排行榜前100名的影片，包括片名、主演、上映时间。
#使用requests和正则表达式
#需要更改cookie才能使用

import requests
import re
#先手动登下网页，过人机检验，将cookie复制到下面
def get_one_page(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Cookie':'__mta=121549623.1638636434030.1638668011774.1638669019933.17; uuid_n_v=v1; uuid=D3CBBFF0552111ECB4599DFBC2DEF6228572D9562F9242D894899F4B2FA7D7A9; _csrf=e12c4063c99291def1fc88126b17e37784a2d6f59156873454e09a50d78d7a5f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1638636433; _lxsdk_cuid=17d8657b03c13-0c3e0edf57515-978183a-144000-17d8657b03dc8; ci=1%2C%E5%8C%97%E4%BA%AC; featrues=[object Object]; _lx_utm=utm_source%3Dmaoyan_appShare%26utm_content%3Dc_yq5np6g4; _lxsdk=D3CBBFF0552111ECB4599DFBC2DEF6228572D9562F9242D894899F4B2FA7D7A9; __mta=121549623.1638636434030.1638636469821.1638636646941.3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1638669020; _lxsdk_s=17d8839363e-7c4-c6d-e8e%7C%7C7'
            }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        text=response.text
        #print(text)
        #写正则表达式，关键是看目标两边的锚。打出来看看是哪边出了问题。
        pattern=re.compile('<p class="name"><a href="/films.*?"{movieId:\d*}">(.*?)</a>.*?star.*?                (.*?)\n.*?releasetime">(.*?)</p>',re.S)
        text=re.findall(pattern,text)
        return text
    return None
#每个电影的信息如下，据此来写re
'''
                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/46818" title="怦然心动" class="image-link" data-act="boarditem-click" data-val="{movieId:46818}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592b122ff8d3387a93ccab6036f616c1.jpg?imageView2/1/w/160/h/220" alt="怦然心动" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/46818" title="怦然心动" data-act="boarditem-click" data-val="{movieId:46818}">怦然心动</a></p>
        <p class="star">
                主演：玛德琳·卡罗尔,卡兰·麦克奥利菲,艾丹·奎因
        </p>
<p class="releasetime">上映时间：2010-07-26(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>        
    </div>

      </div>
    </div>

                </dd>
'''
def write_to_file(content):#list 
    with open('maoyan_result.txt','a',encoding='utf-8')as f:
        for i in range(len(content)):
            line='片名：'+content[i][0]+'\t'+content[i][1]+'\t'+content[i][2]+'\n'
            f.write(line)
    return 

def main(offset):
    url=base_url+str(offset)
    content=get_one_page(url)
    write_to_file(content)    
    

base_url='https://www.maoyan.com/board/4?timeStamp=1638636742476&channelId=40011&index=8&signKey=fe23ceb5a599e086d9f2ba52a4d54e11&sVersion=1&webdriver=false&offset='

for i in range(10):
    main(i*10)
            