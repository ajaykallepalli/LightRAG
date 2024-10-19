import requests
from bs4 import BeautifulSoup
import trafilatura
import PyPDF2
import fitz  # PyMuPDF
import io
import requests
from lxml import html



### EXTRACT URLS FROM WEBSITE

url = "https://arc.net/folder/D0472A20-9C20-4D3F-B145-D2865C0A9FEE"
page = requests.get(url)
tree = html.fromstring(page.content)

urls = tree.xpath('//a/@href')

print(urls)

def extract_text(url):
    try:
        # Determine if the URL is a PDF or a web page
        response = requests.get(url, stream=True)
        content_type = response.headers.get('Content-Type', '').lower()
        
        if 'application/pdf' in content_type:
            return extract_pdf_text(response.content)
        else:
            return extract_webpage_text(url)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None

def extract_webpage_text(url):
    # Try Trafilatura first
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    
    if text:
        return text
    
    # Fallback to BeautifulSoup if Trafilatura fails
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return ' '.join(soup.stripped_strings)

def extract_pdf_text(content):
    # Try PyPDF2 first
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except:
        # Fallback to PyMuPDF if PyPDF2 fails
        try:
            doc = fitz.open(stream=content, filetype="pdf")
            text = ''
            for page in doc:
                text += page.get_text()
            return text
        except:
            return None
        
# Extract text

for url in urls:
    text = extract_text(url)
    if text:
        print(f"Text extracted from {url}:")
        with open("papers.txt", "a") as f:
            f.write(f"\n\n")
            f.write(text)
            f.write("\n" + "\n")
    else:
        print(f"Failed to extract text from {url}")
    print("\n")