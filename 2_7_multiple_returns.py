# Multiple Returns

class WhyAllTheReturns():
    def bloated_method_and_other_stuff(self, food, animal, vehicle, plant, person):

        fuel_type = {'Regular', 'Super', 'Diesel', 'Electric'}

        if animal.can_fly:
            animal.diet = "Birdseed"
            animal.house = "Birdhouse"
            person.name = "Alferd"
            return
        else:
            if vehicle == "Trans Am":
                vehicle.fuel = fuel_type[0]
                vehicle.seats = 5
                return
            elif plant == "Venus Fly-Trap":
                plant.food = "Flys"
                return
            else:
                food = "Donuts"
                return

            diet = "Dog food"
            animal.house = "Dog house"

        return diet

    def create_diet(self, height, number_legs, has_horns, can_fly, food):
        # do cool stuff
        return "Diet plan"


class Animal(object):
    house = "Nothing"
