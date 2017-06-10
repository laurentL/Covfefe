from distutils.core import setup

import sys

from pip.download import PipSession
from pip.req import parse_requirements, InstallRequirement

import covfefe


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


setup(
    name='covfefe',
    version=covfefe.__version__,
    packages=['covfefe'],
    url='https://github.com/laurentL/covfefe',
    license='GPL V3',
    author='laurent labatut',
    author_email='laurent@labatut.net',
    description='Set of base & helpers python api using  git@bitbucket.org:LoloCH/pythonsol.git',
    install_requires=resolv_requires()
)
