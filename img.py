from PIL import Image


def remove_black_border(image_path, output_path, threshold=50):
    # 打开图片
    img = Image.open(image_path)

    width, height = img.size

    left = 0
    top = 360
    right = width
    bottom = height - 300

    # 裁剪图片
    cropped_img = img.crop((left, top, right, bottom))

    gray_img = cropped_img.convert("L")
    # 获取灰度图的边界框
    bbox = gray_img.getbbox()
    print(bbox)
    # 如果图片是全黑的，bbox会是None
    if bbox is None:
        print("图片是全黑的")
        return

    # 裁剪图片
    cropped_img = cropped_img.crop(bbox)

    # 保存裁剪后的图片
    cropped_img.save(output_path)


# 使用示例
remove_black_border("xsd.jpg", "output.jpg")
