from flask import Flask
from flaskr.views.statistics import FacebookAdView

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# main API
facebook_ads_view = FacebookAdView.as_view('facebook-list')
app.add_url_rule('/api/facebook', methods=['GET', 'POST', 'PUT', 'DELETE'], view_func=facebook_ads_view)

if __name__ == '__main__':
    app.run()
