# Assistant Tracker

Tracks assistants of deputies in Chamber of Deputies of the Czech Republic.

## Run

Install dependencies:

```
pip3 install --user -r requirements.txt
```

Create `.env` file with environment settings:

```
DB_CONNECTION_STRING=mongodb://localhost/ass_track
PYTHON_ENV=dev
```

Run web scraper to obtain latest data:

```
python3 scrap.py
```

Run website to show latest data:

```
python3 web.py
```
