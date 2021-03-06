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

### π Education

- **American School of Ulaanbaatar `μ‘Έμ`** (2008.09 ~ 2014.06)<br/>
- **νλλνκ΅ μ μ°μ μκ³΅νλΆ μ»΄ν¨ν°κ³΅νκ³Ό `μ‘Έμ`** (2015.03 ~ 2021.08)<br/>
- **λ€μ΄λ² μ»€λ₯νΈμ¬λ¨ λΆμ€νΈμΊ ν μΉλͺ¨λ°μΌ 6κΈ° iOS `μ±λ¦°μ§ μλ£`** (2021.07 ~ 2021.08)<br/>
- **λ€μ΄λ² μ»€λ₯νΈμ¬λ¨ λΆμ€νΈμΊ ν μΉλͺ¨λ°μΌ 6κΈ° iOS `λ©€λ²μ­ μλ£`** (2021.08 ~ 2021.12)<br/>

### ππ»ββοΈ Experiences

- **ν¬ν­μ λμκ΅μ‘κΈ°κ΄ μ²­μλ μμ νκ΅μ `κ΅μ¬`** (2015.03 ~ 2021.06) </br>
- **νλλνκ΅ μ§λ₯ν μννΈμ¨μ΄κ³΅ν μ°κ΅¬μ€μ `νλΆ μ°κ΅¬μ`** (2019.03 ~ 2021.06) </br>
- **κ΅λ΄ SWμ€μ¬λν μ£Όκ΄, SW κ΅μ‘ λμμ κ³΅λͺ¨μ  `λμ μμ`** (2020.05 ~ 2020.08) </br>
- **νλλνκ΅ ν΅μΌμ λλν μ¬μλ¨μ `νλ‘ νΈμλ κ°λ°μ`** (2020.09 ~ 2021.03) </br>
- **λκ²½κΆ νλ‘κ·Έλλ° κ²½μ§λν `μ₯λ €μ μμ`** (2021.06 ~ 2021.06) </br>

### π Projects

- π€ **νλμμ¬λ΄** : 1400+λͺμ λΆνΈν¨μ ν΄κ²°νλ κ΅λ΄μΈ μ λ³΄μ κ³΅ μ±λ΄ [[GitHub](https://github.com/jeonyeohun/SaeSeomBot)][[ννμ΄μ§](https://pf.kakao.com/_XxaQyK)]
- ππ»ββοΈ **Mate Runner** : μΉκ΅¬μ ν¨κ» λ¬λ¦¬λ μ€μκ° λ°λ μ± [[GitHub](https://github.com/boostcampwm-2021/iOS06-MateRunner)]


### β Recent Blog Posts 
""" 

j=0
for i in feed['entries']:
    if i['category'] == "ν°-μμ΄-μ":
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
