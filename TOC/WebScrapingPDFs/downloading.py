import urllib.request
from finding import pdf_urls

pdf_url = pdf_urls[0]

file_path = "download.pdf"

urllib.request.urlretrieve(pdf_url, file_path)

