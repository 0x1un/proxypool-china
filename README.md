# Python proxy-pool

依赖： 
----
* Python3.6.x
* aiohttp>=1.3.3
* Flask>=0.11.1
* redis>=2.10.5
* requests>=2.13.0
* pyquery>=1.2.17
* redis数据库

安装依赖: `sudo pip3.6 install -r requirements.txt`
  
---------------------------
api开关, 默认开启, 如果需要, 可以在`proxypool/setting.py`中设置。

数据库密码用户名，端口，测试批次，抓取频率都可以在设置文件中进行修改。
