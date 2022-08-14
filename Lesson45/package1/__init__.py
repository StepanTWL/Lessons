print('__init__ package1')#будет выводиться при импортировании любого куска (пакета) из package1

from .file1 import * #после этого в main видно все file1, file2
from .file2 import *

# .  - текущий католог
# .. - выше каталога