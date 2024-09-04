# src/main.py
import sys
from converter import convert_python_to_cpython

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <python_file.py>")
        return

    python_file = sys.argv[1]

    with open(python_file, 'r') as file:
        python_code = file.read()

    c_code = convert_python_to_cpython(python_code)
    print("Generated C Code:")
    print(c_code)

if __name__ == "__main__":
    main()
