from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

_packages = ['vkapi', 'vkapi/methods']

setup(name='vkapi',
      version='0.1.14',
      description='VK API for Python',
      author='Ivan Sosnovik',
      url='https://github.com/ISosnovik/vkAPI',
      packages=_packages,
      install_requires=reqs,
      )
