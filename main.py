from json_parser import parse_json
from generator import MarkdownGenerator
if __name__ == "__main__":

    fp = "test_json.json"

    cols, data = parse_json(fp)

    generator = MarkdownGenerator(cols, data, "test.md")

    generator.generate_header()
    generator.fill_data()