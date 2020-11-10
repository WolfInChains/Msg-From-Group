# VK-Msg-From-Group
Скрипт для отправки сообщений в беседу вк от имени группы. Также добавлен скрипт для получения айди нужной беседы для группы.
## Настройка
Открываем authorization.txt и вставляем токен группы

Для получения токена группы переходим в нужную группу:
```
Управление -> Настройки -> Работа с API -> Создать ключ -> Выставляем галочки и создаем
```
Для получения айди группы переходим в нужную группу:
```
Управление -> Настройки -> Адрес сообщества -> Номер сообщества -> club193643776 -> Копируем только цифры
```
## Компиляция
Чтобы собрать все в .exe файл используем команду:
```
pyinstaller -F MsgFromGroup.py
pyinstaller -F GetChatId.py
```
Чтобы все работало - помещаем .exe файл и authorization.txt в одну папку
