from PIL import Image, ImageDraw, ImageFont
import os

#alphabit = ["ក", "ខ", "គ", "ឃ", "ង", "ច", "ឆ", "ជ", "ឈ", "ញ", "ដ",
 #           "ឋ", "ឌ", "ឍ", "ណ", "ត", "ថ", "ទ", "ធ", "ន", "ប", "ផ"
  #          "ព", "ភ", "ម", "យ", "រ", "ល", "វ", "ស", "ហ", "ឡ", "អ" ]
alphabit = ["ឈ", "ហ", "ល", "ឡ", "ញ", "ង", "ណ", "ស", "ឍ","វ", "យ"]  
for letter in alphabit:
    for filename in os.listdir('Fonts'):
        for i in range(30):
            x = 16
            y = -15
            img = Image.new('RGB', (128, 128), color = (255, 255, 255))
            #img = Image.new('RGB', (256,256), color=(255,255,255))

            fnt = ImageFont.truetype(f'./Fonts/{filename}', 60)
            d = ImageDraw.Draw(img)

            d.text((x - i + 1, y + i), f"{letter}", font=fnt, fill=(0, 0, 0))
        
            if letter == 'ក':
                img.save(f'kor/kor{filename}{i+1}.png')
            elif letter == 'ខ':
                img.save(f'khor/khor{filename}{i+1}.png')
            elif letter == 'គ':
                img.save(f'kur/kur{filename}{i+1}.png')
            elif letter == 'ឃ':
                img.save(f'khur/khur{filename}{i+1}.png') 
            elif letter == 'ង':
                img.save(f'ngor/ngor{filename}{i+1}.png')
            elif letter == 'ច':
                img.save(f'chor/chor{filename}{i+1}.png')
            elif letter == 'ឆ':
                img.save(f'chhor/chhor{filename}{i+1}.png')
            elif letter == 'ជ':
                img.save(f'cher/cher{filename}{i+1}.png')
            elif letter == 'ឈ':
                img.save(f'chher/chher{filename}{i+1}.png')
            elif letter == 'ញ':
                img.save(f'nger/nger{filename}{i+1}.png')
            elif letter == 'ដ':
                img.save(f'dor/dor{filename}{i+1}.png')
            elif letter == 'ឋ':
                img.save(f'der/der{filename}{i+1}.png')
            elif letter == 'ឌ':
                img.save(f'der/der{filename}{i+1}.png')
            elif letter == 'ឍ':
                img.save(f'ther/ther{filename}{i+1}.png')
            elif letter == 'ណ':
                img.save(f'nor/nor{filename}{i+1}.png')
            elif letter == 'ត':
                img.save(f'thor/thor{filename}{i+1}.png')
            elif letter == 'ថ':
                img.save(f'tor/tor{filename}{i+1}.png')
            elif letter == 'ទ':
                img.save(f'thear/thaer{filename}{i+1}.png')
            elif letter == 'ធ':
                img.save(f'thher/thher{filename}{i+1}.png')
            elif letter == 'ន':
                img.save(f'ner/ner{filename}{i+1}.png')
            elif letter == 'ប':
                img.save(f'bor/bor{filename}{i+1}.png')
            elif letter == 'ផ':
                img.save(f'phor/phor{filename}{i+1}.png')
            elif letter == 'ព':
                img.save(f'por/por{filename}{i+1}.png')
            elif letter == 'ភ':
                img.save(f'pher/pher{filename}{i+1}.png')
            elif letter == 'ម':
                img.save(f'mer/mer{filename}{i+1}.png')
            elif letter == 'យ':
                img.save(f'yer/yer{filename}{i+1}.png')
            elif letter == 'រ':
                img.save(f'ror/ror{filename}{i+1}.png')
            elif letter == 'ល':
                img.save(f'lor/lor{filename}{i+1}.png')
            elif letter == 'វ':
                img.save(f'vor/vor{filename}{i+1}.png')
            elif letter == 'ស':
                img.save(f'sor/sor{filename}{i+1}.png')
            elif letter == 'ហ':
                img.save(f'hor/hor{filename}{i+1}.png')
            elif letter == 'ឡ':
                img.save(f'lorl/lorl{filename}{i+1}.png')                                        
            else:
                img.save(f'r/r{filename}{i+1}.png')        

        for j in range(30):
            x = -15
            y = 15
            img = Image.new('RGB', (128, 128), color = (255, 255, 255))
            #img = Image.new('RGB', (256,256), color=(255,255,255))
            
            fnt = ImageFont.truetype(f'./Fonts/{filename}', 60)
            d = ImageDraw.Draw(img)
            d.text((x, y), f"{letter}", font=fnt, fill=(0, 0, 0))
            
            
            if letter == 'ក':
                img.save(f'kor/kor{filename}{j+30}.png')
            elif letter == 'ខ':
                img.save(f'khor/khor{filename}{j+30}.png')
            elif letter == 'គ':
                img.save(f'kur/kur{filename}{j+30}.png')
            elif letter == 'ឃ':
                img.save(f'khur/khur{filename}{j+30}.png') 
            elif letter == 'ង':
                img.save(f'ngor/ngor{filename}{j+30}.png')
            elif letter == 'ច':
                img.save(f'chor/chor{filename}{j+30}.png')
            elif letter == 'ឆ':
                img.save(f'chhor/chhor{filename}{j+30}.png')
            elif letter == 'ជ':
                img.save(f'cher/cher{filename}{j+30}.png')
            elif letter == 'ឈ':
                img.save(f'chher/chher{filename}{j+30}.png')
            elif letter == 'ញ':
                img.save(f'nger/nger{filename}{j+30}.png')
            elif letter == 'ដ':
                img.save(f'dor/dor{filename}{j+30}.png')
            elif letter == 'ឋ':
                img.save(f'der/der{filename}{j+30}.png')
            elif letter == 'ឌ':
                img.save(f'der/der{filename}{j+30}.png')
            elif letter == 'ឍ':
                img.save(f'ther/ther{filename}{j+30}.png')
            elif letter == 'ណ':
                img.save(f'nor/nor{filename}{j+30}.png')
            elif letter == 'ត':
                img.save(f'tor/tor{filename}{j+30}.png')
            elif letter == 'ថ':
                img.save(f'tor/tor{filename}{j+30}.png')
            elif letter == 'ទ':
                img.save(f'thear/thaer{filename}{j+30}.png')
            elif letter == 'ធ':
                img.save(f'thher/thher{filename}{j+30}.png')
            elif letter == 'ន':
                img.save(f'ner/ner{filename}{j+30}.png')
            elif letter == 'ប':
                img.save(f'bor/bor{filename}{j+30}.png')
            elif letter == 'ផ':
                img.save(f'phor/phor{filename}{j+30}.png')
            elif letter == 'ព':
                img.save(f'por/por{filename}{j+30}.png')
            elif letter == 'ភ':
                img.save(f'pher/pher{filename}{j+30}.png')
            elif letter == 'ម':
                img.save(f'mer/mer{filename}{j+30}.png')
            elif letter == 'យ':
                img.save(f'yer/yer{filename}{j+30}.png')
            elif letter == 'រ':
                img.save(f'ror/ror{filename}{j+30}.png')
            elif letter == 'ល':
                img.save(f'lor/lor{filename}{j+30}.png')
            elif letter == 'វ':
                img.save(f'vor/vor{filename}{j+30}.png')
            elif letter == 'ស':
                img.save(f'sor/sor{filename}{j+30}.png')
            elif letter == 'ហ':
                img.save(f'hor/hor{filename}{j+30}.png')
            elif letter == 'ឡ':
                img.save(f'lorl/lorl{filename}{j+30}.png')                                        
            else:
                img.save(f'r/r{filename}{j+30}.png')  
                
     