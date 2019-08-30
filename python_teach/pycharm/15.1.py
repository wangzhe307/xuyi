import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    # strptime：将字符串时间转换为 datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 正则获取 时差字符串
    m = re.match(r'^(UTC)(.*?)(\:.*)$', tz_str)
    # 将字符串转换为数字
    n = int(m.group(2))
    # 创建时区
    tz_utc_n = timezone(timedelta(hours = n))
    # 转换为 UTC 时间
    utc_dt = dt.replace(tzinfo = tz_utc_n)
    # 将时间转换为 timestamp 并返回
    return utc_dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')