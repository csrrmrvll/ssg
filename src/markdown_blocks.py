from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if re.search(r"^#{1,6} .*\n?", block, re.MULTILINE):
        return BlockType.HEADING
    elif re.search(r"^```\n[\s\S]*?```$", block, re.MULTILINE):
        return BlockType.CODE
    elif re.search(r"^> ?.*", block, re.MULTILINE):
        return BlockType.QUOTE
    elif re.search(r"^- .*", block, re.MULTILINE):
        return BlockType.ULIST
    elif re.search(r"^\d+\. .*", block, re.MULTILINE):
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks
