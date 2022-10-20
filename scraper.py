from bs4 import BeautifulSoup
import requests
import json,csv
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.5', }

def removepunct(sentence):
    punc = '''\/'''
    finalsentence=""
    for item in sentence:
        if item not in punc:
            finalsentence+=item
    return finalsentence

def main():
    darazurl = 'https://www.daraz.com.np/catalog/?_keyori=ss&from=input&page=1&q=noodles'
    r = requests.get(darazurl, headers=headers).text
    htmlcontent = r.split("window.pageData")[1]
    htmlcontent =htmlcontent[1:]
    htmlcontent =htmlcontent.split("mainInfo")[0]
    mainlist = htmlcontent.split(",")[:-1]
    finalcontent =''.join(mainlist) 
    print(finalcontent)
    with open('another.json','w') as file:
        json.dump(finalcontent,file)
    # data_dict= json.loads(finalcontent)

main()