import logging
import json
import fire

from model import SIC
from util import StringWrapper, pretty_print, timeit


URL = "https://www.osha.gov/pls/imis/sic_manual.html"
DEFAULT_INDUSTRY_FILE = "industries.json"

logger = logging.getLogger(__name__)


class Main(object):

    @staticmethod
    @timeit(logger)
    def download(filename=DEFAULT_INDUSTRY_FILE):
        logger.info("Starting download procedure...")
        sic = SIC.from_url(URL)
        with open(filename, "w") as file:
            file.write(sic.jsonify())
        pass

    @timeit(logger)
    def search(self, title, exact=False, filename=DEFAULT_INDUSTRY_FILE):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
