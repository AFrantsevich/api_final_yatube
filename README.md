### Краткое описание:
Это учебный проект API, был создан для отработки на практике полученных знаний в области DRF.
Данный код позволяет взаимодействовать по средствам интерфейса API с нашим проектом на Django из прошлого спринта.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AFrantsevich/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

>**Получение JWT токена**

*POST запрос:*

```http://127.0.0.1:8000/api/v1/jwt/create/```

*JSON тело запроса:*
```
{
"username": "string",
"password": "string"
}
```
*Ответ:*
```
{
"refresh": "string",
"access": "string"
}
```

>**Создание поста**

*POST запрос на эндпоинт:*

```http://127.0.0.1:8000/api/v1/posts/ ```

*JSON тело запроса:*
```
{
"text": "string",
"image": "string",
"group": 0
}
```
*Ответ:*
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

>**Добавление комментария**

*POST запрос на эндпоинт:*

```http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ ```

*JSON тело запроса:*
```
{
"text": "string"
}
```
*Ответ:*
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```


### Все ключевые эндпоинты можно получить по запросу:

```
http://127.0.0.1:8000/api/
```