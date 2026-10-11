print("----------------------------------------------")
print("=========== Music Playlist Manager ============")
print("-----------------------------------------------")
print()
t=[]
while True:
    print()
    print("1. Add songs")
    print("2.View Songs")
    print("3.Serach songs")
    print("4.Count Songs by Artist")
    print("5.Show first song and last song")
    print("6.Reverse playlist")
    print("7.Exit")
    print()
    ch=int(input("enter your choice: "))
    print()
    if ch==1:
        sn=input("enter your song name :").lower()
        an=input("enter artist name:").lower()
        dur=input("enter duration(mm:ss):")
        t.append((sn,an,dur))
        print()
        print("Song Added to playlist")

    if ch==2:
        print()
        print("---- playlist -----")
        print()
        c=0
        while c<len(t):
            sn,an,dur=t[c]
            print()
            print(c+1)
            print("song :",sn)
            print("Arist:",an)
            print("duration:",dur)
            c+=1

    if ch == 3:
        s = input("Enter Song to Search: ").lower()

        found = False

        for song in t:
            if song[0] == s:
                print("\nSong Found !!")
                print()
                print("Song     :", song[0])
                print("Artist   :", song[1])
                print("Duration :", song[2])

                found = True
                break

        if found == False:
            print("\nSong Not Found")

    if ch == 4:
        artist=input("enter artist name: ").lower()
        count=0
        for i in t:
            if i[1]==artist:
                count+=1
        print("songs:",count)

    if ch==5:
        if len(t)==0:
            print("Empty Playlist")
        else:
            print("First Song")
            print()
            sn,an,dur=t[0]
            print("Name",sn)
            print("artist:",an)
            print("dur",dur)
            print()
            print("Last Song")
            print()
            sn,an,dur=t[-1]
            print("Name",sn)
            print("artist:",an)
            print("dur",dur)

    if ch==6:
        c=len(t)-1
        while c>=0:
            sn,an,dur=t[c]
            print(c+1)
            print()
            print("song :",sn)
            print("Arist:",an)
            print("duration",dur)
            c-=1

    if ch==7:
        print("Thank You for Using Music Playlist Manager!")
        print()
        break