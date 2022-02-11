import feedparser, datetime

rss_uri="https://jeonyeohun.tistory.com/rss"
feed = feedparser.parse(rss_uri)

markdown_text = """
<div>
  <a href="https://jeonyeohun.tistory.com/">
<img
src="http://img.shields.io/badge/-Tech%20Blog-655ced?style=flat&logo=github&link=https://jeonyeohun.tistory.com/"
style="height : auto; margin-left : 10px; margin-right : 10px;" align="right"/>
</a>
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjeonyeohun&count_bg=%234A75FF&title_bg=%23FDFDFC&icon=&icon_color=%23E7E7E7&title=%F0%9F%91%8B&edge_flat=true" align="right" />
  <a href="https://solved.ac/hunihun956"><img src="http://mazassumnida.wtf/api/mini/generate_badge?boj=hunihun956" align="right" /></a>
</div>

<br/>

### 📚 Education

- **American School of Ulaanbaatar `졸업`** (2008.09 ~ 2014.06)<br/>
- **한동대학교 전산전자공학부 컴퓨터공학 `졸업`** (2015.03 ~ 2021.08)<br/>
- **네이버 커넥트재단 부스트캠프 웹모바일 6기 iOS `챌린지`** (2021.07 ~ 2021.08)<br/>
- **네이버 커넥트재단 부스트캠프 웹모바일 6기 iOS `멤버십`** (2021.08 ~ 2021.12)<br/>

### 🙋🏻‍♂️ Experiences

- **포항시 대안교육기관 청소년 자유학교의 `교사`** (2015.03 ~ 2021.06) </br>
- **한동대학교 지능형 소프트웨어공학 연구실의 `학부 연구생`** (2019.03 ~ 2021.06) </br>
- **교내 SW중심대학 주관, SW 교육 동영상 공모전 `대상 수상`** (2020.05 ~ 2020.08) </br>
- **한동대학교 통일선도대학 사업단의 `프론트엔드 개발자`** (2020.09 ~ 2021.03) </br>
- **대경권 프로그래밍 경진대회 `장려상 수상`** (2021.06 ~ 2021.06) </br>

### 👀 Projects

- 🤖 **한동새섬봇** : 1200+명의 불편함을 해결하는 교내외 정보제공 챗봇 🤖 [[GitHub](https://github.com/jeonyeohun/SaeSeomBot)][[홈페이지](https://pf.kakao.com/_XxaQyK)]
- 🏃🏻‍♂️ **Mate Runner** : 친구와 함께 달리는 실시간 런닝 앱 [[GitHub](https://github.com/boostcampwm-2021/iOS06-MateRunner)]


### ✍ Recent Blog Posts 
""" 

j=0
for i in feed['entries']:
    if i['category'] == "티-아이-엘":
        continue
    j+= 1
    if j >5:
        break
    else:
        dt = i['published']
        markdown_text += f"- [{i['title']}]({i['link']}) <br>\n"

print(markdown_text)
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()  
