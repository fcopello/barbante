""" Tests barbante.api.process_activity_fastlane.
"""

import json

import nose.tools

import barbante.api.process_activity_fastlane as script
import barbante.utils.logging as barbante_logging
import barbante.tests as tests


log = barbante_logging.get_logger(__name__)


def test_script():
    """ Tests a call to script barbante.api.process_activity.
    """
    result = script.main([tests.TEST_ENV, "xxx", "ppp", "buy", "2014-01-01T00:00Z"])
    log.debug(result)
    result_json = json.dumps(result)
    nose.tools.ok_(result_json)  # a well-formed json is enough


if __name__ == '__main__':
    test_script()