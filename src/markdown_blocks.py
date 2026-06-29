def markdown_to_blocks(markdown: str) -> list[str]:
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks
