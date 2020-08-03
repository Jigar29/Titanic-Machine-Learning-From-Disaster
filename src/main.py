from src.data_preparation import Datapreparation
from src.titanic import Titanic

if __name__ == "__main__":
    titanic_obejct = Titanic.getInstance("../data/train.csv", "../data/test.csv", "../data/submission.csv");
    titanic_obejct.prepareData()
    # titanic_obejct.representData()
    titanic_obejct.preProcessData()
    titanic_obejct.autoRun();
