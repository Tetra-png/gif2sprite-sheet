import sys

import imageio
import numpy as np


def main():
    for path in sys.argv[1:]:
        if path[-3:] != "gif":
            print(f"{path}はgif以外の形式なので正常に処理されませんでした。")
            print("処理を続けますか？ y/N")
            if input() != "y":
                sys.exit(1)

            continue

        try:
            cap = imageio.get_reader(path)
            for i, frame in enumerate(cap):
                # print(frame.shape)
                if i == 0:
                    result = frame
                else:
                    result = np.hstack([result, frame])

            imageio.imwrite(f"{path[:-4]}.png", result)

        except Exception as e:
            print(f"エラーが発生しました。({path})")
            print(e)

            print("処理を続けますか？ y/N")
            if input() != "y":
                sys.exit(1)

            continue


if __name__ == "__main__":
    main()
