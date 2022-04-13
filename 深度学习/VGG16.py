import torch
import torch.nn as nn

cfg = {
    # VGG11
    'A': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    # VGG13
    'B': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    # VGG16
    'D': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
    # VGG19
    'E': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M']
}

class VGG16(nn.Module):
    def __init__(self, features, num_classes=3, init_weight=True):
        super(VGG16, self).__init__()
        self.features = features
        # 构造序列器
        self.classifier = nn.Sequential(
            # FC1
            nn.Linear(7*7*512, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            # FC2
            nn.Linear(4906, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            # FC3
            nn.Linear(4096, num_classes)
        )

        if init_weight:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        # reshape为(B, C*W*H)
        x = x.view(x.size(0), -1)
        # 分类
        x = self.classifier(x)
        return x

    # 初始化权重
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)

# 卷积层实现
def make_layers(cfg, batch_normal=False):
    layers = []
    in_channels = 3
    for v in cfg:
        # 池化层
        if v == 'M':
            layers += nn.MaxPool2d(kernel_size=2, stride=2)
        # 卷积层
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            if batch_normal:
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(True)]
            else:
                layers += [conv2d, nn.ReLU(True)]
            in_channels = v
    return nn.Sequential(*layers)

def vgg16(**kwargs):
    model = VGG16(make_layers(cfg['D'], batch_normal=False), **kwargs)
    return model