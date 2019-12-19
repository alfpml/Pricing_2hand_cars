import pandas as pd
import requests
import src.scrap_functions as sc_f
from bs4 import BeautifulSoup

##Coches particulares
links_part=sc_f.linksScrap(750,'https://www.coches.com/coches-segunda-mano/coches-segunda-mano-particulares.htm?page=')
cars_part=sc_f.carsScrap(links_part)
cars_part=pd.DataFrame(cars_part)
cars_part.to_csv('./output/cars_part.csv', index=False)


##Coches concesionarios
links_oca=sc_f.linksScrap(1350,'https://www.coches.com/coches-segunda-mano/coches-ocasion.htm?anyo_hasta=2018&vendedor=1')
cars_oca=sc_f.carsScrap(links_oca)
cars_ocaValencia=pd.DataFrame(cars_oca)
cars_oca.to_csv('./output/cars_oca.csv', index=False)