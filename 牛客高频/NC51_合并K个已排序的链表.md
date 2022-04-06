## def mergeKLists1(self, lists):
### 分治法(参考归并排序)

**思路:**
1. 将列表`list`中的链表分成两部分`left`和`right`分别进行合并
2. 最终剩余两个链表，再合并后输出最终结果
3. 链表拆分时:
* `if len(lists) == 1: return lists[0]`
* `if not lists: return None`
4. 链表合并时:
* `if not l1: return l2`
* `if not l2: return l1`

**代码:**
```
    def mergeKLists1(self, lists):
        # base case
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left_list = self.mergeKLists1(lists[:mid])
        right_list = self.mergeKLists1(lists[mid:])
        rel = self.Mergesort(left_list, right_list)
        return rel
    def Mergesort(selfself, left, right):
        if not left:
            return right
        if not right:
            return left
        dummy = temp = ListNode(0)
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left else right
        return dummy.next
```

## def mergeKLists2(self, lists):
### 枚举法

**思路:**
1. 将所有链表元素加入列表`temp`中,对`temp`排序，之后再利用有序`temp`重建有序链表

**代码:**
```
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        temp = []
        for item in lists:
            while item:
                temp.append(item.val)
                item = item.next
        temp = sorted(temp)
        dummy = p = ListNode(0)
        for i in range(len(temp)):
            p.next = ListNode(temp[i])
            p = p.next
        return dummy.next
```
