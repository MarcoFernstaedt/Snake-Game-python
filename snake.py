from telnetlib import DO
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        # Add a new segment to the snake.
        self.add_seg((self.segments[-1].position()))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
