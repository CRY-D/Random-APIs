from urllib.parse import urljoin
from bs4 import BeautifulSoup
from flask import Blueprint, render_template
from app.models import Entry
from sqlalchemy.sql import func
import requests

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/get_random_row')
def get_random_row():
    entry = Entry.query.order_by(func.random()).first()
    return render_template("main/random.html", entry=entry)


@main_bp.route('/check_status/<path:api_link>', methods=["GET"])
def check_api_status(api_link):
    try:
        favicon_url = None
        response = requests.get(api_link)
        favicon_url = get_favicon_url(response)
        if response.status_code == 200:
            return render_template("main/_status.html", favicon_url=favicon_url, success=True)
        else:
            return render_template("main/_status.html", favicon_url=favicon_url, success=False)

    except requests.RequestException:
        return render_template("main/_status.html", favicon_url=favicon_url, success=False)


def get_favicon_url(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_tag = soup.find('link', rel=['icon', 'shortcut icon'])
    if favicon_tag and 'href' in favicon_tag.attrs:
        favicon_url = urljoin(response.url, favicon_tag['href'])
        return favicon_url
    else:
        return None
