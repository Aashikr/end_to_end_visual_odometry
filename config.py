save_path = "/home/cs4li/Dev/end_to_end_visual_odometry/results"

class TrainConfigs(object):
    timesteps = 0
    batch_size = 0
    input_width = 0
    input_height = 0
    input_channels = 0

    data_source = "camera"

    base_dir = "/home/cs4li/Dev/KITTI/dataset/"

class SeqTrainConfigs(TrainConfigs):
    timesteps = 12
    batch_size = 1
    input_width = 1280
    input_height = 384
    input_channels = 1

    lstm_size = 256
    lstm_layers = 2

    num_epochs = 20
    k = 10

class SeqTrainLidarConfigs(TrainConfigs):
    timesteps = 12
    batch_size = 1
    input_width = 1152
    input_height = 64
    input_channels = 2

    lstm_size = 256
    lstm_layers = 2

    num_epochs = 20
    k = 10

    base_dir = "/media/bapskiko/SpinDrive/kitti/dataset/"
    pickle_dir = "/home/bapskiko/git/end_to_end_visual_odometry/pickles/"
    data_source = "lidar"

class PairTrainConfigs(TrainConfigs):
    timesteps = 1
    batch_size = 30

    input_width = 1280
    input_height = 384
    input_channels = 1

    num_epochs = 50
    k = 1
