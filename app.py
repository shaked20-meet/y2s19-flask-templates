from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	food_1= ["ice cream", "pizza", "macaroons"]
	food_2 = ["rice", "avocado", "nuts"]
	opposite_day = False
	return render_template("index.html", food_1 = food_1,
		food_2 = food_2, opposite_day = opposite_day)


if __name__ == '__main__':
   app.run(debug = True)
