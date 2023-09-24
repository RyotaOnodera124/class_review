class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name  # インスタンス変数
        self.family_name = family_name  # インスタンス変数

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    

ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す
print(ken.full_name())


tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
print(tom.full_name())

