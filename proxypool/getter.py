from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.crawler import Crawler
from proxypool.setting import *
import sys

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            #循环遍历计数器、
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                #使用下表索引取出函数列表中的函数并进行运行
                #爬虫程序返回的是一个迭代器
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                try:
                    '''
                    函数get_proxies是对爬虫结果进行遍历并取出其中的值加入
                    代理列表并且返回代理
                    '''
                    proxies = self.crawler.get_proxies(callback)
                    #proxies: list 
                except Exception:
                    print("\033[1;31;40m这里有错误...\033[0m")
                    print(f'爬虫{callback.__name__}发生了错误，需要进行调试')
                #清除缓存使得结果连续输出
                sys.stdout.flush()
                #遍历列表中的代理，加入数据库
                for proxy in proxies:
                    try:
                        self.redis.add(proxy)
                    except OSError as e:
                        print(f"\033[1;31;40m发生错误...{e.reason}\033[0m")
