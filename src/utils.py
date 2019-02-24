# author everpuck


import urllib.request

def url_get(url, headers={}, timeout=10, retry_times=3):
    res = None
    req = urllib.request.Request(url, headers=headers)
    for _ in range(retry_times):
        try:
            resp = urllib.request.urlopen(req, timeout=timeout)
        except Exception as e:
            print('url get error %s' % e)
            continue
        else:
            res = resp.read().decode('utf-8')
            break
    return res



def test():
    import time
    url = "http://gz-fund.10jqka.com.cn/?module=api&controller=index&action=chart&info=vm_fd_JPY208&start=0930&_=%s" % (int(time.time() * 1000))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        # 'Cookie': 'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1548584673,1548586094; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1548587464; v=Avz8cO7VjMJAWrgeEPYwsp8GzZGt9akmIpy0o9Z9CXPKeZIH_gVwr3KphGIl'
    }
    print(url_get(url, headers=headers))


if __name__ == "__main__":
    test()
