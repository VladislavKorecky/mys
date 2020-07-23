import yaml
import tkinter
import graphics


def loadStory():
    story = True
    section = findSection(yamlReader("config.yml").get("start-id"))
    variables = {}
    for x in yamlReader("variables.yml").get("variables"):
        variables[x] = None
    global root
    if (yamlReader("config.yml").get("graphics")):
        root = tkinter.Tk()
        root.title(findSection(yamlReader("config.yml").get("story-name")))
        #root.overrideredirect(True)
        #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    while story:
        if yamlReader("content.yml").get(section).get("if-enabled") is False:
            options = yamlReader("content.yml").get(section).get("options")
            if (yamlReader("config.yml").get("graphics")):
                img = graphics.loadImage(root, yamlReader("content.yml").get(section).get("image"))
                tkinter.Label(root, image=img).grid(row=0, column=round(len(options) / 2))
            else:
                print(yamlReader("content.yml").get(section).get("text"))
            if options is None:
                exit()
            optionIndex = 0
            for x in options:
                if (yamlReader("config.yml").get("graphics")):
                    tkinter.Button(root, text=x[1]).grid(row=1, column=optionIndex)
                else:
                    print(str(optionIndex + 1) + ". " + x[1])
                optionIndex = optionIndex + 1
            userInput = input()
            optionIndex = int(userInput) - 1
            if (options[optionIndex][2] != None):
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
    root.mainloop()


def yamlReader(file):
    return yaml.safe_load(open(file, "r", encoding='utf8'))


def yamlWriter(file, data):
    yaml.safe_dump(open(file, "w", encoding='utf8'), data)


def findSection(sectionId):
    data = yamlReader("content.yml")
    for x in data:
        if data.get(x).get("id") == sectionId:
            return x
