# Multiple Returns

class WhyAllTheReturns():
    def bloated_method_and_other_stuff(self, food, animal, vehicle, plant, person):

        if animal.can_fly:
            animal.diet = "Birdseed"
            animal.house = "Birdhouse"
            person.name = "Alferd"
        else:
            if vehicle == "Trans Am":
                fuel_type = {'Regular', 'Super', 'Diesel', 'Electric'}

                vehicle.fuel = fuel_type[0]
                vehicle.seats = 5
            elif plant == "Venus Fly-Trap":
                plant.food = "Flys"
            else:
                food = "Donuts"
        return

    def create_diet(self, height, number_legs, has_horns, can_fly, food):
        # do cool stuff
        return "Diet plan"


class Animal(object):
    house = "Nothing"
