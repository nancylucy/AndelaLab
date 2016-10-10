class Car(object):
    ''' You are to create a Car class that can be used to instantiate various vehicles.

    It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

    Let the test guide you to building your Car boiler-plate.'''

    def __init__(self, *args):

        if len(args) == 0:
            self.name = 'General'
            self.model = 'GM'

        if len(args) >= 1:
            self.name = args[0]

        if len(args) >= 2:
            self.model = args[1]

        if self.name in ('Porshe', 'Koenigsegg'): 
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if len(args) >= 3:
            self.car_type = args[2]
        else:
            self.car_type = 'saloon'

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        self.speed = 0

    def is_saloon(self):
        return self.car_type == 'saloon'
        

    def drive(self, spd):
        if self.car_type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = spd ** 10

        return self