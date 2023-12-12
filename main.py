from api.kfc_api import get_api_data
from db.conn import dbinit
from utils.db_write import Crud

if __name__ == '__main__':
    dbinit()
    data = get_api_data()
    written = Crud()
    # for item in data:
    # print(item)
    # written.write(item)
    print(written.get_breakfast_data('Новосибирск', '08:45:00'))
