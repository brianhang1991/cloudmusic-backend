import sqlite3

from djangoProject.models.http.music import Music

def get_musics():

    conn = sqlite3.connect('D:\work\cloudmusic-backend\djangoProject\db\music.db')

    c = conn.cursor()
    print("数据库打开成功")

    musics = []

    cursor = c.execute("SELECT * from MUSIC")

    for row in cursor:
        music = Music(row[0], row[1], row[2])
        musics.append(music)
    conn.close()

    return musics



