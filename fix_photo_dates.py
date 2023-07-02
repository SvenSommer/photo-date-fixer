from datetime import datetime
import os
from PIL import Image
import piexif
from datetime import timedelta

def update_exif_date(img_path, delta):
    # Load the image
    img = Image.open(img_path)

    # Get the existing EXIF data
    exif_dict = piexif.load(img.info["exif"])

    # Get the original date
    original_date_str = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal].decode("utf-8")
    original_date = datetime.strptime(original_date_str, '%Y:%m:%d %H:%M:%S')

    # Update the date
    new_date = original_date + delta
    new_date_str = new_date.strftime('%Y:%m:%d %H:%M:%S')

    # Set the new date
    print(f"writing: {original_date} -> {new_date_str}"  )
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date_str.encode()

    # Write the EXIF data back to the image
    exif_bytes = piexif.dump(exif_dict)
    img.save(img_path, exif=exif_bytes)

def get_delta():

    # Define the dates
    date_old = datetime.strptime('14.02.2014 07:00:00', '%d.%m.%Y %H:%M:%S')
    date_new = datetime.strptime('28.05.2023 14:00:00', '%d.%m.%Y %H:%M:%S')

    # Calculate the delta
    delta = date_new - date_old
    return delta

folder_path = './DCIM/100PHOTO'

delta = get_delta()
print("delta:", delta)
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        update_exif_date(os.path.join(folder_path, filename), delta)
