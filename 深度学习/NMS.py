import numpy as np

def NMS(dets, thresh):
    # 左上角,右下角坐标
    x_min = dets[:, 0]
    y_min = dets[:, 1]
    x_max = dets[:, 2]
    y_max = dets[:, 3]
    # confidence
    score = dets[:, 4]
    # 每个box的面积
    areas = (x_max - x_min + 1) * (y_max - y_min + 1)
    # confidence排序
    # 输出score中元素从大到小排列后对应的index(索引)
    order = score.argsort()[::-1]
    # 保存保留下来的bbox
    keep = []
    while order.size > 0:
        i = order[0]    # 最大confidence对应的index
        keep.append(i)   # 保存最大confidence的bbox的索引
        # 计算当前bbox与剩余bbox的交并比
        # 交集
        Ix_min = np.maximum(x_min[i], x_min[order[1:]])
        Ix_max = np.minimum(x_max[i], x_max[order[1:]])
        Iy_min = np.maximum(y_min[i], y_min[order[1:]])
        Iy_max = np.maximum(y_max[i], y_max[order[1:]])
        # 计算相交区域的W和H,如果无相交区域，则为0
        H = np.maximum(0.0, Iy_max - Iy_min + 1)
        W = np.maximum(0.0, Ix_max - Ix_min + 1)
        Inter = W * H
        # IOU
        iou = Inter/(areas[i] + areas[order[1:]] - Inter)
        # 保留交集小于阈值的bbox的index
        idx = np.where(iou <= thresh)[0]
        order = order[idx + 1]
    return keep


if __name__ == '__main__':
    dets = np.array([
        [204, 102, 358, 250, 0.5],
        [257, 118, 380, 250, 0.7],
        [280, 135, 400, 250, 0.6],
        [255, 118, 360, 235, 0.7]
    ])
    thresh = 0.7
    rel = NMS(dets, thresh)
    print(rel)

