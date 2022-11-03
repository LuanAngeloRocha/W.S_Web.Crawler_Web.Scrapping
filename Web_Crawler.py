import requests 
import re


url = "https://www.fatecpompeia.edu.br/cursos"

r = requests.get(url)
html = r.text.encode("utf8")
search = re.search(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))

print(r.text)