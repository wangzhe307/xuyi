from PIL import Image,ImageFilter
im=Image.open('test.jpg')
w,h=im.size
print('original image size:%sx%s'%(w,h))
im.thumbnail((w//2,h//2))
print('resize image to:%sx%s'%(w//2,h//2))

im2=im.filter(ImageFilter.BLUR)
im2.save('test1.jpg','jpeg')