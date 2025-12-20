from pathlib import Path

TEST = False
PRINT = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_2_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> dict[str, list[str]]:
    processed = {}
    for src, dst in [line.split(": ") for line in data]:
        processed[src] = dst.split()

    return processed


def solve_one(data: dict[str, list[str]], start: str, end: str) -> int:
    def dfs(node: str, i: int):
        if data[node][i] == end:
            return 1

        next_node = data[node][i]
        count = 0
        for next_i in range(len(data[next_node])):
            count += dfs(next_node, next_i)
        return count

    result = 0
    for i in range(len(data[start])):
        result += dfs(start, i)

    return result


def part_one(data: dict[str, list[str]]):
    result = solve_one(data, start="you", end="out")
    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 5 else "[FAILURE]")
    else:
        print()


def solve_two(data: dict[str, list[str]], start: str, end: str) -> int:
    result = 0

    def dfs(start: str, end: str) -> list[list[str]]:
        successful_paths = []
        queue = [{"path": [start], "mul": 1}]
        while queue:
            el = queue.pop(0)
            path = el["path"]
            mul = el["mul"]

            node = path[-1]

            if node == end:
                successful_paths.append({"path": path, "mul": mul})
                continue

            for next_node in data.get(node, []):
                if next_node in {"dac", "fft"} - {end}:
                    continue
                new_path = list(path)
                new_path.append(next_node)
                queue.append({"path": new_path, "mul": mul})

                if (
                    len(queue) > 1
                    and (shared_el := queue[-1]["path"][-1]) != end
                    and sum(
                        to_merge := [
                            queue[-1]["path"][-1] == q["path"][-1] for q in queue
                        ]
                    )
                    > 1
                ):
                    to_merge = [i for i, cond in enumerate(to_merge) if cond][::-1]
                    total_mul = 0
                    for i in to_merge:
                        total_mul += queue[i]["mul"]
                        queue.pop(i)
                    queue.append({"path": [shared_el], "mul": total_mul})

        return successful_paths

    out = dfs(start, end)
    result = sum([p["mul"] for p in out])

    return result


def part_two(data: dict[str, list[str]]):
    result = 0

    sd = solve_two(data, start="svr", end="dac")
    df = solve_two(data, start="dac", end="fft")
    fo = solve_two(data, start="fft", end="out")
    sf = solve_two(data, start="svr", end="fft")
    fd = solve_two(data, start="fft", end="dac")
    do = solve_two(data, start="dac", end="out")

    if PRINT:
        print("svr -> dac:", sd)
        print("dac -> fft:", df)
        print("fft -> out:", fo)
        print()
        print("svr -> fft:", sf)
        print("fft -> dac:", fd)
        print("dac -> out:", do)
        print()
        print(f"{sd} * {df} * {fo} = {sd * df * fo}")
        print(f"{sf} * {fd} * {do} = {sf * fd * do}")

    result = (sd * df * fo) + (sf * fd * do)

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 2 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
