from proxypool.db import RedisClient

conn = RedisClient()

#导入函数
def set(proxy):
    result = conn.add(proxy)
    print(proxy)
    print('录入成功' if result else '录入失败')

#手动导入代理
def scan():
    print('请输入代理, 输入exit退出读入')
    while True:
        proxy = input()
        if proxy == 'exit':
            break
        set(proxy)


if __name__ == '__main__':
    scan()
