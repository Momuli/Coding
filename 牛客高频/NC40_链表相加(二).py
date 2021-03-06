class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addInList(self , head1 , head2 ):
        # write code here
        # 反转链表
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        c = 0   # 进位
        head = head1  # 和链表的头节点  修改head1中元素的值，不重新申请空间
        tail = None   # 指向已求和位的末尾
        while head1 and head2:
            temp1 = head1.val + head2.val + c   # 计算当前位的和
            c = temp1 // 10  # 进位
            head1.val = temp1 % 10  # 非进位存入head1的当前计算的位置
            tail = head1  # tail指向已经计算了和的最后一位，方便之后链接
            head1 = head1.next
        # head1比head2长
        if head1:
            while c > 0 and head1:
                temp2 = head1.val + c
                head1.val = temp2 % 10
                c = temp2 // 10
                tail = head1
                head1 = head1.next
        if head2:
            tail.next = head2
            while c > 0 and head2:
                temp3 = head2.val + c
                c = temp3 // 10
                head2.val = temp3 % 10
                tail = head2
                head2 = head2.next
        # 计算完最后一位，还有进位
        if c > 0:
            c = ListNode(c)
            tail.next = c
        return head

    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = cur
            pre = cur
            cur = temp
        return pre