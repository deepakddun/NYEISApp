from flask import Flask, render_template

app = Flask(__name__)

children = [
    {
        'first': 'Alpha',
        'last': 'Pandey',
        'address': '10 Main Road, Texas, US',
        'dob': '15 April 2022'
    },
    {
        'first': 'Beta',
        'last': 'Pandey',
        'address': '10 Second Road, Texas, US',
        'dob': '10 April 2022'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', children=children , title='Children List')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
