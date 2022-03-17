import sys

import cv2

print(sys.argv)

for path in sys.argv[1:]:
    print(path[-3:])
    if path[-3:] != "gif":
        print(f"{path}はgif以外の形式なので正常に処理されませんでした。")
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
        cv2.imwrite(f"{path}.png", output_image)

    except Exception as e:
        print(f"エラーが発生しました。({path})")
        print("スキップします。")
        continue

cv2.destroyAllWindows()
