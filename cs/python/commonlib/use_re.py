# 正则匹配
import re
# 日志框架
import logging

print(re.findall('\d', 'hello egon 123'))

logging.warning('wrong password more than 3 times')
logging.critical('server is down')
logging.error('error message')