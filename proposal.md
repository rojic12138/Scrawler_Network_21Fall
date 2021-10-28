# 计算机网络和Web技术课程实验设计的初步报告

第四组 – 罗皓 许浩哲


## 反爬虫机制的应对
------------------

### 实验目的

找到目前网络上的人气网站上采用的反爬虫机制，并实现相应的爬虫策略。主要目标：起点中文网、新浪微博、twitter、和reddit（候补为：知乎、北大树洞、pinterest、quora）。候补是因为前列网站的爬取可能太过困难，比如twitter的视频，必要情况下要换成候补的网站。

### 系统设计框架

对不同的网站研究反爬虫机制，针对地研发爬虫机制，目标是高效爬取，最终代码可复用。	

### 技术路线选择

- 准备使用网上已有的python包，尤其是Beautifulsoup来手工编程，达成爬虫的目标。
- 使用GitHub来实时合作，地址为https://github.com/rojic12138/Scrawler_Network_21Fall
- 可能参考已有的包来应对如同CAPTCHA那样的高难度反爬虫机制。

### 程序预计实现进度

目前已经有了初等的爬虫、在研究已选网站有哪些方面的反爬虫机制需要制造应对策略。

- [ ] 11.7前  完成爬虫机制、反爬虫机制的初步调研
- [ ] 11.14 前 学习爬虫的一般写法
- [ ] 11.28 前 两人各自至少完成一个目标网站的爬虫设计，并向- Github提交反爬虫机制、爬取步骤、源程序、参考资料。
- [ ] 12.12 前 两人各自至少完成两个目标网站的爬虫设计，并提交到Github。
- [ ] 1.5前 对上述网站没有涉及的反爬虫机制进行研究，编写报告。
- [ ] 1.12前 提交最终报告。

### 初步研究结果

很多大型网站都有基础的反爬虫机制、如IP blocking、CAPTCHA、只给登录用户看、或者使用AJAX来反爬虫。对于这些基础的反爬虫机制有以下一些应对策略：

- IP Blocking：限制爬虫的访问速度，因为访问的太快会被ban；
- CAPTCHA：可以使用已有的反CAPTCHA包来破解，模拟人工拖动拼图；
- 登录用户：可以让爬虫模拟登录的步骤来破解；
- AJAX：可以使用XML解析器来破解；
- User-Agent Blocking：伪装爬虫请求头的Hearers；
- 图片伪装和CSS偏移：研究网页的JavaScript代码来破解。

### 人员分工

-	[@rojic12138](https://github.com/rojic12138) 罗皓：起点中文网、新浪微博（候补：知乎、北大树洞）
-	[@vspanda](https://github.com/vspanda) 许浩哲：twitter、reddit（候补：pinterest、quora）