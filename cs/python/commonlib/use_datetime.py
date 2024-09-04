#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

now = datetime.now()

dt = datetime(2023, 6, 1, 12, 20)

cday = datetime.strptime('2023-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

print('cday:',cday)

print('strftime:', cday.strftime('%a, %b %d %H:%M'))

print('current - 2.5 days =', cday - timedelta(days=2, hours=12))

t = dt.timestamp()

datetime.fromtimestamp(t)

# 时区
utc_dt =datetime.now(timezone.utc) # 0时区
print(utc_dt)
print(utc_dt+timedelta(hours=8))
