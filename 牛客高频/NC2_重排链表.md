##  def reorderList(self, head )
### 链表反转

**思路:**
1. 利用快慢指针获取后半部分的链表`temp`
2. 将`temp`反转
3. 将前半部分链表`head`和后半部分链表`temp`逐个元素链接

**代码:**
```
class Solution:
    def reorderList(self, head ):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        temp = self.reverse(temp)
        dummy = ListNode(0)
        dummy.next = head
        while head and temp:
            tmp1 = head.next
            tmp2 = temp.next
            head.next = temp
            temp.next = tmp1
            head = tmp1
            temp = tmp2
        return dummy.next

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```