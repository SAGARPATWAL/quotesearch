from setuptools import setup
setup(
  name = 'quotesearch',
  packages = ['quotesearch'], # this must be the same as the name above
  version = '0.1',
  description = 'Searching movie quotes from imdb',
  author = 'Sagar Patwal',
  install_requires= [
    'bs4',
    'mechanize'
  ],
  scripts= ['bin/quotesearch'],
  author_email = 'sagarpatwal@gmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)