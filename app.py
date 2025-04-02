import ast

import streamlit as st


def ast_to_dict(node):
    """Convert an AST node to a dictionary."""
    if isinstance(node, ast.AST):
        return {
            "type": type(node).__name__,
            **{k: ast_to_dict(v) for k, v in ast.iter_fields(node)},
            "lineno": getattr(node, "lineno", None),
            "col_offset": getattr(node, "col_offset", None),
        }
    elif isinstance(node, list):
        return [ast_to_dict(n) for n in node]
    else:
        return node


def main():
    st.title("Python AST Playground")

    # Create a text area for Python code input
    code = st.text_area(
        "Enter Python code:",
        height=200,
        value="def hello_world():\n    print('Hello, World!')",
    )

    if code:
        try:
            # Parse the code to get the AST
            parsed_ast = ast.parse(code)

            # Optionally show a success message
            st.success("AST generated successfully!")

            dump, tree = st.tabs(
                [
                    "Dump",
                    "Tree",
                ]
            )

            with dump:
                # Display the AST dump
                st.subheader("AST Dump:")
                st.code(ast.dump(parsed_ast, indent=2), language="text")

            with tree:
                # Display the AST tree
                st.subheader("AST Tree:")
                st.json(ast_to_dict(parsed_ast), expanded=False)

        except SyntaxError as e:
            st.error(f"Syntax Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
