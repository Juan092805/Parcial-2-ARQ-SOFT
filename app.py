from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def calcular_factorial(num):
    factorial = math.factorial(num)
    
    etiqueta = "par" if factorial % 2 == 0 else "impar"
    
    return jsonify({
        "numero_recibido": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
