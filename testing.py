import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueofgraphs.com/summoner/las/Joyita-LAS#championsData-flex'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    winrate = soup.find(id='graphDD8').text.strip()
    if winrate:
        print(winrate)
    else:
        print(f'No se encontró el winrate.')
    # Aquí puedes continuar con el paso siguiente
else:
    print(f'Error al obtener la página. Código de estado: {response.status_code}')


