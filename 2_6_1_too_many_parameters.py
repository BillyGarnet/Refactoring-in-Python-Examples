# Too many parameters

class TooManyParameters(self):
    def digestion_organizer_system(available_foods, height, item, number_legs, food, has_horns, can_fly, quantity):

        if food.name in available_foods:
            diet = self.create_diet(height, number_legs, has_horns, can_fly, food)
            # diet = avail  able_foods.diet_check()
            diet = self.create_diet()
        else:
            diet = "Can't create a meal plan"

        return diet

    def diet_check(self):
        return "Diet Plan"

    def create_diet(self, height, number_legs, has_horns, can_fly, food):
        # do cool stuff
        return "Diet plan"