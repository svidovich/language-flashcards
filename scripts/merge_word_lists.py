#!/usr/bin/env python3

import argparse
import csv
import json

from typing import List


class MetricError(Exception):
    """
    Custom exception for lists of unequal length
    """
    pass

def read_word_file(file_path: str) -> List[str]:
    word_list = list()
    with open(file_path, 'r') as file_handle:
        for line in file_handle.readlines():
            word_list.append(line)
    return [x.strip() for x in word_list]


def construct_mapping(list_1: List[str], list_2: List[str]) -> dict:
    if len(list_1) != len(list_2):
        raise MetricError("Word lists are of uneqal length.")

    word_mapping = dict()
    for i in range(len(list_1)):
        word_mapping[list_1[i]] = list_2[i]

    return word_mapping


def write_csv(word_mapping: dict, output_file_path: str) -> None:
    with open(output_file_path, 'w') as file_handle:
        writer = csv.writer(file_handle)
        for key, value in word_mapping.items():
            writer.writerow([key, value])


def write_json(word_mapping: dict, output_file_path: str) -> None:
    with open(output_file_path, 'w') as file_handle:
        json.dump(word_mapping, file_handle, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file1', help="First input file to use. Must have same number of words as second file.")
    parser.add_argument('file2', help="Second input file to use. Must have same number of words as first file.")
    parser.add_argument('output_file', help="Output filename")
    parser.add_argument('--output-type', required=False, choices=['csv', 'json'], default='csv', help="Output format.")
    args = parser.parse_args()

    list_1: List[str] = read_word_file(args.file1)
    list_2: List[str] = read_word_file(args.file2)

    word_mapping: dict = construct_mapping(list_1, list_2)
    if args.output_type == 'json':
        write_json(word_mapping, args.output_file)
    else:
        write_csv(word_mapping, args.output_file)


if __name__ == '__main__':
    main()