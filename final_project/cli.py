from luigi import WrapperTask, build
from luigi.util import requires

from .tasks import LoadPricesToDatabase, LoadProductsToDatabase


@requires(LoadProductsToDatabase, LoadPricesToDatabase)
class FinalProjectWrapper(WrapperTask):
    pass


def main():
    build(
        [
            FinalProjectWrapper(
                categories=["mobiltelefoner", "smartklokker", "hodetelefoner"]
            )
        ],
        local_scheduler=True,
    )
