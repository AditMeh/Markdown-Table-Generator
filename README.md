# Markdown-Table-Generator
A tool to generate markdown tables in python

This tool generates markdown files from json files. The JSON files need to be in the following form:


```json
{
    columns: [item_a, item_b, item_c, ...],

    data: [
        {
            item_a: "some value",
            item_b: "some value",
            item_c: "some_value",
            ...
        },
        {
            item_a: "some value",
            item_b: "some value",
            item_c: "some value",
            ...
        },
        ...
    ]
}
```