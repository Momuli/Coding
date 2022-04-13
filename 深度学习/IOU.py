class Rectangle(object):
    def __init__(self, x1, y1, x2, y2, *center):
        # 定义(左上角，右下角)
        self.x_min = x1
        self.x_max = x2
        self.y_min = y1
        self.y_max = y2
        # 定义(x,y,w,h)
        self.center_x = center[0]
        self.center_y = center[1]
        self.width = center[2]
        self.heigh = center[3]

class Solution(object):
    def IOU(self, rec1, rec2):
        # 当为(x, y, w, h)时先转换为(x_min, x_max, y_min, y_max):
        rec1.x_min, rec1.x_max = rec1.center_x - rec1.width / 2, rec1.center_x + rec1.width / 2
        rec1.y_min, rec1.y_max = rec1.center_y - rec1.heigh / 2, rec1.center_y + rec1.heigh / 2
        rec2.x_min, rec2.x_max = rec2.center_x - rec2.width / 2, rec2.center_x + rec2.width / 2
        rec2.y_min, rec2.y_max = rec2.center_y - rec2.heigh/ 2, rec2.center_y + rec2.heigh / 2

        S_1 = (rec1.x_max-rec1.x_min) * (rec1.y_max-rec1.y_min)
        S_2 = (rec2.x_max-rec2.x_min) * (rec2.y_max-rec2.y_min)
        Ix_min = max(rec1.x_min, rec2.x_min)
        Ix_max = min(rec1.x_max, rec2.x_max)
        Iy_min = max(rec1.y_min, rec2.y_min)
        Iy_max = min(rec1.y_max, rec2.y_max)
        if Iy_max > Iy_min and Ix_max > Ix_min:
            Inter = (Iy_max-Iy_min) * (Ix_max-Ix_min)
            res = Inter / (S_1 + S_2 - Inter)
            return res
        else:
            return 0

if __name__ == '__main__':
    rec1 = Rectangle(100, 100, 200, 200, 150, 150, 100, 100)
    rec2 = Rectangle(120, 120, 220, 220, 170, 170, 100, 100)
    rel = Solution().IOU(rec1, rec2)
    print(rel)