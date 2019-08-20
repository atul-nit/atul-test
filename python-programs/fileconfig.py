import re
import json

color = input("enter color to add: ")

new_content = ''


def write_newcontent( new_content):
    print(new_content)
    with open("myconfig.config", "w") as f:
        f.write(new_content)


with open("myconfig.config", "r") as f:
    content = f.read()
    new_content = content
    # print(content)
    parts = re.split(r'\[section:.*\]', content)
    # print(parts)
    parts = parts[1:]
    # print(parts)
    for part in parts:
        # print(part)
        json_part = part.split("=")
        # print(json_part[1])
        json_str = json.loads(json_part[1].strip("\n "))
        # print(json_str)
        # print(type(json_str))
        if json_str.get("color") is not None:

            # print(json_str)
            # print(type(json_str))
            colors = json_str["color"]
            print(json_str)
            print(colors)
            # print(type(colors))
            if color in colors:
                print("color {} is already present".format(color))
            else:
                colors.append(color)
                print(colors)
                json_str["color"] = colors
                print(json_str)
                json_str = json.dumps(json_str)
                print(json_str)
                print(type(json_str))
                json_str = " " + json_str + "\n"
                print(json_str)
                new_part = "=".join([json_part[0], json_str])
                print(new_part)
                new_content = content.replace(part, new_part)
                if new_content != content:
                    write_newcontent(new_content)







