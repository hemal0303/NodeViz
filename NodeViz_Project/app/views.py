# project/app/views.py
from django.http import JsonResponse
from django.shortcuts import render
from treevizer import recursion_viz, recursion_to_png
import treevizer
import os
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "app/generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_name(directory, base_name, extension):
    """
    Get the next available filename with the specified extension by incrementing a number suffix.
    """
    counter = 1
    while True:
        filename = os.path.join(directory, f"{base_name}{counter}.{extension}")
        if not os.path.exists(filename):
            return filename
        counter += 1


def home(request):
    if request.method == "POST":
        code = request.POST.get("code")

        # Example: Secure code execution in a restricted environment
        execution_globals = {}
        execution_locals = {}
        try:
            exec(code, execution_globals, execution_locals)
            result = execution_locals.get("result")
            if result is not None:
                return JsonResponse({"result": result})
            else:
                return JsonResponse({"error": "Code did not produce a valid result"})
        except Exception as e:
            # Log the exception for debugging and monitoring
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=400)

    @treevizer.recursion_viz
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(6)  # Example: Calculate Fibonacci sequence for n=6

    # Get the next available filenames for DOT and PNG files with extensions
    dot_file = get_next_file_name(dot_data_dir, "dot", "dot")
    png_file = get_next_file_name(png_data_dir, "png", "png")

    treevizer.recursion_to_png("fibonacci", dot_path=dot_file, png_path=png_file)

    return render(request, "app/home.html")
