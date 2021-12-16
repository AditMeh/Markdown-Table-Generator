import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Generates markdown table in the given markdown path given path to json file')
    parser.add_argument('-i','--json_fp', help='Json filepath. Will be used to generate table', required=True)
    parser.add_argument('-t','--md_fp', help='Markdown filepath. Table will be stored in a markdown file at this filepath', required=True)
    return parser