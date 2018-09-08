from src.titanic_data_preparation import Titanic

if __name__ == "__main__":
    titanic_obejct = Titanic.getInstance("../data/train.csv", "../data/test.csv");
    titanic_obejct.representData();
    titanic_obejct.autoRun();
