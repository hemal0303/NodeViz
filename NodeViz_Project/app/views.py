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


# def get_next_file_name(directory, base_name, extension):
#     counter = 1
#     while True:
#         filename = os.path.join(directory, f"{base_name}{counter}.{extension}")
#         if not os.path.exists(filename):
#             return filename
#         counter += 1


def execute_code(code, execution_globals, execution_locals):
    """
    Execute Python code and capture both printed output and the result of the last expression.
    """
    # Redirect stdout to capture printed output
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture

    try:
        print("here")
        exec(code)
        printed_output = stdout_capture.getvalue()
        print("printed_output", printed_output)
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


# def home(request):
#     try:
#         if request.method == "POST":
#             code = request.POST.get("code")
#             if not code:
#                 return JsonResponse({"error": "Code is empty"}, status=400)

#             try:
#                 fun_name = extract_function_name(code)
#                 execute_code(code, {}, {})
#                 dot_path = dot_data_dir + "/test.dot"
#                 png_path = png_data_dir + "/test.png"

#                 # treevizer.recursion_to_png(
#                 #     fun_name, dot_path=dot_path, png_path=png_path
#                 # )
#                 to_png(
#                     fun_name,
#                     structure_type="ll",
#                     dot_path=dot_path,
#                     png_path=png_path,
#                 )
#                 return JsonResponse({"result": "Visualization generated successfully"})
#             except Exception as e:
#                 return JsonResponse({"error": str(e)}, status=400)

#         return render(request, "app/home2.html")
#     except Exception as e:
#         print("Found an Error-->", e)


# def home(request):
#     try:
#         if request.method == "POST":
#             code = request.POST.get("code")
#             if not code:
#                 return JsonResponse({"error": "Code is empty"}, status=400)

#             try:
#                 fun_name = extract_function_name_and_decorate(code)
#                 execute_code(code, {}, {})
#                 dot_path = dot_data_dir + "/test.dot"
#                 png_path = png_data_dir + "/test.png"

#                 treevizer.recursion_to_png(
#                     fun_name, dot_path=dot_path, png_path=png_path
#                 )
#                 return JsonResponse({"result": "Visualization generated successfully"})
#             except Exception as e:
#                 return JsonResponse({"error": str(e)}, status=400)

#         return render(request, "app/home2.html")
#     except Exception as e:
#         print("Found an Error-->", e)


# def extract_function_name_and_decorate(code):
#     class RecursionVizTransformer(ast.NodeTransformer):
#         def visit_FunctionDef(self, node):
#             if "recursion_viz" not in [
#                 decorator.id for decorator in node.decorator_list
#             ]:
#                 node.decorator_list.append(ast.Name(id="recursion_viz", ctx=ast.Load()))
#             return node

#     try:
#         parsed_ast = ast.parse(code)
#         transformer = RecursionVizTransformer()
#         transformed_ast = transformer.visit(parsed_ast)

#         for node in ast.walk(transformed_ast):
#             if isinstance(node, ast.FunctionDef):
#                 function_name = node.name
#                 return function_name
#                 # return function_name, node

#         return None, None  # No function found in the code
#     except SyntaxError:
#         return None, None


# views.py

from django.shortcuts import render
import subprocess
import os


def home(request):
    if request.method == "POST":
        user_code = request.POST.get("code")

        # Prefix imports and create Python file content
        file_content = f"""
import treevizer
from treevizer import recursion_viz, to_png


{user_code}
        """

        # Write code to a Python file
        with open("user_code.py", "w") as f:
            f.write(file_content)

        # Run the Python file using os.system
        os.system("python user_code.py")

        return HttpResponse("Script executed successfully.")

    return render(request, "app/home2.html")
