from functions.main_process import *

def main():
    authorization()
    initialization()
    while True:
        # user input
        user_input = input("you: ")
        # exit command
        if user_input == "exit":
            break
        # get recomandation
        recommend_tracks = getRecomandation(user_input)
        # create playlist
        createSpotifyPlaylist(user_input, recommend_tracks)

if __name__ == '__main__':
    main()



