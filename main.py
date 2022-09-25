"""
The program predicts the color name base on csv on the current directory
"""

import sklearn.tree, pandas

def main():
    # convert color_dataset.csv into pandas DataFrame
    data = pandas.read_csv('./color_dataset.csv')

    # selecting columns excluding "Color" as features
    rgbs = data.loc[:, data.columns != 'Color']
    # selecting only the "Color" column as labels
    color_name = data['Color']

    # defining a new decision tree
    color_model = sklearn.tree.DecisionTreeClassifier()
    # training model with processed DataFrame
    color_model.fit(rgbs, color_name)

    is_running = True
    # start the program
    while(is_running):
        print('Enter \'q\' for exit, \'g\' for start guessing:')
        match input():
            case 'g':
                print('Enter Red Value:')
                red = int(input())
                print('Enter Green Value:')
                green = int(input())
                print('Enter Blue Value: ')
                blue = int(input())
                # generating color
                guess = [[red, green, blue]]
                # predicting color with variable 'guess'
                print(color_model.predict(pandas.DataFrame(guess, columns=['Red', 'Green', 'Blue']))[0])
            case 'q':
                is_running = False
                print('Exiting...')
            case _:
                print('Input Error!')

if __name__ == '__main__':
    main()