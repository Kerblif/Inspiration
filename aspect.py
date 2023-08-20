from typing import Union, Any
import os

class Aspect:
    def __init__(self, init_data):
        noartneeded = False

        for key in init_data:
            val = init_data[key]

            match key: 
                case "ID" | "id":
                    self.id = val
                case "Label" | "label":
                    self.label = val
                case "Description" | "description":
                    self.description = val
                case "noartneeded":
                    noartneeded = val
                case "ishidden" | "isHidden":
                    self.ishidden = val
                case "isAspect":
                    self.isaspect = val
                case "icon":
                    self.icon = val
                case "sort":
                    self.sort = val
                case "comments":
                    self.comments = val
                case "commute":
                    self.commute = val
                case _:
                    print("Strange key:", key)
        
        path = f'./data/images/aspects/{self.id}.png'
        self.imagePath = path if os.path.exists(path) else None
    
    def __str__(self):
        return f'ID: {self.id}\nLabel: {self.label}\nImage: {self.imagePath}'
