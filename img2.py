from PIL import Image


def crop_image(image_path, output_path, top_crop, bottom_crop):
    # 打开图片
    img = Image.open(image_path)

    # 获取图片的尺寸
    width, height = img.size

    # 计算新的裁剪区域
    left = 0
    top = top_crop
    right = width
    bottom = height - bottom_crop

    # 裁剪图片
    cropped_img = img.crop((left, top, right, bottom))

    # 保存裁剪后的图片
    cropped_img.save(output_path)


# 使用示例
crop_image("xsd.jpg", "output.jpg", 500, 50)  # 裁剪掉上下各50像素
