"""
The program generates a csv file from training folder
Replace/Add images into each color names' folder for better images
"""
import os, imageio, csv

def get_rgb_from_path(path):
    """
    The function gets the rgb value from the pixel of middle of 'path' image
    and return as a tuple of (R, G, B)
    """
    # read the image from given 'path'
    image = imageio.imread(path, pilmode='RGB')
    # return the tuple (R, G, B) from image
    return tuple(image[int(len(image)/2)][int(len(image[0])/2)])

def main():
    base_path = './training_dataset/'
    # map with key: color_name, value: list of rgb values that maps to color_name
    color_map = {}
    # define each folder's name under 'base_path' as 'process_color'
    for process_color in os.listdir(base_path):
        color_list = []
        # get the file name in 'process_color' folder
        for file_name in (os.listdir(base_path + process_color)):
            relative_path = base_path + process_color + '/'+ file_name
            rgb_tuple = get_rgb_from_path(relative_path)
            # append rgb value tuple into the color_list
            color_list.append(rgb_tuple)
        # update the map with color_name and color_list
        color_map[process_color] = color_list

    # creating a new csv file (if using mac delete the "newline=''" below)
    with open('color_dataset.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # write csv file with attributes: 'Color','Red','Green','Blue'
        csv_writer.writerow(['Color','Red','Green','Blue'])
        for key, list in color_map.items():
            for rgb in list:
                # write rows in the order of: color_name, red_value, green_value, blue value
                csv_writer.writerow([key,rgb[0],rgb[1],rgb[2]])

if __name__ == '__main__':
    main()