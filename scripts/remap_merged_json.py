#!/usr/bin/env python3
"""
Loads JSON object of the form
{
    word: translated_word, ...
}
from a file, and remaps to
[
    {
        <key_language>: word,
        translated_version: translated_word,
        language: <value_language>,
    }, ...
]
"""

import argparse
import json
import jsonschema

from typing import List

# Define a JSON schema that fits arbitrary keys to values
SCHEMA = {
        "type": "object",
        "patternProperties": {
            ".*": { "type": "string" }
        },
        "additionalProperties": False,
}


def load_and_validate_json(input_file_path: str) -> dict:
    with open(input_file_path, 'r') as file_handle:
        data = json.load(file_handle)
    jsonschema.validate(data, schema=SCHEMA)
    return data


def remap(word_mapping: dict, key_language: str, value_language: str) -> List[dict]:
    new_map = list()
    for key, value in word_mapping.items():
        new_map.append(
            {
                "language": value_language,
                key_language: key,
                "translated_version": value
            }
        )
    return new_map


def write_json(word_mapping: dict, output_file_path: str) -> None:
    with open(output_file_path, 'w') as file_handle:
        json.dump(word_mapping, file_handle, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="JSON document to read from")
    parser.add_argument('key_language', help="Language of the keys in the source JSON object.")
    parser.add_argument('value_language', help="Language of the values in the source JSON object.")
    parser.add_argument('output_file', help="File to write to.")
    args = parser.parse_args()

    old_mapping: dict = load_and_validate_json(args.input_file)
    new_mapping: List[dict] = remap(old_mapping, args.key_language, args.value_language)
    write_json(new_mapping, args.output_file)

if __name__ == '__main__':
    main()