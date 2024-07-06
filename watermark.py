from PIL import Image

def watermark(image_path, watermark_path, output_path):
    with open(image_path, 'rb') as f:
        image = Image.open(f)




if __name__ == '__main__':
    pass