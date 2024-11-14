import os
from PIL import Image


def transform_dataset(input_dir, output_dir, mode="images"):
    """
    This function transforms a dataset into the format specified by the documentation of
    :param input_dir: the dir containing the images.
    :param output_dir: the dir which will contain the transformed images. This must be set to point to some dataset in
    the nnUNet_raw folder.
    :return: Nothing.
    """
    for root, dirs, files in os.walk(input_dir):
        for i, file in enumerate(files):
            image_path = os.path.join(root, file)
            with Image.open(image_path) as jpg_img:
                image_name = 'gi_' + str(i).zfill(3) + '_' + str(0).zfill(4)
                if mode == "masks":
                    channel = jpg_img.split()[0]
                    channel = channel.point(lambda pixel: 255 if pixel > 128 else 0)
                    channel.convert("1")
                    channel.save(output_dir + "/" + image_name + ".png", "PNG")
                else:
                    jpg_img.save(output_dir + "/" + image_name + ".png", "PNG")


def check_channels(input_dir):
    """
    This function prints out all the unique pixel of the first image located in the input_dir.
    :param input_dir: the folder where the image is located
    :return: all unique pixel in an image.
    """
    for root, dirs, files in os.walk(input_dir):
        for i, file in enumerate(files):
            print(file)
            image_path = os.path.join(root, file)
            with Image.open(image_path) as jpg_img:
                print(set(list(jpg_img.getdata())))
                return

if __name__ == '__main__':

    source = "./datasets/kvasir_seg/"
    destination = "./nnunetv2/data/nnUNet_raw/Dataset0069_GastrointestinalTract/"

    transform_dataset(input_dir=source + "images",
                      output_dir=destination + "imagesTr")
    transform_dataset(input_dir=source + "masks",
                      output_dir=destination + "labelsTr",
                      mode='masks')
