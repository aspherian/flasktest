import flask
from flask import request, render_template, url_for

app = flask.Flask(__name__)

infocity = {
    'moscow': {
        'content': 'Арарат Парк Хаятт.\n''Один из лучших отелей Москвы, который подарит вам незабываемые впечатления от посещения этого '
                   'города.\n ''40т. рублей за ночь',
        'img': 'msk.png',
        'content1': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре Москвы.\n 35т. рублей за ночь',
        'img1': 'ekb.png',
        'content2': 'AZIMUT Сити.\n ''Один из отелей Екатеринбурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img2": 'spb.png'
    },
    'ekaterinburg': {
        'content': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре Екатеринбурга.\n 35т. рублей за ночь',
        'img': 'ekb.png',
        'content1': 'AZIMUT Сити.\n ''Один из отелей Екатеринбурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img1": 'spb.png',
        'content2': 'Арарат Парк Хаятт.\n''Один из лучших отелей Екатеринбурга, который подарит вам незабываемые '
                    'впечатления от посещения этого'
                   'города.\n ''40т. рублей за ночь',
        'img2': 'msk.png'
    },
    'sanktptb': {
        'content': 'AZIMUT Сити.\n ''Один из отелей Санкт-Петербурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img": 'spb.png',
        'content1': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре СПб.\n 35т. рублей за ночь',
        'img1': 'ekb.png',
        'content2': 'Арарат Парк Хаятт.\n''Один из лучших отелей Екатеринбурга, который подарит вам незабываемые '
                    'впечатления от посещения этого'
                   'города.\n ''40т. рублей за ночь',
        'img2': 'msk.png'
    }
}


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/content')
def content():
    option = request.args.get('selector')
    if option == 'msk':
        content = infocity['moscow']['content']
        img = infocity['moscow']['img']
        content1 = infocity['moscow']['content1']
        img1 = infocity['moscow']['img1']
        content2 = infocity['moscow']['content2']
        img2 = infocity['moscow']['img2']
    elif option == 'ekb':
        content = infocity['ekaterinburg']['content']
        img = infocity['ekaterinburg']['img']
        content1 = infocity['ekaterinburg']['content1']
        img1 = infocity['ekaterinburg']['img1']
        content2 = infocity['ekaterinburg']['content2']
        img2 = infocity['ekaterinburg']['img2']
    elif option == 'spb':
        content = infocity['sanktptb']['content']
        img = infocity['sanktptb']['img']
        content1 = infocity['sanktptb']['content1']
        img1 = infocity['sanktptb']['img1']
        content2 = infocity['sanktptb']['content2']
        img2 = infocity['sanktptb']['img2']
    else:
        content = None
    return render_template('index.html', content=content, img=img, content1=content1, img1=img1, content2=content2, img2=img2)


if __name__ == "__main__":
    app.run(debug=True)
