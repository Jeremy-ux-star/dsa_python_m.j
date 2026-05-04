class person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.validate_age(age)
        
        def validate_age(self, age):
            if age > 0 and age < 100:
                self.age = age
                return self.age