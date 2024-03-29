import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1, 46), 6)
    print(numbers)
    return render_template('lotto.html', numbers=numbers)

@app.route('/lunch')
def lunch():
    menus = ['짜장면', '짬뽕', '파스타', '나주곰탕']
    pick = random.choice(menus)
    return render_template('lunch.html', pick=pick)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def search():
    opgg_url = 'https://www.op.gg/summoner/userName='
    summoner = request.args.get('summoner')
    url = opgg_url + summoner
    
    res = requests.get(url).text
    
    soup = BeautifulSoup(res, 'html.parser')
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
    user_tier = tier.text.strip()

    return render_template('search.html', user_tier=user_tier, summoner=summoner)

if __name__ == "__main__":
    app.run(debug=True)