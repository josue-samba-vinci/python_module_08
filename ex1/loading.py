from __future__ import annotations
try:
    import numpy
except ImportError:
    numpy = None
try:
    import pandas
except ImportError:
    pandas = None
try:
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = None
    plt = None


def check_dependencies() -> bool:
    """Check if required dependencies are installed and print their status."""
    print("Checking dependencies:")
    if pandas is None:
        print("[KO] pandas - Data manipulation not installed")
    else:
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    if numpy is None:
        print("[KO] numpy - Numerical computation not installed")
    else:
        print("[OK] numpy "
              f"({numpy.__version__}) - Numerical computation ready")
    if plt is None:
        print("[KO] matplotlib - Visualization not installed")
    else:
        print("[OK] matplotlib ("
              f"{matplotlib.__version__}) - Visualization ready")
    return all([pandas, numpy, matplotlib])


def generate_matrix_data(size: int) -> numpy.ndarray:
    """Generate a random matrix of given size."""
    if numpy is None:
        raise ImportError("numpy is required to generate matrix data.")
    return numpy.random.rand(size)


def process_matrix_data(data: numpy.ndarray) -> pandas.DataFrame:
    """Process the matrix data and return a DataFrame."""
    if pandas is None:
        raise ImportError("pandas is required to process data.")
    dataframe = pandas.DataFrame(data, columns=["numbers"])
    return dataframe


def display_matrix(dataframe: pandas.DataFrame) -> None:
    if plt is None:
        raise ImportError("pyplot is required to display the matrix")
    plt.hist(dataframe)
    plt.savefig("matrix_analysis.png")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    boolean = check_dependencies()
    print()
    if boolean:
        data = generate_matrix_data(1000)
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        dataframe = process_matrix_data(data)
        print("Generating visualization...")
        display_matrix(dataframe)
        print()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("Please install all the required dependencies using :")
        print("<pip install -r requirements.txt> or <poetry install>")


if __name__ == "__main__":
    main()
