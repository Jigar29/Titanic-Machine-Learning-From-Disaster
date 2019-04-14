from src.data_preparation import Datapreparation
from src.titanic import Titanic
from src.data_preprocessing import DaraPreprocessing

if __name__ == "__main__":
    titanic_obejct = Titanic.getInstance("../data/train.csv", "../data/test.csv");
    titanic_obejct.autoRun();
