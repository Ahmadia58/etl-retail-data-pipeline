from flask import Flask, jsonify
import random, uuid, datetime

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    return jsonify([
        {
            "order_id": str(uuid.uuid4()),
            "customer_name": f"Customer {i}",
            "amount": round(random.uniform(10, 1000), 2),
            "order_date": str(datetime.date.today())
        } for i in range(1000)
    ])

if __name__ == "__main__":
    app.run(debug=True)

