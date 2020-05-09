def strremove(string,letter):
  string=list(string)
  letter=list(letter)
  for x in letter:
    string.remove(x)
  return ("").join(string)

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
myurl="https://cse.buet.ac.bd/faculty/active_fac_short.php"
uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"faculty-block"})
file=open("CSEteachersMail.txt","w")
#container=containers[12]
for container in containers:
  name=container.findAll("a")
  file.write("Name:"+name[0].text+"\n")
  email=container.findAll("p",{"class":"faculty-email"})
  #print(email[0].text)
  emails=email[0].text.split(":")
  emails=emails[1].split(",")
  allmails=[]
  for mail in emails:
    data=mail
    
    if "AT" in mail:
      inp=mail.split("AT") 
      afterat=inp[1].split("DOT")
      for i,_ in enumerate(afterat):
        while(" " in afterat[i]):
          afterat[i]=strremove(afterat[i]," ")
      afterat=(".").join(afterat)
      while(" " in inp[0]):
        inp[0]=strremove(inp[0]," ")
      data=inp[0]+"@"+afterat
    
    elif "spam" in mail:
      continue
    else:
      while(" " in data):
        data=strremove(data," ")
    allmails.append(data)
  temp=(";").join(allmails)
  file.write("Emails:"+temp+"\n")
  file.write("\n")
file.close()  

    

