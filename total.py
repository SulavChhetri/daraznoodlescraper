import requests
import json,csv,pandas as pd


with open('./files/stopwords.txt', 'r')as file:
    lines = [line.rstrip('\n') for line in file]


def scrape(darazurl):
    r = requests.get(darazurl).text
    jsonresponse = json.loads(r.split("window.pageData=")[1].split('</script>')[0])
    mainlist = jsonresponse['mods']['listItems']
    with open('productprice.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Product name','Price'])
        for item in mainlist:
            price = 'Rs.'+ str(int(float(item['utLogMap']['current_price'])))
            writer.writerow([item['name'],price])

def stopwordsremover(sentence):
    nostopword_sentence =list()
    for item in sentence.split():
        if not item.lower() in lines:
            nostopword_sentence.append(item)
    return nostopword_sentence

def remove_punctuation(sentence):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    finalsentence=""
    for item in sentence:
        if item not in punc:
            finalsentence+=item
    return finalsentence

def ngramcreator(strings,n_grams):
    finallist = []
    nostopword = stopwordsremover(strings)
    nostopword =' '.join(nostopword)
    splitlist = remove_punctuation(nostopword).split()
    n_grams_range = len(splitlist)-n_grams+1
    if (len(splitlist)<n_grams):
        return [remove_punctuation(strings)]
    else:
        for x in range(n_grams_range):
            finalstring = '' 
            for i in range(n_grams):  
                finalstring =finalstring+' '+splitlist[x+i]
            finallist.append(finalstring.lstrip())
        return finallist


def quantitygen(item):
    quantitylist = ['Packs','packs','Pack of','pcs','Pieces','Pack','RamenPack']
    n_gram = ngramcreator(item,2)
    for items in n_gram:
        if not (''.join(items.split()).isalpha()):
            for ite in items.split():
                if ite in quantitylist:
                    for itee in items.split():
                        if itee.isnumeric():
                            return itee


def csvquantity():
    products = pd.read_csv('productprice.csv')
    product_name= list(products['Product name'])
    product_price = list(products['Price'])
    with open('pp_quantity.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Price','Quantity'])
        for value in range(len(product_name)):
            quantity = quantitygen(product_name[value])
            if quantity==None:
                quantity =1
            writer.writerow([product_name[value],product_price[value],quantity])


def main(url):
    try:
        csvquantity()
    except:
        scrape(url)
        csvquantity()

main('https://www.daraz.com.np/catalog/?_keyori=ss&from=input&page=1&q=noodles')