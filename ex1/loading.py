try:
    import numpy
except ImportError:
    numpy = None
try:
    import pandas
except ImportError:
    pandas = None
try:
    import requests
except ImportError:
    requests = None
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
        print("[KO] numpy - Numerical computing not installed")
    else:
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computing ready")
    if plt is None:
        print("[KO] matplotlib - Visualization not installed")
    else:
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    return all([pandas, numpy, matplotlib])


def generate_matrix_data(size: int) -> numpy.ndarray:
    """Generate a random matrix of given size."""
    if numpy is None:
        raise ImportError("numpy is required to generate matrix data.")
    return numpy.random.rand(size)

def process_data(data: numpy.ndarray) -> pandas.DataFrame:
    """Process the matrix data and return a DataFrame."""
    if pandas is None:
        raise ImportError("pandas is required to process data.")
    pandas.