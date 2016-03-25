## 公众号文章抓取

### 前置条件
* python 2.7
* scrapy: pip install scrapy

### 使用步骤
```
git clone ssh://g@gitlab.baidu.com:8022/zdh/mpspider.git
cd mpspider
scrapy crawl sogou -a query=array -a pagelimit=2 --set DOWNLOAD_DELAY=5 -o array.csv -t csv
```
参数说明：
* query: 公众号名称
* DOWNLOAD_DELAY: 抓取间隔，单位秒；搜狗对爬虫封禁比较变态， IP 被封禁之后需要小时级才能解封；默认间隔15秒，不要设置太小；
* -o: 结果输出文件

### 结果样例
array.csv, 正文没有提取
```
date,url,author,title
2016-03-23,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403439969&idx=1&sn=4a3b10fda94f673f6576451bbbaca651&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,做到slack就能成为slack吗？
2016-03-07,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403250471&idx=1&sn=6537e73240f2b670f85f1fcd4ba1f468&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,我不知道你不知道我不知道你不知道
2016-03-09,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403275549&idx=1&sn=360c97b521d983f723799168a10007dd&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,为什么需要刻意去做一些让自己不舒服的事情
2016-03-10,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403285320&idx=1&sn=271e350d68d8221f5a4a0488deb9b3be&3rd=MzA3MDU4NTYzMw==&scene=6,贝塔猫,也说AlphaGo
2016-03-11,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403296093&idx=1&sn=6b088243b476b3b7170b19c13866be57&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,比行为更重要的是你的思维方式
2016-03-12,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403306060&idx=1&sn=dca407e5376b55e00ff05f1b29227586&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,《纸牌屋》中的那一支香烟
2016-03-15,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403336509&idx=1&sn=4669f766c28297d23933ff3afa4d1407&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,三种互联网思维（一）
2016-03-16,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403348301&idx=1&sn=f28e85dc5f2a4a041100b0e18f8465a9&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,三种互联网思维（二）
2016-03-18,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403363035&idx=1&sn=4e50feefdb3b6b48f2de0b09e9d453b9&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,看财报 2015 Q4 腾讯
2016-03-21,http://mp.weixin.qq.com/s?__biz=MjM5OTIwMzQyMQ==&mid=403401255&idx=1&sn=7a82bd0025a2d3f4e1d9a4b5df78aef0&3rd=MzA3MDU4NTYzMw==&scene=6,张勇,为什么屏蔽百度抓取后，淘宝又在百度购买推广
```
