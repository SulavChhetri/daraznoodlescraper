import requests
import json,csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.5', }


def main():
    darazurl = 'https://www.daraz.com.np/catalog/?_keyori=ss&from=input&page=1&q=noodles'
    r = requests.get(darazurl, headers=headers).text
    jsonresponse = json.loads(r.split("window.pageData=")[1].split('</script>')[0])
    mainlist = jsonresponse['mods']['listItems']
    with open('output.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Product name','Price'])
        for item in mainlist:
            price = 'Rs.'+ str(int(float(item['utLogMap']['current_price'])))
            writer.writerow([item['name'],price])


main()