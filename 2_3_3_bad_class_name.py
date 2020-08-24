from datetime import timedelta
# bad or confusing class names
class thing(object):
    i = 5

    def jump(self):
        return 'Jump up and down'

    def run(self):
        return "Run fast"

    def stop(self):
        return "Stop"

class id(object):
    i = 1
    action = thing
    action.jump()


class CorporateFactoryExtensionManagerUtility(object):
    start = timedelta()
    print(start.days, start.seconds)
