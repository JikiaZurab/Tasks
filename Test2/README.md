# Обмен валюты
## Запуск программы

Запустить программу можно двумя способами:

__I.__  Исполнив main.py прописав в командной строке из корневой папку, команда представленную ниже

```
python main.py
```
__НО__ Вам необходимо предварительно установить некоторые библиотеки:

```
pip install requests
pip install sqlalchemy
pip install sqlalchemy-utils
```

__II.__ Использовать Pull запрос с Docker. [Репозиторий на Docker-hub](https://hub.docker.com/repository/docker/brodzilla/py_currency_exchanger/general), где представлена вся информация о репозитории. Pull-запрос для данного репозитория выглядит так:

```
docker pull brodzilla/py_currency_exchanger:tagname
```

Далее Вы можете использовать в терминале команду

```
make run
```
или

```
docker run -it -v D:\PC\GitHub\Test1\Test2:/app --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix brodzilla/py_currency_exchanger
```

##Работа с программой

Запущенная программа выглядит подобным образом. Окно и виджету могут выглядеть слегка по-другому в зависимости от системы исполнителя.

