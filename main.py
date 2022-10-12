from bs4 import BeautifulSoup

import requests

website_header = ["data-science","digital-marketing","entrepreneurship","marketing","technology","ux"]
#here we created two list for storing program name and concepts covered points
header =[]
concepts=[]
Dict= {}

for head in website_header:
  #to hold data of each program 
  response = requests.get("https://knowthychoice.in/blog/ktc-intern-"+head)
  web_page = response.text
  
  soup = BeautifulSoup(web_page, "html.parser")
  h2 = soup.find('h2').getText()
  header.append(h2)  #storing all the program name into header list
  unordered = soup.find_all('ul') #here we hold all the ul in a program

  concept_list= unordered[5] #because concept covered point was in fifth unordered list of every program page

  eachProgram_concept_list =[] #here we store each concept points in this list 
  for ul in concept_list:
    eachProgram_concept_list.append(ul.getText())
    
  concepts.append(eachProgram_concept_list) #here we store all the concepts list together  


#using this loop we will create a dictionary
for h in header:
  for c in concepts:
    Dict[h]=c
    break;

print(str(Dict))
  


    




  
  
  



  
  
  
  
 
  
  
  


