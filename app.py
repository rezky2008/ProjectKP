from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['csvfile']
        if file.filename == '':
            return render_template('index.html', message='Pilih file CSV yang akan diunggah!')
        
        if file and file.filename.endswith('.csv'):
            # Simpan file ke direktori yang diinginkan
            filename2 = "static/data/"+file.filename
            file.save(filename2)
            
            # Proses file CSV
            with open(filename2, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                datas = list(csvreader)
            
            return render_template('index.html', message='File CSV berhasil diunggah!', data=datas)
        else:
            return render_template('index.html', message='Format file tidak didukung. Hanya file CSV yang diperbolehkan!')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
