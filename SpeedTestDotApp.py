import speedtest as spt
server = spt.Speedtest()
server.get_best_server()
down = server.download()
down = down/1000000
print("Download speed =")
print(down)
up = server.upload()
up = up/1000000
print("upload speed =")
print(up)
