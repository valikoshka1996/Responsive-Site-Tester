from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
from utils.screenshot import capture_screenshots
from utils.analyzer import analyze_site

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/screenshots'

# Перевірка наявності папки для збереження скріншотів
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Помилка при видаленні {file_path}: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder_size = get_folder_size(app.config['UPLOAD_FOLDER'])
        if folder_size > 10 * 1024 * 1024:
            clear_folder(app.config['UPLOAD_FOLDER'])
        url = request.form['url']
        session_id = str(uuid.uuid4())
        screenshot_paths = capture_screenshots(url, session_id)
        analysis = analyze_site(url)
        return render_template('result.html', screenshots=screenshot_paths, analysis=analysis)
    return render_template('index.html')

# Запуск сервера лише один раз
if __name__ == '__main__':
    app.run(debug=True, host='45.129.99.xx', port=5021)
