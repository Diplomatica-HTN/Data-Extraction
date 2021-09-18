from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests 

root = "https://www.google.com/"
search_engine_string = 'search?q='
search_engine_other_half = '&sxsrf=AOaemvIiKfd8dkMCkRXEhoZm3rjXFGMzCQ:1631931499445&source=lnms&tbm=nws&sa=X&ved=2ahUKEwikm8nKuofzAhUPElkFHVshBFUQ_AUoAnoECAEQBA&biw=1295&bih=697&dpr=2'
user_search = input("What would you like to search for?: ")
user_search = user_search.strip(" ")
new_link = root + search_engine_string + user_search + search_engine_other_half

link = new_link

#link = 'https://www.google.ca/search?q=politics&sxsrf=AOaemvIiKfd8dkMCkRXEhoZm3rjXFGMzCQ:1631931499445&source=lnms&tbm=nws&sa=X&ved=2ahUKEwikm8nKuofzAhUPElkFHVshBFUQ_AUoAnoECAEQBA&biw=1295&bih=697&dpr=2' 
 # Change this link after by switiching the keyword after q


lst = []
req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    #print(soup)
    for item in soup.find_all('div', attrs={'class':'kCrYT'}):
        try:
            try:
                raw_link = (item.find('a', href=True)['href'])
                link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
                if not link in lst:
                    lst.append(link)
                else:
                    pass
            except IndexError:
                break
        except TypeError:
            pass

print(lst)





