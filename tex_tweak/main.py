import sys
import os
import argparse
import warnings
from pathlib import Path


ARGS = None


def is_target_file(file):
    """Returns true for a valid target [file].
    """
    return file.is_file()


def list_dir_groom(abs_path):
    """Returns the list of directories
    and the list of files ([abs_path] offspring).
    """
    dirs, files = [], []

    for i in os.listdir(abs_path):
        if i[0] != ".":
            x = abs_path.joinpath(i)
            if x.is_dir():
                dirs.append(x)
            else:
                if is_target_file(x):
                    files.append(x)

    return dirs, files


def traverse_target_tree(tgt_dir):
    """Recursively traverses the target directory [tgt_dir]
    and yields a sequence of file names.
    """
    dirs, files = list_dir_groom(tgt_dir)

    for d in dirs:
        yield from traverse_target_tree(d)

    for f in files:
        yield f


def tweak():
    """Tweak all files.
    """
    for i in traverse_target_tree(ARGS.tgt_dir):
        print(f"{i}")


def retrieve_args():
    """Retrieve Command Line Arguments.
    """
    parser = argparse.ArgumentParser(
        description="""LaTeX code tweaker
        """
    )

    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    parser.add_argument("tgt_dir", help="target directory")
    rg = parser.parse_args()
    rg.tgt_dir = Path(rg.tgt_dir).absolute()  # Takes care of the trailing slash, too.

    return rg


def main():
    """Script entry point.
    """
    global ARGS

    try:
        warnings.resetwarnings()
        warnings.simplefilter("ignore")

        ARGS = retrieve_args()
        tweak()
    except KeyboardInterrupt as e:
        sys.exit(e)
