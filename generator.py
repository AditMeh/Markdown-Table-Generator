"""
This file generates the markdown document and saves it
"""


from typing import Dict, List


class MarkdownGenerator:
    def __init__(self, cols: List[str], data: List[Dict[str, str]], fp: str) -> None:
        self.COL_BREAK = "|"
        self.BREAKER = "---"
        assert(fp.endswith(".md"))
        
        self.cols = cols
        self.data = data
        self.file = open(fp, "w")
    
    def generate_header(self):
        top_row = self.COL_BREAK + self.COL_BREAK.join(self.cols) + self.COL_BREAK
        breaker = self.COL_BREAK + self.COL_BREAK.join([self.BREAKER for _ in self.cols]) + self.COL_BREAK

        self.file.write(top_row + "\n" + breaker + "\n")

    def fill_data(self):
        str_to_write = ""
        for item in self.data:
            items_list = [item[key] for key in self.cols]
            row = self.COL_BREAK + self.COL_BREAK.join(items_list) + self.COL_BREAK + "\n"
            str_to_write += row
        
        self.file.write(str_to_write)