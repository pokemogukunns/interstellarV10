from flask import Flask, send_from_directory

app = Flask(__name__)

# デフォルトのルートまたはindexの場合、index.htmlを返す
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def serve_index():
    return send_from_directory('.', 'index.html')

# それ以外のすべてのリクエストをキャッチしてindex.jsを返す
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('.', 'index.js')

if __name__ == '__main__':
    app.run(debug=True)
