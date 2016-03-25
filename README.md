## 公众号文章抓取

### 前置条件
* python 2.7
* scrapy: pip install scrapy

### 使用步骤
```
git clone ssh://g@gitlab.baidu.com:8022/zdh/mpspider.git
cd mpspider
scrapy crawl sogou -a query=小道消息 -a pagelimit=1 --set DOWNLOAD_DELAY=5 -o items.csv -t csv
```
参数说明：
* query: 公众号名称
* pagelimit: 抓取的页数，一页10篇文章，默认为1
* DOWNLOAD_DELAY: 抓取间隔，单位秒；搜狗对爬虫封禁比较变态， IP 被封禁之后需要小时级才能解封；默认间隔15秒，不要设置太小；
* -o: 结果输出文件
* withContent: 提取正文，默认0，不提取

### 结果样例
正文没有提取
```
date,url,author,title
2016-03-24,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403183461&idx=1&sn=bfd21c414d66f77969e4cc85abb0f65e&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,中国最早的网民在网上都聊啥？2016-03-12,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=402910106&idx=1&sn=aa4c9dfda6c960a0c2a15ce0cbf791bd&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,苹果这个月能发布什么新产品? 我期待这些产品的改进
2016-03-15,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=402983937&idx=1&sn=04e5093d153ff1743f882209cb849a5e&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,产品的价值观
2016-03-15,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=402994793&idx=1&sn=d911f33c83cb847857ec237f91cb59b3&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,我为什么讨厌「饿了么」们
2016-03-16,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403008090&idx=1&sn=032880c60665ba45255a38a612b4158e&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,这一次，我们想改变医疗这个行业
2016-03-17,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403040823&idx=1&sn=4c5504a5b9ca2ee73371bc0de8583e21&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,信息焦虑怎么缓解
2016-03-18,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403064185&idx=1&sn=f7a8dd0008ba36210cd57bf194ac2327&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,时间追杀令
2016-03-19,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403093815&idx=1&sn=8e849ef4d77407055b073d4eb55a2ea6&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,你们公司设计一张图片要多少成本?
2016-03-21,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403125548&idx=1&sn=60c201d5631224331929bbb98b884b97&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,小道观察：猎豹移动的打法
2016-03-22,http://mp.weixin.qq.com/s?__biz=MjM5ODIyMTE0MA==&mid=403140154&idx=1&sn=6c691056694035676e5dfe9101597d61&3rd=MzA3MDU4NTYzMw==&scene=6,Fenng,免于恐惧的自由
```
