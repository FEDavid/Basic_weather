import io

def generate_script(filename):
    print(filename)
    output = filename + "script.txt"
    with open(filename, "r") as f:
        content = f.read()
    with open(output, "w") as f:
        f.write(content)