import turtle
import math

class Name():
    def F():
        eu = turtle.Turtle()

        '''
                150
            -------------
            |     100    | 30
            |    --------
            |   | 30
        200 |    -------|
            |   ___80___| 30
            |   |
            |   | 110
            |___|
        
            50
        '''

        eu.forward(150)
        eu.right(90)

        eu.forward(30)
        eu.right(90)

        eu.forward(100)
        eu.left(90)

        eu.forward(30)
        eu.left(90)

        eu.forward(80)
        eu.right(90)

        eu.forward(30)
        eu.right(90)

        eu.forward(80)
        eu.left(90)

        eu.forward(110)
        eu.right(90)

        eu.forward(50)
        eu.right(90)

        eu.forward(200)

    def R():
        eu = turtle.Turtle()

        '''
                    150
                |-------------|
                |             |
                |             | 70
                | 30     120  |
         200    |-------------|
                |    \
                |     \
                |      \        130
                |       \
                |        \
         
        '''

        eu.forward(150)
        eu.right(90)

        eu.forward(70)
        eu.right(90)

        eu.forward(120)
        eu.left(110)

        eu.forward(130)
        eu.backward(130)
        eu.right(110)

        eu.forward(30)

        eu.left(90)
        eu.forward(130)
        eu.backward(200)

    def E():
        eu = turtle.Turtle()

        '''
                        150
                |--------------|
                |              | 60
                |     |--80----|
                |  25 |_60__          
           200  |           | 30
                |     |-60--|
                |   25|___80__         
                |             |
                |_____________| 60
        
                    150
        '''

        eu.forward(150)
        eu.right(90)

        eu.forward(60)
        eu.right(90)

        eu.forward(80)
        eu.left(90)

        eu.forward(25)
        eu.left(90)

        eu.forward(60)
        eu.right(90)

        eu.forward(30)
        eu.right(90)

        eu.forward(60)
        eu.left(90)

        eu.forward(25)
        eu.left(90)

        eu.forward(80)
        eu.right(90)

        eu.forward(60)
        eu.right(90)

        eu.forward(150)
        eu.right(90)

        eu.forward(200)

    def D():
        eu = turtle.Turtle()

        '''
                    80
                |--------|
                |        ||
                |        |  |
                |        |   |
                |        |    |
            200 |        |    |   70
                |        |   |    F(x) = parabola não determinada...
                |        |  |       Essa é a função que representa essa parabola
                |        | |
                |________|
                    
                    80
                
        '''

        def Funcao():
            # F(x) =
            b = 1
            a = 1
            c = 6
            bascara = (b ** 2) - (4 * a * c)
            X1 = ((-b) + math.sqrt(bascara) / (2 * a))
            X2 = ((-b) - math.sqrt(bascara) / (2 * a))

            return [X1, X2]

        eu.forward(80)
        eu.right(90)

        eu.forward(200)
        eu.right(90)

        eu.forward(150)
        eu.right(90)

        eu.forward(200)






Name.F()