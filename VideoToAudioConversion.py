import os
path = "/home/hasanmdmehadi/Desktop"
for filename in os.listdir(path):
    if (filename.endswith(".webm")):
        os.system("ffmpeg -i {0} -vn -ar 16000 -ac 2 -ab 16 -f wav output{0}.wav")
    else:
        continue
