import base64
import time

# 画像ファイル名
s_filename = ''

# デコード済みファイル名
s_filename += '=' * (-len(s_filename) % 4)  # パディング文字を追加
i_filename = int.from_bytes(base64.urlsafe_b64decode(s_filename.replace('-', '+').replace('_', '/')), 'big')

# 日時
time_ms = (i_filename >> 46) + 1288834974657
time_sec = time_ms / 1000.0
date_str = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(time_sec + time.timezone + 9 * 3600))

print(date_str)
