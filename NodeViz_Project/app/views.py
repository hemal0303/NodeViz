# project/app/views.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import traceback
import sys
import io
from treevizer import recursion_viz, recursion_to_png, to_png
import ast
import treevizer


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "app/generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_name(directory, base_name, extension):
    counter = 1
    while True:
        filename = os.path.join(directory, f"{base_name}{counter}.{extension}")
        if not os.path.exists(filename):
            return filename
        counter += 1


# def execute_code(code, execution_globals, execution_locals):
#     """
#     Execute Python code and capture both printed output and the result of the last expression.
#     """

#     # Redirect stdout to capture printed output
#     stdout_capture = io.StringIO()
#     sys.stdout = stdout_capture

#     try:
#         exec(code)
#         printed_output = stdout_capture.getvalue()
#         return printed_output
#     except Exception as e:
#         traceback.print_exc()
#         return str(e)
#     finally:
#         # Restore stdout
#         sys.stdout = sys.__stdout__


def get_binary_tree_impl(request):
    binary_tree_impl = """
    class Node:
        def __init__(self, key=0, data=0, left=None, right=None, parent=None):
            self.key = key
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent

        def has_parent(self):
            return self.parent is not None

        def has_left_child(self):
            return self.left is not None

        def has_right_child(self):
            return self.right is not None

    Note: Do not create any Other class like BinaryTree and inherit Node class to it. Just Define methods which you do normally in Separate BinaryTree Class.        
    """
    return JsonResponse({"implementation": binary_tree_impl})


def get_linked_list_impl(request):
    linked_list_impl = """
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    after defining your solution at the end call below function with relavent head as per your traversal method

    to_png(
        enter head variable name,
        structure_type="ll",
        dot_path=dot_path,
        png_path=png_path,
    )        
    """
    return JsonResponse({"implementation": linked_list_impl})


def get_recursion_impl(request):
    recursion_impl = """
    @recursion_viz  <--- wrap your function with this decorator
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    factorial(n) # make sure to call the function :D        
    """
    return JsonResponse({"implementation": recursion_impl})


def extract_function_name(code):
    try:
        parsed_ast = ast.parse(code)
        function_name = None
        for node in ast.walk(parsed_ast):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name
        return function_name
    except SyntaxError:
        return None


import os
from django.http import HttpResponse
from django.shortcuts import render
import subprocess

def get_next_script_name():
    base_name = "user_script"
    count = 0
    while True:
        if count != 0:
            script_name = f"{base_name}{count}.py"
        else:
            script_name = f"{base_name}.py"    
        if not os.path.exists(os.path.join("user_code", script_name)):
            return script_name
        count += 1

def home(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
    if request.method == "POST":
        user_code = request.POST.get("code")
        script_name = get_next_script_name()
        file_path = os.path.join("user_code", script_name)

        file_content = f"""
import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_location(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return filename
        counter += 1

def get_next_file_name(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return concated  # Return only the filename, not the full path
        counter += 1        

dot_path = get_next_file_location(dot_data_dir, "dot_file", '.dot')
png_path = get_next_file_location(png_data_dir, "png_file", '.png')

{user_code}
file_name = get_next_file_name(png_data_dir, "png_file", '.png')
print(file_name)
"""

        file_content += "\n"

        # Write code to the Python file
        with open(file_path, "w") as f:
            f.write(file_content)

        # Run the Python file using subprocess and capture output
        try:
            file_name = subprocess.check_output(["python", file_path], stderr=subprocess.STDOUT, universal_newlines=True)
            print("output", file_name)
            return JsonResponse({"filepath": file_name})
            return HttpResponse(f"Script executed successfully with output: {output}")
        except subprocess.CalledProcessError as e:
            error_message = f"Script execution failed with error: {e.output}"
            # Handle error message or return as needed
            return JsonResponse({"error": error_message})

        return HttpResponse("Script executed successfully.")

    return render(request, "app/home2.html")


