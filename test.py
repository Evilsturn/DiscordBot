from datetime import datetime
# 204230
# 012345
now = datetime.now().strftime("%H%M%S")
sec = int(now[4:6])
print(sec)
