from json_parser import parse_json
from generator import MarkdownGenerator
from argparser import create_parser

if __name__ == "__main__":
    parser = create_parser()

    args = parser.parse_args()

    cols, data = parse_json(args.json_fp)

    generator = MarkdownGenerator(cols, data, args.md_fp)

    generator.generate_header()
    generator.fill_data()