import os
import time
from threading import Thread
from mail import send_email
from mylog import setup_logger
from common import transaction_time
from utils import url_get
from config import FUND_NICK_LIST


logger = setup_logger(logger_name='main', logger_path='logger')


def main():
    subject = "%s_基信息" % time.strftime("%Y-%m-%d %H:%M", time.localtime()) 
    content = []

    for fund_info in FUND_NICK_LIST:
        time_str, rate = check_fund(fund_info)
        line = "%s -- %s : %s" % (fund_info['name'], time_str, rate)
        content.append(line)
    
    content.sort(key=lambda x : abs(float(x.split(":")[-1])), reverse=True)
    content = "\n".join(content)
    # print(content)
    send_email(subject, content)


def check_fund(fund_info):
    host = 'gz-fund.10jqka.com.cn'
    url = "http://%s/?module=api&controller=index&action=chart&info=%s&start=0930&_=%s" \
        % (host, fund_info['nick'], int(time.time() * 1000))
    referer = 'http://fund.10jqka.com.cn/%s/' % fund_info['code']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Referer': referer,
        'Host': host
        # 'Cookie': 'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1548584673,1548586094; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1548587464; v=Avz8cO7VjMJAWrgeEPYwsp8GzZGt9akmIpy0o9Z9CXPKeZIH_gVwr3KphGIl'
    }
    res = url_get(url, headers=headers)
    try:
        time_str, price_n, price_y, _ = res.split('~')[2][:-1].split(";")[-1].split(',')
    except Exception as e:
        logger.error('error in parse http res, %s', e)
    
    rational = (float(price_n) - float(price_y)) * 100 / float(price_y)
    return time_str, round(rational, 4)


if __name__ == "__main__":
    main()
