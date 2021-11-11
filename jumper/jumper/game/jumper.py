class Jumper:

    def __init__(self):
        self._lines = 0

    def draw_jumper(self):
        """Draws an image of the jumper based on the current number of lines"""
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

    def cut_line(self):
        """Cuts a line from the jumper"""
        self._lines -= 1
