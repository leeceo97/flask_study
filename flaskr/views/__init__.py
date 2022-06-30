from flask import Flask
from flaskr.views.statistics import FacebookAdView, FacebookAdDetailView

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# main API
facebook_ads_view = FacebookAdView.as_view('facebook-list')
facebook_ads_detail_view = FacebookAdDetailView.as_view('facebook-detail')
app.add_url_rule('/api/facebook', methods=['GET', 'POST'], view_func=facebook_ads_view)
app.add_url_rule('/api/facebook/<string:name>', methods=['GET', 'PUT', 'DELETE'], view_func=facebook_ads_detail_view)
if __name__ == '__main__':
    app.run()
