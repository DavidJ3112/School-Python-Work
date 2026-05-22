import turtle

speed: int = 4

Location: dict = {
    "linksonder": (0,0),
    "rechtsonder": (150,0),
    "linksboven": (0,150),
    "rechtsboven": (150,150),
    "dak": (75,220),
}

t = turtle.Turtle()

t.speed(speed)

t.goto(Location["rechtsonder"])
t.goto(Location["linksboven"])
t.goto(Location["dak"])
t.goto(Location["rechtsboven"])
t.goto(Location["linksboven"])
t.goto(Location["linksonder"])
t.goto(Location["rechtsboven"])
t.goto(Location["rechtsonder"])

turtle.done()