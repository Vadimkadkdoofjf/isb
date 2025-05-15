from enum import Enum

DEFAULT_DIRECTORY = r"C:\Users\padim\PycharmProjects\isb\lab_3"
FILTER = "JSON Files (*.json)"


class IconTypes(Enum):
    Critical = ("critical",)
    Warning = ("warning",)
    Question = ("question",)
    Information = ("information",)
    NoIcon = ""