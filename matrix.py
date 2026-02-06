import numpy as np

def input_matrix(name="Matrix"):
    """Function to input a matrix from the user."""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements row by row for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Number of elements must match columns.")
            return None
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, title="Result"):
    """Display matrix in structured format."""
    print(f"\n{title}:")
    print(matrix)

def matrix_operations():
    while True:
        print("\n--- Matrix Operations Tool ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")
        
        if choice == '1':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A + B, "Addition Result")
            else:
                print("Error: Matrices must have the same dimensions for addition.")
        
        elif choice == '2':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A - B, "Subtraction Result")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
        
        elif choice == '3':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                display_matrix(np.dot(A, B), "Multiplication Result")
            else:
                print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
        
        elif choice == '4':
            A = input_matrix("Matrix")
            display_matrix(A.T, "Transpose Result")
        
        elif choice == '5':
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:
                display_matrix(np.linalg.det(A), "Determinant Result")
            else:
                print("Error: Determinant can only be calculated for square matrices.")
        
        elif choice == '6':
            print("Exiting Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    matrix_operations()