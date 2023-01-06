from global_diary_logger import GlobalDiaryLogger


# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s :: %(name)s :: %(message)s')


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger_instance = GlobalDiaryLogger(self.__class__.__name__)
        logger = logger_instance.get_logger()
        logger.info('Employee Created: {} - {}'.format(self.fullname, self.email))
        logger.warning('Caution!!')

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


emp_1 = Employee('Ajay', 'Thakur')
emp_2 = Employee('Abhay', 'Thakur')
emp_3 = Employee('Bijay', 'Singh')
