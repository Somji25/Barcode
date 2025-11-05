from flask import Flask, request, jsonify
import random, base64, io
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/generate_barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    prod_name = data.get('productName')
    category = data.get('category')
    
    abbr = {
        "ไฟฟ้า":"01","แมคคานิค":"02","ทั่วไป":"03"
    }.get(category, "XX")
    
    code = abbr + str(random.randint(100000,999999))
    
    buf = io.BytesIO()
    bc = barcode.get('code39', code, writer=ImageWriter())
    bc.write(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    
    return jsonify({"barcodeCode": code, "imageBase64": b64})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
