# Scripts!

### merge_word_lists.py

This script takes in as arguments two files filled with newline delimited words of two different languages where there is a direct
mapping, line-to-line between the files, of translation. That is, the first word in the first file will be the translated version of
the first word in the second file, the second word in the first file will be the translated version of the second word in the second
file, and so on.

As output, it produces one of two types of files:

- A simple CSV like

```
the,ο
of,του
to,προς το
and,και
a,ένα
```

- A JSON document like

```
{
    "the": "ο",
    "of": "του",
    "to": "προς το",
    "and": "και",
    "a": "ένα",
    "in": "σε",
    "is": "είναι",
    "it": "το",
    "you": "εσύ",
    "that": "ότι",
    ...
}
```

*By default, it produces a CSV file.*

### remap_merged_json.py

This script takes in merged JSON output from  a file produced by `merge_word_lists.py` and transforms it. Arguments required include the path to
the file to be remapped, the language of the keys in that file, the language of the values in that file, and the path to an output file, to which will
be written new JSON of the form

```
[
    {
        language: <value_language>,
        <key_language>: original_key,
        translated_version: original_value
    }, ...
]
```

That is, given the output above, we would receive

```
[
    {
        "language": "greek",
        "english": "the",
        "translated_version": "ο"
    },
    {
        "language": "greek",
        "english": "of",
        "translated_version": "του"
    },
    {
        "language": "greek",
        "english": "to",
        "translated_version": "προς το"
    },
    {
        "language": "greek",
        "english": "and",
        "translated_version": "και"
    },
    {
        "language": "greek",
        "english": "a",
        "translated_version": "ένα"
    }, ...
]
```

# Data!

Included are several datasets. I am publishing because I don't think any datasets like these exist for Greek, and I think that's just a travesty. For the record, you can do this for _any language_. I chose Greek because I want to learn Greek, and it's what I'll be testing my application with.

### 500_most_common_english.txt

The 500 most commonly used words in English, taken from [vocabularybuilding.org](http://www.vocabularybuilding.org/500-most-commonly-used-english-words.html), curated to a line-by-line format.

### 500_most_common_greek.txt

The 500 most commonly used words in English from the above file, translated to Greek using Google Translate.

### 1000_most_common_english.txt

The 1000 most commonly used words in English, taken from [1000mostcommonwords.com](https://1000mostcommonwords.com/1000-most-common-english-words/),curated to a line-by-line format.

### 1000_most_common_greek.txt

The 1000 most commonly used words in Greek from the above file, translated to Greek using Google Translate.

### merge_output.json

The result of running `merge_word_lists.py` on `500_most_common_english.txt` and `### 500_most_common_greek.txt`, specifying JSON output format.

### merge_output.csv

The result of running `merge_word_lists.py` on `500_most_common_english.txt` and `### 500_most_common_greek.txt`, specifying CSV output format.

### english_to_greek.json

The result of running `remap_merged_json.py` on `merge_output.json`.