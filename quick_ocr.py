import PIL.Image as Image
import easyocr
import sys

reader = easyocr.Reader(["en"])
img = Image.open("data_image.jpg")
w, h = img.size
result = reader.readtext("data_image.jpg")
row_1 = []
row_2 = []
for pos, s, p in result:
    if p < 0.3:
        pass
    l, r, u, d = pos[0][0], pos[1][0], pos[0][1], pos[2][1]
    s = s.replace(",", ".")
    s = s.replace("..", ".")
    s = s.replace(" ", "")
    if not "." in s:
        try:
            s = "{:.1f}".format(float(s)/10)
        except BaseException:
            pass
    if l+r > w:
        row_2.append(s)
    else:
        row_1.append(s)
sys.stdout = open("ocr_res.csv", "w")
for i in range(min(len(row_1), len(row_2))):
    print(",".join([row_1[i], row_2[i]]))
