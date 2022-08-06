
# Домашние задания по курсу Django-Rest-Framework

ДЗ №1
Реализовано:
* Собственная модель авторизации пользователя. 
* Добавлено свойство unique полю email
* Подключена стандартная админка на /admin/.
* Написан алгоритм генерации .env файла с секретным ключем для django
* Добавленны команды:
  * filldb - заполняет БД. При генерации пишет данные для авторизации.
  * cleardb - очищает БД  
* Имя супер пользователя admin - пароль смотри при выполнении filldb

## Порядок развертывания

```
git clone git@github.com:nekdfl/todoyou-gb.git
cd todoyou-gb
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py filldb
python manage.py runserver 127.0.0.1:8000
```
