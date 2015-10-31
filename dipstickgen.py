import svgwrite
import json
import argparse


WIDTH_ADDITION = 5.0
HEIGHT_ADDITION = 5.0
X_VIEWBOX_OFFSET = (WIDTH_ADDITION / 2) * -1
Y_VIEWBOX_OFFSET = (HEIGHT_ADDITION / 2) * -1


def readFileHelper(filename, mode):
    data = ''
    try:
        with open(filename, mode) as f:
            data = f.read()
    except:
        print 'Error: Could open/read file %s' % filename

    return data


def main(cmdargs):
    # Read all the necessary files
    config = json.loads(readFileHelper(cmdargs.inputfile, 'r'))
    stylesheet = readFileHelper('styles/%s_%s.css' % (cmdargs.style, config['package']), 'r')
    # Precalculate some sizes and positions
    width = float(config['width'])
    height = float(config['height'])
    pins = config['numPins']
    pinWidth = width / 2.0
    pinHeight = height / (pins / 2.0)
    canvasWidth = width + WIDTH_ADDITION
    canvasHeight = height + HEIGHT_ADDITION

    # Start drawing
    img = svgwrite.Drawing(cmdargs.outputfile, ('%.2fmm' % canvasWidth, ('%.2fmm') % canvasHeight),
                           viewBox=('%.2f %.2f %.2f %.2f' % (X_VIEWBOX_OFFSET, Y_VIEWBOX_OFFSET, canvasWidth, canvasHeight)),
                           profile='full')
    img.add(img.style(stylesheet))
    img.add(img.rect(insert=(X_VIEWBOX_OFFSET, Y_VIEWBOX_OFFSET), size=('100%', '100%'), class_='debugborder'))

    for i in xrange(0, (pins / 2)):
        pin1 = config['pins'][i]
        pin2 = config['pins'][(pins - 1) - i]
        rectClassLeft = ' '.join(['pin', pin1['group']]).strip()
        rectClassRight = ' '.join(['pin', pin2['group']]).strip()
        textClassLeft = ' '.join([rectClassLeft, 'left'])
        textClassRight = ' '.join([rectClassRight, 'right'])

        # Add the first rectangle
        img.add(img.rect(insert=(0, (pinHeight * i)), size=(pinWidth, pinHeight), class_=rectClassLeft))
        # Add the first text element
        img.add(img.text(pin1['name'], insert=(0.3, (pinHeight * (i + 1)) - 0.2), class_=textClassLeft))

        # Add the second rectangle
        img.add(img.rect(insert=(pinWidth, (pinHeight * i)), size=(pinWidth, pinHeight), class_=rectClassRight))
        # Add the second text element
        img.add(img.text(pin2['name'], insert=(width - 0.3, (pinHeight * (i + 1)) - 0.2), class_=textClassRight))

    img.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a pinout sticker for dual inline packages.')
    parser.add_argument('-s', dest='style', default='default', help='define a different style to use for your sticker')
    parser.add_argument('inputfile', help='name of the json pin definition file.')
    parser.add_argument('outputfile', help='name of the image file.')
    main(parser.parse_args())
