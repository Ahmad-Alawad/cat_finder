class Cat(object):
    """A Cat object."""

    def __init__(self, name, img_url):
        self.name = name
        self.img_url = img_url


alex = Cat("Alex", "static/img/alex.jpg")
instance = Cat("Instance", "static/img/instance.jpg")
melcat = Cat("Melcat", "static/img/melcat.jpg")

all_cats = [alex, instance, melcat]