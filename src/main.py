from src.data_preparation import Datapreparation

if __name__ == "__main__":
    train_data_obj = Datapreparation("../data/train.csv")
    train_data_obj.createDataFrameFromCSVFile()
    test_data_obj = Datapreparation("../data/test.csv")
    test_data_obj.createDataFrameFromCSVFile()