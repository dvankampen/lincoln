"""Main module for creating and managing Lincoln Logs and Layers."""

from lincolnlog import LincolnLog
from lincolnlayer import LincolnLayer

log_catalog = [
    LincolnLog(length=2, rotation='horizontal', transform=(0, 0)),
    LincolnLog(length=3, rotation='vertical', transform=(1, 1)),
    LincolnLog(length=4, rotation='horizontal', transform=(2, 2)),
]

def main():
    """Main function to create Lincoln Logs and add them to a Lincoln Layer."""
    layer = LincolnLayer()
    for log in log_catalog:
        layer.add_log(log)
    print(layer)


if __name__ == "__main__":
    main()
