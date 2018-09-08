from src.data_preparation import Datapreparation, Titanic

if __name__ == "__main__":
    titanic_obejct = Titanic.getInstance("../data/train.csv", "../data/test.csv")
    print(titanic_obejct.training_object.dataframe)