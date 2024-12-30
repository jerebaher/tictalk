import statsig
from app.logger import logging
from app.config import get_settings

settings = get_settings()

if not settings.STATSIG_API_KEY:
    logging.error("Statsig API key is not set in the configuration!")
    raise ValueError("Statsig API key is missing!")

try:
    statsig.initialize(settings.STATSIG_API_KEY)
except:
    logging.error("Statsig API key not found.")

logging.info("Statsig client initialized successfully.")


def is_feature_enabled(user, feature):
    """
        Verifica si una característica está habilitada para un usuario.

        :param user: Objeto que contiene la información del usuario.
        :param feature: Nombre de la característica a verificar.
        :return: Booleano indicando si la característica está habilitada.
    """

    return statsig.check_gate(user, feature)
