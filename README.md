# Pi Approximation
Approximation of PI by the Monte Carlo method using Python and the Pygame library (Still a work in progress.)

# Maths
![Setup Diagram](https://i.imgur.com/qAQI9ro.png)

Let's take the radius of the circle as r
Therefore each side of the square is 2r

The area of the circle is πr²
The area of the square is 4r²

If each of the points in the square and circle were to be filled then,

$$\frac{\pi r^2}{4r^2} = \frac {number \ of \ points \ in \ circle}{number \ of \ points \ in \ square}$$

Throught this we get $\pi$ as,

$$\pi = 4 \cdot \frac{number \ of \ points \ in \ circle}{number \ of \ points \ in \ square}