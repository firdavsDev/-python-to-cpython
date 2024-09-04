# src/converter.py
import ast

def convert_python_to_cpython(python_code):
    # Parse Python code to AST
    tree = ast.parse(python_code)
    
    # Generate C code
    c_code = generate_c_code(tree)
    
    return c_code

def generate_c_code(tree):
    c_code = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            c_code.append(f"int {node.name}(int a, int b) {{")
            for n in node.body:
                if isinstance(n, ast.Return):
                    ret_val = ast.dump(n.value)
                    c_code.append(f"    return {ret_val};")
            c_code.append("}")
    
    return "\n".join(c_code)
