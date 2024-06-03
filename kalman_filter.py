import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cm
import pandas as pd

class KalmanFilter:
    """
    Kalman filter for aircraft data
    """

    def __init__(self, data):
        self.data = data


train_data = pd.read_csv('data/F16traindata_CMabV_2024.csv')
C_m = train_data.iloc[:, 0].to_numpy()
Z_k = train_data.iloc[:, 1:4].to_numpy()  # alpha_m, beta_m, V_m
U_k = train_data.iloc[:, 4:7].to_numpy()  # u_dot, v_dot, w_dot

print(C_m.size())