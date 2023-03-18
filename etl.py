import os 
import psycopg2
import pandas as pd
import glob
from sql_queries import *


def get_all_jsons_in_folder(path):
    json_files = []
    for root,folders,files in os.walk(path):
        all_files = glob.glob(os.path.join(root,"*json"))
        for f in all_files:
            json_files.append(os.path.abspath(f))
    return json_files


def process_log_data_file(filepath,cur):

    log_files = get_all_jsons_in_folder(filepath)

    for file in log_files:
        df = pd.read_json(file,lines = True)
        user_data = df[["userId","firstName","lastName","gender","level"]].values.tolist()
    
    cur.executemany(INSERT_INTO_USER_TABLE,user_data)

    temp_df=df[df["page"]=="NextSong"].copy()
    
    temp_df["ts"]=pd.to_datetime(temp_df["ts"],unit="ms")
    
    time_df_values = (temp_df.ts, temp_df.ts.dt.hour , temp_df.ts.dt.day , temp_df.ts.dt.dayofweek , temp_df.ts.dt.month , temp_df.ts.dt.year , temp_df.ts.dt.weekday)
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels, time_df_values)))
    
    time_df.reset_index(drop=True,inplace=True)
    
    time_data=time_df.values.tolist()
    
    cur.executemany(INSERT_INTO_SESSION_TABLE,time_data)

    log_df = df.copy()
    log_df["ts"]=pd.to_datetime(log_df["ts"],unit="ms")

    for index, row in log_df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(SELECT_SONG_ARTIST_ID, (row.song, row.artist, row.length))
        result = cur.fetchone()
        
        if result:
            song_id,artist_id =result
        else:
            song_id,artist_id=None,None
    
        songplay_data=[index+1,song_id,artist_id,row.level,row.ts,row.userId,row.sessionId,row.location,row.userAgent]
        cur.execute(INSERT_INTO_PLAYED_TABLE,songplay_data)
    

def process_song_data_file(filepath,cur):

    song_files = get_all_jsons_in_folder(filepath)

    for file in song_files:
        df = pd.read_json(file,lines=True)
        song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values.tolist()

    cur.executemany(INSERT_INTO_SONG_TABLE,song_data)

    artist_data = df[['artist_id','artist_name','artist_latitude','artist_longitude','artist_location']].values.tolist()

    cur.executemany(INSERT_INTO_ARTIST_TABLE,artist_data)


def main():
    try:
        conn = psycopg2.connect(host="localhost",dbname="sparkifydb",user="postgres",password="admin")
    except psycopg2.Error() as e:
        print('error on connecting to new database')
        print(e)

    try:
        cur = conn.cursor()
    except psycopg2.Error() as e:
        print("error on creating cursor")
        print(e)

    path_for_song_data = r'C:\Users\Canopus-57\postgresDM\data\song_data'
    
    path_for_log_data = r'C:\Users\Canopus-57\postgresDM\data\log_data'

    process_song_data_file(path_for_song_data,cur=cur)

    process_log_data_file(path_for_log_data,cur=cur)

    conn.commit()

    conn.close()

if __name__ == "__main__":
    main()
