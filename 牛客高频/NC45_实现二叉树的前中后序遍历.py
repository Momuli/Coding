class Solution:
    def threeOrders(self, root):
        pre_res = []
        mid_res = []
        post_res = []
        def preorder(cur):
            if not cur:
                return
            pre_res.append(cur.val)
            preorder(cur.left)
            preorder(cur.right)
        def midorder(cur):
            if not cur:
                return
            midorder(cur.left)
            mid_res.append(cur.val)
            midorder(cur.right)
        def postorder(cur):
            if not cur:
                return
            postorder(cur.left)
            postorder(cur.right)
            post_res.append(cur.val)
        preorder(root)
        midorder(root)
        postorder(root)
        return [pre_res, mid_res, post_res]