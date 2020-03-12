import sys
import os
import argparse
import warnings


args = None


def tweak():
    print(f"Hello, World ({os.getcwd()})!")


def retrieve_args():
    parser = argparse.ArgumentParser(
        description="""LaTeX code tweaker
    """
    )

    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    rg = parser.parse_args()
    return rg


def main():
    global args

    try:
        warnings.resetwarnings()
        warnings.simplefilter("ignore")

        args = retrieve_args()
        tweak()
    except KeyboardInterrupt as e:
        sys.exit(e)
