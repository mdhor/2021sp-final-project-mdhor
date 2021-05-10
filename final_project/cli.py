import os
from unittest.mock import MagicMock

import django
from csci_utils.canvas.canvas import SubmissionHelper
from environs import Env
from luigi import WrapperTask, build
from luigi.util import requires

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()


from .tasks import LoadPricesToDatabase, LoadProductsToDatabase


@requires(LoadProductsToDatabase, LoadPricesToDatabase)
class FinalProjectWrapper(WrapperTask):
    pass


def main():
    """ Main for running project and submitting """
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

    env = Env()
    env.read_env()

    submission = SubmissionHelper.quick_start(
        env.str("CANVAS_URL"),
        env.str("CANVAS_TOKEN"),
        "CSCI E-29",
        "Final Project",
    )

    quiz_submission = MagicMock()
    quiz_submission.id = ""
    quiz_submission.attempt = ""

    submission.submit_assignment(quiz_submission, submit=True)
