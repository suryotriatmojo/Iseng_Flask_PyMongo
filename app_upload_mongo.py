from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os # => ngatur path di mana file disimpan

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './simpan_gambar'
client = MongoClient('mongodb://localhost:27017/')
db = client['suryo_db']
col = db['cpns']

# home route
@app.route('/')
def home():
    return render_template('formulir.html')

# route GET & POST data
@app.route('/dataku', methods=['GET', 'POST'])
def dataku():
    if request.method == 'POST':
        nama = request.form['namaku']
        usia = request.form['usiaku']
        data = request.files['fotoku']                                # key ['file'] untuk mendapatkan file-nya dari request.files yg berupa type immutable dictionary
        namafile = secure_filename(data.filename)                       # mendapatkan nama file dari file yg diupload
        data.save(os.path.join(app.config['UPLOAD_FOLDER'], namafile))  # => jadinya ./simpan_gambar/namafile
        link = 'http://127.0.0.1:5000/kirim/' + namafile

        data = {
            "nama": nama,
            "usia": usia,
            "link": link
        }
        z = col.insert_one(data)
        print(z.inserted_id)

        cari = {'_id': z.inserted_id}

        for i in col.find(cari):
            nama_db = i['nama']
            usia_db = i['usia']
            link_db = i['link']

        return render_template('sukses.html', nama = nama_db, usia = usia_db, link = link_db)
    else:
        jml = col.find().count()
        # print(jml)
        if jml > 0:
            data_json = []
            for i in col.find():
                id = i['_id']
                nama = i['nama']
                usia = i['usia']
                link = i['link']
                data_dict = {
                    "_id": str(id),
                    "nama": nama,
                    "usia": usia,
                    "link": link
                }
                data_json.append(data_dict)
            return jsonify(data_json)
        else:
            return jsonify({'status': 'Tidak ada data'})
    

@app.route('/kirim/<bebas>')
def kirim_gambar(bebas):
    return send_from_directory('simpan_gambar', bebas)

# activate server
if __name__ == '__main__':
    app.run(debug = True)