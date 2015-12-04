import urllib, urlparse, os

from .query_maker import QueryMaker
from .query_strategy import ExperimentUpdate
from .views import experi_table_url
from .errors import QueryError

# sync_url = experi_table_url
# When genotype database down:
sync_url = urlparse.urljoin('file:', urllib.pathname2url(
    "C:/Users/cfpbtj/PycharmProjects/genotypedatasearch/experi_list.csv"
))


def sync_with_genotype_db():
    syncer = QueryMaker(ExperimentUpdate)
    try:
        syncer.make_query('', sync_url)
    except QueryError as e:
        print("Syncing Failed because:\n" + str(e))