from flask import Flask, request, jsonify
from services.hotel_service import HotelService

app = Flask(__name__)

# Route pour comparer les prix d'hôtels
@app.route('/compare/hotels', methods=['GET'])
def compare_hotels():
    destination = request.args.get('destination')
    check_in = request.args.get('check_in')
    check_out = request.args.get('check_out')
    guests = request.args.get('guests', 1)
    
    if not all([destination, check_in, check_out]):
        return jsonify({'error': 'Missing parameters'}), 400
    
    service = HotelService()
    results = service.compare_prices(destination, check_in, check_out, guests)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
