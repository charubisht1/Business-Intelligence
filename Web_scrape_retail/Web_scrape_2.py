
from bs4 import BeautifulSoup
import requests
import sys
import lxml
import csv
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

headers = {"user-agent": USER_AGENT}
r = requests.get("https://www.bewakoof.com/marvel-local-collection/sizes-XS--sizes-M--gender-women", headers=headers)

print("Status code: ", r.status_code)

if r.status_code == 200:
    soup = BeautifulSoup(r.content, "lxml")
else:
    print("Code is not valid")
    sys.exit(0)

items = soup.find("div", {"class": "categoryGridWrapper clearfix"})
item_name = items.find_all("div", {"class": "clr-shade4 h3-p-name"})
item_price = items.find_all("div", {"class": "discountedPriceText clr-p-black"})
out_filename = "dqtest3.csv"
headers = ["Item","Price"]
f = open(out_filename, "w+", encoding="ISO-8859-1", errors="ignore")
writer = csv.writer(f)
writer.writerow(headers)
a = []
b = []
for i in item_name:
    a.append(i.text)
for i in item_price:
    b.append(i.text)
for i in range(0,len(b)):
    c = a[i],b[i]
    writer.writerow(c)
f.close()  # Close the file
