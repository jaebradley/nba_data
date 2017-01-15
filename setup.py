from setuptools import setup, find_packages
setup(
  name = 'nba_data',
  packages = find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34'],
  version = '1.0',
  description = 'A nba stats client',
  author = 'Jae Bradley',
  author_email = 'jae.b.bradley@gmail.com',
  url = 'https://github.com/jaebradley/nba_data', # use the URL to the github repo
  download_url = 'https://github.com/jaebradley/nba_data/tarball/1.1', # I'll explain this in a second
  keywords = ['nba', 'nba_data'], # arbitrary keywords
  classifiers = [],
)
