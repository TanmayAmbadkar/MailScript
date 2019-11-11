from PIL import Image 
  
def main(): 
    try: 
        img = Image.open("FinalPass1.jpg")  
          
        img2 = Image.open("QRCodesPng\\201951018.png")  
        img2.save("201951018.jpg","JPEG")
        img.paste(img2, (50, 600)) 
          
        #Saved in the same relative location 
        img.save("pasted_picture.jpg") 
          
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()