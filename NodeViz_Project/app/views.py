# project/app/views.py
from django.http import JsonResponse
from django.shortcuts import render
from treevizer import to_png
import os
import traceback

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


import io
import sys
import traceback


def execute_code(code, execution_globals, execution_locals):
    """
    Execute Python code and capture both printed output and the result of the last expression.
    """
    # Redirect stdout to capture printed output
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture

    try:
        exec(code, execution_globals, execution_locals)
        printed_output = stdout_capture.getvalue()
        return printed_output
    except Exception as e:
        traceback.print_exc()
        return str(e)
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__


def visualize_linked_list(linked_list):
    print("===>>>>>>", linked_list.__dict__)

    dot_file = os.path.join(dot_data_dir, "linked_list.dot")
    png_file = os.path.join(png_data_dir, "linked_list.png")
    # to_png(dot_file, png_file)
    to_png(linked_list, structure_type="ll", dot_path=dot_file, png_path=png_file)


def home(request):
    if request.method == "POST":
        code = request.POST.get("code")
        if not code:
            return JsonResponse({"error": "Code is empty"}, status=400)

        try:
            result = execute_code(code, {}, {})
            print("result", result)
            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # Create a linked list and insert nodes
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_at_end(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

        def print_ll(self):
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    # Create a linked list and insert nodes
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    # Print the linked list
    linked_list.print_ll()

    # Visualize the linked list
    visualize_linked_list(linked_list)

    return render(request, "app/home2.html")
