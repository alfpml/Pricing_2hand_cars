import pandas as pd
import requests
from bs4 import BeautifulSoup

def linksScrap(lim,url):
    ##lim=750
    pages=[i for i in range(lim-1)]
    links=[]
    for i in pages:
        ##url = 'https://www.coches.com/coches-segunda-mano/coches-segunda-mano-particulares.htm?page={}'.format(i)
        soup = BeautifulSoup((requests.get(url+str(i))).text, 'html.parser')
        pl1 = soup.findAll('a',{"class":"pill-information","class":"primary-link"})
        for e in pl1:
            links.append(e.get('href'))
    return links


def linksScrap2(lim1,lim2,url):
    ##lim=750
    pages=[i for i in range(lim1,lim2)]
    links=[]
    for i in pages:
        ##url = 'https://www.coches.com/coches-segunda-mano/coches-segunda-mano-particulares.htm?page={}'.format(i)
        soup = BeautifulSoup((requests.get(url+str(i))).text, 'html.parser')
        pl1 = soup.findAll('a',{"class":"pill-information","class":"primary-link"})
        for e in pl1:
            links.append(e.get('href'))
    return links

def carsScrap(links):
    cars=[]
    for l in links:
        ##Getting URLS
        soup = BeautifulSoup((requests.get(l)).text, 'html.parser')
        ##Labels
        featureLabels = soup.findAll('div',{"class":"index-card__technical-data-label"})
        labels=[(e.get_text('div')).strip() for e in featureLabels] 
        ##Values
        feautureValues = soup.findAll('div',{"class":"index-card__technical-data-info"})
        values=[(e.get_text('div')).strip() for e in feautureValues] 
        ##creating Tuple
        features = zip(labels,values)
        ##creating dict
        featuresD = dict(features)
        ##modelo
        models = soup.findAll('ol',{"class":"breadcrumb breadcrumb--index-card"})
        mod=[]
        for e in models:
            for i in range(len(e.find_all("a"))):
                mod.append(((e.find_all("a")[i]).get_text('li')))
                ##adding modelo
                featuresD['model']=mod
            cars.append(featuresD)
    return cars

