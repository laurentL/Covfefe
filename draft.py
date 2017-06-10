import sys

from pip.download import PipSession
from pip.req import parse_requirements, InstallRequirement


def resolv_requires():
    """
    resolv dependencies
    :return:
    """

    if sys.version_info < (3, 4, 2):
        return_list = list()
        for item in parse_requirements('requirements_legacy.txt', session=PipSession()):

            assert isinstance(item, InstallRequirement)
            return_list.append(item.name)
        for item in parse_requirements('requirements.txt', session=PipSession()):
            assert isinstance(item, InstallRequirement)
            return_list.append(item.name)
        return return_list

    return parse_requirements('requirements.txt', session='hack')


t  = resolv_requires()

pass