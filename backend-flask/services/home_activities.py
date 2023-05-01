from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging

from lib.db import db

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(logger, cognito_user_id=None):
    logger.info("HomeActivities")
    sql = db.template('create_home.sql')
    results = db.query_array_json(sql)
    return results