import pytest
import sys
import subprocess
from libs.config.conf import ENVIRONMENT_PATH, CATEGORIES_PATH, RESULTS_PATH, REPORT_PATH

WIN = sys.platform.startswith('win')
HISTORY = REPORT_PATH + f'\history'

def main():

    steps = [
        "pytest",
        "copy {} allure-results".format(ENVIRONMENT_PATH) if WIN else "cp {} allure-results".format(ENVIRONMENT_PATH),
        "copy {} allure-results".format(CATEGORIES_PATH) if WIN else "cp {} allure-results".format(CATEGORIES_PATH),
        "copy {} {}".format(HISTORY,RESULTS_PATH) if WIN else "cp {} allure-results".format(PROPERTIES_PATH),
        "allure generate allure-results -c -o allure-report",
        "allure open allure-report"
    ]

    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == '__main__':
    main()
