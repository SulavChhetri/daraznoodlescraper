from asyncio.windows_events import NULL
import pandas as pd
import csv

with open('./files/stopwords.txt', 'r')as file:
    lines = [line.rstrip('\n') for line in file]

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

def weightgen(item):
    items = item.split()
    a = ''.join(items).lower()
    weight = []
    for i in range(len(a)):
        if a[i].isnumeric():
            if not weight:
                weight.append(a[i])
            else:
                weight.append(a[i])
                if a[i+1]=='g':
                    return str(''.join(weight))
        else:
            weight= []


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

def main():
    products = pd.read_csv('./files/output.csv')
    product_name= list(products['Product name'])
    product_price = list(products['Price'])
    with open('final.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Price','Quantity','Weight','Unit of Weight'])
        for value in range(len(product_name)):
            weight = weightgen(product_name[value])
            quantity = quantitygen(product_name[value])
            if quantity==None:
                quantity =1
            if weight ==None:
                writer.writerow([product_name[value],product_price[value],quantity,weight])
                continue
            writer.writerow([product_name[value],product_price[value],quantity,weight,'gm'])

        


main()