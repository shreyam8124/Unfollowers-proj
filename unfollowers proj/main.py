from bs4 import BeautifulSoup


with open('following.html', 'r', encoding='utf-8') as file:
    following = file.read()
with open('followers.html', 'r', encoding='utf-8') as file:
    followers = file.read()

following = BeautifulSoup(following, 'html.parser')
followers = BeautifulSoup(followers, 'html.parser')

spans_following = following.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
idsOfFollowing = [span.text.strip() for span in spans_following]

spans_followers = followers.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
idsOfFollowers = [span.text.strip() for span in spans_followers]

for ids in idsOfFollowing:
    if ids not in idsOfFollowers:
        print(ids)
