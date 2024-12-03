class myClass:
    __myHe = 27

    def __inside(self):
        print("I am inside myClass.")

    def bye(self):
        print("Private Variable value = ",myClass.__myHe)


foo = myClass()
foo.bye()
foo.__myHe
foo.__inside()