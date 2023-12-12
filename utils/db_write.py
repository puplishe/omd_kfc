from db.conn import connection


class Crud:
    def __init__(self, conn=connection()) -> None:
        self.conn = conn

    def write(self, data):
        cursor = self.conn.cursor()
        validated_data = self.validation(data)
        print(validated_data)
        cursor.execute('''
            INSERT INTO kfc_locations (name, city, address, latitude, longitude, breakfast_start, breakfast_end, open_time, closed_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', validated_data)
        self.conn.commit()
        return print('Data written into DB successfully')

    def validation(self, response_data):
        validated_data = (
            response_data['storePublic']['title']['ru'],
            response_data['storePublic']['contacts']['city']['ru'],
            response_data['storePublic']['contacts']['streetAddress']['ru'] if response_data['storePublic']['contacts']['streetAddress'] else None,
            response_data['storePublic']['contacts']['coordinates']['geometry']['coordinates'][1],
            response_data['storePublic']['contacts']['coordinates']['geometry']['coordinates'][0],
            response_data['storePublic']['menues'][0]['availability']['regular']['startTimeLocal'] if response_data[
                'storePublic']['menues'][0]['availability']['regular']['startTimeLocal'] else None,
            response_data['storePublic']['menues'][0]['availability']['regular']['endTimeLocal'] if response_data[
                'storePublic']['menues'][0]['availability']['regular']['endTimeLocal'] else None,
            response_data['storePublic']['openingHours']['regularDaily'][0]['timeFrom'] if response_data['storePublic']['openingHours']['regularDaily'] else None,
            response_data['storePublic']['openingHours']['regularDaily'][0]['timeTill'] if response_data['storePublic']['openingHours']['regularDaily'] else None
        )
        return validated_data

    def get_breakfast_data(self, city, breakfast_time):
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM kfc_locations
        WHERE city = ? AND breakfast_start <= ? AND breakfast_end >= ?
        ''', (city, breakfast_time, breakfast_time))

        result = cursor.fetchall()
        conn.close()
        return result
