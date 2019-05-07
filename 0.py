from pymongo import MongoClient

# connect to server, name x
x = MongoClient('mongodb://localhost:27017/')

# print(x.list_database_names())  # mendapatkan list database

db = x['suryo_db']
col = db['produk']
cari = {'harga': {'$gt': 1000000}}
cari2 = {'nama': 'Headset'}

# print(col.find())           # keluarnya object <pymongo.cursor.Cursor object at 0x10455df98>
# print(list(col.find()))     # keluar list data di dalam database suryo_db

# for i in col.find():
#     print(i)                  # keluar langsung dictionary

for i in col.find(cari2):
    print(i)