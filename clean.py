import os
reader = open("./log/log.txt", 'r',encoding="utf-8")
arr = []
chatText = reader.readlines()
chatLinesCount = len(chatText)
for c in range(chatLinesCount):
    chatContent = chatText[c]
    if(chatContent.strip()=='\n'):
        continue
    if(chatContent.strip().startswith("2019-")):
        continue
    if(chatContent.strip()=='' or chatContent.strip().startswith("[图片]") or chatContent.strip().startswith("[表情]")):
        continue
    print(chatContent)
    arr.append(chatContent.strip("\n").strip("\r"))
with open("./log/clean.txt",'w',encoding="utf-8") as f:
    for line in arr:
        f.write(line)