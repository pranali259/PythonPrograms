#https://www.youtube.com/watch?v=9h_ysU2zO48

import cv2
import matplotlib.pyplot as plt
def main():
    imgpath = "D:\TempI\Tanish.jpg"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Tanish')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    
if __name__=="__main__":
    main()
