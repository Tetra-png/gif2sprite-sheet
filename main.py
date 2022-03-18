import sys

import cv2
import numpy as np

for path in sys.argv[1:]:
    print(path[-3:])
    if path[-3:] != "gif":
        print(f"{path}はgif以外の形式なので正常に処理されませんでした。")
        print("処理を続けますか？ y/N")
        if input() != "y":
            sys.exit(1)

        continue

    try:
        cap = cv2.VideoCapture(path)

        images = []

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                images.append(frame)
            else:
                cap.release()

        output_image = cv2.hconcat(images)
        output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2BGRA)
        output_image[:, :, 3] = np.where(np.all(output_image == 255, axis=-1), 0, 255)  # 白色のみTrueを返し、Alphaを0にする
        cv2.imwrite(f"{path[:-3]}.png", output_image)

    except Exception as e:
        print(f"エラーが発生しました。({path})")
        print(e)

        print("処理を続けますか？ y/N")
        if input() != "y":
            sys.exit(1)

        continue

cv2.destroyAllWindows()
