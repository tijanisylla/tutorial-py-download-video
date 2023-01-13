# Only for educational purposes.
from pytube import YouTube

def download_video(link):
    yt_object = YouTube(link)
    yt_object = yt_object.streams.get_highest_resolution()
    
    try:
        yt_object.download()
        print("Downloading Successful !!! ") 
        
    except:
        print("Error Occured !!! ")
    print("Downloading Successful !!! ")


def my_input():
    video_input = input("Enter a link video: ")
    func = download_video(video_input)
    return func

if __name__ == "__main__":
    my_input()


#============== Incase you run into SSL python certificate Error, do the following ==============
# 1)- Open your terminal
# 2)- Check your python version : python3 -— version
# 3)- Then replace the python version with your-py-version down below. 
#     * Example: 
#     * python3.8
#     * /Applications/Python\ 3.8/Install\ Certificates.command

# 4)- /Applications/Python\ your-py-version/Install\ Certificates.command