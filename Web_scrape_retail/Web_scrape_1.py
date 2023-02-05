from bs4 import *
import requests
import sys
import lxml
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

headers = {"user-agent": USER_AGENT}
r = requests.get("https://www.statology.org/logistic-regression-vs-linear-regression/", headers=headers)
print("Status code: ", r.status_code)
if r.status_code == 200:
    # resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    #print(soup.prettify())

else:
    print("Code is not valid")
    sys.exit(0)

# name the output file to write to local disk
out_filename = "dq_test1.txt"
# Print heading and text in file
title = soup.find("header", {"class": "entry-header entry-header-single"}).text
# print (title)
results = soup.find("div",{"class":"entry-content entry-content-single"})
res_p = results.find_all("p")
# for p in res_p:
#     print(p.text)


f = open(out_filename, "w")
print(title, file=open(out_filename, "a"))
print(190*'#',file=open(out_filename, "a", encoding='utf-8'))
for p in res_p:
    my_text = p.text
    print(my_text, file=open(out_filename, "a", encoding='utf-8'))
f.close()  # Close the file


