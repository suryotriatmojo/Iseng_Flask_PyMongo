from pymongo import MongoClient

# connect to server, name x
x = MongoClient('mongodb://localhost:27017/')

# print(x.list_database_names())  # mendapatkan list database

db = x['suryo_db']
col = db['produk']

nama = input('Ketik nama produk: ')
harga = input('Ketik harga produk: ')

data = {'nama': nama, 'harga': int(harga)}
z = col.insert_one(data)    # memasukkan 1 data ke database mongo
print(z.inserted_id)        # mendapatkan id terakhir di-insert

for i in col.find({'_id': z.inserted_id}):
    print('Data sukses tersimpan!')
    print(i)