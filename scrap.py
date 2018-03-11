import config
import db
import spider

snapshot = spider.scrap_snapshot()
db.save_snapshot(snapshot)
