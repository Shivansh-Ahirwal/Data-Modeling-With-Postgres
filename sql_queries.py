# DROP TABLE QUERIES

DROP_SONG_DATA_TABLE = """DROP TABLE IF EXISTS SONG_DATA"""

DROP_USER_DATA_TABLE = """DROP TABLE IF EXISTS USER_DATA"""

DROP_SESSION_TIME_TABLE = """DROP TABLE IF EXISTS SESSION_TIME"""

DROP_ARTIST_DATA_TABLE = """DROP TABLE IF EXISTS ARTIST_DATA"""

DROP_SONG_PLAYED_TABLE = """DROP TABLE IF EXISTS SONG_PLAYED"""

# CREATE TABLE QUERIES

CREATE_USER_DATA_TABLE = """CREATE TABLE USER_DATA(user_id varchar PRIMARY KEY NOT NULL, firstname varchar, lastname varchar, gender varchar,level varchar)"""

CREATE_SONG_DATA_TABLE = """CREATE TABLE SONG_DATA(song_id varchar PRIMARY KEY NOT NULL, title varchar, duration float, year int, artist_id varchar)"""

CREATE_SESSION_TIME_TABLE = """CREATE TABLE SESSION_TIME(start_time timestamp PRIMARY KEY, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL)"""

CREATE_SONG_PLAYED_TABLE = """CREATE TABLE SONG_PLAYED(song_play_id serial PRIMARY KEY NOT NULL, user_id int, level varchar, song_id varchar, location varchar, useragent varchar, page varchar,session_id int)"""

CREATE_ARTIST_DATA_TABLE = """CREATE TABLE ARTIST_DATA(artist_id varchar PRIMARY KEY NOT NULL, artist_name varchar, artist_latitude varchar, artist_longitude varchar, artist_location varchar)"""

# INSERT DATA INTO TABLE QUERIES

INSERT_INTO_USER_TABLE = ("""INSERT INTO USER_DATA(user_id,firstname,lastname,gender,level) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level""")

INSERT_INTO_SONG_TABLE = ("""INSERT INTO SONG_DATA(song_id,title,duration,year,artist_id) VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

INSERT_INTO_SESSION_TABLE = ("""INSERT INTO SESSION_TIME(start_time,hour,day,week,month,year,weekday) VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

INSERT_INTO_ARTIST_TABLE = ("""INSERT INTO ARTIST_DATA(artist_id,artist_name,artist_latitude,artist_longitude,artist_location) VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

INSERT_INTO_PLAYED_TABLE = ("""INSERT INTO SONG_PLAYED(song_play_id,user_id,level,song_id,location,useragent,page,session_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

SELECT_SONG_ARTIST_ID = ("""SELECT song_id,SONG_DATA.artist_id FROM SONG_DATA JOIN ARTIST_DATA ON SONG_DATA.artist_id=ARTIST_DATA.artist_id WHERE title = %s AND name = %s AND duration= %s""")
# LIST OF QUERIES TO ACCESS ALL QUERIES EASILY

CREATE_QUERIES = [CREATE_USER_DATA_TABLE,CREATE_SONG_DATA_TABLE,CREATE_SESSION_TIME_TABLE,CREATE_SONG_PLAYED_TABLE,CREATE_ARTIST_DATA_TABLE]

INSERT_QUERIES = [INSERT_INTO_USER_TABLE,INSERT_INTO_SONG_TABLE,INSERT_INTO_SESSION_TABLE,INSERT_INTO_ARTIST_TABLE,INSERT_INTO_PLAYED_TABLE]

DROP_TABLE_QUERIES = [DROP_SONG_DATA_TABLE, DROP_SESSION_TIME_TABLE, DROP_ARTIST_DATA_TABLE, DROP_SONG_PLAYED_TABLE, DROP_USER_DATA_TABLE]