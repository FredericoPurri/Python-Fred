import turtle


def Anel():
    tartaruga = turtle.Turtle()

    tartaruga.color('red', 'yellow')
    tartaruga.begin_fill()
    while True:
        tartaruga.forward(200)
        tartaruga.left(170)
        print(tartaruga.pos())
        print(abs(tartaruga.pos()))
        if abs(tartaruga.pos()) < 1:
            break
        ''' a posição da tartarua = tartaruga.pos(), é um vetor 2D,
                       a função abs retorna o valor absoluto desse vetor   '''
    tartaruga.end_fill()


Anel()
