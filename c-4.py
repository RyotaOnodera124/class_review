class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name  # インスタンス変数
        self.family_name = family_name  # インスタンス変数
        self.age = age  # インスタンス変数

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age <= 65:
            return 1500
        elif 65 <= self.age:
            return 1200

    def info_csv(self):
        per_fee = self.entry_fee()
        print(f"{self.full_name()}, {self.age}, {per_fee}")
  

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す


tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.info_csv()  # "Tom Ford,57,1500" という値を返す


ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


# returnは関数(メソッド)から値を返すために使う、その関数が計算した結果や値を他の部分で使えるようにする
