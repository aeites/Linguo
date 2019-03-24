from PIL import Image, ImageFont, ImageDraw
import PIL.ExifTags
import os

class OverlayHandler:
    # args: image path, text to overlay
    def add_overlay(self, image, label):
        self.font_path = u'resources/Lato-Regular.ttf'
        base = Image.open(image).convert('RGBA')
        width, height = base.size

        ## COMMMENT ME OUT IF THE IMAGES COME OUT BAD
        if width > height:
            base = base.rotate(270, expand=True)
        ## END COMMENT ME OUT

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new(base.mode, base.size, (255,255,255,0))

        # get a drawing context
        d = ImageDraw.Draw(txt)
        shadowcolor = (255,255,255,300)
        xl = height*.1    ## top left x coord
        yl = height*.9    ## top left y coord
        xr = width*.7     ## bottom right x coord
        yr = width*.9     ## bottom right y coord
        self.font = ImageFont.truetype(self.font_path, 250)

        # make 2 strings, if necessary
        text1 = label
        text2 = ""
        if len(text1) > 20:
            text1 = label[0:19]
            text1 = text1 + '-'
            text2 = label[19:50]
            d.rectangle([(xl, yl), (xr, yr)], fill="#000000", outline=None)
            d.text((xl, yl), text1, (255,255,255),font=self.font)
            xnew = xl+10
            ynew = yl+300
            d.text((xnew, ynew), text2, (255,255,255),font=self.font)
        else:
            d.rectangle([(xl, yl), (xr, yr)], fill="#000000", outline=None)
            d.text((xl, yl), text1, (255,255,255),font=self.font)

        print(text1)
        print(text2)

        out = Image.alpha_composite(base, txt)
        out.show()

        bits = image.split('.')
        file = bits[0] + "_processed." + bits[1]
        base.save(file, "JPEG")
        return file

#path=u'C:/Users/kelly/Downloads/taco_bell.jpg'

#o = OverlayHandler()
#o.add_overlay(path, "The lion sleeps tonight")

# write it back to the filename_processed
