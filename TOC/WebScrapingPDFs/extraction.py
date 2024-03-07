import requests

def extract_page_source(url):
    response = requests.get(url)
    return response.text


url = "https://www.cmi.ac.in/~madhavan/courses/aml2021/"
page_source = extract_page_source(url)

file_p  = "source.txt"

with open (file_p,"w") as file: 
    file.write(page_source)
    
