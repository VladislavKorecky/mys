import yaml
import tkinter
import graphics


def loadStory():
    story = True
    section = findSection(yamlReader("config.yml").get("start-id"))
    variables = {}
    for x in yamlReader("variables.yml").get("variables"):
        variables[x] = None
    while story:
        if yamlReader("content.yml").get(section).get("if-enabled") is False:
            print(yamlReader("content.yml").get(section).get("text"))

            if (yamlReader("config.yml").get("graphics")):
                root = tkinter.Tk()
                root.title(findSection(yamlReader("config.yml").get("story-name")))
                img = graphics.loadImage(root, yamlReader("content.yml").get(section).get("image"))
                tkinter.Label(root, image=img).pack()
                root.mainloop()
                root.destroy()
            
            options = yamlReader("content.yml").get(section).get("options")
            if options is None:
                exit()
            optionIndex = 0
            for x in options:
                print(str(optionIndex + 1) + ". " + x[1])
                optionIndex = optionIndex + 1
            userInput = input()
            optionIndex = int(userInput) - 1
            variables[options[optionIndex][2][0]] = options[optionIndex][2][1]
            section = findSection(options[optionIndex][0])
        else:
            checker = 0
            for x in yamlReader("content.yml").get(section).get("if"):
                if variables[x[0]] == x[1]:
                    checker = checker + 1
            if checker == len(yamlReader("content.yml").get(section).get("if")):
                section = findSection(yamlReader("content.yml").get(section).get("do"))
            else:
                section = findSection(yamlReader("content.yml").get(section).get("else"))


def yamlReader(file):
    return yaml.safe_load(open(file, "r", encoding='utf8'))


def yamlWriter(file, data):
    yaml.safe_dump(open(file, "w", encoding='utf8'), data)


def findSection(sectionId):
    data = yamlReader("content.yml")
    for x in data:
        if data.get(x).get("id") == sectionId:
            return x


"""def loadFirstLine(lines):
    print(firstLine[firstLine.index("(\"") + 2:firstLine.index("\")")])
    loadSection(lines, lines[0])


def loadSection(lines, key):
    lines.pop(0)
    for line in lines:
        if key == line[0:line.index("(")]:
            print(line[line.index("(\"") + 2:line.index("\")")])
            options = line[line.index("-") + 1:len(line)].split(",")
            if options[0] == "!end":
                exit()
            optionNumber = 1
            for option in options:
                print(str(optionNumber) + ". " + option[option.index("(\"") + 2:option.index("\")")])
                optionNumber += 1
            usersOption = input()
            usersOption = int(usersOption) - 1
            loadSection(lines, options[usersOption][0:options[usersOption].index("(")])"""
