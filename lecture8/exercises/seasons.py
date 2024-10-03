from datetime import date

Class Age:
    def __init__(self, birthday, age_minutes):
        self.birthday = birthday
        self.age_minutes = age_minutes

    @classmethod
    def get(cls):
        birthday = input("Birthday in YYYY-MM-DD: ")
        return cls(birthday)   

    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, birthday):
        if not birthday:
            raise ValueError("Missing Name")
        self._birthday = birthday


        


def main():
    





if __name__ == "__main__":
    main()