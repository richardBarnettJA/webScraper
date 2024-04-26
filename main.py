import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub User: ')

url = 'https://github.com/'+github_user

r = requests.get(url)
if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', { 'class' : 'avatar-user'})['src']
    print("Profile Image Link: ", profile_image)
else:
    print("User '" + github_user + "' not available!")