class Animal:
    def __init__(self, name):
        self.name = name

        def eat():
            print('{} is eating'.format(self.name))

        def drink():
            print('{} is drinking.'.format(self.name))

