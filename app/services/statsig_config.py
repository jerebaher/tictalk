import statsig
from app.logger import logging
from app.config import STATSIG_API_KEY

statsig.initialize(STATSIG_API_KEY)
logging.info("Statsig client initialized successfully.")

def is_feature_enabled(user, feature):
    return statsig.check_gate(user, feature)