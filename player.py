from genericpath import exists
import vlc
import os
from colorama import Fore, init

init()

b = Fore.LIGHTBLUE_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
r = Fore.RESET

if not "directory.txt" in os.listdir(os.getcwd()):
    file = open("directory.txt", "w")
    directory = input("[+] Enter music directory path: ")
    file.write(directory)
    file.close()

directory_file = open("directory.txt", "r")
path = directory_file.read()
directory_file.close()

def zero(number):
    if number < 10:
        out = "00" + str(number)
    elif number < 100:
        out = "0" + str(number)
    else:
        out = str(number)
    
    return out

class player():
    def playFile(self, file, path, volume):
        try:
            self.mediaplayer
        except AttributeError:
            varExists = False
        else:
            varExists = True
        
        if varExists:
            if self.mediaplayer.is_playing():
                self.mediaplayer.stop()

        self.mediaplayer = vlc.MediaPlayer(path+ "/" + file)
        self.mediaplayer.play()

        self.__init__(path, "Song playing", file, volume)

    def stop(self, path, volume):
        self.mediaplayer.stop()

        self.__init__(path,"Song stopped.", "", volume)

    def helpPage(self, path, song, volume):
        os.system("clear")

        print("HELP")
        print("====")
        print("")
        print("####\tPlay song / change directory")
        print("help\tShows this help.")
        print("stop\tStopps playing song.")
        print("back\tJumps up one directory.")
        print("play\tPlays paused song.")
        print("pause\tPauses playing song.")
        print("exit\tCloses this program.")
        print("")
        input()

        self.__init__(path, "Help page closed.", song, volume)

    def pause(self, path, song, volume):
        self.mediaplayer.pause()
    
        self.__init__(path, "Song paused.", song, volume)

    def playPaused(self, path, song, volume):
        self.mediaplayer.play()

        self.__init__(path, "Song playing.", song, volume)

    def __init__(self, path, status, song, volume):
        os.system("clear")

        print("PLAYER")
        print("======")
        print("")

        if song != "":
            print(y + "[>] | " + song + r)
        else:
            print(r + "[>] | " + r)

        print("[i] | " + status)
        print("[/] | " + path)
        print("[%] | " + str(volume))
        print("")

        files = []
        number = 0

        for file in os.scandir(path):
            if file.name.endswith(".mp3"):
                print(zero(number) + " | " + g + file.name + r)
            else:
                print(zero(number) + " | " + b + file.name + r)

            files.append(file.name)

            number = number + 1

        print("")
        x = input("[+] | ")

        if x == "stop":
            self.stop(path, volume)

        elif x == "pause":
            self.pause(path, song, volume)

        elif x == "play":
            self.playPaused(path, song, volume)

        elif x == "exit":
            quit()

        elif x == "back":
            self.backOneDir(path, song, volume)

        elif x == "help":
            self.helpPage(path, song, volume)

        elif x == "volume":
            self.changeVolume(path, song)

        else:
            if files[int(x)].endswith(".mp3"):
                self.playFile(files[int(x)], path, volume)
            else:
                self.changedir(files[int(x)], path, song, volume)

    def changedir(self,folder, path, song, volume):
        path2 = path + "/" + folder

        self.__init__(path2, "Directory changed.", song, volume)

    def backOneDir(self, path, song, volume):
        splitted = path.split("/")
        path3 = "/".join(splitted[:len(splitted)-1])

        self.__init__(path3, "One directory up.", song, volume)


    def changeVolume(self, path, song):
        volume = int(input("[%] | "))
        self.mediaplayer.audio_set_volume(volume)

        self.__init__(path, "Volume Changed.", song, volume)

player(path, "Welcome", "", 100).__init__(path, "Welcome", "", 100)
