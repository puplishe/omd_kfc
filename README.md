# About 
Первое задание ТЗ от OMD group

# SQL Запрос
Реализована функция, которая делает SQL запрос по типу 
'''
        SELECT * FROM kfc_locations
        WHERE city = ? AND breakfast_start <= ? AND breakfast_end >= ?
        ''', (city, breakfast_time, breakfast_time))

В функцию необходимо передать интересующие параметры и будет выдан результат

Либо чистый SQL запрос 
SELECT * 
FROM kfc_restaurants
WHERE city = 'Новосибирск' AND breakfast_time <= '08:45';