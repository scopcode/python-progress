album_dict = []


def make_album(artist_name, album_name, year = ""):
    album = {"Artist Name" : artist_name.title(),
             "Album Name" : album_name.title()}
    if year:
        album["year"] = year
    
    return album


while True:
    name = input("Enter the name of the artist : ")
    if name.lower() == "q" :
        break
    album = input("Enter the name of the album : ")
    if album.lower() == "q" :
        break
    calendar = input("Enter the year of the album : ")
    if calendar.lower() == "q" :
        break
    final_album = make_album(name,album,calendar)
    print(final_album)
    print("If You Want To Exit Just Press Q at any time and " 
    "we'll show you the final dictionary")
    album_dict.append(final_album)

for item in album_dict:
    print("\n")
    for key,value in item.items():
        print( key.title() + " - " + value.title())

