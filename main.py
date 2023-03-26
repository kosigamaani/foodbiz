from flask import Flask, render_template

app = Flask(__name__)

MENU = {
  "Starters": [{
    "id": 1,
    "title": "Veg Manchurian",
    "price": "Rs. 250",
  }, {
    "id": 2,
    "title": "Paneer Manchurian",
    "price": "Rs. 230",
  }, {
    "id": 3,
    "title": "Gobi Manchurian",
    "price": "Rs. 200",
  }, {
    "id": 4,
    "title": "Vadai",
    "price": "Rs. 20",
  }],
  "Main Course": [{
    "id": 5,
    "title": "Veg Unlimited Meals",
    "price": "Rs. 250",
  }, {
    "id": 6,
    "title": "Veg limited Meals",
    "price": "Rs. 230",
  }],
  "Beverages": [{
    "id": 7,
    "title": "Tea",
    "price": "Rs. 50",
  }, {
    "id": 8,
    "title": "Coffee",
    "price": "Rs. 30",
  }]
}


@app.route('/', methods=['GET'])
def root_path():
  return render_template('home.html', menu_dict=MENU)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
