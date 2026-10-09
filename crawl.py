from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup, Tag
from html.parser import HTMLParser

def normalize_url(url: str) -> str:
    parsed = urlsplit(url)
    return parsed.netloc + '/' + parsed.path.strip('/')

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    h_tag = soup.find('h1') or soup.find('h2')
    return h_tag.get_text(strip=True) if isinstance(h_tag, Tag) else ''

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    main_tag = soup.find('main')
    if main_tag:
        p_tag = main_tag.find('p')
    else:
        p_tag = soup.find('p')
    return p_tag.get_text(strip=True) if isinstance(p_tag, Tag) else ''

def get_urls_from_html(html: str, base_url: str):
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup('a')
    if not anchors:
        return []
    urls = [href for anchor in anchors if (href := anchor.get('href')) is not None]
    parsed_urls = [urljoin(base_url, link) for link in urls]
    return parsed_urls
