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


def execute_code(code, execution_globals, execution_locals):
    """
    Execute Python code and capture both printed output and the result of the last expression.
    """
    # Redirect stdout to capture printed output
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture

    try:
        exec(code)
        printed_output = stdout_capture.getvalue()
        return printed_output
    except Exception as e:
        traceback.print_exc()
        return str(e)
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__


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
    """
    return JsonResponse({"implementation": binary_tree_impl})


def get_linked_list_impl(request):
    linked_list_impl = """
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    """
    return JsonResponse({"implementation": linked_list_impl})


def get_recursion_impl(request):
    recursion_impl = """
    @recursion_viz
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
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
    if request.method == "POST":
        user_code = request.POST.get("code")

        if not os.path.exists("user_code"):
            os.makedirs("user_code")

        script_name = get_next_script_name()
        file_path = os.path.join("user_code", script_name)

        file_content = f"""
import treevizer
from treevizer import recursion_viz, to_png
import o

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

{user_code}
        """

        # Write code to the Python file
        with open(file_path, "w") as f:
            f.write(file_content)

        # Run the Python file using subprocess and capture output
        try:
            output = subprocess.check_output(["python", file_path], stderr=subprocess.STDOUT, universal_newlines=True)
            print("output", output)
            # Process output as needed
            return HttpResponse(f"Script executed successfully with output: {output}")
        except subprocess.CalledProcessError as e:
            error_message = f"Script execution failed with error: {e.output}"
            # Handle error message or return as needed
            return HttpResponse(error_message)

        return HttpResponse("Script executed successfully.")

    return render(request, "app/home2.html")


