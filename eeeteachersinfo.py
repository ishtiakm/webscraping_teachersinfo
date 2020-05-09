def strremove(string,letter):
  string=list(string)
  letter=list(letter)
  for x in letter:
    string.remove(x)
  return ("").join(string)



from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
myurl="https://eee.buet.ac.bd/faculty"
uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()
file=open("teachers.txt","w")
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"col-lg-3 col-sm-6"})
for container in containers:
  name=container.findAll("div",{"class":"team_title radius_lbrb_10 text-center"})
  _,n,d,_=name[0].text.split("\n")
  file.write("Name:"+n+"\n")                   
  file.write("Designation:"+d+"\n") 
  name=container.findAll("div",{"class":"team_single_info"})
  a=(name[0].text).split("\n")
  data=[]
  for info in a:
    if bool(info):
      data.append(info)
  if len(data)==6:
    _,email,room,cell,site,_=data
  elif len(data)==5:
    room="Not_Given"
    _,email,cell,site,_=data
  file.write("Room_no.:"+room+"\n")                   
  file.write("Email_id:"+email+"\n")
  file.write("Cell:"+cell+"\n")                   
  file.write("Website:"+site+"\n")
  file.write("\n") 

file.close()
