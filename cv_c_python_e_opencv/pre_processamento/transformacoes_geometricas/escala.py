import cv2 as cv

imgOriginal = cv.imread('pre_processamento/einstein.jpg', 0)

imgModificada = cv.resize(imgOriginal,
                          None,
                          fx=0.8,
                          fy=0.8,
                          interpolation=cv.INTER_CUBIC)

cv.imshow('Imagem Original', imgOriginal)
cv.imshow('Imagem Modificada', imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()
