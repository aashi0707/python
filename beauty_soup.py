from bs4 import beautifulsoup
import requests
response=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text
soup=bs4.BeautifulSoup(response,'lxml')
result=soup.find('table',class_='table')
a=[]
b=[]
c=[]
d=[]
e=[]
for row in result.findAll("tr"):
    cell=row.findAll('td')
    if len(cell)>0:
        a.append(str(cell[0].find(text=True)))
        b.append(str(cell[1].find(text=True)))
        c.append(str(cell[2].find(text=True)))
        d.append(str(cell[3].find(text=True)))
        e.append(str(cell[4].find(text=True)))
print(b)
print(a)
print(c)
print(d)
print(e)
