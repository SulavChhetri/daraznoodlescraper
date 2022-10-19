import requests
from bs4 import BeautifulSoup
import json,csv

cookies = {
    'lzd_cid': '38ed3dc4-336e-44c9-ba05-94fc712b19e8',
    't_uid': '38ed3dc4-336e-44c9-ba05-94fc712b19e8',
    'daraz-marketing-tracker': 'hide',
    'hng': 'NP|en-NP|NPR|524',
    'curTraffic': 'lazada',
    'userLanguageML': 'en-NP',
    't_fv': '1666197575285',
    't_sid': 'asU2BFPDG5wOfGFRujhLYvfQrIcMej9y',
    'utm_origin': 'https://www.google.com/',
    'utm_channel': 'SEO',
    '_tb_token_': 'eeb887f4bb0b1',
    'cna': 'RhbXG7zELA8CAWde/UHct1bO',
    'lzd_sid': '18940e250ba61a5d1de5ce9807ef212a',
    '_m_h5_tk': 'ccd8617a22f10c479e4d7f304f4c68be_1666208014919',
    '_m_h5_tk_enc': 'acca1d35bb788e351c16fb7a3012f0bb',
    '_gcl_au': '1.1.316952795.1666197576',
    '_gid': 'GA1.3.1444981138.1666197576',
    'xlly_s': '1',
    '_fbp': 'fb.2.1666197576207.461163837',
    'JSESSIONID': '35AD740B4E5F419D8D1D4672384FADE9',
    '_bl_uid': 'm6ljC9e9fFgvyb0v0p9w6dz1C1CX',
    '_ga_GEHLHHEXPG': 'GS1.1.1666197575.1.1.1666197593.0.0.0',
    '_ga': 'GA1.3.953840882.1666197576',
    'cto_bundle': 'cD5SE19ZYWpEdWU0N3hhMk9KdWxFa2hIR3FlVkIlMkZXOXNqeDVKJTJCYkdQYnRlM2E2Y3lvOGM3RExSYVpsdkl4cXVTR2phOHJBV09vVmJVJTJCVGtFclA1R3VIM2Q3VWFqbjhSNiUyQktzWW1RT0JEJTJGamR4eHFWYmJVWEFPQjQ0aFF1QyUyRnE1ZEVVUg',
    'isg': 'BAMDdYd_ZDrp6SjODVcBlKAkkseteJe6f-d3aDXhNWKH9CIWvUt_Cqcmbpy60u-y',
    'tfstk': 'c2kcB3YCDjPjIjptPqwXQGAmUbAda5d4lAkrUnQ4msTEsaMY0sb1a6RbP34vRE51.',
    'l': 'eBP1L6aHTsar-t4LBO5Bhurza77TCIOb8PVzaNbMiInca6GFtEC1nNCUHPe9SdtjQtfejetynVdhfdnkSiUdgI35nse2w4Ps_Y96-',
}

headers = {
    'authority': 'www.daraz.com.np',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.daraz.com.np/catalog/?q=noodles&_keyori=ss&from=input&spm=a2a0e.searchlist.search.go.259e18353yB7H1',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
}

params = {
    'q': 'noodles',
    '_keyori': 'ss',
    'from': 'input',
    'spm': 'a2a0e.searchlist.search.go.50e81835Uw3bpU',
}

r = requests.get('https://www.daraz.com.np/catalog/', params=params, cookies=cookies, headers=headers)

htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,"html.parser")

linkdict =soup.find_all("script")[-1].string
jsonresponse = json.loads(linkdict)
linknoodles = jsonresponse['itemListElement']
with open('output.csv','w')as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name","Price"])
    for item in linknoodles:
        link = item['url']
        request = requests.get(link).text
        content = BeautifulSoup(request,'html.parser')
        # a = content.find_all('script')[-11].text
        # price = "Rs."
        # pricelist = a.split('"')
        # pricelist= pricelist[5500:]
        # for i in range(len(pricelist)):
        #     print(pricelist[i])
        #     if pricelist[i] =='value':
        #         price =price+pricelist[i+1]
        #         break
        # print(price)
        productname = content.find_all('meta')[6]['content']
        writer.writerow([productname,])