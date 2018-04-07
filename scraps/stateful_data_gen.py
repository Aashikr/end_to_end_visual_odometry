import data
import config


train_data_gen = data.StatefulDataGen(config.SeqTrainConfigs, "/home/cs4li/Dev/KITTI/dataset/",
                                      ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"])
