from core.utils import setup
from core.config import ConfigDjango, ConfigJazzmin, ConfigAPI


setup(locals(), ConfigDjango)
setup(locals(), ConfigJazzmin)
setup(locals(), ConfigAPI)