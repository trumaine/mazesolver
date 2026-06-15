from graphics import Window, Line, Point

def main() -> None:
    win = Window(800, 600)
    line1 = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line1, "black")
    line2 = Line(Point(50, 100), Point(400, 450))
    win.draw_line(line2, "red")
    line3 = Line(Point(50, 150), Point(400, 500))
    win.draw_line(line3, "blue")
    win.wait_for_close()


main()