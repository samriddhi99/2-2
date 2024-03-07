import re

with open("source.txt", "r") as file:
    string = file.read()
    
pattern = r'<a\s+[^>]*href\s*=\s*["\']([^"\'>]*lecture[^"\'>]*\.pdf)["\'][^>]*>(.*?)</a>'
pdf_links = re.findall(pattern, string)


pdf_urls = []
for pdf_link in pdf_links:
    pdf_urls.append("https://www.cmi.ac.in/~madhavan/courses/aml2021/" + pdf_link[0])

