import flask
from flask import request, render_template, url_for

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/content')
def content():
    option = request.args.get('selector')
    if option == 'msk':
        content = 'Арарат Парк Хаятт.\n' \
                  'Один из лучших отелей Москвы, который подарит вам незабываемые впечатления от посещения этого города.\n ' \
                  '40т. рублей за ночь'
        img = 'msk.png'
    elif option == 'ekb':
        content = 'Хаятт Плейс.\n ' \
                  'Крутой пятизвездочный отель прямо в центре Екатеринбурга.\n ' \
                  '35т. рублей за ночь'
        img = 'ekb.png'
    elif option == 'spb':
        content = 'AZIMUT Сити.\n ' \
                  'Один из отелей Санкт-Петербурга, достойный быть названным лучшим.\n ' \
                  '50т. рублей за ночь'
        img = 'spb.png'
    else:
        content = None
    return render_template('index.html', content=content, img=img)


if __name__ == "__main__":
    app.run(debug=True)
