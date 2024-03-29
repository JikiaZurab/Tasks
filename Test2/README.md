# Обмен валюты
## Запуск программы

Запустить программу можно двумя способами:

__I.__  Исполнив main.py, прописав в командной строке из корневой папки, команду представленную ниже

```
python main.py
```
__Обратите внимание,__ Вам необходимо предварительно установить некоторые библиотеки:

```
pip install requests
pip install sqlalchemy
pip install sqlalchemy-utils
```

__II.__ Использовать Pull запрос с Docker. [Репозиторий на Docker-hub](https://hub.docker.com/repository/docker/brodzilla/py_currency_exchanger/general), где представлена вся информация о репозитории. Pull-запрос для данного репозитория выглядит так:

```
docker pull brodzilla/py_currency_exchanger:tagname
```

Далее Вы можете использовать в терминале следующую команду. Не забудьте включить Xming в вашей Windows системе или XQuartz для MacOS.

```
make run
```
или

```
docker run -it -v D:\PC\GitHub\Test1\Test2:/app --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix brodzilla/py_currency_exchanger
```


## Работа с программой

Запущенная программа выглядит подобным образом. Окно и виджету могут выглядеть слегка по-другому в зависимости от системы исполнителя.

![Главное окно программы](https://github.com/JikiaZurab/Test1/assets/22364092/52d4be37-75d0-4d2d-9f1a-608632d5cbb5)

Надпись сверху отвечает за предоставление информации о наличии данных по курсу валют. Если надпись гласит "Нет данных о курсах валют", это значит у программы нет БД, из которой она могла бы взять информацию. В противном случае надпись будет нести информацию о свежести курса валют, как представлено ниже:

![Подключена БД](https://github.com/JikiaZurab/Test1/assets/22364092/4ca0cdf9-27df-4064-bc1b-eeec174c8a8c)

### Кнопка "Обмен Валюты"

Для обмена валюты необходимо соблюсти несколько правил. Во-первых, если вы не введете сумму для обмена, Вы не сможете получить желаемого результата, но над кнопкой появится подсказка.

![Вы не ввели сумму для обмена](https://github.com/JikiaZurab/Test1/assets/22364092/21d370f5-4230-40e7-a979-5270f5e8e43e)

Во-вторых, не имея курса валют Вы также не сможете получить результата и над кнопкой снова появится подсказка.

![Пожалуйста, получитк сначала курс валют](https://github.com/JikiaZurab/Test1/assets/22364092/2129e9cb-8fdc-4863-a38e-312e76f4b95d)

В-третьих, Вы должны выбрать в верхнем выпадающем списке валюту, которую хотите обменять, а в нижнем которую хотите получить. Если все сделано правильно Вы увидите необходимую Вам информацию над кнопкой.

 ![Обмен валюты](https://github.com/JikiaZurab/Test1/assets/22364092/f1b44aae-3f00-472f-85d7-ef12525774d0)

### Кнопка "Посмотреть курс"

Если БД нет, то данная кнопка просто выводит сообщение.

![Просотр курса валют без БД](https://github.com/JikiaZurab/Test1/assets/22364092/40ed517c-4051-4064-894d-aa1a51b8a7e0)

В противном случае, откроется вспомогательное окно с курсом всех валют относительно курса USD.

![Вспомогательное окно](https://github.com/JikiaZurab/Test1/assets/22364092/5c1e8720-2202-4a59-8ad0-ca2e3813e77f)

### Кнопка "Получить актуальный курс"

Это кнопка создает/переписывает БД внося в нее актуальный курс валют. Курс валюты получается при помощи [ExchangeRate-API](https://www.exchangerate-api.com/docs/python-currency-api)

### БД

База данных _currencyRates.db_ состоит из одной таблицы _Currency_. Таблица имеет следующий вид.


| id (PK) | currency (varchar) | rate (real) | date (date) |
| ----------- | ----------- | ----------- | ----------- |
| 1 |'USD' | 1.0 | Fri, 02 Jun 2023 00:00:01 +0000|
| ***    | ***   |*** | ***   |








