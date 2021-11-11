class Jumper:

    def __init__(self):
        self._lines = 4

    def draw_jumper(self):
        """Draws an image of the jumper based on the current number of lines"""

        if self._lines == 4:

            print("-------------")
            print("")
            print("/___/_\_\\")
            print(" \\     /")
            print("  \\   /")
            print("   \O/")
            print("    |")
            print("   / \\")
            print("")
            print("/\\/\\/\\/\\/\\/\\/\\/\\")

        elif self._lines == 3:
            print("-------------")
            print("")
            print(" \\     /")
            print("  \\   /")
            print("   \O/")
            print("    |")
            print("   / \\")
            print("")
            print("/\\/\\/\\/\\/\\/\\/\\/\\")

        elif self._lines ==2:
            print("-------------")
            print("")
            print("  \\   /")
            print("   \O/")
            print("    |")
            print("   / \\")
            print("")
            print("/\\/\\/\\/\\/\\/\\/\\/\\")

        elif self._lines == 1:

            print("-------------")
            print("")
            print("   \O/")
            print("    |")
            print("   / \\")
            print("")
            print("/\\/\\/\\/\\/\\/\\/\\/\\")

        else:
            print("-------------")
            print("")
            print("   \\x/")
            print("    |")
            print("   / \\")
            print("/\\/\\/\\/\\/\\/\\/\\/\\")





    

    def cut_line(self):
        """Cuts a line from the jumper"""
        self._lines -= 1
    

