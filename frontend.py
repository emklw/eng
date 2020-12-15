# jesli importujemy tylko zwyklym import, backend file nie bedzie execu. output
# dlatego uzywamy : from 'file' import * (=asterix wszystko)


from backend import *
print(backend.translate("Orange"))