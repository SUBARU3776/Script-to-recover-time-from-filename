import base64

# 画像ファイル名
s_filename = 'FvgpjpKaYAI7ePk'
# デコード済みファイル名
s_filename += '=' * (-len(s_filename) % 4)  # パディング文字を追加
i_filename = int.from_bytes(base64.urlsafe_b64decode(s_filename.replace('-', '+').replace('_', '/')), 'big')
# 日時
time_ms = (i_filename >> 46) + 1288834974657
time_sec = time_ms / 1000.0
date_str = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(time_sec))

print(date_str)