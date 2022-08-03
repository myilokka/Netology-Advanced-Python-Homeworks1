from Salary import Salary
from DbPeople import DbPeople
from datetime import datetime


def date_time():
    res = datetime.today()
    return res


if __name__ == '__main__':
    print(date_time())
    s = Salary()
    print(s.calculate_salary())
    dbp = DbPeople()
    print(dbp.get_employees())
