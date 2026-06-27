class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list['HTMLNode'] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method should be implemented in subclasses")

    def props_to_html(self) -> str:
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, {self.value}, {self.children}, {self.props})"
