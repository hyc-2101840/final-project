from flask import Flask, request, render_template, jsonify
from pipeline import classifyImg
app = Flask(__name__)
def process_image(net, link):
    result = classifyImg(net, url=link)
    return result
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_text = request.form['text'] if request.form['text'] != '' else 'test.jpg'
        network = "resnet18.onnx"
        result = process_image(network, user_text)
        return jsonify({'result': result})  
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)