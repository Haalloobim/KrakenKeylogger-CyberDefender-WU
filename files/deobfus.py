url = 'aht1.sen/hi/coucys.erstmaofershma//s:tpht'
url = url[::-1]

for i in range(0, len(url), 2):
    if i == len(url) - 1:
        print(url[i])
        break
    else:
        print(url[i+1] + url[i], end='')