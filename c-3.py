class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name  # インスタンス変数
        self.family_name = family_name  # インスタンス変数
        self.age = age  # インスタンス変数

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
    def entry_fee(self):
        if self.age < 20:
            print(1000)
        elif 20 <= self.age <= 65:
            print(1500)
        elif 65 <= self.age:
            print(1200)
    

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name()  # "Ken Tanaka" という値を返す
ken.age  # 15 という値を返す
print(ken.entry_fee())


tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.full_name()  # "Tom Ford" という値を返す
tom.age  # 57 という値を返す
print(tom.entry_fee())


ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.full_name()  # "Tokugawa Ieyasu"という値を返す
ieyasu.age  # 73 という値を返す
print(ieyasu.entry_fee())
