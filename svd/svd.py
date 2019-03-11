#  -*- coding:utf-8 -*-

import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl
from pprint import pprint


# 利用svd对图像进行压缩

def restore(sigma, u, v, k):  # 奇异值、左特征向量、右特征向量
    m = len(u)
    n = len(v[0])
    a = np.zeros((m, n))
    a = np.dot(u[:, :k], np.diag(sigma[:k])).dot(v[:k, :])
    a.clip(0, 255)
    return np.rint(a).astype('uint8')


if __name__ == "__main__":
    A = Image.open("xiazai4.jpg", 'r')
    output_path = r'.\Pic'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    a = np.array(A)
    K = 50
    # 获取每一个通道的U sigma V
    # u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])
    # u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])
    # u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])

    # 分离通道的另一种方法
    r, g, b = A.split()
    # 获取每一个RGB通道的U sigma V
    u_r, sigma_r, v_r = np.linalg.svd(r)
    u_g, sigma_g, v_g = np.linalg.svd(g)
    u_b, sigma_b, v_b = np.linalg.svd(b)

    plt.figure(figsize=(10, 10), facecolor='w')
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    for k in range(1, K + 1):
        print(k)
        R = restore(sigma_r, u_r, v_r, k)
        G = restore(sigma_g, u_g, v_g, k)
        B = restore(sigma_b, u_b, v_b, k)
        I = np.stack((R, G, B), 2)
        Image.fromarray(I).save('%s\\svd_%d.png' % (output_path, k))
        if k <= 12:
            plt.subplot(3, 4, k)
            plt.imshow(I)
            plt.axis('off')
            plt.title(u'奇异值个数：%d' % k)
    plt.suptitle(u'SVD与图像分解', fontsize=18)
    plt.tight_layout(2)
    plt.subplots_adjust(top=0.9)
    plt.show()
