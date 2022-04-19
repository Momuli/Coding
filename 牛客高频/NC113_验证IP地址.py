class Solution:
    def solve(self , IP):
        # 如果存在'.':验证是否是IPv4
        if '.' in IP:
            for item in IP.split('.'):
                # 包含非数字 or 不在[0,255] or 0开头
                if not item.isdigit() or not '0' <= item <= '255' or item[0] == '0':
                    return 'Neither'
            return 'IPv4'
        # 如果存在':':验证是否是IPv6
        if ':' in IP:
            for item in IP.split(':'):
                # item是'' or item 存在重复0
                if not item or len(item) > 1 and item.count('0') == len(item):
                    return 'Neither'
                # item[i]是字母但不在'ABCDEF'范围内
                for i in range(len(item)):
                    if not item[i].isdigit() and not item[i] in 'abcdef' and not item[i] in 'ABCDEF':
                        return 'Neither'
            return 'IPv6'
