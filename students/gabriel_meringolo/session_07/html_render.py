

class Element():
    tag = "html"

    def __init__(self, content=None, **kwargs):
        #for key in kwargs:
        #    print('{}="{}"'.format(key,kwargs.get(key)))
        self.content = []
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind="    "):
        start_tag = "<{}>".format(self.tag)
        f.write(start_tag + "\n")
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(ind + str(el) + "\n")
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag + "\n")


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"


class Head(Element):
    tag = "head"


class OneLineTag(Element):

    def render(self, f, ind="    "):
        f.write("<{}>".format(self.tag))
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        f.write("</{}>".format(self.tag) + "\n")


class Title(OneLineTag):
    tag = "title"
