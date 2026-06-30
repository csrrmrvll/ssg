import os
import shutil

from textnode import TextNode, TextType


def publish_content(origin: str = "static", destination: str = "public") -> None:
    try:
        print(f"Publishing content from {origin} to {destination}")
        abs_origin = os.path.abspath(origin)
        abs_destination = os.path.abspath(destination)
        print(f"Absolute origin: {abs_origin}")
        print(f"Absolute destination: {abs_destination}")
        if not os.path.exists(abs_origin):
            raise FileNotFoundError(f"Origin directory '{origin}' does not exist.")
        if not os.path.isdir(abs_origin):
            raise NotADirectoryError(f"Origin '{origin}' is not a directory.")
        if os.path.exists(abs_destination) and not os.path.isdir(abs_destination):
            raise NotADirectoryError(f"Destination '{destination}' is not a directory.")
        if abs_origin == abs_destination:
            raise ValueError("Origin and destination directories cannot be the same.")
        if os.path.exists(abs_destination):
            print(f"Destination directory '{destination}' already exists. Removing it.")
            shutil.rmtree(abs_destination)
        # else:
        #     print(f"Destination directory '{destination}' does not exist. Creating it.")
        #     os.makedirs(abs_destination)
        if not os.access(abs_origin, os.R_OK):
            raise PermissionError(f"Origin directory '{origin}' is not readable.")
        if not os.access(abs_destination, os.W_OK):
            print(f"Destination directory '{destination}' is not writable.")

        print(f"Copying content from '{origin}' to '{destination}'...")
        shutil.copytree(abs_origin, abs_destination)
        print(f"Content published successfully from '{origin}' to '{destination}'.")
        os.listdir(abs_destination)
    except Exception as e:
        print(f"An error occurred while publishing content: {e}")


def main() -> None:
    publish_content()


if __name__ == "__main__":
    main()
