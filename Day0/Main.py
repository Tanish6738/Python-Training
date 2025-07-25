class GrandParent:
    def GrandParentDetail(self):
        print("I am Grand Parent")


class Parent1(GrandParent):
    def Parent1Detail(self):
        print("I am Parent 1")


class Parent2(GrandParent):
    def Parent2Detail(self):
        print("I am Parent 2")


class Childern(Parent1, Parent2):
    def ChildrenDetail(self):
        print("I am Childern ")

obj = Childern()

obj.ChildrenDetail()
obj.GrandParentDetail()
obj.Parent1Detail()
obj.Parent2Detail()