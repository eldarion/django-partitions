import sys, os

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'django-partitions'
package = 'partitions'
copyright = u'2011, Eldarion'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = '%sdoc' % package
latex_documents = [
  ('index', '%s.tex' % package, u'%s Documentation' % package,
   u'Eldarion', 'manual'),
]
man_pages = [
    ('index', package, u'%s Documentation' % package,
     [u'Eldarion'], 1)
]

sys.path.insert(0, os.pardir)
m = __import__(package)

version = m.__version__
release = version
