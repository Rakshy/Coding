class list_to_tree:
    def __init__(self):
        self.root=None
        self.left=None
        self.right=None
    def get_root(self):
        return self.root
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_left(self,l):
        self.left=l
    def set_right(self,r):
        self.right=r
