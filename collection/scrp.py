import requests
from bs4 import BeautifulSoup

urls = ['https://ambuda.org/texts/raghuvamsham/1', 'https://ambuda.org/texts/raghuvamsham/2']

def extract_tags(url, tag_name, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        tags = soup.find_all(tag_name)

        with open(output_file, 'a', encoding='utf-8') as file:
            for tag in tags:
                file.write(str(tag) + '\n')

        return f"data appended to {output_file}"

    else:
        return f"Failed. Status code: {response.status_code}"

def cleanTags(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        content = input_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        clean_text = [tag.get_text(strip=True) for tag in soup.find_all('s-lg')]

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for text in clean_text:
            output_file.write(text + '\n')

    return f"Cleaned text written to {output_file}"

for url in urls:
    result = extract_tags(url, 's-lg', "output.txt")
print(result)

result = cleanTags('output.txt', 'cleaned_output.txt')
print(result)

