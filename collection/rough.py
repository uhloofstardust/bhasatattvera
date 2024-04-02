url_file = 'urls.txt'

with open(url_file, 'r', encoding='utf-8') as file:
    urls = (file.read()).split('\n')
    
