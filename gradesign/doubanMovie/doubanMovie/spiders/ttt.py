import re
# s = '                            1994 / 美国 / 犯罪 剧情'
s = '                            1993 / 中国大陆 香港 / 剧情 爱情 同性'
res = re.split('\xa0*/\xa0*', s)
print(res[1])
# if ' ' in res[1]:
#     print(res[1].split())
print(res[2])
if ' ' in res[2]:
    print(res[2].split())
