use rand::Rng;

fn main() {
    // Define the dimensions of the matrices
    let rows_a = 3;
    let cols_a = 3;
    let rows_b = 3;
    let cols_b = 3;

    // Generate random matrices
    let matrix_a = generate_random_matrix(rows_a, cols_a);
    let matrix_b = generate_random_matrix(rows_b, cols_b);

    // Perform matrix multiplication
    let result = multiply_matrices(&matrix_a, &matrix_b);

    // Print the result
    println!("Matrix A:");
    print_matrix(&matrix_a);
    println!("Matrix B:");
    print_matrix(&matrix_b);
    println!("Result of Matrix Multiplication:");
    print_matrix(&result);
}

fn generate_random_matrix(rows: usize, cols: usize) -> Vec<Vec<f64>> {
    let mut rng = rand::thread_rng();
    (0..rows)
        .map(|_| (0..cols).map(|_| rng.gen_range(1.0..10.0)).collect())
        .collect()
}

fn multiply_matrices(matrix_a: &Vec<Vec<f64>>, matrix_b: &Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    let rows_a = matrix_a.len();
    let cols_a = matrix_a[0].len();
    let cols_b = matrix_b[0].len();
    let mut result = vec![vec![0.0; cols_b]; rows_a];

    for i in 0..rows_a {
        for j in 0..cols_b {
            for k in 0..cols_a {
                result[i][j] += matrix_a[i][k] * matrix_b[k][j];
            }
        }
    }

    result
}

fn print_matrix(matrix: &Vec<Vec<f64>>) {
    for row in matrix {
        for val in row {
            print!("{} ", val);
        }
        println!();
    }
}
