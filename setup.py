from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='vkapi',
      version='0.1.8',
      description='VK API for Python',
      author='Ivan Sosnovik',
      url='https://github.com/ISosnovik/vkAPI',
      packages=['.vkapi'],
      package_dir={'vkapi': ''},
      install_requires=reqs,
      )
