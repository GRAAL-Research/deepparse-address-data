# Script to merge all the files from a directory into a single one file for easier training.

import os
from argparse import ArgumentParser
from pickle import load, dump
from random import shuffle


def main(args):
    files = list(os.walk(args.files_directory))[0][2]

    datasets = dict()

    for dataset in files:
        loaded_data = load(open(os.path.join(args.files_directory, f'./{dataset}'), 'rb'))

        datasets[dataset.replace('.p', '')] = loaded_data

    index_list = [i for i in range(len(files))]

    global_list = []

    for i in range(args.number_of_samples):
        shuffle(index_list)

        for index in index_list:
            try:
                pair = datasets[files[index].replace('.p', '')][i]
            except IndexError:
                continue

            global_list.append(pair)

    dump(global_list, open(os.path.join(args.saving_path, f"{args.file_name}.p"), 'wb'))


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate a merged address data file.")

    parser.add_argument("files_directory", type=str, help="The directory where the files are located.")
    parser.add_argument("number_of_samples", type=int, help="The number of addresses to sample per country.")
    parser.add_argument("saving_path", type=str, help="The path to save the generated file.")
    parser.add_argument("file_name", type=str, help="The name to give the generated file without an extension.")

    parsed_args = parser.parse_args()

    main(parsed_args)
