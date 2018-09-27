import re, requests, json

newrows = re.findall('value="(.*?)"', str(open('parse.txt', "r", encoding="UTF-8").readlines()))

url = "https://plus.yle.fi/2017-05-ylioppilaskone/data/"
for n in sorted(newrows, key=str.lower):
    data = requests.get(url + n.replace('ö', 'o').replace('ä', 'a').replace(' ', '%20').lower() + '.json')
    if data.status_code == 200:
        print(n, end=": ")
        for i in json.loads(data.content):
            print(i["name"], end=", ")
        print()
