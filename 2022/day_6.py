def get_data_one() -> str:
    with open("inputs/day_6.txt", "r") as file:
        signal = file.read().rstrip("\n")
    return signal


def solve(signal: str, marker_len: int):
    for s_idx in range(len(signal) - marker_len - 1):
        marker = set([signal[idx] for idx in range(s_idx, s_idx + marker_len)])
        if len(marker) == marker_len:
            print(s_idx + marker_len)
            break


if __name__ == "__main__":
    data = get_data_one()
    solve(signal=data, marker_len=4)
    solve(signal=data, marker_len=14)
