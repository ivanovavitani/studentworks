<h1>Практическая работа №1</h1>
<h3>Создание GeoJSON из Excel с использованием MongoDB </h3>

* Импорт модулей
    > Были импортированы модули openpyexl, geojson, random и pymongo
    
* Написание функции прочтения файла exl
    > Функция читает лист в исходном файле data.exl, возвращает координаты, которые записываются в
  > массивы и объединяются с помощью zip
  
* Функция-генератор выборок
    > Функция генерирует выборки после подключения к базе данных MongoDB, создания базы данных, 
  > коллекции и пустых features
  
* Аргументы, features и коллекция
    > После создания списка координат формируем аргументы, features и их коллекции
  
* Создание GeoJSON
    > Происходит запись в файл формата GeoJSON и выгрузка в MongoDB
  
* Формирование выборок
    > Происходит формирование выборок на основе определенных атрибутов

