'''
title: 异常处理

1. 主动抛出异常 raise
2. 捕获异常 try except
'''

import logging

try:
    raise Exception('错误')
except Exception as e:
    logging.exception(e)
finally:
    print('finally...')