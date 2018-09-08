from src.legacy.data_preparation import Datapreparation
from src.titanic_data_preparation import Titanic

if __name__ == "__main__":
    titanic_obejct = Titanic.getInstance("../data/train.csv", "../data/test.csv")
    print(titanic_obejct.training_object.dataframe)