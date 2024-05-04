# downradar.py-tool
# это библиотека была создана только лишь для примера работы requests + pypasser я ни коим образом не пытаюсь невредить сайту downradar.ru 
# если вы создатель downradar.ru то можете со мной связатся по почте 1nveak7lcbzi@mail.ru и я удалю данный репозиторий

для начала установите [ffmpeg](https://ffmpeg.org/) и положите в папку с библиотекой

```py
import downradar #ставим библиотеку
```

пример page
```py
page = downradar.page('example.com')

page.send_comment('username', 'title', 'comment') #отправляем комментарий на страницу
page.ping() #отправляем запросы то что не работает сайт
```

пример comments
```py
comments = downradar.comments(1337) #id комментария можно узнать при наведении на решётку возле имени

comments.dislike() #думаю тут всё понятно нравится и не нравится
for i in range(5):
    comments.like()
```
