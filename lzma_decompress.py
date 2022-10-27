import os
import pickle
from argparse import ArgumentParser

import compress_pickle


def absolute_file_paths(directory: str):
    """
    Function to get all the absolute path of files into a directory.
    :param directory: The directory to yield all the absolute file paths from.
    :return: Yield all the path in a main directory.
    """

    for dir_path, _, filenames in os.walk(directory):
        for f in filenames:
            if f.endswith(".lzma"):
                yield os.path.abspath(os.path.join(dir_path, f))


def main(args) -> None:
    """
    Script to decompress the dataset from lzma compress files into pickled one.
    The decompress directory will correspond of the following subdirectory:
    /path_to_save/clean_data/test/...
    /path_to_save/clean_data/train/...
    /path_to_save/clean_data/zero_shot/...
    /path_to_save/incomplete_data/test/...
    /path_to_save/incomplete_data/train/...
    """
    paths = absolute_file_paths(args.files_directory)

    for path in paths:
        pickled_data = compress_pickle.load(path, compression="lzma")
        filename = path.split(os.path.sep)[-1].replace(".lzma", ".p")  # get the filename and convert .lzma extension to .p
        file_path = os.path.join(*path.split(os.path.sep)[-4:-1])  # extract the directory tree
        path_to_save = os.path.join(args.path_to_save,
                                    file_path)  # append the tree with the path to the saving directory
        os.makedirs(path_to_save, exist_ok=True)  # create directory tree if doesn't already exist
        # dump in pickle format in chunked mode
        with open(os.path.join(path_to_save, filename), "wb") as file:
            pickle.dump(pickled_data, file)
        
        # cleanup of the LZMA file
        os.remove(path)

if __name__ == "__main__":
    parser = ArgumentParser(description='Decompress all the LZMA pickled file into "normal" pickled file.')

    parser.add_argument("files_directory", type=str, help="The directory where the files to decompress are located.")
    parser.add_argument("path_to_save", type=str, help="The directory where to save the decompress files.")

    parsed_args = parser.parse_args()

    main(parsed_args)
