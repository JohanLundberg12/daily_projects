from .train import train
from .test import test

# A library consists of packages (folders) which consists of files (modules)
# Specifying an init file lets us treat our folder like a module (a file)
# We thus avoid redundant imports such as "from model.model import train" or "from model.model import test"
# We can now simply use "from model import train" or "from model import test"
# This simplifies our imports
