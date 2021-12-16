# Markdown-Table-Generator
A tool to generate markdown tables in python

This tool generates markdown tables from json files, then it stores them inside a markdown filepath passed in by the user. The JSON files need to be in the following form:


```javascript 
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

### How to use
___
```python generate_markdown.py -i <json filename>.json -t <markdown filename>.md```
