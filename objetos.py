import turtle

tortuguita = turtle.Turtle()
otraTortuguita = turtle.Turtle()
lentorra = turtle.Turtle()

lentorra.speed(2)
lentorra.shape('turtle')
lentorra.color('brown')
lentorra.right(90)
lentorra.fd(50)

tortuguita.speed(100)
tortuguita.shape('turtle')
tortuguita.color('pink')
tortuguita.fd(50)

otraTortuguita.speed(100)
otraTortuguita.color('green')
otraTortuguita.left(90)
otraTortuguita.fd(50)

#porcion de codigo que encapsula tanto funcionalidad como atributos, valores, variables
#esto nos permite lidiar con la complejidad