import re


def clean_html(raw_html: str):
    cleaner = re.compile('<.*?>')
    clean_text = re.sub(cleaner, '', raw_html)
    return clean_text
