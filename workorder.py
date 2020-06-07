import requests
from bs4 import BeautifulSoup
import re

url = 'https://petro-canada.corrigo.com/Customer/Login.aspx'
values = {'UserName': 'Bo08156',
          'Password': 'Ellaabby1970',
          'Company': 'CBRE Suncor'}

s = requests.session()

r = s.post(url, data=values)

stuff = s.get('https://petro-canada.corrigo.com/Customer/Home')


soup = BeautifulSoup(stuff.text, "html.parser")


#print (stuff.text) 

# , string=('AssignedTo'))

stuff2 = soup.body.findAll('td')#, text='Open')

#stuff2 = soup.select('AssignedTo')

print(stuff2)





#for div in stuff2:
 #   print(div)
  #  print('-' *80)
