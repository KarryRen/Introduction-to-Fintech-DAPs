# -*- coding: utf-8 -*-
# @Time    : 2024/10/20 12:10
# @Author  : Karry Ren

""" The config information. """

# ************************************************************************************ #
# ********************************** BASIC SETTINGS ********************************** #
# ************************************************************************************ #
RANDOM_SEED = [0, 42, 913][0]  # the random seed
SAVE_PATH = f"exp_factors/rs_{RANDOM_SEED}/"  # the save path of UCI electricity experiments
LOG_FILE = SAVE_PATH + f"log_{RANDOM_SEED}.log"  # the log file path
MODEL_SAVE_PATH = SAVE_PATH + "trained_models/"  # the saving path of models
IMAGE_SAVE_PATH = SAVE_PATH + "pred_images/"  # the saving path of pred images

# ************************************************************************************ #
# ************************************ FOR DATASET *********************************** #
# ************************************************************************************ #
FACTOR_DATA_PATH = "../../../Data"
TIME_STEPS = 1
BATCH_SIZE = 1024 * 2
FACTOR_NUM = 26

# ************************************************************************************ #
# ******************************* FOR NET CONSTRUCTING ******************************* #
# ************************************************************************************ #
LR = 0.001  # the learning rate
LOSS_REDUCTION = "mean"  # the loss reduction

# ************************************************************************************ #
# ********************************* FOR NET TRAINING ********************************* #
# ************************************************************************************ #
# ---- Train Model ---- #
EPOCHS = 1500
