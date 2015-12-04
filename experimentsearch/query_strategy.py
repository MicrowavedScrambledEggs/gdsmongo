from .models import Experiment, DataSource
from datetime import datetime, tzinfo, timedelta

ZERO = timedelta(0)


class UTC(tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


class AbstractQueryStrategy:
    """
    query_strategy for QueryMaker. All instances must have a file_name class
    field and an implemented create_model method

    Essentially tells the QueryMaker which file to save the query to and which
    model to build from the rows in the query file
    """

    @staticmethod
    def create_model(row):
        raise NotImplementedError("Concrete QueryStrategy missing this method")


class ExperimentQueryStrategy(AbstractQueryStrategy):

    file_name = "experi_list.csv"
    data_source_url = "data_source/?name="
    download_url = "download/"

    @staticmethod
    def create_model(row):
        # Creates and returns an experiment model from the values in the row
        name = row['name']
        who = row['pi']
        when = datetime.strptime(row['createddate'], "%Y-%m-%d %X.%f+00:00")
        when = when.replace(tzinfo=UTC())
        ds = ExperimentQueryStrategy.data_source_url + name.replace(" ", "+")
        dl = ExperimentQueryStrategy.download_url + name.replace(" ", "+") + "/"
        return Experiment(
            name=name, primary_investigator=who, date_created=when,
            download_link=dl, data_source=ds,
        )


class ExperimentUpdate(AbstractQueryStrategy):

    file_name = ExperimentQueryStrategy.file_name

    @staticmethod
    def create_model(row):
        # Creates and returns an experiment model from the values in the row
        name = row['name']
        who = row['pi']
        when = datetime.strptime(row['createddate'], "%Y-%m-%d %X.%f+00:00")
        when = when.replace(tzinfo=UTC())
        ds = ExperimentQueryStrategy.data_source_url + name.replace(" ", "+")
        dl = ExperimentQueryStrategy.download_url + name.replace(" ", "+") + "/"
        Experiment.objects.get_or_create(
            name=name, date_created=when,
            defaults={'primary_investigator': who, 'download_link': dl,
                      'data_source': ds}
        )


class DataSourceQueryStrategy(AbstractQueryStrategy):

    file_name = "ds.csv"

    @staticmethod
    def create_model(row):
        # Creates a models.DataSource from the values in the given row
        supplieddate = datetime.strptime(row['supplieddate'], "%Y-%m-%d").date()
        return DataSource(
            name=row['name'], is_active=row['is_active'], source=row['source'],
            supplier=row['supplier'], supply_date=supplieddate,
        )
