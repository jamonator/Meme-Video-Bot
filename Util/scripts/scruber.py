import re

def scrub_text(text):
    # Remove question marks
    text = text.replace("?", "")
    
    # Remove non-alphanumeric and non-whitespace characters
    text = re.sub(r'[^\w\s]', '', text)
    
    return text
