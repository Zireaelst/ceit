class Singer:
    def __init__(self, fullname, country, music_type):
        self.fullname = fullname
        self.country = country
        self.music_type = music_type

    def __str__(self):
        return f"Singer: {self.fullname}, country: {self.country}, type: {self.music_type}"


class Album:
    def __init__(self, title, year, singer):
        self.title = title
        self.year = year
        self.singer = singer

    def __str__(self):
        return f"Album: {self.title}, year: {self.year}, singer: {self.singer.fullname}"


def main():
    singers = []
    albums = []

    while True:
        print("\n1) Create an album")
        print("2) Create a singer")
        print("3) List singers")
        print("4) List albums")
        print("5) Exit")

        choice = input("\nWhat would you like to do: ")

        if choice == "1":
            if not singers:
                print("No singers available. Please create a singer first.")
                continue

            title = input("Enter album name: ")
            year = input("Enter album year: ")

            print("\nSingers:")
            for i, singer in enumerate(singers, start=1):
                print(f"{i}. {singer}")

            try:
                singer_choice = int(input("\nChoose a singer for this album [enter a number]: "))
                if 1 <= singer_choice <= len(singers):
                    selected_singer = singers[singer_choice - 1]
                    albums.append(Album(title, year, selected_singer))
                    print("<<Album is created>>")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            fullname = input("Enter singer name: ")
            music_type = input("Enter music type: ")
            country = input("Enter country: ")

            singers.append(Singer(fullname, country, music_type))
            print("<<Singer is created>>")

        elif choice == "3":
            if not singers:
                print("No singers to display.")
            else:
                print("\nSingers are listed below:")
                for i, singer in enumerate(singers, start=1):
                    print(f"{i}. {singer}")

        elif choice == "4":
            if not albums:
                print("No albums to display.")
            else:
                print("\nAlbums are listed below:")
                for i, album in enumerate(albums, start=1):
                    print(f"{i}. {album}")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
