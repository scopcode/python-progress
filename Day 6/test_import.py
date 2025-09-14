from make_models import make_models 
from make_models import make_models as mm
import model_prepared as mp
from model_prepared import *

unfinised_1 = ["Tajmahal", "Qutub Minar", "Ram Madir", "Red fort"]
finished_1 = []
make_models(finished_1,unfinised_1)
unfinished_2 = ["billboard", "Alchemy", "physics", "chemistry"]
finished_2 = []
mm(finished_1,unfinished_2)

model_prepared(finished_1)
mp.model_prepared(finished_2)