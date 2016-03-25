## spider for mp

### 前置条件
* python 2.7
* scrapy: pip install scrapy

### 使用步骤
```
git clone ssh://g@gitlab.baidu.com:8022/zdh/mpspider.git
cd mpspider
scrapy crawl sogou -a query=array --set DOWNLOAD_DELAY=5 -o array.csv -t csv
```
参数说明：
* query: 公众号名称
* DOWNLOAD_DELAY: 抓取间隔，单位秒；搜狗对爬虫封禁比较变态， IP 被封禁之后需要小时级才能解封；默认间隔15秒，不要设置太小；
* -o: 结果输出文件


