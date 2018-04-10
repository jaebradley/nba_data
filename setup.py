from setuptools import setup, find_packages
setup(
  name = 'nba_data',
  packages = find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34'],
  version = '1.9.2',
  description = 'An NBA Stats Client',
  author = 'Jae Bradley',
  author_email = 'jae.b.bradley@gmail.com',
  url = 'https://github.com/jaebradley/nba_data',
  download_url = 'https://github.com/jaebradley/nba_data/tarball/1.9.2',
  keywords = ['nba', 'nba_data'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7',
  ],
)
