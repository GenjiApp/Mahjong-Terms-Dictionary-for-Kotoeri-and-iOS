#! /usr/bin/env python3.4
# coding: utf-8

import sys, argparse, re, csv, plistlib

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile', nargs = '+', type = argparse.FileType('r', encoding = 'utf-16'))
arg_parser.add_argument('-o', '--outfile', type = argparse.FileType('wb'), default = sys.stdout.buffer)
args = arg_parser.parse_args()

terms = []
for fp in args.infile:
    csvreader = csv.reader(fp, skipinitialspace = True, strict = True)
    for row in csvreader:
        if len(row) < 3: continue
        if re.search('動詞|五段|形容詞', row[2]): continue
        term = dict(
            phrase = row[1],
            shortcut = row[0],
            timestamp = 0
        )
        terms.append(term)

plistlib.dump(terms, args.outfile)
