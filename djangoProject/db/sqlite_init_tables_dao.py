#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('music.db')

print ("数据库打开成功")

c = conn.cursor()

c.execute("INSERT INTO MUSIC (ID,NAME,LOCAL_PATH) \
      VALUES (1, '倉木麻衣 - Tonight, I feel close to you (wiht 孫 燕姿Yan-Zi)',"
          "'musics/倉木麻衣 - Tonight, I feel close to you (wiht 孫 燕姿Yan-Zi).mp3')")

c.execute("INSERT INTO MUSIC (ID,NAME,LOCAL_PATH) \
      VALUES (2, '毛不易 - 呓语', 'musics/毛不易 - 呓语.mp3')")

c.execute("INSERT INTO MUSIC (ID,NAME,LOCAL_PATH) \
      VALUES (3, '王宇宙Leto,乔浚丞 - 若月亮没来 (若是月亮还没来)', 'musics/王宇宙Leto,乔浚丞 - 若月亮没来 (若是月亮还没来).mp3')")

conn.commit()
print ("数据插入成功")
conn.close()