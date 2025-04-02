import ast

import streamlit as st


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

            # Display the AST dump
            st.subheader("AST Dump:")
            st.code(ast.dump(parsed_ast, indent=2), language="text")

            # Optionally show a success message
            st.success("AST generated successfully!")
        except SyntaxError as e:
            st.error(f"Syntax Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
