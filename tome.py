from typing import Union, Any

class Tome:
    id: str
    label: str
    description: Union[str, None]
    aspects: Any
    slots: Any
    xexts: Any
    xtriggers: Any
    inherits: Any
    unique: bool
    audio: Union[str, None]
    manifestationtype: Union[str, None]

    def __init__(self, init_data):
        for key in init_data:
            val = init_data[key]

            match key: 
                case "ID" | "id":
                    self.id = val
                case "label" | "Label":
                    self.label = val
                case "description" | "Description":
                    self.description = val
                case "aspects":
                    # TODO: make aspect class
                    self.aspects = val
                case "slots":
                    # TODO: slots meaning
                    self.slots = val
                case "xexts":
                    # TODO: make xexts class
                    self.xexts = val
                case "xtriggers":
                    # TODO: make xtriggers class
                    self.xtriggers = val
                case "inherits":
                    self.inherits = val
                case "unique":
                    self.unique = val
                case "audio":
                    self.audio = val
                case "manifestationtype":
                    self.manifestationtype = val
                case _:
                    print("Strange key:", key)

    def __str__(self):
        return f'ID: {self.id}\nLabel: {self.label}'
