# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 如果链表为空,返回None
        if not head:
            return
        # 哈希表,建立新旧节点的映射
        dict_h = dict()
        cur = head   # cur指向原链表的当前节点
        while cur:
            dict_h[cur] = Node(cur.val)     # 建立新的节点,此时next和random都为空
            cur = cur.next
        # 设置新节点的next和random指向
        cur = head
        while cur:
            # dict_h[cur]:当前节点cur所对应的复制的新节点
            dict_h[cur].next = dict_h.get(cur.next)
            dict_h[cur].random = dict_h.get(cur.random)
            cur = cur.next
        return dict_h[head]

    def copyRandomList2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # head为空
        if not head:
            return None
        # 复制新节点并合并新旧链表
        cur = head
        while cur:
            temp = Node(cur.val)
            # 插入复制的新节点
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        # 设置新节点的random指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next
        # 拆分链表
        dummy = new = head.next   # 新链表头结点
        cur = head    # 指向旧链表头结点
        # 虽然两条链表合并了,但是只要一个尾结点,而新链表的new指针会先到达新节点,因此用new.next作为终止条件
        while new.next:
            cur.next = cur.next.next
            new.next = new.next.next
            cur = cur.next
            new = new.next
        cur.next = None   # 给旧链表补上尾结点,否则链表不完整,会报错
        return dummy








        if not head:
            return
        cur = head
        # 拼接
        while cur:
            pre = Node(cur.val)
            pre.next = cur.next
            cur.next = pre
            cur = cur.next.next
        # 复制random指引
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        cur = head
        dum = pree = head.next
        while pree.next:
            cur.next = cur.next.next
            pree.next = pree.next.next
            cur = cur.next
            pree = pree.next
        cur.next = None
        return dum

