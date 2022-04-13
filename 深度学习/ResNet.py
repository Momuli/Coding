import torch
import torch.nn as nn
import math
import torch.utils.model_zoo as model_zoo

# 常见3*3卷积结构
def conv3(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)
# ****
# 残差网络的basicblock: 3*3 + 3*3
class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self, inplanes, outplanes, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        # conv1
        self.conv1 = conv3(inplanes, outplanes, stride)
        self.bn1 = nn.BatchNorm2d(outplanes)
        self.relu = nn.ReLU(True)
        # conv2
        self.conv2 = conv3(outplanes, outplanes)
        self.bn2 = nn.BatchNorm2d(outplanes)
        # 下采样
        self.downsample = downsample
        self.stride = stride
    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out = out + residual
        out = self.relu(out)

        return out

# ***
# Bottleneck: 1*1 + 3*3 + 1*1
class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, outplanes, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        # conv1 : 1*1
        self.conv1 = nn.Conv2d(inplanes, outplanes, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(outplanes)
        # conv2: 3*3
        self.conv2 = nn.Conv2d(outplanes, outplanes, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(outplanes)
        # conv3: 1*1
        self.conv3 = nn.Conv2d(outplanes, outplanes*4, kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(outplanes*4)
        self.relu = nn.ReLU(True)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out = out + residual
        out = self.relu(out)

        return out

# 不同深度ResNet中block堆叠个数
# ResNet18: ResNet(BasicBlock[2,2,2,2])
# ResNet34: ResNet(BasicBlock[3,4,6,3])
# Resnet50: ResNet(Bottleneck[3,4,6,3])
# ResNet101:ResNet(Bottleneck[3,4,23,3])
# ResNet152:ResNet(Bottleneck[3,8,36,3])

# ResNet18
def ResNet18(pretrained=False):
    model = ResNet(BasicBlock, [2, 2, 2, 2])
    if pretrained:
        model.load_state_dic(model_zoo.load_url('***'))
    return model

def ResNet50(pretrained=False):
    model = ResNet(Bottleneck, [3, 4, 6, 3])
    if pretrained:
        model.load_state_dict(model_zoo.load_url('***'))

class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=1000):
        super(ResNet, self).__init__()
        self.inplanes = 64
        # conv1: 7*7
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(True)
        # max_pooling
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        # layer1:
        self.layer1 = self._make_layer(block, 64, layers[0])
        # layer2:
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        # layer3:
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        # layer4:
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        # avg_pooling
        self.avgpool = nn.AvgPool2d(7)
        self.fc = nn.Linear(512*block.expansion, num_classes)

    def _make_layer(self, block, planes, blocks, stride=1):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.inplanes, planes*block.expansion, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(planes*block.expansion),
            )
            layers = []
            layers.append(block(self.inplanes, planes, stride, downsample))
            self.inplanes = planes * block.expansion
            for i in range(1, blocks):
                layers.append(block(self.inplanes, planes))
            return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
