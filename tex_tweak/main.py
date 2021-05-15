"""
LaTeX source tweaker.
"""
import sys
import os
import asyncio
import argparse
import warnings
from pathlib import Path
from typing import List, Tuple, AsyncIterator, Any


ARGS: Any = None


def is_target_file(file: Path) -> bool:
    """
    Returns true for a valid target [file].
    """
    return file.is_file()


def list_dir_groom(abs_path: Path) -> Tuple[List[Path], List[Path]]:
    """
    Returns the list of directories
    and the list of files ([abs_path] offspring).
    """
    dirs, files = [], []

    for i in os.listdir(abs_path):
        if i[0] != ".":
            path = abs_path.joinpath(i)
            if path.is_dir():
                dirs.append(path)
            else:
                if is_target_file(path):
                    files.append(path)

    return dirs, files


async def traverse_target_tree(tgt_dir: Path) -> AsyncIterator[Path]:
    """
    Recursively traverses the target directory [tgt_dir]
    and yields a sequence of file names.
    """
    dirs, files = list_dir_groom(tgt_dir)

    for directory in dirs:
        async for file in traverse_target_tree(directory):
            yield file

    for file in files:
        yield file


async def tweak() -> None:
    """
    Tweak all files.
    """
    async for i in traverse_target_tree(ARGS.tgt_dir):
        print(f"{i}")


def retrieve_args() -> Any:
    """
    Retrieve Command Line Arguments.
    """
    parser = argparse.ArgumentParser(
        description="""LaTeX code tweaker
        """
    )

    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    parser.add_argument("tgt_dir", help="target directory")

    args = parser.parse_args()
    args.tgt_dir = Path(
        args.tgt_dir
    ).absolute()  # Takes care of the trailing slash, too.

    return args


def main() -> None:
    """
    Script entry point.
    """
    global ARGS

    try:
        warnings.resetwarnings()
        warnings.simplefilter("ignore")

        ARGS = retrieve_args()
        asyncio.run(tweak())
    except KeyboardInterrupt as kbd:
        sys.exit(kbd)


if __name__ == "__main__":
    main()
