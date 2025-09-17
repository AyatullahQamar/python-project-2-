import sqlite3

conn=sqlite3.connect("youtube_videos_db")

cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    ) 
''')
conn.commit()

def list_videos():
        print("\n")
        print("*"*70)
        cursor.execute("SELECT * FROM videos")
        for row in cursor.fetchall():
            print(row)
        print("\n")
        print("*"*70)


def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?) ",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    list_videos()
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=? ",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    list_videos()
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Video Manager | Choose An Option") 
        print("1. List all videos ")
        print("2. Add a video ")
        print("3. Update videos ")
        print("4. Delete videos ")
        print("5. Exit App")

        choice=input("Enter an option :")

        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter a video: ")
            time=input("Enter duration of video :")
            add_video(name,time)

        elif choice=='3':
            video_id=int(input("Enter video id "))
            name=input("Enter a video: ")
            time=input("Enter duration of video :")
            update_video(video_id,name,time)

        elif choice=='4':
            video_id=int(input("Enter the number of video to be deleted :"))
            delete_video(video_id)

        elif choice=='5':
            break
        else:
            print("Invalid index")

    conn.close()


if __name__=="__main__":
    main()