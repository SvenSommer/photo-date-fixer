# Fix EXIF Datetime

This Python script is used to correct the EXIF datetime in a batch of image files. This is particularly useful if your camera had the incorrect date set when the photos were taken. 

The script takes the EXIF datetime from each image, adds a time delta, and then writes the new date back to the image's EXIF data.

## Requirements

The script requires Python 3 and the following Python packages:
- `Pillow`
- `piexif`

You can install these with pip using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage
1. Define your time delta by modifying the get_delta() function in fix_exif_datetime.py. The script currently includes a sample time delta.

2. Modify folder_path in fix_exif_datetime.py to point to the directory containing the images you want to modify.

3. Run the script with python fix_exif_datetime.py.

## Note
Please back up your images before running this script to prevent any accidental data loss.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details