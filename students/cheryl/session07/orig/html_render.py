#!/usr/bin/env python3


class Element:
    tag_name = "html"
    indent = 4

    def __init__(self, content=None, **kwargs):
        '''
        initializer

        :param content:
        :type content: list
        '''
        self.style = None
        self.id = None
        self.content = []
        if content is not None:
            self.content.append(content)
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'style' in kwargs:
            self.style = kwargs['style']

    def append(self, obj):
        '''
        append to the contents

        :param obj: new obj
        :type obj: string or Element
        '''
        self.content.append(obj)

    def render(self, file_out, ind=""):
        '''
        render the tag and the strings in the content

        :param file_out: - a file-like object that you can write to
        :type file_out:
        :param ind: the indentation level
        :type ind: string
        '''
        file_out.write(ind)
        file_out.write("<{}".format(self.tag_name))
        if self.style is not None:
            file_out.write(' style="{}"'.format(self.style))
        if self.id is not None:
            file_out.write(' id="{}"'.format(self.id))
        file_out.write(">\n")
        for ele in self.content:
            if type(ele) == str:
        #  try:
         #   except AttributeError:
                ind = ind + "  "
                file_out.write(ind)
                file_out.write(str(ele))
                file_out.write("\n")
            else:
                ind = ind + "  "
                ele.render(file_out, ind)

        ind = ind[0:-2]
        file_out.write(ind)
        file_out.write("</{}>\n".format(self.tag_name))


class Html(Element):
    tag_name = "html"


class Body(Element):
    tag_name = "body"


class Head(Element):
    tag_name = "head"


class Title(Element):
    tag_name = "title"


class P(Element):
    tag_name = "p"


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        '''
        render the tag and the strings in the content

        :param file_out: - a file-like object that you can write to
        :type file_out:
        :param ind: the indentation level
        :type ind: string
        '''
        file_out.write(ind)
        file_out.write("<{}>".format(self.tag_name))
        for ele in self.content:
            try:
                ele.render(file_out, ind="  ")
            except AttributeError:
                file_out.write(str(ele))
        file_out.write("</{}>\n".format(self.tag_name))


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        '''
        render the tag and the strings in the content

        :param file_out: - a file-like object that you can write to
        :type file_out:
        :param ind: the indentation level
        :type ind: string
        '''
        ind = ind[0:-2]
        file_out.write(ind)
        file_out.write("<{}".format(self.tag_name))
        if self.style is not None:
            file_out.write(" style={}".format(self.style))
        if self.id is not None:
            file_out.write(" id={}".format(self.id))
        file_out.write("/>\n")


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class H(OneLineTag):
    def __init__(self, level, content):
        self.tag_name = "H" + str(level)
        OneLineTag.__init__(self, content)

class A(Element):
    tag_name = 'a'

    def __init__(self, link, content):
        self.link = link
        Element.__init__(self, content)

    def render(self, file_out, ind=""):
        '''
        render the tag and the strings in the content

        :param file_out: - a file-like object that you can write to
        :type file_out:
        :param ind: the indentation level
        :type ind: string
        '''
        file_out.write(ind)
        file_out.write('<{} href="{}"'.format(self.tag_name, self.link))
        if self.style is not None:
            file_out.write(' style="{}"'.format(self.style))
        if self.id is not None:
            file_out.write(' id="{}"'.format(self.id))
        file_out.write(">")
        for ele in self.content:
            if type(ele) == str:
        #  try:
         #   except AttributeError:
                file_out.write(str(ele))
            else:
                ele.render(file_out, ind)
        file_out.write("</{}>\n".format(self.tag_name))

class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"
