from itertools import combinations_with_replacement
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

_ = [data := data.replace(i, "") for i in "[]{}()" if i in data]
lines = data.split("\n")

def findMinButtonPresses(lights, buttons):
    n_buttons = len(buttons)
    target = [1 if l == "#" else 0 for l in lights]
    for minP in range(1, 100):
        for presses in combinations_with_replacement(range(n_buttons), minP):
            if checkLights(target, buttons, presses):
                return minP
    return minP

def checkLights(target, buttons, presses):
    n_lights = len(target)
    light_counts = [0] * n_lights
    for button_idx in presses:
        for light_idx in buttons[button_idx]:
            light_counts[light_idx] += 1
    return all((count % 2) == target[i] for i, count in enumerate(light_counts))

ans1 = 0
for l in lines:
    x = l.split()
    lights = list(x[0])
    joltage = x[-1]
    buttons = [list(map(int,y.split(","))) for y in x[1:-1]]
    ans1+=findMinButtonPresses(lights, buttons)
    
print(ans1)

# Part 2 to come