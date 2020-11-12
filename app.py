from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
	y = "Home Page"
	return render_template('home.html', x=y)

@app.route('/store')
def Store():
	store_list = ['Water', 'Coke', 'Book', 'Guitar', 'Bar']
	return render_template('store.html', store_list=store_list)

@app.route('/test/<string:name>/')
def Test(name):
    return render_template('test.html', name = name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
