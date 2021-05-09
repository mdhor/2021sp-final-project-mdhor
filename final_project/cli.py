from luigi import WrapperTask, build
from luigi.util import requires

from .tasks import LoadPricesToDatabase, LoadProductsToDatabase


@requires(LoadProductsToDatabase, LoadPricesToDatabase)
class FinalProjectWrapper(WrapperTask):
    pass


def main():

    # Fix for removing unwanted logging by requests/bs4 in Travis
    import os
    import sys

    f = open(os.devnull, "w")
    sys.stdout = f

    build(
        [
            FinalProjectWrapper(
                categories=["mobiltelefoner", "smartklokker", "hodetelefoner"]
            )
        ],
        local_scheduler=True,
        log_level="INFO",
    )
