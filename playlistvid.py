from pytube import Playlist

# 0AK80

playlist_url = input()
playlist = Playlist(playlist_url)


print(len(playlist.video_urls))


for video in playlist.videos:
    
    video.streams.get_highest_resolution().download()


print('--------All downloads have finished--------')
