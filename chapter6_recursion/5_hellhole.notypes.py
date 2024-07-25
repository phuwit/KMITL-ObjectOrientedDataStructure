MAX_REACH = 3

settings = input('Creating a simulated hell scenario: ').split('/')

height = int(settings.pop(0))
problematic_thorns = settings.pop(0).split(',')
max_energy = float(settings.pop(0))
tiredness = {1: 0, 2: 0, 3: 0}
tiredness_raw = settings.pop(0).split(',')
if len(tiredness_raw) > 1:
    for i, value in enumerate(tiredness_raw):
        tiredness[i+1] = float(value)
        continue
elif tiredness_raw != 0:
    tiredness_all = float(tiredness_raw.pop())
    tiredness = {1: tiredness_all, 2: tiredness_all, 3: tiredness_all}

print(
f'''Height: {height}
thorn At: {problematic_thorns}
Max Tiredness: {max_energy}
Tiredness Values: {tiredness}''')
problematic_thorns = [int(n) for n in problematic_thorns]

def get_paths(current_level, used_energy):
    if used_energy > max_energy:
        return [False]

    if not current_level == 0 and current_level in problematic_thorns:
        return [False]

    if current_level >= height:
        if used_energy > max_energy or current_level > height:
            return [False]
        return [True]

    paths = []
    for step_size in range(1, MAX_REACH + 1):
        paths.extend(get_paths(
            current_level=(current_level + step_size),
            used_energy=(used_energy + tiredness[step_size])
            ))

    return paths

valid_paths = sum(1 for i in get_paths(current_level=0, used_energy=0) if i is True)

print(f'''--------------------------------------------------
The ways to escape is/are {valid_paths} ways''')