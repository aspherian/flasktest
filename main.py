import flask
from flask import request, render_template, url_for
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = flask.Flask(__name__)

infocity = {
    'msk': {
        'content': 'Арарат Парк Хаятт.\n''Один из лучших отелей Москвы, который подарит вам незабываемые впечатления от посещения этого '
                   'города.\n ''40т. рублей за ночь',
        'img': 'msk.png',
        'content1': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре Москвы.\n 35т. рублей за ночь',
        'img1': 'ekb.png',
        'content2': 'AZIMUT Сити.\n ''Один из отелей Екатеринбурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img2": 'spb.png',
        "name" : "Moscow"
    },
    'ekb': {
        'content': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре Екатеринбурга.\n 35т. рублей за ночь',
        'img': 'ekb.png',
        'content1': 'AZIMUT Сити.\n ''Один из отелей Екатеринбурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img1": 'spb.png',
        'content2': 'Арарат Парк Хаятт.\n''Один из лучших отелей Екатеринбурга, который подарит вам незабываемые '
                    'впечатления от посещения этого'
                   'города.\n ''40т. рублей за ночь',
        'img2': 'msk.png',
        "name" : "Ekaterinburg"
    },
    'spb': {
        'content': 'AZIMUT Сити.\n ''Один из отелей Санкт-Петербурга, достойный быть названным лучшим.\n ''50т. рублей за ночь',
        "img": 'spb.png',
        'content1': 'Хаятт Плейc. Крутой пятизвездочный отель прямо в центре СПб.\n 35т. рублей за ночь',
        'img1': 'ekb.png',
        'content2': 'Арарат Парк Хаятт.\n''Один из лучших отелей Екатеринбурга, который подарит вам незабываемые '
                    'впечатления от посещения этого'
                   'города.\n ''40т. рублей за ночь',
        'img2': 'msk.png',
        "name" : "Saint-Petersburg"
    },
    'nsk' : {
        "name" : "Novosibirsk",
    },
    'irk' : {
        "name" : "Irkutsk"
    },
    'bar' : {
        "name" : "Barnaul"
    }
}



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/content')
def content():
    option = request.args.get('selector1')
    option1 = request.args.get('selector')
    name0 = infocity['{0}'.format(option1)]['name']
    name1 = infocity['{0}'.format(option)]['name']
    content = infocity['{0}'.format(option)]['content']
    img = infocity['{0}'.format(option)]['img']
    content1 = infocity['{0}'.format(option)]['content1']
    img1 = infocity['{0}'.format(option)]['img1']
    content2 = infocity['{0}'.format(option)]['content2']
    img2 = infocity['{0}'.format(option)]['img2']
    geolocator = Nominatim(user_agent="my_app")
    location1 = geolocator.geocode(infocity['{0}'.format(option1)]['name'])
    location2 = geolocator.geocode(infocity['{0}'.format(option)]['name'])
    distance = int(geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km)
    vremya = int(distance / 360)
    price = distance * 3
    return render_template('index.html', content=content, img=img, content1=content1, img1=img1, content2=content2, img2=img2, distance=distance, vremya=vremya, price = price, name0=name0, name1=name1)


if __name__ == "__main__":
    app.run(debug=True)
