class Hello:
    def GET(self, name):
        if not name:
            name = 'eliazar'
        return 'Hola, ' + name + '!'