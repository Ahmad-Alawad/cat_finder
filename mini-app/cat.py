class Cat(object):
    """A Cat object."""

    def __init__(self, name, img_url):
        self.name = name
        self.img_url = img_url


    def __repr__(self):
        """Convenience method to show information about cat in console."""

        return "<Cat: %s>" %self.name

alex = Cat("Alex", "static/img/alex.jpg")
instonce = Cat("Instonce", "static/img/instonce.jpg")
melcat = Cat("Melcat", "static/img/melcat.jpg")
all_cats = [alex, instonce, melcat]