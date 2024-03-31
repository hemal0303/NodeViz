from treevizer import recursion_viz
import treevizer


@recursion_viz
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)

treevizer.recursion_to_png("fibonacci", dot_path="working.dot", png_path="working.png")
