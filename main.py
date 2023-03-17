import cv2 as cv
import pytesseract
from pytesseract import Output
import webbrowser

video = cv.VideoCapture(-1)

def recog():

    words = []

    while True:
        success, frame = video.read()
        img = frame

        data = pytesseract.image_to_data(img, output_type=Output.DICT)
        

        n_boxes = len(data['text'])

        for i in range(n_boxes):
            if data['conf'][i] > 75:
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

                # print(x, y, w, h)

                img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                cv.imshow('camera', img)
                    
                if len(data['text'][i]) > 0:
                    words.append(data['text'][i])
                    
        for i in words:
            print(i)

        if cv.waitKey(1) & 0xFF == 27:
            break

    video.release()
    cv.destroyAllWindows()

    return words
    # print(f"words list: {words}")

    
def google_search(*text):

    query_words = ''

    for x in text:
        query_words += x
        query_words += ' '

    url = f'https://www.google.com/search?q={query_words}'

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('/usr/bin/google-chrome'))

    webbrowser.get('chrome').open(url)


# def search(search_number):
#     return google_search([search_number], recog.words[search_number + 1])

