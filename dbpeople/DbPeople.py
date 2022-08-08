class DbPeople:
    def __init__(self, name='Эрни', job_title='стажер'):
        self.name = name
        self.job_title = job_title

    def get_employees(self):
        return f'Имя сотрудника: {self.name}, должность: {self.job_title}'
