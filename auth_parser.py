class Configuration:
    def __init__(self, file_name: str, seapartor: str) -> None:
        self.file_name = file_name
        self.separator = seapartor

def parse(objects: list, conf: Configuration):
    objects_cp = objects
    class ParsedObject:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
    parsed_objects = []
    f = open(conf.file_name, "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # Here we search for the objects
    for position, line in enumerate(content):
        line = line.strip()
        for obj in objects_cp:
            obj_name = type(obj).__name__
            if obj_name in line:
                parsed_objects.append(ParsedObject(obj_name, position))
    
    # Here we parse the attributes
    for index, parsed_object in enumerate(parsed_objects):
        nextIndex = index+1
        current_position = parsed_object.position + 1
        next_position = parsed_objects[nextIndex].position if nextIndex != len(parsed_objects) else None
        sliced_content = content[current_position:next_position] if next_position != None else content[current_position:]
        for line in sliced_content:
            line = line.strip()
            if conf.separator in line:
                partitioned_string = line.partition(conf.separator)
                objects_cp[index].__setattr__(partitioned_string[0], partitioned_string[2])
    return objects_cp
    
