#! /usr/bin/env python3

from __future__ import print_function
import sys

import argparse
import os.path
from flashtext import KeywordProcessor

# References:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# References:
# https://dev.to/vi3k6i5/regex-was-taking-5-days-to-run-so-i-built-a-tool-that-did-it-in-15-minutes-c98
class DonLimpioLogCleaner:
    canRun = False

    def __init__(self):
        self.keywordProcessor = KeywordProcessor()

    def __init__(self, filename):
        self.keywordProcessor = KeywordProcessor()
        self.setKeywords(filename)

    def setKeyword(self, word):
        self.keywordProcessor.add_keyword(word.strip())

    def setKeywords(self, filename):
        if not os.path.isfile(filename):
            eprint("error: <{}> file not exists".format(filename))
            return
        with open(filename) as f:
            for line in f:
                line = line.strip()
                self.keywordProcessor.add_keyword(line)
            self.canRun = True

    def processLine(self, line, invertMatch=False):
        line = line.strip()
        keywordsFound = self.keywordProcessor.extract_keywords(line)
        if keywordsFound and invertMatch==False:
            print(line)
        elif not keywordsFound and invertMatch==True:
            print(line)

    def processFile(self, filename, invertMatch=False):
        if not os.path.isfile(filename):
            eprint("error: <{}> file not exists".format(filename))
            return
        if self.canRun:
            i = 1
            with open(filename) as f:
                try:
                    for line in f:
                        try:
                            self.processLine(line, invertMatch)
                        except:
                            eprint("error: cannot process line {}".format(i))
                            pass
                        i += 1
                except:
                    eprint("error: cannot process line {} in file {}"
                        .format(i, filename))
                    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        metavar='FILE',
                        required=True,
                        help='Obtain patterns from FILE, one per line')
    parser.add_argument('-f', '--file',
                        metavar='FILE',
                        required=True,
                        help='Obtain log file to process')
    parser.add_argument('-v', '--invert-match',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Invert the sense of matching,\
                                to select non-matching lines.')
    args = parser.parse_args()

    if args.input:
        donlimpio = DonLimpioLogCleaner(args.input)
        if args.file:
            donlimpio.processFile(args.file, args.invert_match)

if __name__ == '__main__':
    main()
