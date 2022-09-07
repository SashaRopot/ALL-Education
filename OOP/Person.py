class Person():
    @staticmethod
    def is_adult(age):
        if age >18:
            return True
        else:
            return False
print(Person.is_adult(3))
